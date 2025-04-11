# Cardiovascular Risk Predictor

A web application built with Streamlit that predicts cardiovascular disease risk based on patient health metrics.

## 📋 Overview

This application uses a machine learning model to predict the risk of cardiovascular disease based on various health parameters. The model was trained on cardiovascular health data and provides risk assessments to help users understand their potential cardiovascular health risks.

## 🔧 Features

- User-friendly interface for inputting health parameters
- Real-time prediction of cardiovascular disease risk
- Visual representation of risk factors
- Recommendations based on prediction results

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cardio-risk-predictor.git
   cd cardio-risk-predictor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Model File

Make sure the trained model file `cardio_model.pkl` is in the root directory of the project. If you need to train the model yourself, use the provided notebook in the `model_training` directory.

### Running the Application

Run the Streamlit app:
```
streamlit run app.py
```

The application will open in your default web browser.

## 🖥️ Usage

1. Enter the required health parameters in the sidebar:
   - Age
   - Gender
   - Blood pressure (systolic & diastolic)
   - Cholesterol level
   - Blood glucose level
   - BMI (Body Mass Index)
   - Smoking status
   - Alcohol intake
   - Physical activity level
   - Family history

2. Click on the "Predict Risk" button to see your cardiovascular disease risk assessment.

3. Review the prediction results and recommendations.

## 🔬 Model Details

The prediction model was trained using [algorithm/model type] on a dataset of cardiovascular health records. The model achieved [accuracy/performance metrics] during validation.

Key features that influence the prediction include:
- Blood pressure
- Cholesterol levels
- Age
- Lifestyle factors

## 📁 Project Structure

```
cardio-risk-predictor/
├── app.py                  # Main Streamlit application
├── cardio_model.pkl        # Trained machine learning model
├── requirements.txt        # Python dependencies
├── .streamlit/             # Streamlit configuration
│   └── config.toml         # Streamlit theme configuration
├── model_training/         # Model training scripts and notebooks
│   └── train_model.ipynb   # Jupyter notebook for model training
└── data/                   # Data files (if included)
    └── processed/          # Processed datasets
```

## 📊 Development

To modify or improve the model:

1. Explore the data and model training process in `model_training/train_model.ipynb`
2. Train a new model and export it as `cardio_model.pkl`
3. Update the app.py file if your model requires different input parameters

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- Data sources: Kaggle.com
- Libraries used: Streamlit, Scikit-learn, Pandas, NumPy, Joblib
