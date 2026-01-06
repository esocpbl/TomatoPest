from ultralytics import YOLO

if __name__ == '__main__':
    # 1. Panggil Otak AI yang sudah jadi (best.pt)
    # Asumsi: file best.pt kamu taruh di folder ini juga
    model = YOLO('best.pt')

    # 2. Lakukan Validasi (Ujian Ulang)
    # Ini akan menghasilkan Confusion Matrix baru dan angka mAP
    metrics = model.val(
        data=r'C:\Users\ASUS\OneDrive\01_Persiapan_Data\data.yaml', 
        split='val'  # Menggunakan data validasi
    )

    # 3. Tampilkan Hasil
    print(f"mAP50: {metrics.box.map50}")
    print(f"mAP50-95: {metrics.box.map}")