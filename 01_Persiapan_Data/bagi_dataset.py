import os
import shutil
import random

# ================= KONFIGURASI =================
# 1. Folder tempat gambarmu sekarang (SUMBER)
source_folder = r'C:\Users\ASUS\Proyek_Deteksi_Hama_Tomat\images'

# 2. Folder baru yang akan dibuat (TUJUAN)
# Kita taruh folder baru ini di luar folder images supaya rapi
output_folder = r'C:\Users\ASUS\Proyek_Deteksi_Hama_Tomat\dataset_final'

# 3. Pembagian Data (Total harus 1.0 atau 100%)
train_ratio = 0.7  # 70% untuk latihan
val_ratio   = 0.2  # 20% untuk validasi (ulangan harian)
test_ratio  = 0.1  # 10% untuk testing (ujian akhir)
# ===============================================

def split_dataset():
    # Cek apakah folder sumber ada
    if not os.path.exists(source_folder):
        print(f"[ERROR] Folder sumber tidak ditemukan: {source_folder}")
        return

    # Kumpulkan semua file gambar (JPG, PNG, JPEG)
    files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Acak urutan file supaya tersebar merata
    random.shuffle(files)
    
    total_files = len(files)
    print(f"Total gambar ditemukan: {total_files}")
    
    # Hitung jumlah file untuk setiap bagian
    train_count = int(total_files * train_ratio)
    val_count = int(total_files * val_ratio)
    test_count = total_files - train_count - val_count # Sisa untuk test

    print(f"Akan dibagi menjadi: Train={train_count}, Val={val_count}, Test={test_count}")

    # Fungsi pembantu untuk memindahkan file
    def move_files(file_list, split_name):
        # Buat folder tujuan: dataset_final/train/images dan dataset_final/train/labels
        images_dest = os.path.join(output_folder, split_name, 'images')
        labels_dest = os.path.join(output_folder, split_name, 'labels')
        
        os.makedirs(images_dest, exist_ok=True)
        os.makedirs(labels_dest, exist_ok=True)
        
        for filename in file_list:
            # Tentukan nama file gambar dan file label (.txt)
            base_name = os.path.splitext(filename)[0]
            txt_name = base_name + ".txt"
            
            src_image = os.path.join(source_folder, filename)
            src_label = os.path.join(source_folder, txt_name)
            
            # Pindahkan Gambar
            shutil.copy(src_image, os.path.join(images_dest, filename))
            
            # Pindahkan Label (Jika ada)
            if os.path.exists(src_label):
                shutil.copy(src_label, os.path.join(labels_dest, txt_name))
            else:
                print(f"[WARNING] Label tidak ditemukan untuk gambar: {filename}")

    # Eksekusi pembagian
    print("Sedang menyalin file ke folder 'train'...")
    move_files(files[:train_count], 'train')
    
    print("Sedang menyalin file ke folder 'val'...")
    move_files(files[train_count:train_count+val_count], 'val')
    
    print("Sedang menyalin file ke folder 'test'...")
    move_files(files[train_count+val_count:], 'test')

    print("\nSUKSES! Dataset telah dibagi.")
    print(f"Lokasi dataset baru: {output_folder}")
    print("Cek foldernya sekarang!")

if __name__ == "__main__":
    split_dataset()