import streamlit as st
import pandas as pd
import numpy as np
import time
import random

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

# --- GELİŞMİŞ YAPAY ZEKA FONKSİYONU ---
def yapay_zeka_onerisi(metin, seviye):
    metin = metin.lower()
    oneri = ""
    
    # 1. ACİL DURUM KONTROLÜ
    if seviye > 8:
        oneri = "⚠️ Stres seviyen alarm veriyor! Şu an mantıklı düşünmek zor olabilir. Lütfen her şeyi bırak ve 'Nefes Egzersizi' sekmesine gidip 3 tur nefes al."
    
    # 2. İLİŞKİ VE DUYGUSAL SORUNLAR
    elif "kavga" in metin or "sevgili" in metin or "eşim" in metin or "arkadaş" in metin or "tartış" in metin or "ayrıl" in metin:
        oneri = "💔 Kalp kırıklığı veya tartışmalar enerjini sömürebilir. Şu an öfkeyle bir mesaj atmadan veya konuşmadan önce kendine 1 saat 'Bekleme Süresi' ver. Duygularını yazmak, onlarla konuşmaktan daha iyi gelebilir."
        
    # 3. YORGUNLUK VE UYKUSUZLUK
    elif "yorgun" in metin or "uyku" in metin or "bitkin" in metin or "halsiz" in metin or "göz" in metin:
        oneri = "🔋 Vücudun sana 'Şarjım bitti' sinyali veriyor. Zorlama. İmkanın varsa 20 dakikalık bir 'Güç Uykusu' (Power Nap) yap. Yoksa yüzünü soğuk suyla yıka ve kafein yerine bol su iç."

    # 4. GÜZELLİK VE ÖZGÜVEN KAYGISI (YENİ)
    elif "çirkin" in metin or "sivilce" in metin or "kilo" in metin or "ayna" in metin or "bakımsız" in metin or "saç" in metin:
        oneri = "🌸 Kendine haksızlık etme. Güzellik kalıplara sığmaz, bir histir. Bugün kendini şımart: Bir yüz maskesi yap, en sevdiğin kıyafetini giy veya aynaya bakıp kendine gülümse. Sen değerlisin."

    # 5. GELECEK KAYGISI (YENİ)
    elif "gelecek" in metin or "korku" in metin or "belirsiz" in metin or "ne olacağım" in metin or "mezun" in metin:
        oneri = "🔮 Gelecek henüz gelmedi, geçmiş ise geçti. Elinde sadece 'Şu An' var. 5 yıl sonrasını düşünerek bugünü zehir etme. Sadece bugünün küçük hedeflerine odaklan, yol kendiliğinden açılır."

    # 6. MADDİ KAYGILAR (YENİ)
    elif "para" in metin or "borç" in metin or "ekonomi" in metin or "zam" in metin or "harcama" in metin or "maaş" in metin:
        oneri = "💸 Maddi stres çok ağırdır ama senin değerini cüzdanın belirlemez. Kontrol edebileceğin şeylere odaklan (basit bir bütçe planı gibi). Ve unutma: En iyi şeyler (temiz hava, gün batımı, yürüyüş) hala bedava."

    # 7. YALNIZLIK HİSSİ (YENİ)
    elif "yalnız" in metin or "kimse" in metin or "tek" in metin or "dost" in metin or "sıkıl" in metin:
        oneri = "🫂 Yalnız hissetmek, kimsesiz olduğun anlamına gelmez. Bazen kendinle baş başa kalmak bir fırsattır. Eğer sosyalleşmek istersen, eski bir dostuna sadece 'Nasılsın?' yazmak harika bir başlangıçtır."

    # 8. TRAFİK VE YOL
    elif "trafik" in metin or "yol" in metin or "metrobüs" in metin:
        oneri = "🚗 Trafiği kontrol edemezsin ama tepkilerini edebilirsin. Bu süreyi kendine ayırdığın bir zaman olarak gör. Sevdiğin bir podcasti veya sesli kitabı aç."
        
    # 9. OKUL VE SINAV
    elif "ders" in metin or "sınav" in metin or "okul" in metin or "proje" in metin:
        oneri = "📚 Bilgi yüklemesi yaşıyorsun. Beynin dolu bir bardak gibi. Pomodoro tekniği (25 dk çalış, 5 dk mola) uygula. O 5 dakikada ekrana bakma, uzaklara bak."
        
    # 10. İŞ VE KARİYER
    elif "iş" in metin or "patron" in metin or "toplantı" in metin or "müşteri" in metin:
        oneri = "💼 İş stresi eve taşınmamalı. Derin bir nefes al ve omuzlarını düşür. Kendine şunu sor: 'Bu problem 1 yıl sonra benim için ne kadar önemli olacak?'"
        
    # 11. GENEL/TANIMSIZ DURUMLAR
    else:
        oneri = "🌿 Bazen sebepsiz yere de daralabiliriz. Kendine bir bitki çayı veya soğuk bir içecek ısmarla. Omuzlarını gevşet ve 3 derin nefes al."
    
    return oneri

# --- YAN MENÜ ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3663/3663335.png", width=100)
st.sidebar.title("🌿 Streskıran")
secim = st.sidebar.radio(
    "Menü", 
    ["Ana Sayfa (Durum Bildir)", "Stres Analizi", "Nefes Egzersizi", "🎧 Rahatlama Alanı", "📝 Şükür Günlüğü"]
)

# --- SAYFA 1: ANA SAYFA ---
if secim == "Ana Sayfa (Durum Bildir)":
    # Fotoğraf genişliği ayarlandı
    st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", width=400)
    st.title("Bugün Nasıl Hissediyorsun?")
    st.markdown("Seni üzen, yoran veya kaygılandıran şeyi aşağıya yaz.")
    
    stres_seviyesi = st.slider("Stres Seviyen (1 = Çok Sakin, 10 = Patlamak Üzere)", 1, 10, 5)
    durum_metni = st.text_area("Seni ne strese soktu?", height=100, placeholder="Örn: Çok yorgunum, kendimi çirkin hissediyorum, sınavım var...")

    if st.button("Çözüm Önerisi Al"):
        if durum_metni:
            with st.spinner('Yapay Zeka durumunu analiz ediyor...'):
                time.sleep(1.5)
                oneri = yapay_zeka_onerisi(durum_metni, stres_seviyesi)
                st.success("Analiz Tamamlandı!")
                st.info(oneri)
        else:
            st.warning("Lütfen boş bırakma, seni anlamam için bir şeyler yazmalısın.")

# --- SAYFA 2: STRES ANALİZİ ---
elif secim == "Stres Analizi":
    st.title("📊 Stres Takip Paneli")
    chart_data = pd.DataFrame(
        np.random.randint(1, 10, size=(7, 1)),
        columns=['Stres Seviyesi'],
        index=["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    )
    st.line_chart(chart_data)
    st.info("💡 İpucu: Verilerine göre Salı günleri stresin artıyor. Salı sabahları kısa bir meditasyon yapabilirsin.")

# --- SAYFA 3: NEFES EGZERSİZİ ---
elif secim == "Nefes Egzersizi":
    st.title("🌬️ 4-7-8 Nefes Tekniği")
    st.markdown("Bu teknik, sinir sistemini sakinleştirmek için dünyaca kabul görmüş bir yöntemdir.")
    
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

# --- SAYFA 4: RAHATLAMA ALANI ---
elif secim == "🎧 Rahatlama Alanı":
    st.title("🎧 Seslerle Rahatla")
    st.write("Stresli anlarda frekansını değiştirmek için bir mod seç.")

    tab1, tab2, tab3 = st.tabs(["🌧️ Yağmur Sesi", "🔥 Şömine", "🎹 Odaklanma"])

    with tab1:
        st.write("Hafif bir yağmur sesi zihni temizler.")
        st.video("https://www.youtube.com/watch?v=mPZkdNFkNps")
    
    with tab2:
        st.write("Çıtırdayan ateş sesi güven hissi verir.")
        st.video("https://www.youtube.com/watch?v=K0pJRo0XU8s")
        
    with tab3:
        st.write("Ders çalışırken veya çalışırken dinleyebileceğin Lo-Fi müzikler.")
        st.video("https://www.youtube.com/watch?v=jfKfPfyJRdk")

# --- SAYFA 5: ŞÜKÜR GÜNLÜĞÜ ---
elif secim == "📝 Şükür Günlüğü":
    st.title("📝 Pozitif Günlük")
    st.write("Beynimiz olumsuza odaklanmaya meyillidir. Bunu kırmak için bugün iyi giden 3 şeyi yaz.")

    # Session State (Geçici Hafıza)
    if 'gunluk' not in st.session_state:
        st.session_state['gunluk'] = []

    yeni_not = st.text_input("Bugün seni ne mutlu etti?")
    
    if st.button("Günlüğüme Ekle"):
        if yeni_not:
            tarih = time.strftime("%d.%m.%Y %H:%M")
            st.session_state['gunluk'].append(f"{tarih} - {yeni_not}")
            st.success("Eklendi! Harikasın.")
        else:
            st.warning("Lütfen boş bırakma :)")

    st.markdown("---")
    st.subheader("📖 Geçmiş Notların")
    
    if len(st.session_state['gunluk']) > 0:
        for notum in reversed(st.session_state['gunluk']):
            st.info(notum)
    else:
        st.write("Henüz bir şey eklemedin. İlk güzel anını yaz!")