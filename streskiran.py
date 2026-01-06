import streamlit as st
import pandas as pd
import numpy as np
import time

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Streskıran", page_icon="🌿", layout="centered")

# --- STİL VE CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f8f5;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 10px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FONKSİYONLAR ---
def yapay_zeka_onerisi(metin, seviye):
    metin = metin.lower()
    oneri = ""
    if seviye > 7:
        oneri = "⚠️ Stres seviyen çok yüksek. Lütfen önce 'Nefes Egzersizi' sekmesine git ve 2 dakika mola ver."
    elif "trafik" in metin or "yol" in metin:
        oneri = "🚗 Trafikteysen kontrol edemeyeceğin şeyler için üzülme. Şu an senin için sakinleştirici bir podcast veya klasik müzik listesi iyi gelebilir."
    elif "ders" in metin or "sınav" in metin or "okul" in metin:
        oneri = "📚 Zihnin dolmuş olabilir. Pomodoro tekniği uygula: 25 dk çalış, 5 dk arkanı yaslan ve hiçbir şey yapma."
    elif "iş" in metin or "patron" in metin or "toplantı" in metin:
        oneri = "💼 İş stresi eve taşınmamalı. Derin bir nefes al ve kendine şu soruyu sor: 'Bu sorun 1 yıl sonra önemli olacak mı?'"
    else:
        oneri = "🌿 Yaşadığın durum zorlayıcı olabilir. Kendine bir bardak su al ve omuzlarını gevşet."
    return oneri

# --- YAN MENÜ ---
st.sidebar.title("🌿 Streskıran")
secim = st.sidebar.radio("Menü", ["Ana Sayfa (Durum Bildir)", "Stres Analizi", "Nefes Egzersizi"])

# --- SAYFA 1: ANA SAYFA ---
if secim == "Ana Sayfa (Durum Bildir)":
    # use_column_width yerine use_container_width kullanıldı (Hatayı çözer)
    st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.title("Bugün Nasıl Hissediyorsun?")
    
    stres_seviyesi = st.slider("Stres Seviyen (1 = Çok Sakin, 10 = Patlamak Üzere)", 1, 10, 5)
    durum_metni = st.text_area("Seni ne strese soktu?", height=100)

    if st.button("Çözüm Önerisi Al"):
        with st.spinner('Yapay Zeka durumunu analiz ediyor...'):
            time.sleep(1.5)
            oneri = yapay_zeka_onerisi(durum_metni, stres_seviyesi)
            st.success("Analiz Tamamlandı!")
            st.info(oneri)

# --- SAYFA 2: STRES ANALİZİ ---
elif secim == "Stres Analizi":
    st.title("📊 Stres Takip Paneli")
    chart_data = pd.DataFrame(
        np.random.randint(1, 10, size=(7, 1)),
        columns=['Stres Seviyesi'],
        index=["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    )
    st.line_chart(chart_data)
    st.info("💡 İpucu: Salı günleri stresin artıyor. Kısa molalar ver.")

# --- SAYFA 3: NEFES EGZERSİZİ ---
elif secim == "Nefes Egzersizi":
    st.title("🌬️ 4-7-8 Nefes Tekniği")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        basla = st.button("Egzersizi Başlat")

    if basla:
        progress_bar = st.progress(0)
        status_text = st.empty()
        for tur in range(3):
            for i in range(1, 5):
                status_text.markdown(f"### 🔵 Burnundan Derin Nefes Al... ({i})")
                progress_bar.progress(i * 5)
                time.sleep(1)
            for i in range(1, 8):
                status_text.markdown(f"### ✋ Nefesini Tut... ({i})")
                time.sleep(1)
            for i in range(1, 9):
                status_text.markdown(f"### 💨 Ağzından Yavaşça Ver... ({i})")
                progress_bar.progress(20 + (i * 10))
                time.sleep(1)
        status_text.markdown("### 🎉 Harika! Daha sakin hissediyor musun?")
        st.balloons()