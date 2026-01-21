```markdown
---
title: Drinks Ordering System API & Menu
status: active
tags: [FastAPI, Python, SQLAlchemy, Vue.js, Alembic, SQLite]
vision: "To provide a scalable, real-time platform for managing drink menus and facilitating customer orders."
---

## Description

The Drinks project is a full-stack application designed for managing a dynamic drinks menu and handling customer orders. It is structured as a mono-repository containing a Python API backend and a separate Vue.js frontend client.

The **Backend API** is built on FastAPI and SQLAlchemy, providing endpoints for managing drinks, tracking user sessions (including temporary guest users), handling physical `Coasters` (potential device mapping), and processing orders. It uses Alembic for database migrations against a default SQLite database.

The **Frontend Client** (located in `drinks-menu/`) is a Vue 3 application that serves as the visual menu and ordering interface.

## Setup/Installation

This project requires Python 3.9+ and Node.js/npm.

### 1. Backend API Setup

The API serves the core functionality and uses a SQLite file (`drinks.db`) by default.

```bash
# 1. Install dependencies
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

# 2. Run initial database migration (creates the drinks.db file)
alembic upgrade head

# 3. Start the API server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

### 2. Frontend Client Setup

The frontend application is located in the `drinks-menu` directory.

```bash
# 1. Navigate to the client directory
cd drinks-menu

# 2. Install Node dependencies
npm install

# 3. Run the development server
npm run serve
```
The client typically runs on port 8080 and is configured to proxy requests to the backend API.

## Tech Stack

### Backend (API)

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Core programming language |
| **Web Framework** | FastAPI | High-performance asynchronous API framework |
| **ORM** | SQLAlchemy | Object Relational Mapper for database interaction |
| **Database** | SQLite (Default) | Simple file-based database for development |
| **Migrations** | Alembic | Database schema migration tool |
| **Server** | Uvicorn | ASGI server for running FastAPI |

### Frontend (Menu)

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Framework** | Vue 3 | Reactive JavaScript library for building the UI |
| **Tooling** | Vue CLI | Standardized setup and configuration |
| **Packaging** | Webpack | Module bundler (via Vue CLI) |
```