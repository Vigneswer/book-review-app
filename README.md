
# 📚 Book Review App

A backend API service built with **FastAPI**, **SQLite**, and **SQLAlchemy** for managing books and their reviews.

---

## ✅ Features

- Add and list books
- Post and retrieve reviews for each book
- In-memory cache for fast `GET /books`
- SQLite database integration using SQLAlchemy
- Unit tests with Pytest
- OpenAPI docs via Swagger UI

---

## 📘 How to Run the Service

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vigneswer/book-review-app.git
cd book-review-app
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate     # On Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

➡️ Open in browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔄 Database Setup / "Migration"

Since this uses **SQLite + SQLAlchemy**, no migration tool is needed — just run:

### 📌 Option A: From Python shell

```python
from app.models.database import Base, engine
from app.models import models
Base.metadata.create_all(bind=engine)
```

### 📌 Option B: Add a reset script (`reset_db.py`)

```python
from app.models.database import Base, engine
from app.models import models

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
```

Then run:

```bash
python reset_db.py
```

---

## 🧪 Run Tests

Tests are written using **Pytest**.

### ✅ Run with:

```bash
$env:PYTHONPATH="."
pytest
```

> On Mac/Linux:

```bash
PYTHONPATH=. pytest
```

### Included tests:

- `test_get_books()` – confirms book list returns successfully
- `test_add_book()` – checks book addition API

---

## 📁 Project Structure

```
book-review-app/
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── books.py
│   ├── models/
│   │   ├── models.py
│   │   └── database.py
│   └── tests/
│       └── test_main.py
├── README.md
└── .gitignore
```

---

## 🧾 Tech Stack

- **FastAPI** – Backend framework
- **SQLite** – Lightweight DB
- **SQLAlchemy** – ORM
- **Uvicorn** – ASGI server
- **Pytest** – Testing framework

---

## 📄 License

This project is open for review and educational purposes.
