# PHISHING-URL-DETECTOR
Phishing URL detection system built using Machine Learning and Flask. The application analyzes URL features and predicts whether a website is safe or malicious. Designed with a cyber-themed UI and trained using a Random Forest model for real-time phishing detection.
# AI Phishing URL Detector

## Problem Statement

Phishing websites are a major cybersecurity threat. These malicious websites trick users into revealing sensitive information such as passwords, banking details, and personal data. Many users are unable to distinguish between legitimate and fake URLs, which leads to security breaches.

This project aims to build a phishing URL detection system that analyzes URLs and predicts whether they are safe or malicious.

---

## Solution

This project uses Machine Learning with Python to detect phishing URLs based on various features such as:

- URL length
- Presence of HTTPS
- Suspicious keywords
- Special characters
- IP address detection
- Number of digits in URL

The system extracts these features and feeds them into a trained ML model that predicts whether the URL is phishing or safe.

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- HTML/CSS
- Machine Learning
- Random Forest Classifier

---

## Project Structure

```
phishing-detector
│
├── app.py
├── train_model.py
├── feature_extractor.py
├── phishing_model.pkl
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

## How to Run the Project

### Step 1: Install Dependencies

```
pip install flask pandas scikit-learn numpy
```

### Step 2: Train Model

```
python train_model.py
```

### Step 3: Run Application

```
python app.py
```

### Step 4: Open Browser

```
http://127.0.0.1:5000
```

---

## How It Works

1. User enters a URL
2. System extracts features
3. ML model analyzes URL
4. Prediction is generated
5. UI displays Safe / Phishing

---

## Example Test URLs

Phishing:
```
http://secure-login-paypal.com
http://verify-bank-account.com
http://free-bonus-claim-now.net
```

Safe:
```
https://google.com
https://github.com
```

---

## Features

- AI-based phishing detection
- Real-time URL analysis
- Confidence score
- Cyber-themed UI
- Lightweight and fast

---

## Future Improvements

- Use larger dataset
- Add browser extension
- Add blacklist API
- Improve accuracy
- Deploy online

---

## Author

Student Project – Phishing URL Detection System
