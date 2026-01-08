import os
import glob
import chromadb
from chromadb.utils import embedding_functions

class RAGEngine:
    def __init__(self, data_dir="data", db_path="vectordb"):
        # Setup paths
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.base_dir, data_dir)
        self.db_path = os.path.join(self.base_dir, db_path)
        
        # Initialize Client
        # We use a persistent client so we don't lose the embeddings on restart
        self.client = chromadb.PersistentClient(path=self.db_path)
        
        # Use a simple embedding function (default is all-MiniLM-L6-v2)
        # This downloads the model locally on first run.
        self.embedding_fn = embedding_functions.DefaultEmbeddingFunction()
        
        self.collection_name = "portfolio_knowledge_base"
        self.collection = self.get_or_create_collection()
        
        # Always reload documents to ensure freshness
        print("Reloading documents from data directory...")
        existing_ids = self.collection.get()['ids']
        if existing_ids:
            self.collection.delete(ids=existing_ids)
        self.load_documents()

    def get_or_create_collection(self):
        return self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_fn
        )

    def load_documents(self):
        """And loads all .txt files from the data directory into the vector DB."""
        if not os.path.exists(self.data_path):
            print(f"Data directory {self.data_path} not found.")
            return

        documents = []
        metadatas = []
        ids = []

        # Find all txt files
        files = glob.glob(os.path.join(self.data_path, "*.txt"))
        
        for file_path in files:
            filename = os.path.basename(file_path)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    
                # Simple chunking by paragraphs or just loading the whole file if small
                # For this portfolio, files are small enough to be chunks themselves usually,
                # but let's split by double newline to be safe.
                chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
                
                for i, chunk in enumerate(chunks):
                    documents.append(chunk)
                    metadatas.append({"source": filename, "chunk_id": i})
                    ids.append(f"{filename}_{i}")
                    
            except Exception as e:
                print(f"Error reading {filename}: {e}")

        if documents:
            print(f"Adding {len(documents)} chunks to Vector DB...")
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print("Docs loaded!")
        else:
            print("No documents found to load.")

    def query(self, query_text, n_results=3):
        """Retrieve top k relevant chunks."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        # results['documents'] is a list of lists (since we can query multiple texts)
        if results['documents']:
            return results['documents'][0]
        return []
