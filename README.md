# 🤖 AI Chatbot (FastAPI + Gemini + Redis)

A lightweight **AI-powered chatbot** built with **FastAPI**, **Google Gemini API**, and **Redis** for caching responses.  
This project demonstrates modern API integration, containerization, and environment-based key management.

---

## 🚀 Features
- 💬 Generates intelligent responses using **Google Gemini API**
- ⚡ Built with **FastAPI** — high-performance web framework
- 🧠 **Redis caching** for improved performance
- 🐳 Fully containerized with **Docker Compose**
- 🔒 Secure **environment variable** handling via `.env` file
- 🔧 Ready for local or cloud deployment

---

## 🗂️ Project Structure
AI-Chatbot/
│
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── ai_engine.py # Gemini API integration
│ ├── cache.py # Redis caching logic
│ └── requirements.txt # Python dependencies
│
├── docker-compose.yml # Multi-service setup (FastAPI + Redis)
├── Dockerfile # Container build instructions
├── .env # Environment variables (not tracked)
├── .gitignore # Ignore sensitive/local files
└── README.md # Documentation


---

## ⚙️ Prerequisites
Before running the project, ensure the following are installed:

- 🐍 [Python 3.10+](https://www.python.org/downloads/)
- 🐳 [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- 💻 [VS Code](https://code.visualstudio.com/)

---

## 🔑 Environment Variables
Create a `.env` file in the **project root** (same level as `docker-compose.yml`):

.env

GEMINI_API_KEY=your_gemini_api_key_here
REDIS_HOST=redis
REDIS_PORT=6379


> ⚠️ Do not commit your `.env` file or Gemini API key to GitHub.

---

## 🐳 Run with Docker

### 1️⃣ Build and start services
```bash
docker-compose up --build

```

curl -X POST http://127.0.0.1:8000/chat \
-H "Content-Type: application/json" \
-d '{"message": "Hello!"}'

🧪 Testing the API

You can test the endpoints using any of these:

🧭 Swagger UI → http://127.0.0.1:8000/docs

🧩 Postman

🧾 cURL

🧠 VS Code REST Client

| Command                     | Description                    |
| --------------------------- | ------------------------------ |
| `docker-compose up --build` | Build and start all containers |
| `docker-compose down`       | Stop and remove containers     |
| `docker logs chatbot-1`     | View FastAPI logs              |
| `redis-cli ping`            | Test Redis connection          |

