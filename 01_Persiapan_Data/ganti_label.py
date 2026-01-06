import os

# ================= KONFIGURASI =================
# Pastikan alamat folder ini benar sesuai laptopmu
folder_path = r"C:\Users\ASUS\Proyek_Deteksi_Hama_Tomat\images"

# MENGUBAH DARI 0 (Kutu Kebul) MENJADI 1 (Helicoverpa)
target_lama = '0'
target_baru = '1' 

# Rentang nomor file yang mau diperbaiki (101 sampai 200)
mulai = 101
selesai = 200
# ===============================================

print(f"--- MEMULAI OPERASI PERBAIKAN LABEL ---")
print(f"Target: Mengubah class {target_lama} menjadi {target_baru}")
print(f"Rentang File: {mulai} s.d {selesai}")
print("-" * 40)

count_berhasil = 0

for i in range(mulai, selesai + 1):
    # Nama file: data_hama_01 (101).txt
    nama_file = f"data_hama_01 ({i}).txt"
    lokasi_file = os.path.join(folder_path, nama_file)

    # Cek apakah file ada
    if os.path.exists(lokasi_file):
        # 1. BACA FILE
        with open(lokasi_file, 'r') as file:
            baris_data = file.readlines()

        data_baru = []
        perubahan = False

        # 2. CEK SETIAP BARIS
        for baris in baris_data:
            bagian = baris.strip().split()
            
            # Pastikan baris tidak kosong
            if len(bagian) > 0:
                # Jika angka depannya '0', ganti jadi '1'
                if bagian[0] == target_lama:
                    bagian[0] = target_baru
                    perubahan = True
                
                # Gabungkan kembali
                data_baru.append(" ".join(bagian) + "\n")
        
        # 3. SIMPAN PERUBAHAN
        if perubahan:
            with open(lokasi_file, 'w') as file:
                file.writelines(data_baru)
            print(f"[BERHASIL] {nama_file} label diubah ke {target_baru}")
            count_berhasil += 1
        else:
            print(f"[LEWAT] {nama_file} tidak perlu diubah (sudah benar/beda label).")
            
    else:
        print(f"[ERROR] {nama_file} tidak ditemukan!")

print("-" * 40)
print(f"SELESAI! Total {count_berhasil} file berhasil diperbaiki.")