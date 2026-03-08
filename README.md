# Vue + FastAPI Monorepo Template

This is a modern monorepo template using the following tech stack:

### Frontend
- **Vue 3** + **Vite**
- **Tailwind CSS**
- **Pinia** (State Management)
- **Bun** (Package Manager & Runner)
- **Socket.IO Client**

### Backend
- **FastAPI**
- **uv** (Package Manager)
- **MongoDB** (Motor async driver)
- **Socket.IO Server** (python-socketio)

### DevOps & Tools
- **Docker Compose**
- **GitHub Actions** (CI pipeline)

## Getting Started

### Run with Docker Compose

The easiest way to start the entire stack is with Docker Compose:

```bash
docker-compose up --build
```

- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend API: [http://localhost:8000](http://localhost:8000)
- MongoDB: `localhost:27017`

### Run Locally (Without Docker)

You will need **Bun**, **uv**, and a running **MongoDB** instance.

1. **Start Backend:**
   ```bash
   cd backend
   uv pip install -r pyproject.toml
   ## or just uv pip install --system fastapi uvicorn python-socketio motor pydantic
   uv run uvicorn app.main:app --reload
   ```

2. **Start Frontend:**
   ```bash
   cd frontend
   bun install
   bun run dev
   ```

## Repository Structure

```
.
├── backend/                  # FastAPI Application
│   ├── app/
│   │   └── main.py
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/                 # Vue Application
│   ├── src/
│   │   ├── main.js
│   │   ├── App.vue
│   │   ├── style.css
│   │   └── stores/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── .github/workflows/ci.yml  # GitHub Actions Workflow
└── docker-compose.yml        # Full-stack orchestrator
```
