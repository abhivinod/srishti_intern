# Model Deployment

Building a model is only half the work; making it accessible is the other half. This folder contains scripts and applications focused on taking trained machine learning models and deploying them.

## Directory Structure
* **`Basics/`:** Contains introductory scripts (`app.py`, `simple_ml.py`) to understand the mechanics of serving a Python-based ML model as a web application.
* **`deployed_projects/`:** Contains the deployment code for specific projects. Currently includes `iris_app.py`, which serves predictions based on the Iris dataset model.

**Tech Stack:** Python, Flask/Streamlit (depending on the framework used in `app.py`).