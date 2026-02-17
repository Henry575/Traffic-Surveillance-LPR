# 🚦 Traffic Surveillance System using YOLOv8 & OCR

An AI-powered Traffic Surveillance System that detects vehicles using YOLOv8, extracts license plate numbers using OCR, and validates vehicle documents such as RC, Insurance, and PUC.

---

## 📌 Project Overview

This project demonstrates a modular Computer Vision pipeline for:

- Vehicle Detection using YOLOv8
- License Plate Text Extraction using EasyOCR
- Indian License Plate Format Validation using Regex
- Document Expiry Verification using a Mock Vehicle Database

The system simulates a real-world smart traffic monitoring solution.

---

## 🛠️ Tech Stack

- Python 3.10
- OpenCV
- YOLOv8 (Ultralytics)
- EasyOCR
- PyTorch
- NumPy
- Regex (Pattern Validation)

---

## 🏗️ Project Architecture

Traffic-Surveillance-LPR
│
├── assets/ # Input images & demo screenshots
├── models/ # YOLO model (ignored in Git)
├── outputs/ # Generated results (ignored in Git)
├── src/
│ ├── main.py
│ ├── plate_detection.py
│ └── ocr_reader.py
│
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ System Workflow

1. Load input vehicle image
2. Detect vehicle using YOLOv8
3. Crop detected vehicle region
4. Extract license plate text using EasyOCR
5. Validate Indian license plate format using Regex
6. Check RC, Insurance, and PUC expiry status
7. Display document validation results

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Traffic-Surveillance-LPR.git
cd Traffic-Surveillance-LPR
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add YOLO Model
Download YOLOv8 model from Ultralytics and place it inside:

models/yolov8n.pt
4️⃣ Run the System
python src/main.py
📷 Sample Output
Example Console Output:

🚗 Detecting license plate...
Vehicle detected successfully.

🔍 Reading plate number...
Detected Vehicle Number: MH20EE7602

📋 Checking Document Status...
RC Expiry: ✅ VALID
Insurance Expiry: ❌ EXPIRED
PUC Expiry: ❌ EXPIRED
🎯 Key Features
Modular and scalable architecture

Real-time vehicle detection logic

Regex-based Indian plate validation

Automated document verification simulation

Clean separation of detection, OCR, and validation layers

🚀 Future Improvements
Real-time CCTV video feed integration

Database connectivity (MySQL / Firebase)

Blacklisted vehicle detection

Automatic challan generation

Deployment as Web Application

👨‍💻 Author
Vishnu Prasath
Software Engineering Student
Interested in AI, ML & Computer Vision