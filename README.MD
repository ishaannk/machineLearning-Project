# 🎓 Student Performance Predictor

An end-to-end machine learning project that predicts student math scores and risk levels based on demographic and academic features. Deployed on AWS Elastic Beanstalk with a production-ready Flask web application.

**🌐 Live Demo:** [http://student-performance-env.eba-cvqd8nbt.us-west-2.elasticbeanstalk.com/](http://student-performance-env.eba-cvqd8nbt.us-west-2.elasticbeanstalk.com/)

## 🚀 Key Features

- **End-to-End ML Pipeline**: Modular architecture with data ingestion, transformation, training, and prediction pipelines
- **Model Comparison**: Evaluates 7+ algorithms (Random Forest, XGBoost, CatBoost, Gradient Boosting, etc.) with hyperparameter tuning
- **MLOps Integration**: MLflow + DagsHub for experiment tracking and model versioning
- **Production Deployment**: Dockerized Flask app deployed on AWS Elastic Beanstalk
- **Risk Classification**: Automatically categorizes students as Low/Medium/High risk based on predicted scores

## 🛠️ Tech Stack

**Machine Learning:**
- Scikit-learn, CatBoost, XGBoost
- GridSearchCV for hyperparameter optimization
- Custom preprocessing pipeline (OneHotEncoder, StandardScaler)

**MLOps & Deployment:**
- MLflow for experiment tracking
- DagsHub for model registry
- Docker for containerization
- AWS Elastic Beanstalk for cloud deployment

**Web Framework:**
- Flask (RESTful API)
- HTML/CSS frontend

**Data Engineering:**
- Pandas, NumPy
- MySQL integration support
- Custom exception handling & logging

## 📊 Model Performance

The pipeline automatically selects the best-performing model based on R² score, RMSE, and MAE metrics. Models are evaluated using cross-validation and logged to MLflow for reproducibility.

## 🏗️ Project Structure

```
mlproject1/
├── src/mlproject/
│   ├── components/          # Data ingestion, transformation, training
│   ├── pipelines/           # Training & prediction pipelines
│   └── utils.py             # Helper functions
├── artifacts/               # Trained models & preprocessors
├── flask_app.py            # Production Flask application
├── Dockerfile              # Container configuration
└── requirements.txt        # Dependencies
```

## 🚦 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mlproject1
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**
   ```bash
   python app.py
   ```

4. **Run the Flask app**
   ```bash
   python flask_app.py
   ```

5. **Access the web interface**
   - Open `http://localhost:5000` in your browser

## 📝 Usage

Input student features (gender, ethnicity, parental education, lunch type, test preparation, reading/writing scores) to predict:
- **Math Score**: Predicted numerical score (0-100)
- **Risk Level**: Low 🟢 (≥80), Medium 🟡 (50-79), High 🔴 (<50)

## 🔧 Key Highlights for Recruiters

✅ **Production-Ready**: Fully deployed and accessible web application  
✅ **Best Practices**: Clean code architecture, error handling, logging  
✅ **MLOps Expertise**: Experiment tracking, model versioning, reproducibility  
✅ **Cloud Deployment**: AWS Elastic Beanstalk with Docker containerization  
✅ **Model Engineering**: Automated model selection, hyperparameter tuning, preprocessing pipelines  

---

**Built with ❤️ using Python, Flask, and AWS**
