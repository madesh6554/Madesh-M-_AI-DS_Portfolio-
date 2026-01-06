# Madesh M – AI & ML Engineer / Data Scientist Portfolio

This repository contains the complete source code for my personal portfolio website and backend API.  
It showcases my real‑world work in **AI, machine learning, data science, analytics, and data visualization**, built using a modern full‑stack setup (React + Tailwind + Framer Motion on the frontend, Flask + SQLite on the backend).

The portfolio highlights:
- End‑to‑end **ML projects** (classification, regression, NLP, time‑series, and dashboarding).
- Internship work on **EDA, feature engineering, model training, and reporting**.
- Interactive **visualizations and dashboards** (Tableau, Plotly, Matplotlib/Seaborn).
- A clean, recruiter‑friendly UI with animations, responsive design, and multiple role‑based resumes.

---

## 🔹 Tech Stack

**Frontend**
- React.js (SPA)
- Tailwind CSS for styling
- Framer Motion for smooth animations
- Chart.js / `react-chartjs-2` for skill visualizations
- Axios for API calls

**Backend**
- Flask (Python)
- SQLite for storing contact messages
- `python-dotenv` for environment/config management
- `smtplib` + Gmail App Passwords for email notifications (optional)

**Other Tools & Skills**
- Python, NumPy, Pandas, Scikit‑Learn, TensorFlow/Keras
- Tableau, Matplotlib, Seaborn, Plotly
- Git & GitHub, VS Code / Cursor

---

## 🔹 Portfolio Structure

**Frontend (`frontend/`)**
- `src/components/Home.jsx` – Hero section with:
  - Professional static profile image wrapped in a **futuristic HUD‑style circular ring**.
  - Neon blue glowing outer ring with interactive rotation that responds to mouse movement.
  - Dynamic typewriter roles (AI & ML Engineer, Data Scientist, etc.).
  - Role‑based **“Download Resume”** modal (Data Analyst, AI & ML Engineer, Data Scientist, Business Analyst, General Resume).
- `src/components/Projects.jsx` – Detailed project cards for:
  - AI ModelHub projects (multiple models under one hub).
  - Internship projects like **Email Spam Detection**, **Car Price Prediction**, **Unemployment Analysis** with metrics and visualization galleries.
  - An ongoing **Conversational AI Tutor (RAG)** project and future project ideas.
  - Image sliders for charts and analysis screenshots.
- `src/components/Certificates.jsx` – Dedicated **Certificates** section with:
  - Auto‑advancing spotlight carousel.
  - Category filters (Internships, Courses, Achievements).
  - Embedded PDF previews for certificates hosted under `public/certificates`.
- `src/components/Skills.jsx` – **My Skills** section:
  - Category tabs (Programming, AI & ML, Visualization, Frameworks & Tools).
  - Interactive bar chart + doughnut chart based on real proficiency levels.
  - Detailed grid with animated progress bars.
- `src/components/Contact.jsx` – **Get In Touch** page:
  - Clean “Let’s Connect” card with my **email, phone, and location**.
  - Social links (GitHub, LinkedIn, Twitter/X).
- `src/components/Navbar.jsx`, `Footer.jsx`, `About.jsx` – Global navigation, about section, and footer.

**Backend (`backend/`)**
- `app.py` – Flask app exposing:
  - `/api/projects` – sample project data (initially) for experimentation.
  - `/api/skills` – skills structured by category.
  - `/api/contact` – endpoint to accept contact messages from the frontend and store them in SQLite (`portfolio.db`).
  - `send_email_notification()` – optional email notification function that can send:
    - A notification email to **me (`madesh6554@gmail.com`)**.
    - A confirmation email back to the sender.
- `EMAIL_SETUP.md` – Step‑by‑step guide to configure Gmail App Password and `.env` file for secure email sending.
- `requirements.txt` – Backend dependencies.

---

## 🔹 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/madesh6554/Madesh-M-_AI-DS_Portfolio-.git
cd Madesh-M-_AI-DS_Portfolio-
```

### 2. Backend setup (`backend/`)

```bash
cd backend
python -m venv venv
venv\Scripts\activate         # On Windows
pip install -r requirements.txt

# (optional) create .env from EMAIL_SETUP.md if you want email notifications
python app.py                 # runs on http://localhost:5000
```

### 3. Frontend setup (`frontend/`)

```bash
cd ../frontend
npm install
npm start                     # runs on http://localhost:3000
```

The React app will fetch data and send contact requests to the Flask backend at `http://localhost:5000`.

---

## 🔹 Key Features

- **Modern Hero Section**
  - Static portrait with **glowing, rotating outer HUD ring** that responds to cursor movement.
  - Dark sci‑fi theme, but still clean and professional for recruiters.
  - Clear CTAs: “View My Work”, “Download Resume” (with role selection).

- **Projects Showcase**
  - Real internship projects with genuine datasets and Jupyter notebooks.
  - Visualization galleries and sliders for charts.
  - Ongoing Conversational AI Tutor (RAG + STT + TTS) and upcoming AI project ideas.

- **Certificates & Achievements**
  - Auto‑sliding spotlight view and full grid.
  - Correct titles and PDF previews embedded in the UI.

- **Skills Visualization**
  - Chart‑based overview (bar + doughnut) and detailed progress bars.
  - Skills inferred from **actual projects and certificates**, not random numbers.

- **Contact & Communication**
  - Clear direct contact info (email, phone, location, social links).
  - Optional backend email notifications via Gmail App Password (documented in `EMAIL_SETUP.md`).

---

## 🔹 Deployment

This repo is designed so that:
- The **frontend** can be deployed on platforms like Vercel, Netlify, or GitHub Pages (with a small tweak).
- The **backend** can be deployed separately (Render, Railway, etc.) if email/contact API is required in production.

The code is organized to be easy to extend with more projects, certificates, or skill categories as my experience grows.

---

## 🔹 About Me

I’m **Madesh M**, an **AI & ML Engineer / Data Scientist** with strong foundations in mathematics, statistics, and hands‑on data science.  
This portfolio is not just a UI; it’s a reflection of my real work in **building, deploying, and explaining** data‑driven solutions.

If you’re interested in collaborating, hiring, or discussing AI/ML ideas, feel free to reach out:
- **Email**: `madesh6554@gmail.com`  
- **GitHub**: `https://github.com/madesh6554`  
- **LinkedIn**: `https://linkedin.com/in/madesh-m-15037b273`


