from ultralytics import YOLO
import cv2
import os

# 1. Panggil "Otak" AI (best.pt)
# Pastikan file best.pt ada di folder yang sama
model = YOLO(r"C:\Users\ASUS\DETEKSI_HAMA_TOMAT\04_Aplikasi_Web\best (1).pt")

# 2. Tentukan gambar yang mau dites
nama_gambar = r"C:\Users\ASUS\Proyek_Deteksi_Hama_Tomat\hewan.jpg"

# Cek dulu apakah gambarnya benar-benar ada
if not os.path.exists(nama_gambar):
    print(f"Error: Gambar '{nama_gambar}' tidak ditemukan! Cek lagi nama filenya.")
else:
    print(f"Sedang memeriksa gambar: {nama_gambar} ...")

    # 3. Lakukan Deteksi
    # save=True akan menyimpan hasil gambar yang sudah ada kotak deteksinya
    # Tambahkan conf=0.1 agar AI lebih sensitif (mau menebak walau ragu-ragu)
    results = model.predict(source=nama_gambar, save=True, show=True, conf=0.1)

    print("Selesai! Hasil deteksi disimpan di folder 'runs/detect/predict'.")