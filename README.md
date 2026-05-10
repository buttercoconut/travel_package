# README.md
# Travel Package Application

## Overview
This repository contains a full-stack application for managing travel packages. The backend is built with FastAPI and the frontend with Vue 3 and Vite.

## Prerequisites
- Docker & Docker Compose
- Node.js (for local dev, optional)

## Running with Docker Compose
```bash
# Build and start services
docker-compose up --build
```

The backend will be available at `http://localhost:8000` and the frontend at `http://localhost:5173`.

## Development
### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints
- `GET /packages/` – List all packages
- `POST /packages/` – Create a new package
- `GET /packages/{id}` – Retrieve a package
- `PUT /packages/{id}` – Update a package
- `DELETE /packages/{id}` – Delete a package

## License
MIT
