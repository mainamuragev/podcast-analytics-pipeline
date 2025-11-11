---

## 🎙️ Joe Rogan Podcast Analytics Pipeline

A real-time data pipeline engineered to extract, transform, and visualize YouTube performance metrics for the **Joe Rogan Experience**. Built for modularity, transparency, and recruiter-facing clarity — with full containerization and local relevance.

---

### 🚀 Features

- **Automated ingestion** of Joe Rogan podcast episodes via `yt-dlp`
- **Structured transformation** using `pandas` and `PySpark`
- **Clean PostgreSQL schema** optimized for analytics
- **Airflow DAGs** for orchestrated, reproducible workflows
- **Grafana dashboards** for real-time metrics (views, likes, comments, CTR)
- **Docker Compose** setup for seamless local deployment

---

### 🛠️ Tech Stack

| Layer         | Tools Used                                      |
|--------------|--------------------------------------------------|
| Ingestion     | `yt-dlp`, Airflow                               |
| Transformation| `pandas`, `PySpark`                             |
| Storage       | PostgreSQL                                      |
| Orchestration | Apache Airflow                                  |
| Visualization | Grafana                                         |
| Containerization| Docker Compose                                |

---

### 📦 Folder Structure

```
joe-rogan-analytics/
├── dags/                  # Airflow DAGs for ingestion & transformation
├── data/                  # Raw and processed data
├── notebooks/             # Exploratory analysis and schema design
├── grafana/               # Dashboard configs and provisioning
├── docker-compose.yml     # Full pipeline orchestration
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

---

### 📈 Sample Metrics Tracked

- Total views per episode
- Like-to-view ratio
- Comment volume and sentiment (optional NLP module)
- Click-through rate (CTR) estimates
- Episode duration vs engagement

---

### 🧪 Local Deployment

```bash
# Clone the repo
git clone https://github.com/yourusername/joe-rogan-analytics.git
cd joe-rogan-analytics

# Start the pipeline
docker-compose up --build

# Access Airflow UI
http://localhost:8080

# Access Grafana dashboards
http://localhost:3000
```

---

### 📣 Why This Project?

This pipeline showcases:
- Real-time ingestion and transformation of public media data
- Modular architecture for scaling across podcasts or channels
- Recruiter-facing dashboards with clear, actionable insights
- Local relevance for media analytics in Kenya and beyond

---
