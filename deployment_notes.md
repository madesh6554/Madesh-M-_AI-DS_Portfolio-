# Deployment Notes

## Backend (Render)

1.  **Environment Variables**:
    - Add `OPENAI_API_KEY` (or `GEMINI_API_KEY`) to Render's environment variables.
    - Ensure `PYTHON_VERSION` is set to 3.9+ (ChromaDB requirement).

2.  **Build Command**:
    - `pip install -r requirements.txt`
    - **Important**: Render's free tier interacts with persistent disk storage differently. 
    - For a simple persistent vector DB, `chromadb` writes to disk (`vectordb/`). On Render free tier, the disk is ephemeral (wiped on deploy).
    - **Fix**: The `RAGEngine` in `rag.py` checks if the DB is empty on startup and re-ingests the `data/*.txt` files. This is fine for this size of data.
    - **Persistent Storage**: If you want true persistence, add a "Disk" in Render settings and mount it to `/opt/render/project/src/backend/vectordb`.

3.  **Start Command**:
    - `gunicorn app:app` (or `python app.py` for dev).

## Frontend (Vercel)

1.  **Environment Variables**:
    - `REACT_APP_API_URL`: Set this to your Render backend URL (e.g., `https://your-app.onrender.com`).
    - **Update Code**: In `frontend/src/components/Chatbot.jsx`, currently the fetch URL is hardcoded to `http://localhost:5000`. 
    - **Action Item**: Change line 36 of `Chatbot.jsx` to use the environment variable:
      ```javascript
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
      const response = await fetch(`${apiUrl}/api/chatbot`, { ... });
      ```

2.  **Build Settings**:
    - Framework: Create React App
    - Build Command: `npm run build`
    - Output Directory: `build`

## Local Testing

1.  **Backend**:
    ```bash
    cd backend
    pip install -r requirements.txt
    set OPENAI_API_KEY=your_key
    python app.py
    ```

2.  **Frontend**:
    ```bash
    cd frontend
    npm install
    npm start
    ```
