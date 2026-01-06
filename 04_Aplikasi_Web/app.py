import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# ==========================================
# 1. KAMUS DATA & SOLUSI (DATABASE PINTAR)
# ==========================================
# Di sini kita menyimpan resep penanganan untuk setiap hama
# Pastikan urutan ID (0, 1, 2) sesuai dengan classes.txt kamu!

solusi_hama = {
    0: { # ID 0: Kutu Kebul
        "nama": "Kutu Kebul (Bemisia tabaci)",
        "bahaya": "Menghisap cairan daun, menyebabkan daun keriting, menguning, dan kerdil. Juga membawa virus gemini.",
        "pencegahan": [
            "✅ Pasang perangkap lekat warna kuning (Yellow Sticky Trap).",
            "✅ Bersihkan gulma di sekitar tanaman (sanitasi).",
            "✅ Gunakan varietas tomat yang tahan virus."
        ],
        "penanganan": [
            "💊 Semprotkan insektisida nabati (minyak mimba/neem oil).",
            "💊 Gunakan musuh alami seperti kumbang macan (Menochilus sexmaculatus).",
            "💊 Jika parah, gunakan insektisida berbahan aktif Imidakloprid (sesuai dosis)."
        ]
    },
    1: { # ID 1: Helicoverpa Armigera
        "nama": "Ulat Buah (Helicoverpa Armigera)",
        "bahaya": "Melubangi buah tomat dan memakan daun/bunga. Buah menjadi busuk dan tidak laku jual.",
        "pencegahan": [
            "✅ Lakukan rotasi tanaman (jangan tanam tomat terus menerus).",
            "✅ Pasang perangkap feromon sex untuk menangkap ngengat jantan.",
            "✅ Tanam tanaman perangkap (seperti bunga matahari) di pinggir lahan."
        ],
        "penanganan": [
            "💊 Pungut ulat secara manual jika jumlahnya sedikit.",
            "💊 Semprotkan bakteri biologi Bacillus thuringiensis (Bt).",
            "💊 Gunakan insektisida jika serangan sudah di atas ambang batas."
        ]
    },
    2: { # ID 2: Aphids
        "nama": "Kutu Daun (Aphids)",
        "bahaya": "Menghisap cairan tanaman dan mengeluarkan embun madu yang memicu jamur jelaga (daun jadi hitam).",
        "pencegahan": [
            "✅ Gunakan mulsa plastik perak untuk memantulkan cahaya (mengusir kutu).",
            "✅ Hindari penggunaan pupuk Nitrogen (N) berlebihan.",
            "✅ Jaga kebersihan lahan dari tanaman inang liar."
        ],
        "penanganan": [
            "💊 Semprot dengan air sabun cair (sunlight) konsentrasi rendah.",
            "💊 Gunakan musuh alami: Kepik (Ladybug).",
            "💊 Semprot insektisida berbahan aktif Abamectin jika parah."
        ]
    }
}

# ==========================================
# 2. KONFIGURASI HALAMAN WEB
# ==========================================
st.set_page_config(page_title="Dokter Tomat AI", page_icon="🍅", layout="centered")

st.markdown("<h1 style='text-align: center;'>🍅 Dokter Tanaman Tomat</h1>", unsafe_allow_html=True)
st.write("---")
st.info("Aplikasi ini menggunakan **Artificial Intelligence (YOLOv8)** untuk mendeteksi hama dan memberikan solusi penanganan secara instan.")

# Sidebar
st.sidebar.header("⚙️ Pengaturan")
confidence = st.sidebar.slider("Akurasi Minimum (Confidence)", 0.0, 1.0, 0.40)

# ==========================================
# 3. LOAD MODEL
# ==========================================
try:
    model = YOLO(r"C:\Users\ASUS\DETEKSI_HAMA_TOMAT\04_Aplikasi_Web\best (1).pt")
except Exception as e:
    st.error(f"Error: File 'best.pt' tidak ditemukan. Pastikan file model ada di folder ini! ({e})")
    st.stop()

# ==========================================
# 4. INPUT GAMBAR
# ==========================================
pilihan = st.radio("Pilih Metode Input:", ("📂 Upload Gambar", "📸 Gunakan Kamera"), horizontal=True)

image = None

if pilihan == "📂 Upload Gambar":
    uploaded_file = st.file_uploader("Pilih foto daun/buah tomat...", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

elif pilihan == "📸 Gunakan Kamera":
    camera_image = st.camera_input("Ambil foto langsung")
    if camera_image is not None:
        image = Image.open(camera_image)

# ==========================================
# 5. PROSES DETEKSI & SOLUSI
# ==========================================
if image is not None:
    # Tampilkan gambar asli
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Gambar Asli", use_column_width=True)
    
    # Tombol Deteksi
    if st.button("🔍 Analisa Hama Sekarang", type="primary"):
        with st.spinner('Sedang memeriksa tanaman...'):
            # Prediksi
            results = model.predict(image, conf=confidence)
            
            # Ambil Gambar Hasil (Plot)
            res_plotted = results[0].plot()
            res_image = Image.fromarray(res_plotted[..., ::-1])
            
            # Tampilkan Hasil Gambar
            with col2:
                st.image(res_image, caption="Hasil Deteksi AI", use_column_width=True)

            # --- BAGIAN PINTAR: MENAMPILKAN SOLUSI ---
            boxes = results[0].boxes
            if len(boxes) == 0:
                st.success("✅ Alhamdulillah! Tidak ditemukan hama pada gambar ini. Tanaman terlihat sehat.")
            else:
                st.warning(f"⚠️ Terdeteksi **{len(boxes)}** hama!")
                
                # Cari jenis hama apa saja yang unik (supaya tidak muncul dobel)
                hama_terdeteksi = set()
                for box in boxes:
                    class_id = int(box.cls[0]) # Mengambil ID kelas (0, 1, atau 2)
                    hama_terdeteksi.add(class_id)
                
                st.write("---")
                st.subheader("📋 Laporan & Solusi Penanganan")

                # Loop untuk menampilkan solusi setiap jenis hama yang ketemu
                for id_hama in hama_terdeteksi:
                    if id_hama in solusi_hama:
                        info = solusi_hama[id_hama]
                        
                        # Pakai Expander biar rapi (bisa diklik untuk buka/tutup)
                        with st.expander(f"🔴 Deteksi: {info['nama']}", expanded=True):
                            st.markdown(f"**Bahaya:** {info['bahaya']}")
                            
                            c1, c2 = st.columns(2)
                            with c1:
                                st.markdown("### 🛡️ Pencegahan")
                                for tips in info['pencegahan']:
                                    st.write(tips)
                            with c2:
                                st.markdown("### 💊 Penanganan/Pengobatan")
                                for obat in info['penanganan']:
                                    st.write(obat)
                    else:
                        st.error(f"Hama dengan ID {id_hama} terdeteksi, tapi data solusinya belum ada di database.")