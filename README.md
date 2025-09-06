# DeepCure: ADC Activity Prediction Prototype

This project is an interactive web application built with Streamlit that serves as a functional prototype for the "DeepCure" platform. It simulates the platform's core functionality: predicting the efficacy of Antibody-Drug Conjugates (ADCs) based on their constituent parts.

![Logo](https://github.com/SnackitPal/DeepCure-Prototype/blob/main/Logo%20of%20DeepCure.png?raw=true)

## 🚀 Features

- **Interactive UI**: A clean and user-friendly interface to input ADC components.
- **Simulated Predictions**: Demonstrates the potential output of the AI model by using two hard-coded case studies (one active, one inactive) based on real-world scientific data.
- **Educational Component**: Includes an animated GIF and a clear explanation of what ADCs are and how they work.
- **Real-World Data**: The case studies are populated with actual protein sequences and SMILES strings to provide a scientifically authentic experience.

## 🛠️ Setup & Installation

Follow these steps to run the application locally.

### 1. Prerequisites

- Python 3.7+
- `pip` for package installation

### 2. Create a Virtual Environment

It is highly recommended to run this project in a dedicated virtual environment.

```bash
# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

The required Python packages are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## 🏃‍♀️ Running the Application

Once the dependencies are installed, you can run the Streamlit application with a single command:

```bash
streamlit run app.py
```

This will open a new tab in your default web browser with the running application.

## 🌐 Deployment

This application is deployed on the Streamlit Community Cloud and is publicly accessible.

> **Note**: The public link will be added here once the deployment is complete.
