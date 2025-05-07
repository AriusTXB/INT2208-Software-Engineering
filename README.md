### README.md

# 📰 Online News Recommender

A scalable, secure, and AI-powered news recommendation system built with **FastAPI**, **MongoDB**, and **OpenAI GPT**.

---

## 🚀 Features

- 🧠 GPT-powered summarization of news articles
- 🔍 Fast news title search
- 🔐 JWT-based authentication & RBAC
- 📊 User read statistics tracking
- 💎 Premium article subscription system
- 🔁 Personalized recommendations based on read history

---

## 🛠 Tech Stack

- **Backend:** FastAPI (Python 3.10)
- **Database:** MongoDB (with Motor async driver)
- **AI Integration:** OpenAI GPT-3.5
- **Auth:** JWT (PyJWT)
- **Containerization:** Docker + Docker Compose

---

## 📁 Project Structure

```
app/
├── controllers/       # API route controllers
├── services/          # Business logic
├── repositories/      # Database operations
├── models/            # Pydantic schemas
├── utils/             # GPT, JWT, password hashers
├── db/                # MongoDB connection
├── routes.py          # Router registration
└── main.py            # FastAPI app startup
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/online-news-recommender.git
cd online-news-recommender
```

### 2. Add environment variables
Create a `.env` file:
```env
MONGODB_URI=mongodb://localhost:27017/news_db
OPENAI_API_KEY=your_openai_key_here
JWT_SECRET=your_jwt_secret_here
```

### 3. Build and run with Docker Compose
```bash
docker-compose up --build
```
Visit: [http://localhost:8000](http://localhost:8000)

---

## 📬 API Endpoints

| Endpoint                  | Method | Description                          |
|--------------------------|--------|--------------------------------------|
| `/auth/register`         | POST   | Register a new user                  |
| `/account/profile`       | GET    | Get user profile                     |
| `/account/profile`       | PUT    | Update user profile                  |
| `/account/delete`        | DELETE | Delete user account                  |
| `/subscription/start`    | POST   | Start a premium subscription         |
| `/subscription/cancel`   | POST   | Cancel a subscription                |
| `/premium/articles`      | GET    | Get premium articles                 |
| `/news/read/{news_id}`   | GET    | Read a news article (add to history) |
| `/news/recommendations`  | GET    | Get personalized recommendations     |
| `/stats/user`            | GET    | View your reading statistics         |
| `/stats/global`          | GET    | Global engagement stats              |

Auto-generated OpenAPI docs available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests (optional)
```bash
pytest
```

---

## 👥 Authors
- Tran Xuan Bao
- Phan Hoang Dung
- Nguyen Khanh Tung
- Nguyen Dang Dao

Group 3 — INT2208 3, UET - VNU, 05/2025

---

## 📄 License
MIT — feel free to use, modify, and share.
