from ultralytics import YOLO
import glob
import os

# 1. Panggil Model
model = YOLO('best.pt')

# 2. Tentukan lokasi folder gambar TEST (Sesuaikan dengan laptopmu)
# Contoh: C:/Users/ASUS/Proyek_Deteksi_Hama_Tomat/dataset_final/test/images
folder_test = r"C:\Users\ASUS\Proyek_Deteksi_Hama_Tomat\dataset_final\test\images"

# Ambil semua file .jpg di folder itu
gambar_list = glob.glob(os.path.join(folder_test, "*.jpg"))

if len(gambar_list) > 0:
    print(f"Sedang mengetes {len(gambar_list)} gambar...")
    
    # 3. Prediksi Semuanya Sekaligus
    # save=True artinya simpan gambar hasil deteksi
    results = model.predict(source=folder_test, save=True, conf=0.25)
    
    print("Selesai! Cek folder 'runs/detect/predict' untuk lihat hasilnya.")
else:
    print("Tidak ditemukan gambar jpg di folder tersebut. Cek path-nya lagi.")