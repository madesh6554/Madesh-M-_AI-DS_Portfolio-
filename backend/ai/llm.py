import os
from abc import ABC, abstractmethod
import openai
import google.generativeai as genai

class LLMClient(ABC):
    @abstractmethod
    def generate_response(self, prompt: str, system_prompt: str) -> str:
        pass

class OpenAIClient(LLMClient):
    def __init__(self, api_key=None, model="gpt-4o-mini"):
        self.client = openai.OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model

    def generate_response(self, prompt: str, system_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI Error: {e}")
            return f"Error connecting to AI: {str(e)}"

class GeminiClient(LLMClient):
    def __init__(self, api_key=None, model="gemini-1.5-flash"):
        import google.generativeai as genai
        genai.configure(api_key=api_key or os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model)

    def generate_response(self, prompt: str, system_prompt: str) -> str:
        try:
            full_prompt = f"{system_prompt}\n\nUser Query: {prompt}"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            print(f"Gemini Error: {e}")
            return f"Error connecting to AI: {str(e)}"

class HuggingFaceClient(LLMClient):
    def __init__(self, api_key=None, model="mistralai/Mistral-7B-Instruct-v0.2"):
        from huggingface_hub import InferenceClient
        self.api_key = api_key or os.getenv("HUGGINGFACE_API_KEY")
        self.model = model
        self.client = InferenceClient(api_key=self.api_key)

    def generate_response(self, prompt: str, system_prompt: str) -> str:
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat_completion(
                model=self.model,
                messages=messages,
                max_tokens=500
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"HuggingFace Error: {e}")
            return f"Error connecting to AI: {str(e)}"

def get_llm_client():
    provider = os.getenv("LLM_PROVIDER", "").lower()
    
    if provider == "gemini":
        return GeminiClient()
    elif provider == "huggingface":
        return HuggingFaceClient()
    elif provider == "openai":
        return OpenAIClient()
    
    # Auto-detection fallback
    if os.getenv("GEMINI_API_KEY"):
        return GeminiClient()
    elif os.getenv("HUGGINGFACE_API_KEY"):
        return HuggingFaceClient()
    elif os.getenv("OPENAI_API_KEY"):
        return OpenAIClient()
    else:
        print("Warning: No viable LLM API key found.")
        return OpenAIClient(api_key="dummy")
