# 🚀 Concurrent Task Scheduler

A distributed systems inspired **Concurrent Task Scheduler** built using **Python, FastAPI, multithreading, SQLite, and a real-time monitoring dashboard**.

This project demonstrates:
- concurrent task execution
- priority-based scheduling
- dependency handling using DAG concepts
- retry mechanisms
- REST APIs
- real-time dashboard monitoring
- cloud deployment using Render

---

# 🌐 Live Demo

## 🔹 Dashboard
https://concurrent-task-scheduler.onrender.com/dashboard

## 🔹 API Documentation
https://concurrent-task-scheduler.onrender.com/docs

## 🔹 GitHub Repository
https://github.com/Praharsha08/concurrent-task-scheduler

---

# 📌 Project Overview

This system simulates how modern backend systems process multiple jobs concurrently while maintaining execution rules and scheduling order.

The scheduler:
- accepts tasks through REST APIs
- stores tasks in SQLite
- executes tasks concurrently using worker threads
- tracks retries and failures
- manages dependencies between tasks
- visualizes execution statistics through a live dashboard

---

# ✨ Key Features

## ✅ Concurrent Task Execution
- Executes multiple tasks simultaneously using multithreading
- Improves throughput and responsiveness

## ✅ Priority-Based Scheduling
- Tasks are executed based on assigned priorities
- Higher priority tasks are processed first

## ✅ Dependency Management
- Supports task dependencies using DAG-style execution
- Ensures dependent tasks execute only after prerequisite completion

## ✅ Retry Mechanism
- Failed tasks can automatically retry execution
- Improves fault tolerance and reliability

## ✅ REST API Integration
- Built using FastAPI
- Interactive Swagger API documentation included

## ✅ Real-Time Dashboard
- Live monitoring dashboard using HTML, CSS, and Jinja2
- Displays:
  - total tasks
  - completed tasks
  - failed tasks
  - queue status
  - execution duration
  - recent activity

## ✅ SQLite Database Integration
- Persistent task storage
- Lightweight and efficient local database solution

## ✅ Cloud Deployment
- Successfully deployed on Render
- Publicly accessible web application

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| Multithreading | Concurrent task execution |
| SQLite | Database storage |
| Jinja2 | Template rendering |
| HTML/CSS | Dashboard frontend |
| Uvicorn | ASGI server |
| Render | Cloud deployment |
| Git & GitHub | Version control |

---

# 🧠 System Architecture

```text
Client Request
       ↓
FastAPI REST API
       ↓
Task Scheduler
       ↓
Priority Queue + Dependency Handling
       ↓
Worker Threads
       ↓
Task Execution
       ↓
SQLite Storage
       ↓
Dashboard Monitoring
```

---

# 📂 Project Structure

```text
concurrent-task-scheduler/
│
├── api/
│   ├── server.py
│   └── task_functions.py
│
├── scheduler/
│   ├── scheduler.py
│   ├── task.py
│   └── worker.py
│
├── database/
│   └── db.py
│
├── templates/
│   └── dashboard.html
│
├── logs/
│
├── requirements.txt
├── Procfile
├── main.py
└── README.md
```

---

# ⚙️ API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API Home |
| POST | `/tasks` | Create new task |
| GET | `/tasks` | Fetch all tasks |
| GET | `/tasks/{task_id}` | Fetch single task |
| GET | `/status` | Scheduler statistics |
| GET | `/dashboard` | Real-time monitoring dashboard |
| GET | `/docs` | Swagger API documentation |

---

# 📊 Dashboard Features

The dashboard provides:
- live task statistics
- task execution table
- recent activity feed
- queue monitoring
- scheduler health monitoring
- execution duration tracking

---

# 🚀 Deployment

The project is deployed on Render using:
- FastAPI
- Uvicorn
- Procfile configuration
- requirements.txt dependency management

---

# 💡 Learning Outcomes

Through this project, I gained hands-on experience with:

- concurrent programming
- multithreading
- backend system design
- distributed systems concepts
- REST API development
- task scheduling algorithms
- dependency management using DAG concepts
- cloud deployment
- real-time monitoring dashboards
- Git & GitHub workflows

---

# 📈 Resume Highlights

- Built a distributed systems inspired concurrent task scheduler using FastAPI and multithreading
- Implemented priority-based scheduling and DAG-style dependency management
- Developed a real-time monitoring dashboard with task analytics
- Integrated SQLite for persistent task storage
- Deployed the complete application publicly on Render

---

# 🔮 Future Improvements

- Redis/RabbitMQ integration
- Docker containerization
- WebSocket-based live updates
- Authentication & authorization
- Kubernetes deployment
- Distributed worker nodes
- Celery integration
- Advanced analytics dashboard

---

# 👨‍💻 Author

## PP Praharsha

