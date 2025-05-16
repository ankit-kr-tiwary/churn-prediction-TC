


# Customer Churn Prediction API

This project demonstrates how to deploy a machine learning model to predict customer churn using a REST API built with Flask, and containerize it using Docker.

## Project Structure

```
churn_api/
├── app.py                   # Flask app exposing REST API
├── model/
│   └── churn_model.pkl      # Pretrained churn prediction model (RandomForest)
├── Dockerfile               # Docker container setup
├── requirements.txt         # Python dependencies
├── test_input.json          # Sample input to test the API
└── .github/
    └── workflows/
        └── main.yml         # (Optional) GitHub Actions CI/CD setup
```

---

## Getting Started

### Requirements

- Docker (for containerization)
- Python 3.11+ (if running locally without Docker)

---

##  Step-by-Step Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/churn_api.git
cd churn_api
```

> Or download the project as a `.zip` file and extract it.

### 2. (Optional) Train and Save the Model

If `churn_model.pkl` is missing, retrain it using your notebook and save:

```python
import joblib
joblib.dump(rf, 'model/churn_model.pkl')
```

### 3. Build and Run with Docker

```bash
docker build -t churn-api .
docker run -p 5000:5000 churn-api
```

### 4. Test the API

Visit the homepage:
[http://localhost:5000](http://localhost:5000)

Send a POST request to `/predict`:

```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d @test_input.json
```

---

## Sample Input (`test_input.json`)

```json
{
  "gender_Male": 1,
  "SeniorCitizen": 0,
  "Partner_Yes": 1,
  "Dependents_Yes": 0,
  "tenure": 5.2,
  "PhoneService_Yes": 1,
  "MultipleLines_No phone service": 0,
  "InternetService_Fiber optic": 1,
  "OnlineSecurity_No": 1,
  "OnlineBackup_Yes": 0,
  "DeviceProtection_No": 1,
  "TechSupport_No": 1,
  "StreamingTV_Yes": 1,
  "StreamingMovies_No": 0,
  "Contract_Month-to-month": 1,
  "PaperlessBilling_Yes": 1,
  "PaymentMethod_Electronic check": 1,
  "MonthlyCharges": 75.2,
  "TotalCharges": 300.5
}
```

---

## CI/CD (Optional)

This project optionally supports **GitHub Actions**.

### `.github/workflows/main.yml`

- Installs dependencies
- Runs basic checks or unit tests
- Can be extended to deploy containers to cloud

---

## Future Scope

| Metric           | Tool                   | Purpose                          |
|------------------|------------------------|----------------------------------|
| Model Drift      | Evidently / Alibi      | Track distribution changes       |
| API Latency      | Prometheus + Grafana   | Response monitoring              |
| Request Logs     | ELK Stack / CloudWatch | Debug & usage logs               |

---

## Deployment to cloud services

- Deploy on AWS ECS / Fargate / Lambda
- Use GCP Cloud Run or Azure Container Apps
- For large-scale use: Kubernetes (GKE, EKS)

---

## Maintainer

This project was built as part of a Data Science MLOps interview task.

---

## 📄 License

This project is for educational/demo purposes only.
