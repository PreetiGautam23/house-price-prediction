# House Price Prediction Web App — CodTech Internship (Task 3)

## Overview

This project is an end-to-end Machine Learning web application developed using Flask. It predicts the estimated price of a house based on user inputs such as area, number of bedrooms, bathrooms, and age of the house.

## Features

- Data preprocessing
- Machine Learning model using Linear Regression
- Model serialization using Joblib
- Flask web application
- User-friendly HTML/CSS interface
- Real-time prediction

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
- CSS

## Project Structure

```
HousePricePrediction/
│── app.py
│── train_model.py
│── house_prices.csv
│── model.pkl
│── README.md
│── requirements.txt
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
```

## How to Run

```bash
pip install -r requirements.txt
python train_model.py
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Deliverable

An end-to-end Machine Learning web application using Flask that demonstrates data preprocessing, model training, prediction, and deployment, fulfilling the requirements of **CodTech Data Science Internship – Task 3**.

---

*Part of the CodTech IT Solutions Data Science Internship — Task 3: End-to-End Data Science Project.*