from ultralytics import YOLO

# 1. Load Your Best Model
# Ensure the path points correctly to your best.pt file
model = YOLO(r'C:\Users\ASUS\Proyek_Deteksi_Hama_Tomat\best.pt')

print("Starting Camera... (Press 'q' on the keyboard to STOP)")

# 2. Start Live Detection from Webcam
# source='0' means using the main laptop webcam
# show=True means displaying the video window
# conf=0.80 means only showing detections if confidence is above 80% (high accuracy)
model.predict(source='0', show=True, conf=0.80)