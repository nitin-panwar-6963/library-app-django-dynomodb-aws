# 📚 Library Registration System (Django + DynamoDB)

A modern **Library Registration Web App** built with **Django**, **AWS DynamoDB**, and **Docker**, featuring a **premium dark UI** and scalable cloud-ready architecture.

---

## 🚀 Features

* 🔐 User Registration & Login
* 🌙 Premium Dark Theme UI (Glassmorphism)
* ☁️ AWS DynamoDB Integration (NoSQL Database)
* 🐳 Dockerized Setup
* ⚡ Fast & Lightweight (No traditional DB needed)
* 📱 Responsive Design

---

## 🏗️ Tech Stack

* **Backend:** Django
* **Database:** AWS DynamoDB
* **Frontend:** HTML, Bootstrap 5 (Dark UI)
* **Cloud:** AWS
* **Containerization:** Docker & Docker Compose

---

## 📁 Project Structure

```
library_app/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── .env
│
├── app/
│   ├── manage.py
│   ├── config/
│   ├── library/
│   ├── templates/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/library-app.git
cd library-app
```

---

### 2️⃣ Create `.env` File

```
SECRET_KEY=your_secret_key

AWS_REGION=ap-south-1
DYNAMODB_TABLE=LibraryUsers
```

> ⚠️ If running on EC2, **do NOT add AWS keys**. Use IAM Role instead.

---

### 3️⃣ Create DynamoDB Table

Go to AWS Console → DynamoDB

```
Table Name: LibraryUsers
Primary Key: email (String)
```

---

### 4️⃣ Run with Docker

```
docker-compose up --build
```

---

### 5️⃣ Open in Browser

```
http://localhost:8000
```

---

## ☁️ AWS Configuration

### ✅ Recommended (Production)

Use **IAM Role** with EC2 instead of access keys.

* Attach role to EC2
* Add permission: `AmazonDynamoDBFullAccess`

---

### ❌ Not Recommended

* Hardcoding AWS keys in `.env`

---

## 🧪 How It Works

```
User Form → Django Views → boto3 → DynamoDB → Stored Data
```

---

## 📊 Viewing Data in DynamoDB

1. Open AWS Console
2. Go to DynamoDB
3. Select Table: `LibraryUsers`
4. Click **Explore Items**

---

## 🔐 Security Improvements (Recommended)

* Use password hashing (`bcrypt`)
* Add Django authentication system
* Implement JWT/Auth sessions

---

## 🚀 Future Enhancements

* 📚 Book Management System (Add / Issue / Return)
* 👨‍💼 Admin Dashboard
* 📊 Analytics Dashboard
* ⚛️ React Frontend (Modern UI)
* ☁️ Full AWS Deployment (EC2 + Nginx + S3)

---

## 🐳 Docker Commands

```
docker-compose up --build
docker-compose down
```

---

## ⚠️ Common Issues

### ❌ ModuleNotFoundError: config

✔ Fix Docker working directory to `/app/app`

---

### ❌ DynamoDB not connecting

✔ Check region, table name, IAM role

---

## 👨‍💻 Author

**Nitin Panwar**
B.Tech CSE | Django & AWS Developer

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🛠️ Contribute

---

## 📜 License

This project is licensed under the MIT License.
