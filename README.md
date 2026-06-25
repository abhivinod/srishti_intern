<!-- Badges Section -->
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
# 🚀 AI/ML Internship Projects

This repository contains my project work during my AI/ML internship at Srishti Innovative. It covers a full machine learning pipeline: from data manipulation and exploratory data analysis (EDA) to model training and interactive web deployment.

## 📁 Repository Structure

* **`libraries/`**: Jupyter notebooks for foundational data science tools (NumPy, Pandas, Matplotlib).
* **`projects/`**: Core machine learning and deep learning models (includes datasets, notebooks, and exported models).
  * *Iris_EDA*: Exploratory Data Analysis on the Iris dataset.
  * *Decision_Trees*: Classification for Social Network Ads and Iris flowers.
  * *Logistic_Regression_Ads*: Logistic Regression and SVM models.
  * *KMeans_Clustering*: Unsupervised learning for mall customer segmentation.
  * *ANN_Customer_Churn*: Deep learning model predicting bank customer churn.
* **`model_deployment/`**: Interactive web applications built with Streamlit to test the models in a user-friendly UI.

## ⚙️ Quick Setup

**1. Clone the repository**
`git clone https://github.com/abhivinod/srishti_intern.git`
`cd srishti_intern

**2. Create & Activate a Virtual Environment**
Windows: `python -m venv venv` then `venv\Scripts\activate`
Mac/Linux: `python3 -m venv venv` then `source venv/bin/activate`

**3. Install Dependencies**
`pip install -r requirements.txt`

## 💻 How to Run

**Option A: Explore Data & Training (Jupyter)**
To view the code and model training steps, start the Jupyter server and open the `.ipynb` files in the `libraries` or `projects` folders:
`jupyter notebook`

**Option B: Run the Deployed Web Apps (Streamlit)**
To interact with the final models through a web interface, run these commands in your terminal:
`streamlit run model_deployment/Basics/app.py`
`streamlit run model_deployment/deployed_projects/iris_app.py`