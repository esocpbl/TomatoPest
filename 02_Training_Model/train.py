from ultralytics import YOLO

if __name__ == '__main__':
    # 1. Load model dasar (Nano version - paling ringan)
    model = YOLO('yolov8n.pt') 

    # 2. Mulai Training
    # Pastikan file data.yaml ada di folder 01 atau arahkan path-nya dengan benar
    # results akan otomatis tersimpan di folder 'runs'
    model.train(
        data=r'C:\Users\ASUS\OneDrive\01_Persiapan_Data\data.yaml',  # Mundur satu folder untuk cari data.yaml
        epochs=50, 
        imgsz=640, 
        batch=16,
        name='hasil_training_tomat'
    )