import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import time 

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Gas Ideal",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Kalkulator Gas Ideal")
st.caption("Hukum Gas + Studi Kasus + Regresi Linear (Full Streamlit)")

st.markdown("---")

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.selectbox(
    "📌 Pilih Menu",
    ["Home", "Studi Kasus", "Hukum Boyle", "Hukum Charles", "Hukum Gay-Lussac", "Gas Ideal", "Regresi Linear"]
)

# =========================
# HOME
# =========================
if menu == "Home":

    st.subheader("👋 Selamat Datang")

    st.success("Aplikasi ini dibuat full Streamlit tanpa library error 🚀")

    st.markdown("""
    ### 🔬 Fitur:
    - Studi Kasus
    - Hukum Boyle
    - Hukum Charles
    - Hukum Gay-Lussac
    - Gas Ideal (PV = nRT)
    - 📈 Regresi Linear (LINE CHART)
    """)

    st.balloons()

# =========================
# STUDI KASUS
# =========================
elif menu == "Studi Kasus":
    
    pilihan = st.selectbox(
        "Pilih Studi Kasus",
        ["Analisis Gas Ideal","Simulasi Massa Jenis Gas"]
    )
#===================================
#ANALISIS GAS IDEAL
#===================================
if pilihan == "Analisis Gas Ideal":
        
        st.subheader("🧪 Studi Kasus Gas Ideal")
        
        P = st.number_input("Tekanan (atm)", value=1.0)
        V = st.number_input("Volume (L)", value=10.0)
        n = st.number_input("Mol gas", value=1.0)
        T = st.number_input("Suhu (K)", value=300.0)
        
        R = 0.0821

    if st.button("Analisis"):

        PV = P * V
        nRT = n * R * T

        st.write(f"PV = {PV:.3f}")
        st.write(f"nRT = {nRT:.3f}")

        if abs(PV - nRT) < 1:
            st.success("Sistem sesuai Gas Ideal ✅")
        else:
            st.warning("Ada deviasi dari gas ideal ⚠️")

# ====================================
# SIMULASI MASSA JENIS GAS
# ====================================
elif pilihan == "Simulasi Massa Jenis Gas":

    st.title("Simulasi Gas Ideal Interaktif")
    
    st.write("""
    Aplikasi ini menghitung massa jenis gas menggunakan persamaan gas ideal.

    Pengguna dapat mengubah:
    - tekanan (atm)
    - suhu (K)
    - Bobot Molekul gas (g/mol)
    """)

# ====================================
# INPUT PENGGUNA
# ====================================

    st.subheader("Input Variabel")

    P = st.slider(
    "Tekanan Gas (atm)",
        0.1,
        10.0,
        2.0,
        0.1
    )

    T = st.slider(
        "Suhu Gas (K)",
        100,
        1000,
        298
    )

    M = st.number_input(
        "Bobot Molekul Gas (g/mol)",
        value=32.0
    )

    R = 0.082

# ====================================
# KECEPATAN ANIMASI
# ====================================

    kecepatan = max(1, 12 - (T / 100))

# ====================================
# PENJELASAN
# ====================================

    st.info(
        f"""
        Tekanan = {P} atm
        
        Suhu = {T} K
        
        Bobot Molekul = {M} g/mol
        
        Semakin tinggi suhu, partikel bergerak semakin cepat.
        """
    )

# ====================================
# HTML + CSS ANIMASI
# ====================================

    html_code = f"""
    <!DOCTYPE html>
    <html>
    
    <head>
    
    <style>
    
    body {{
    margin:0;
    overflow:hidden;
    background-color:transparent;
    }}

    .kotak {{
    width:100%;
    height:420px;

    position:relative;
    overflow:hidden;

    border-radius:20px;

    background:
    radial-gradient(circle,
    #1e3a8a,
    #020617);

    border:2px solid cyan;

    box-shadow:
    0px 0px 25px rgba(0,255,255,0.4);
    }}

    .bola {{

    width:18px;
    height:18px;

    position:absolute;

    border-radius:50%;

    background:cyan;

    box-shadow:
    0 0 15px cyan,
    0 0 30px cyan;
    }}

    .b1 {{
    animation: gerak1 {kecepatan}s linear infinite alternate;
    }}

    .b2 {{
    animation: gerak2 {kecepatan*0.8}s linear infinite alternate;
    }}

    .b3 {{
    animation: gerak3 {kecepatan*1.2}s linear infinite alternate;
    }}

    .b4 {{
    animation: gerak4 {kecepatan*0.6}s linear infinite alternate;
    }}

    @keyframes gerak1 {{
    
    from {{
        transform: translate(0px,0px);
        }}

    to {{
        transform: translate(320px,240px);
        }}
        }}

    @keyframes gerak2 {{
    
    from {{
        transform: translate(0px,200px);
        }}

    to {{
        transform: translate(280px,-60px);
        }}
        }}

    @keyframes gerak3 {{
    
    from {{
        transform: translate(150px,0px);
        }}
        
        to {{
        transform: translate(-120px,250px);
        }}
        }}

    @keyframes gerak4 {{
    
    0% {{
        transform: translate(0px,0px);
        }}
        
    25% {{
        transform: translate(220px,50px);
        }}

    50% {{
        transform: translate(100px,220px);
        }}

    75% {{
        transform: translate(260px,130px);
        }}

    100% {{
        transform: translate(50px,260px);
        }}
        }}

    </style>

    </head>

    <body>

    <div class="kotak">

    <div class="bola b1"
    style="left:20px; top:20px;">
    </div>

    <div class="bola b2"
    style="left:80px; top:100px;">
    </div>

    <div class="bola b3"
    style="left:180px; top:150px;">
    </div>

    <div class="bola b4"
    style="left:300px; top:80px;">
    </div>

    <div class="bola b1"
    style="left:400px; top:200px;">
    </div>

    <div class="bola b2"
    style="left:520px; top:140px;">
    </div>

    <div class="bola b3"
    style="left:620px; top:240px;">
    </div>

    <div class="bola b4"
    style="left:700px; top:100px;">
    </div>

    </div>

    </body>
    </html>
    """

# ====================================
# TAMPILKAN ANIMASI
# ====================================

    st.subheader("🌌 Simulasi Pergerakan Partikel")

    components.html(
        html_code,
        height=430
    )

# ====================================
# PERSAMAAN GAS IDEAL
# ====================================

    st.subheader("Persamaan Gas Ideal")

    st.latex(r"PV = nRT")

    st.write(
        "Untuk mencari massa jenis gas:"
    )

    st.latex(r"\rho = \frac{PM}{RT}")

# ====================================
# PERHITUNGAN OTOMATIS
# ====================================

    hasil = (P * M) / (R * T)

# ====================================
# LANGKAH PERHITUNGAN
# ====================================

    st.subheader("Langkah Perhitungan")

    st.latex(
        rf"\rho = \frac{{({P})({M})}}{{({R})({T})}}"
    )

    st.latex(
        rf"\rho = {hasil:.2f}\ g/L"
    )

# ====================================
# TOMBOL HASIL + kesimpulan
# ====================================

    if st.button("✨ Tampilkan Hasil"):
        # Efek loading
        with st.spinner("Menghitung massa jenis gas..."):
            
            progress = st.progress(0)
            
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
     # Efek sukses
        st.success("Perhitungan berhasil✨!")
        st.balloons()
        
        st.markdown(
            f"""
            <div style="
            background:linear-gradient(to right,#BFEFFF,#87CEFA);
            padding:30px;
            border-radius:20px;
            color:black;
            box-shadow:0px 0px 25px rgba(137,207,240,0.6);
            animation: fadein 1s;
            ">
            
            <h1 style="
            text-align:center;
            font-size:40px;
            ">
            Massa Jenis Gas
            </h1>
            
            <hr>
            
            <h2 style="
            text-align:center;
            font-size:35px;
            ">
            {hasil:.2f} g/L
            </h2>
            
            <br>
            
            <h3> Kesimpulan</h3>
            
            <p style="font-size:20px; line-height:1.8;">
            
            Dengan:
            <br>
            • tekanan = {P} atm
            <br>
            • suhu = {T} K
            <br>
            • Bobot Molekul = {M} g/mol
            <br><br>
            
            maka massa jenis gas adalah:
            
            <b>{hasil:.2f} g/L</b>
            
            </p>
            
            </div>
            """,
            
            unsafe_allow_html=True
        )

# ====================================
# TEST
# ====================================

    assert hasil > 0, "Hasil tidak boleh negatif"
# AKHIR BLOK:
# elif pilihan == "Simulasi Massa Jenis Gas"
# dan juga akhir blok:
# elif menu == "Studi Kasus"


# =========================
# BOYLE
# =========================
elif menu == "Hukum Boyle":

    st.subheader("📘 Hukum Boyle")

    st.latex(r"P_1V_1=P_2V_2")

    P1 = st.number_input("P1", value=1.0)
    V1 = st.number_input("V1", value=1.0)
    P2 = st.number_input("P2", value=2.0)

    if st.button("Hitung V2"):
        if P2 != 0:
            V2 = (P1 * V1) / P2
            st.success(f"V2 = {V2:.3f} L")

# =========================
# CHARLES
# =========================
elif menu == "Hukum Charles":

    st.subheader("📘 Hukum Charles")

    st.latex(r"\frac{V_1}{T_1}=\frac{V_2}{T_2}")

    V1 = st.number_input("V1", value=1.0)
    T1 = st.number_input("T1 (K)", value=273.0)
    T2 = st.number_input("T2 (K)", value=300.0)

    if st.button("Hitung V2"):
        V2 = (V1 * T2) / T1
        st.success(f"V2 = {V2:.3f} L")

# =========================
# GAY LUSSAC
# =========================
elif menu == "Hukum Gay-Lussac":

    st.subheader("📘 Hukum Gay-Lussac")

    st.latex(r"\frac{P_1}{T_1}=\frac{P_2}{T_2}")

    P1 = st.number_input("P1", value=1.0)
    T1 = st.number_input("T1 (K)", value=273.0)
    T2 = st.number_input("T2 (K)", value=300.0)

    if st.button("Hitung P2"):
        P2 = (P1 * T2) / T1
        st.success(f"P2 = {P2:.3f} atm")

# =========================
# GAS IDEAL
# =========================
elif menu == "Gas Ideal":

    st.subheader("📘 Persamaan Gas Ideal")

    st.latex(r"PV=nRT")

    P = st.number_input("P (atm)", value=1.0)
    V = st.number_input("V (L)", value=1.0)
    n = st.number_input("n (mol)", value=1.0)

    R = 0.0821

    if st.button("Hitung T"):
        T = (P * V) / (n * R)
        st.success(f"Suhu = {T:.2f} K")

# =========================
# REGRESI LINEAR (LINE CHART)
# =========================
elif menu == "Regresi Linear":

    st.subheader("📈 Regresi Linear (LINE CHART Streamlit)")

    x_input = st.text_input("Data P (pisahkan koma)", "1,2,3,4,5")
    y_input = st.text_input("Data V (pisahkan koma)", "10,8,6,4,2")

    if st.button("Hitung & Grafik"):

        # convert data
        x = np.array([float(i) for i in x_input.split(",")])
        y = np.array([float(i) for i in y_input.split(",")])

        # regresi linear
        m, b = np.polyfit(x, y, 1)
        y_pred = m * x + b

        st.success(f"Persamaan: V = {m:.3f}P + {b:.3f}")

        # =========================
        # DATAFRAME
        # =========================
        df = pd.DataFrame({
            "P": x,
            "V (data asli)": y,
            "V (regresi)": y_pred
        })

        # urutkan biar grafik rapi
        df = df.sort_values("P")

        # =========================
        # 📈 LINE CHART (STREAMLIT NATIF)
        # =========================
        st.line_chart(df.set_index("P"))

        st.dataframe(df)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("🚀 Full Streamlit Version | Tanpa Matplotlib | Aman dijalankan")
