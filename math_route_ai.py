import streamlit as st
import google.generativeai as genai

# ==============================================================================
# SAYFA AYARLARI & TASARIM
# ==============================================================================
st.set_page_config(page_title="Matematik Ders Rehberi", page_icon="🎓", layout="centered")

footer_css = """
<style>
.kucuk-logo {
    position: fixed;
    bottom: 15px;
    left: 20px;
    font-size: 14px;
    font-weight: 800;
    color: #6c757d; 
    z-index: 9999;
    font-family: 'Arial', sans-serif;
    letter-spacing: 2px;
    user-select: none; 
}
</style>
<div class="kucuk-logo">ZY</div>
"""
st.markdown(footer_css, unsafe_allow_html=True)

# ==============================================================================
# VERİ TABANI 
# ==============================================================================
dersler_db = {
    # 1. SINIF ZORUNLU
    "MAT1103": {"ad": "Lineer Cebir I", "sinif": 1, "yariyil": 1, "kategori": "Cebir", "tur": "ZORUNLU", "icerik": "Lineer denklem sistemleri, matris operasyonları, özdeğer analizleri, vektör uzayları. Yapay zeka ve makine öğrenmesindeki matris algoritmalarının temelidir.", "meslekler": ["Yapay Zeka ve Makine Öğrenmesi Mühendisi", "3B Grafik Yazılımcısı", "Veri Bilimci"]},
    "MAT1105": {"ad": "Soyut Matematik I", "sinif": 1, "yariyil": 1, "kategori": "Soyut Matematik", "tur": "ZORUNLU", "icerik": "Önermeler mantığı, ispat teknikleri, kümeler ve bağıntılar. Yazılım test ve mantık süreçleri için kritik zemin hazırlar.", "meslekler": ["Formel Doğrulama Mühendisi", "Veritabanı Mimarı"]},
    "MAT1107": {"ad": "Analitik Geometri I", "sinif": 1, "yariyil": 1, "kategori": "Geometri", "tur": "ZORUNLU", "icerik": "2 ve 3 boyutlu uzayda vektörlerin geometrik temsili, koordinat sistemleri. Otonom navigasyon ve bilgisayar grafikleri için temeldir.", "meslekler": ["Otonom Sistemler Mühendisi", "Bilgisayar Görüsü Uzmanı"]},
    "MAT1109": {"ad": "Analiz I", "sinif": 1, "yariyil": 1, "kategori": "Analiz", "tur": "ZORUNLU", "icerik": "Limit, süreklilik, türev ve optimizasyon. Makine öğrenmesindeki hata optimizasyonu algoritmalarına altyapı sağlar.", "meslekler": ["Algoritma Uzmanı", "Fizik Motoru Yazılımcısı"]},
    "MAT1104": {"ad": "Lineer Cebir II", "sinif": 1, "yariyil": 2, "kategori": "Cebir", "tur": "ZORUNLU", "icerik": "Soyut vektör uzayları, lineer dönüşümler, köşegenleştirme. Kuantum hesaplama ve boyut indirgeme (PCA) için çekirdektir.", "meslekler": ["Kuantum Yazılım Mühendisi", "Yapay Zeka Araştırmacısı"]},
    "MAT1106": {"ad": "Soyut Matematik II", "sinif": 1, "yariyil": 2, "kategori": "Soyut Matematik", "tur": "ZORUNLU", "icerik": "Sayılabilirlik, modüler aritmetik, cebirsel sistemlere giriş. Kriptoloji ve şifreleme algoritmalarının temelidir.", "meslekler": ["Kriptolog", "Blokzincir Mühendisi"]},
    "MAT1110": {"ad": "Analiz II", "sinif": 1, "yariyil": 2, "kategori": "Analiz", "tur": "ZORUNLU", "icerik": "Belirli/belirsiz integraller, seriler, Taylor açılımları. Sinyal işleme ve veri analitiğine zemin hazırlar.", "meslekler": ["Sinyal İşleme Mühendisi", "Veri Analisti"]},
    "MAT1108": {"ad": "Analitik Geometri II", "sinif": 1, "yariyil": 2, "kategori": "Geometri", "tur": "ZORUNLU", "icerik": "3 boyutlu uzayda kuadrik yüzeyler, koordinat dönüşümleri. 3B oyun motorları ve medikal görüntüleme temelidir.", "meslekler": ["CAD/CAM Yazılım Mühendisi", "3B Rekonstrüksiyon Uzmanı"]},

    # 2. SINIF ZORUNLU & SEÇMELİ
    "IST2225": {"ad": "İstatistik I", "sinif": 2, "yariyil": 1, "kategori": "İstatistik", "tur": "ZORUNLU", "icerik": "Olasılık uzayları, rastgele değişkenler, dağılımlar. Yapay zeka parametre tahminleri ve A/B testlerinin omurgasıdır.", "meslekler": ["Veri Bilimci", "Risk Analisti"]},
    "MAT2205": {"ad": "Topoloji I", "sinif": 2, "yariyil": 1, "kategori": "Topoloji", "tur": "ZORUNLU", "icerik": "Açık/kapalı kümeler, süreklilik, tıkızlık. Topolojik Veri Analizi (TDA) ve manifold öğrenmesine temel oluşturur.", "meslekler": ["Topolojik Veri Analisti", "Ağ Mimarisi Uzmanı"]},
    "MAT2253": {"ad": "Bilgisayar Programlama I", "sinif": 2, "yariyil": 1, "kategori": "Yazılım", "tur": "ZORUNLU", "icerik": "Algoritmik düşünme, döngüler, veri tipleri. Matematiksel problemleri koda dökme (QBasic/Python vb.) pratiği sağlar.", "meslekler": ["Yazılım Geliştiricisi", "Hesaplamalı Matematik Uzmanı"]},
    "MAT2255": {"ad": "Analiz III", "sinif": 2, "yariyil": 1, "kategori": "Analiz", "tur": "ZORUNLU", "icerik": "Çok değişkenli fonksiyonlar, kısmi türevler. Derin öğrenme (Geri yayılım) algoritmalarının matematiksel modelini kurar.", "meslekler": ["Derin Öğrenme Mühendisi", "Ekonometri Uzmanı"]},
    "MAT2229": {"ad": "Matematik Laboratuvarı I", "sinif": 2, "yariyil": 1, "kategori": "Yazılım", "tur": "SEÇMELİ", "icerik": "Bilgisayarlı cebir sistemleriyle (Python vb.) görselleştirme ve algoritmik kök bulma.", "meslekler": ["Bilimsel Yazılım Geliştiricisi"]},
    "MAT2267": {"ad": "Matematik Tarihi", "sinif": 2, "yariyil": 1, "kategori": "Tarih", "tur": "SEÇMELİ", "icerik": "Matematiğin felsefi evrimi ve düşünce tarihi.", "meslekler": ["Bilim İletişimcisi"]},
    "MAT2333": {"ad": "Tasarı Geometri", "sinif": 2, "yariyil": 1, "kategori": "Geometri", "tur": "SEÇMELİ", "icerik": "Üç boyutlu nesneleri 2B düzlemde ifade etme, izdüşümler.", "meslekler": ["3B Modelleme Yazılımcısı"]},
    "IST2226": {"ad": "İstatistik II", "sinif": 2, "yariyil": 2, "kategori": "İstatistik", "tur": "ZORUNLU", "icerik": "Hipotez testleri, regresyon analizi. Makine öğrenmesindeki veri çıkarım süreçlerinin temelidir.", "meslekler": ["Makine Öğrenmesi Modelleyicisi"]},
    "MAT2206": {"ad": "Topoloji II", "sinif": 2, "yariyil": 2, "kategori": "Topoloji", "tur": "ZORUNLU", "icerik": "Metrik uzaylar, Tychonoff teoremi. Karmaşık uzay indirgemeleri ve yüksek boyutlu veri analitiği.", "meslekler": ["Robotik Hareket Planlama Mühendisi"]},
    "MAT2254": {"ad": "Bilgisayar Programlama II", "sinif": 2, "yariyil": 2, "kategori": "Yazılım", "tur": "ZORUNLU", "icerik": "Nesne yönelimli programlama (OOP), hata yakalama ve arayüz (Tkinter vb.) geliştirme mantığı.", "meslekler": ["Backend Geliştiricisi", "Simülasyon Yazılımcısı"]},
    "MAT2256": {"ad": "Analiz IV", "sinif": 2, "yariyil": 2, "kategori": "Analiz", "tur": "ZORUNLU", "icerik": "Vektör alanları, Green/Gauss teoremleri. Geometrik derin öğrenme ve akışkanlar mekaniği.", "meslekler": ["Geometrik Derin Öğrenme Uzmanı"]},
    "MAT2230": {"ad": "Matematik Laboratuvarı II", "sinif": 2, "yariyil": 2, "kategori": "Yazılım", "tur": "SEÇMELİ", "icerik": "Diferansiyel denklemlerin bilgisayar ortamında simülasyonu.", "meslekler": ["Hesaplamalı Simülasyon Uzmanı"]},
    "MAT2270": {"ad": "Sayılar Teorisi", "sinif": 2, "yariyil": 2, "kategori": "Cebir", "tur": "SEÇMELİ", "icerik": "Modüler aritmetik, kriptografi temelleri.", "meslekler": ["Siber Güvenlik Uzmanı"]},
    "MAT2272": {"ad": "Kombinatorik", "sinif": 2, "yariyil": 2, "kategori": "Ayrık Matematik", "tur": "SEÇMELİ", "icerik": "Sayma algoritmaları, algoritma karmaşıklığı analizleri.", "meslekler": ["Algoritma Mühendisi"]},
    "MAT2276": {"ad": "İngilizce Matematiksel Kavramlar", "sinif": 2, "yariyil": 2, "kategori": "İletişim", "tur": "SEÇMELİ", "icerik": "Akademik makale okuma ve terimlere hakimiyet.", "meslekler": ["Ar-Ge Araştırmacısı"]},

    # 3. SINIF ZORUNLU & SEÇMELİ
    "MAT3301": {"ad": "Cebir I", "sinif": 3, "yariyil": 1, "kategori": "Cebir", "tur": "ZORUNLU", "icerik": "Grup teorisi, simetri grupları. Siber güvenlik mimarilerinin çekirdeği.", "meslekler": ["Kriptoloji Mimarı"]},
    "MAT3313": {"ad": "Nümerik Analiz I", "sinif": 3, "yariyil": 1, "kategori": "Uygulamalı Matematik", "tur": "ZORUNLU", "icerik": "Sayısal kök bulma algoritmaları. Mühendislik optimizasyonları için temel.", "meslekler": ["Algoritma Optimizasyon Uzmanı"]},
    "MAT3315": {"ad": "Diferensiyel Denklemler I", "sinif": 3, "yariyil": 1, "kategori": "Diferansiyel Denklemler", "tur": "ZORUNLU", "icerik": "Dinamik sistemlerin denklemlenmesi. Yapay sinir ağlarındaki sürekli zamanlı modeller.", "meslekler": ["Kontrol Sistemleri Mühendisi"]},
    "MAT3317": {"ad": "Kompleks Fonksiyonlar Teorisi I", "sinif": 3, "yariyil": 1, "kategori": "Analiz", "tur": "ZORUNLU", "icerik": "Kompleks düzlem, analitik fonksiyonlar. Kuantum sistemleri için analiz.", "meslekler": ["Sinyal İşleme Mühendisi"]},
    "MAT3319": {"ad": "Diferensiyel Geometri I", "sinif": 3, "yariyil": 1, "kategori": "Geometri", "tur": "ZORUNLU", "icerik": "Uzay eğrileri, Frenet çatıları. Otonom robot kollarının yörünge kinematiği.", "meslekler": ["Robotik Kinematik Uzmanı"]},
    "MAT3321": {"ad": "Algoritmalar ve Veri Yapıları", "sinif": 3, "yariyil": 1, "kategori": "Yazılım", "tur": "SEÇMELİ", "icerik": "Veri yapıları, arama/sıralama algoritmalarının Big-O analizi.", "meslekler": ["AI Veri Yapıları Mühendisi"]},
    "MAT3322": {"ad": "Makine Öğrenmesi İçin Matematik", "sinif": 3, "yariyil": 2, "kategori": "Yapay Zeka", "tur": "SEÇMELİ", "icerik": "Gradient Descent, PCA, Maximum Likelihood. AI modellerinin arka planındaki saf matematik.", "meslekler": ["Makine Öğrenmesi Araştırmacısı", "Derin Öğrenme Mühendisi"]},
    "MAT3336": {"ad": "Optimizasyon", "sinif": 3, "yariyil": 2, "kategori": "Optimizasyon", "tur": "SEÇMELİ", "icerik": "Lineer olmayan optimizasyon, maliyet minimizasyonu. Yapay zeka maliyet fonksiyonları için elzem.", "meslekler": ["Yapay Zeka Optimizasyon Uzmanı"]},

    # 4. SINIF ZORUNLU & SEÇMELİ
    "MAT4001": {"ad": "Bitirme Projesi", "sinif": 4, "yariyil": 1, "kategori": "Genel", "tur": "ZORUNLU", "icerik": "Özgün araştırma, proje raporlama ve savunma.", "meslekler": ["Ar-Ge Modelleme Uzmanı"]},
    "MAT4413": {"ad": "Diferensiyel Denklem Sistemleri", "sinif": 4, "yariyil": 1, "kategori": "Dinamik Sistemler", "tur": "SEÇMELİ", "icerik": "Çoklu değişkenli sistemlerin kararlılık analizi.", "meslekler": ["Otonom Sistemler Ar-Ge Mühendisi"]},
    "MAT4433": {"ad": "İleri Programlama", "sinif": 4, "yariyil": 1, "kategori": "Yazılım", "tur": "SEÇMELİ", "icerik": "Büyük ölçekli simülasyon kodları optimizasyonu ve tasarım kalıpları.", "meslekler": ["Kıdemli Yazılım Mühendisi"]},
    "BLM446": {"ad": "Bulanık Mantık (Fuzzy Logic)", "sinif": 4, "yariyil": 2, "kategori": "Yapay Zeka", "tur": "SEÇMELİ", "icerik": "Kesin olmayan verilerin algoritmik modellenmesi. Karar destek sistemleri için kritiktir.", "meslekler": ["Yapay Zeka Mühendisi"]}
}

# ==============================================================================
# ARAYÜZ TASARIMI
# ==============================================================================
st.title("🎓 Matematik Bölümü Kariyer ve Yapay Zekâ Rehberi")
st.write("Derslerin teorik içeriklerini inceleyebilir veya doğrudan Yapay Zekâ asistanına danışarak kariyer rotanı çizebilirsin.")

# 3 Sekme oluşturuyoruz: Listeleme, Sorgulama ve AI Asistan
tab1, tab2, tab3 = st.tabs(["📚 Müfredat Listesi", "🔍 Detaylı Ders Sorgula", "🤖 Yapay Zekâ Kariyer Asistanı"])

with tab1:
    filtre = st.radio("Listelenecek Ders Türü:", ["TÜMÜ", "ZORUNLU", "SEÇMELİ"], horizontal=True)
    st.divider()
    for sinif in [1, 2, 3, 4]:
        sinif_dersleri = {k: v for k, v in dersler_db.items() if v["sinif"] == sinif and (filtre == "TÜMÜ" or v["tur"] == filtre)}
        if sinif_dersleri:
            st.subheader(f"📌 {sinif}. Sınıf Dersleri")
            sirali_dersler = sorted(sinif_dersleri.items(), key=lambda x: (x[1]['yariyil'], x[1]['tur'], x[0]))
            for kod, d in sirali_dersler:
                etiket = "🔴 ZORUNLU" if d["tur"] == "ZORUNLU" else "🟢 SEÇMELİ"
                donem_adi = "Güz" if d["yariyil"] == 1 else "Bahar"
                with st.expander(f"**{kod}** - {d['ad']} | {etiket}"):
                    st.caption(f"**Kategori:** {d['kategori']} | **Dönem:** {d['sinif']}. Sınıf / {d['yariyil']}. Yarıyıl ({donem_adi})")
                    st.markdown(f"**📖 İçerik:** {d['icerik']}")
                    st.write("**🎯 Kariyer Yolları:**")
                    for meslek in d['meslekler']:
                        st.markdown(f"- *{meslek}*")

with tab2:
    st.subheader("Özel Ders Arama")
    ders_listesi = ["Bir ders seçin..."] + sorted(list(dersler_db.keys()))
    secilen_kod = st.selectbox("Ders Kodu Seçin:", ders_listesi)
    if secilen_kod != "Bir ders seçin...":
        d = dersler_db[secilen_kod]
        donem_adi = "Güz" if d["yariyil"] == 1 else "Bahar"
        st.success(f"**{secilen_kod} - {d['ad']}**")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Statü:** {d['tur']}")
            st.info(f"**Dönem:** {d['sinif']}. Sınıf / {d['yariyil']}. Yarıyıl ({donem_adi})")
        with col2:
            st.info(f"**Kategori:** {d['kategori']}")
        st.write("---")
        st.write(f"**İçerik Detayı:**\n{d['icerik']}")
        st.write("---")
        st.write("**Bu Dersin Hazırladığı Meslekler:**")
        for m in d['meslekler']:
            st.markdown(f"- **{m}**")

# ==============================================================================
# YAPAY ZEKA ASİSTANI (GÜVENLİ - ŞİFREYİ STREAMLIT'TEN ÇEKER)
# ==============================================================================
with tab3:
    st.subheader("🤖 Yapay Zekâ Öğrenci Danışmanı")
    st.markdown("""
    Bu asistan; arka planda **Google Gemini AI** dil modelini kullanarak matematik bölümü müfredatını analiz eder. 
    Kariyer hedefinizi yazın, size hangi dersleri almanız gerektiğini anlatsın!
    """)
    
    st.divider()

    # Şifreyi açıkça yazmıyoruz, Streamlit'in gizli kasasından çekiyoruz!
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        st.error("Sistem Hatası: API Anahtarı sunucuda bulunamadı! Lütfen Streamlit ayarlarından Secrets kısmını kontrol edin.")
        api_key = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
if prompt := st.chat_input("Örn: Yapay zeka mühendisi olmak istiyorum, 3. sınıfta hangi seçmeli dersleri almalıyım?"):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if api_key:
            try:
                genai.configure(api_key=api_key)
                
                # Google'ın açıkça istediği en güncel modeli yazıyoruz:
                model = genai.GenerativeModel('gemini-3.6-flash')
                
                sistem_istemi = f"""
                Sen bir üniversitenin Matematik Bölümü öğrencileri için tasarlanmış profesyonel bir Akademik Yapay Zeka Danışmanısın.
                Sadece aşağıda sana verdiğim ders veri tabanını kullanarak öğrencilere kariyer ve ders seçimi tavsiyeleri ver.
                Veri tabanı dışında ders uydurma. Yanıtların kibar, teşvik edici ve net olsun.
                
                Müfredat Veri Tabanı:
                {dersler_db}
                
                Öğrencinin Sorusu: {prompt}
                """
                
                with st.chat_message("assistant"):
                    with st.spinner("Müfredat analiz ediliyor..."):
                        response = model.generate_content(sistem_istemi)
                        st.markdown(response.text)
                
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                with st.chat_message("assistant"):
                    st.error(f"Bağlantı hatası oluştu: {e}")
