# 🍅 Tomato Pest Detection System (YOLOv8)

This system is designed to help farmers detect tomato pests automatically using Artificial Intelligence.

## 🎯 Key Features
- **Automatic Detection:** Uses the lightweight and fast YOLOv8 Nano model.
- **3 Pest Types:** Capable of recognizing Silverleaf Whitefly, Helicoverpa armigera, and Aphids.
- **Treatment Recommendations:** Provides pesticide and prevention recommendations based on the detected pest.

## 📂 Project Structure
This project is organized based on the development workflow:
1. **01_Persiapan_Data**: Scripts for splitting the dataset and configuration files (`data.yaml`).
2. **02_Training_Model**: Training scripts, evaluation, and the AI model file (`best.pt`).
3. **04_Hasil_Model**: Testing, training, and validation results in image format.
4. **03_Aplikasi_Web**: Source code for the Streamlit-based web application.

## 🚀 How to Run (Installation)
1. Clone this repository.
2. Navigate to the application folder: `cd 03_Aplikasi_Web`
3. Install libraries: `pip install -r requirements.txt`
4. Run the application: `streamlit run app.py`

---
*Created by: - PBL_Society 2026*