A full-stack price comparison system that compares grocery offers from Aldi and Lidl using a FastAPI backend, scraping layer, PostgreSQL database, and React frontend.

🚀 Project Overview

This project collects grocery offers from different stores and allows users to compare prices in a simple UI.

🧠 Features
🛒 Compare products (Milk, Bread, etc.)
🧹 Web scraping (Aldi working, Lidl fallback layer)
⚡ FastAPI backend
🗄 PostgreSQL database integration
🌐 React + Vite frontend
🔄 Auto data refresh via scraper
📊 Clean UI for product comparison

🏗 Architecture
Frontend (React + Vite)
        ↓
FastAPI Backend
        ↓📁 Project Structure
Super_Offer_Flat_AI/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── scraper/
│   │   ├── run_scraper.py
│   │   ├── aldi_scraper.py
│   │   └── lidl_scraper.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml
└── README.md
Scraper Layer (Aldi + Lidl)
        ↓
PostgreSQL Database

⚙️ Backend Setup (FastAPI)

1. Create virtual environment
python -m venv venv
venv\Scripts\activate
2. Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary requests beautifulsoup4 playwright
python -m playwright install
3. Run backend
cd backend
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000
📡 API Endpoints
🟢 Health Check
GET /

Response:

{"message": "Backend Running 🚀"}
🟡 Scrape Data
GET /scrape

✔ Fetches data from Aldi (working)
✔ Lidl uses fallback/experimental scraping

🔵 Compare Products
GET /compare/{product}

Example:

/compare/Milk

Response:

[
  {
    "product": "Milk",
    "store": "Aldi",
    "price": 1.29
  }
]

🗄 Database (PostgreSQL)
Start DB using Docker
docker-compose up -d
Connect to DB
docker exec -it postgres-db psql -U admin -d offersdb
View data
SELECT * FROM offers;

🌐 Frontend Setup (React + Vite)
1. Install dependencies
cd frontend
npm install

3. Run frontend
npm run dev

Frontend runs at:

http://localhost:5173
🧪 UI Features
Dropdown to select product (Milk, Bread, Rice)
Shows Aldi vs Lidl comparison
Auto-fetches backend API
Responsive design using Tailwind CSS
🧹 Scraper Logic
Aldi Scraper
Returns structured product list
Works reliably with static data extraction
Lidl Scraper
Uses Playwright-based navigation
Limited due to:
JavaScript rendering
Anti-bot protection
Dynamic API loading

👉 Currently uses fallback/hybrid approach

⚠️ Known Limitations
Lidl data is unstable due to anti-scraping measures
Prices may be placeholder or fallback values

Scraper structure may change if websites update UI
🚀 Next Improvements (Roadmap)
🔥 Backend Enhancements

Improve Lidl API scraping (network interception)
Add caching layer (Redis)
Add scheduled scraping jobs

⚙️ DevOps
Dockerize full system
Jenkins CI/CD pipeline
Kubernetes deployment (CronJobs for scraper)
GitOps (ArgoCD)

📊 Observability
Grafana dashboards
Prometheus metrics
Logging with Loki

🤖 AI Layer
Cheapest store predictor
Smart deal recommendation engine

🧠 Tech Stack
FastAPI
React + Vite
PostgreSQL
Playwright
BeautifulSoup
Docker
Jenkins (planned)
Kubernetes (planned)






