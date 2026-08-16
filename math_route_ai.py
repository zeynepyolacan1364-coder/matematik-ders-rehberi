import streamlit as st

st.set_page_config(page_title="Matematik Ders Rehberi", page_icon="🎓", layout="centered")

# Sayfanın sol altına sabitlenmiş minik firma logosu (ZY) tarzı tasarım
footer_css = """
<style>
.kucuk-logo {
    position: fixed;
    bottom: 15px;
    left: 20px;
    font-size: 14px;
    font-weight: 800;
    color: #6c757d; /* Hafif silik şık bir gri tonu */
    z-index: 9999;
    font-family: 'Arial', sans-serif;
    letter-spacing: 2px;
    user-select: none; /* Metnin seçilmesini engeller, logo hissi verir */
}
</style>
<div class="kucuk-logo">ZY</div>
"""
st.markdown(footer_css, unsafe_allow_html=True)

dersler_db = {
    "MAT1103": {
        "ad": "Lineer Cebir I (Linear Algebra I)", "sinif": 1, "yariyil": 1, "kategori": "Cebir", "tur": "ZORUNLU",
        "icerik": "Bu ders; lineer denklem sistemlerinin çözümü, matris operasyonları, matrislerin cebirsel özellikleri, eşelon biçim, kofaktör açılımı ve elemanter matrisler yardımıyla matris tersi bulma tekniklerini kapsar. Özel ve parçalanmış matris yapıları ile determinant uygulamalarından başlayarak; karakteristik polinom, özdeğer (eigenvalue) analizleri, vektör kavramı ve reel vektör uzayı ($R^n$) gibi soyut matematiksel yapıları teorik ve uygulamalı boyutta ele alır. Yapay zekadaki matris çarpanlarına ayırma algoritmalarından bilgisayar grafiklerindeki 3B dönüşümlere, veri bilimindeki boyut indirgeme yöntemlerinden mühendislik simülasyonlarına kadar tüm vektörel ve matrisel sistemlerin temel omurgasını oluşturur.",
        "meslekler": ["Yapay Zeka ve Makine Öğrenmesi Mühendisi", "3B Grafik & Oyun Motoru Yazılımcısı", "Veri Bilimci (Boyut İndirgeme Uzmanı)"]
    },
    "MAT1105": {
        "ad": "Soyut Matematik I (Abstract Mathematics I)", "sinif": 1, "yariyil": 1, "kategori": "Soyut Matematik", "tur": "ZORUNLU",
        "icerik": "Bu ders; önermeler mantığı, niceleyiciler ile doğrudan ispat, çelişkiyle ispat ve matematiksel tümevarım gibi temel ispat tekniklerini kapsar. Kümeler teorisi, küme operasyonları, kartezyen çarpım, bağıntı çeşitleri (denklik ve sıralama bağıntıları) ile fonksiyon kavramını (birebirlik, örtenlik ve bileşke) aksiyomatik boyutta ele alır. Matematiksel düşünme, soyutlama ve rigoröz (kesin) mantıksal akıl yürütme becerisini kazandırarak üst düzey cebir, analiz ve teorik bilgisayar bilimlerinin en temel zeminini oluşturur.",
        "meslekler": ["Formel Doğrulama Mühendisi", "Veritabanı Mimarı", "Yazılım Mantık ve Test Uzmanı"]
    },
    "MAT1107": {
        "ad": "Analitik Geometri I (Analytic Geometry I)", "sinif": 1, "yariyil": 1, "kategori": "Geometri", "tur": "ZORUNLU",
        "icerik": "Bu ders; 2 ve 3 boyutlu uzayda vektörlerin geometrik temsilini, doğru ve düzlem denklemlerini ile dik, kutupsal ve küresel koordinat sistemlerindeki dönüşümleri kapsar. Konik kesitlerini (elips, hiperbol, parabol) ve ikinci dereceden eğrilerin matrisel yöntemlerle standart biçimlere indirgenmesini analitik olarak inceler. Bilgisayar grafiklerinde nesne konumlandırmadan otonom araçların yörünge takibine ve robotik kolların uzamsal hesaplamalarına kadar tüm geometrik yazılımların temelini oluşturur.",
        "meslekler": ["Otonom Sistemler ve Navigasyon Mühendisi", "Bilgisayar Görüsü (Computer Vision) Uzmanı", "Coğrafi Bilgi Sistemleri (CBS/GIS) Yazılımcısı"]
    },
    "MAT1109": {
        "ad": "Analiz I (Analysis I)", "sinif": 1, "yariyil": 1, "kategori": "Analiz", "tur": "ZORUNLU",
        "icerik": "Bu ders; reel sayılar sisteminin aksiyomatik yapısını, dizileri, yakınsaklığı, limitin epsilon-delta tanımını ve fonksiyonlarda süreklilik kavramını kapsar. Türev tanımı, türev alma kuralları, Rolle ve Ortalama Değer Teoremleri ile L'Hopital kuralı gibi türevin temel araçlarını teorik ve uygulamalı boyutta ele alır. Değişimin ve ivmenin matematiğini oluşturarak fiziksel simülasyonlardan makine öğrenmesindeki optimizasyon algoritmalarına kadar tüm sürekli matematiksel modellerin temellerini atar.",
        "meslekler": ["Algoritma ve Optimizasyon Uzmanı", "Fizik Motoru Yazılımcısı", "Finansal Modelleme Analisti"]
    },
    "MAT1104": {
        "ad": "Lineer Cebir II (Linear Algebra II)", "sinif": 1, "yariyil": 2, "kategori": "Cebir", "tur": "ZORUNLU",
        "icerik": "Bu ders; soyut vektör uzayları, alt uzaylar, lineer bağımsızlık, taban (baz), boyut ve lineer dönüşümlerin matris temsilini kapsar. İç çarpım uzayları, Gram-Schmidt dikleştirme yöntemi, özdeğer-özvektör analizi, köşegenleştirme (diyagonalleştirme), Jordan kanonik formu ve kuadratik formları teorik ve uygulamalı boyutta ele alır. Kuantum hesaplamadan makine öğrenmesindeki boyut indirgeme algoritmalarına (PCA/SVD), boyutlar arası geometrik dönüşümlerden veri matrislerinin optimizasyonuna kadar ileri düzey yazılım ve veri biliminin çekirdeğini oluşturur.",
        "meslekler": ["Kuantum Yazılım Mühendisi", "Yapay Zeka Araştırmacısı (Boyut İndirgeme Uzmanı)", "Robotik Kinematik Mühendisi"]
    },
    "MAT1106": {
        "ad": "Soyut Matematik II (Abstract Mathematics II)", "sinif": 1, "yariyil": 2, "kategori": "Soyut Matematik", "tur": "ZORUNLU",
        "icerik": "Bu ders; kardinalite (kümelerin gücü), sonsuz kümeler, sayılabilirlik kavramı ve Cantor hipotezi gibi ileri düzey küme teorisi konularını kapsar. Bölünebilme teorisi, modüler aritmetik ve Zn yapıları üzerinden cebirsel sistemlere geçiş yaparak yarı grup, grup, halka ve cisim gibi yapay/soyut cebirsel sistemlerin temel özelliklerini inceler. Kriptoloji, şifreleme algoritmaları, kodlama teorisi ve soyut cebirin ileriki konularını anlamak için gerekli olan yapıyı inşa eder.",
        "meslekler": ["Kriptolog ve Siber Güvenlik Araştırmacısı", "Blokzincir Protokol Mühendisi", "Kodlama Teorisi Uzmanı"]
    },
    "MAT1110": {
        "ad": "Analiz II (Analysis II)", "sinif": 1, "yariyil": 2, "kategori": "Analiz", "tur": "ZORUNLU",
        "icerik": "Bu ders; belirli ve belirsiz integral kavramlarını, Riemann integralini, Kalkülüsün Temel Teoremini ve gelişmiş integrasyon tekniklerini kapsar. İntegral yardımıyla alan, hacim ve yay uzunluğu hesaplarının yanı sıra dizi ve serileri, kuvvet serilerini, Taylor ve Maclaurin açılımlarını detaylıca inceler. Karmaşık fonksiyonların polinomsal yaklaşımlarından veri analitiğindeki zaman serilerine, sinyal işlemeden alan-hacim hesaplarına kadar birçok alana matematiksel zemin hazırlar.",
        "meslekler": ["Sinyal ve Görüntü İşleme Mühendisi", "Aktüer ve Risk Analisti", "Sayısal Metotlar Uzmanı"]
    },
    "MAT1108": {
        "ad": "Analitik Geometri II (Analytic Geometry II)", "sinif": 1, "yariyil": 2, "kategori": "Geometri", "tur": "ZORUNLU",
        "icerik": "Bu ders; 3 boyutlu uzayda ikinci dereceden kuadrik yüzeyleri (küre, silindir, koni, elipsoid, hiperboloid ve paraboloid) ve bu yüzeylerin düzlem kesitlerini detaylıca inceler. Dönel yüzeyler, teğet düzlemler, dik doğrular ve uzaysal koordinat dönüşümlerinin cebirsel ve geometrik analizini kapsar. 3B oyun motorlarındaki çarpışma algılanmasından (collision detection), mimari parametrik modellemeye ve medikal görüntüleme (MR/BT 3D tarama) sistemlerine kadar geniş bir uygulama alanına sahiptir.",
        "meslekler": ["CAD/CAM Yazılım Mühendisi", "Oyun Motoru Fizik & Çarpışma Mühendisi", "Medikal Görüntüleme ve 3B Rekonstrüksiyon Uzmanı"]
    },
    "IST2225": {
        "ad": "İstatistik I (Statistics I)", "sinif": 2, "yariyil": 1, "kategori": "İstatistik", "tur": "ZORUNLU",
        "icerik": "Bu ders; veri özetleme tekniklerini, olasılık uzaylarını, rastgele değişkenleri ve temel olasılık dağılımlarını (Binom, Poisson, Normal vb.) kapsar. Beklenen değer, varyans, moment üreten fonksiyonlar ile olasılık kuramının omurgasını oluşturan Büyük Sayılar Yasası ve Merkezi Limit Teoremi'ni matematiksel aksiyomlarla ele alır. Veri analitiğinden yapay zeka modellerindeki parametre tahminlerine, finansal risk analizinden A/B testlerine kadar belirsizlik içeren tüm karar verme mekanizmalarının ve istatistiksel çıkarımların temelini oluşturur.",
        "meslekler": ["Veri Bilimci ve Veri Analisti", "Kredi ve Risk Analisti", "Biyoistatistik Uzmanı"]
    },
    "MAT2205": {
        "ad": "Topoloji I (Topology I)", "sinif": 2, "yariyil": 1, "kategori": "Topoloji", "tur": "ZORUNLU",
        "icerik": "Bu ders; topolojik uzay kavramını, açık ve kapalı kümeleri, taban ve alt taban yapılarını, komşulukları ve ayırma aksiyomlarını kapsar. Topolojik uzaylarda süreklilik, homeomorfizma, tıkızlık (compactness) ve bağlantılılık (connectedness) gibi şekillerin esnetilip büküldüğünde korunan soyut geometrik niteliklerini matematiksel aksiyomlarla ele alır. Yüksek boyutlu karmaşık verilerin şekilsel analizini yapan Topolojik Veri Analizi (TDA) yöntemlerinden yapay zekadaki manifold öğrenmesine (Manifold Learning), ağ mimarilerinden kuantum fiziğine kadar soyut matematiksel modellemenin en temel taşlarından birini oluşturur.",
        "meslekler": ["Topolojik Veri Analisti (TDA)", "Manifold Öğrenme Uzmanı (Yapay Zeka)", "Ağ Mimarisi Uzmanı"]
    },
    "MAT2253": {
        "ad": "Bilgisayar Programlama I (Computer Programming I)", "sinif": 2, "yariyil": 1, "kategori": "Uygulamalı Matematik / Yazılım", "tur": "ZORUNLU",
        "icerik": "Bu ders; algoritmik düşünme yapısını, temel veri tiplerini, akış kontrol mekanizmalarını (döngüler, koşullu ifadeler), fonksiyon tanımlamayı ve diziler/matrisler üzerinde veri işlemeyi kapsar. Matematiksel problemleri ve sayısal yöntemleri (kök bulma, matris operasyonları, seriler) bilgisayar ortamında koda dönüştürme ve algoritma karmaşıklığını anlama süreçlerini uygulamalı olarak ele alır. Veri biliminden yapay zekaya, yazılım mühendisliğinden matematiksel modellemeye kadar teorik matematiği endüstriyel ve dijital çözümlere dönüştüren en kritik ilk basamağı oluşturur.",
        "meslekler": ["Yazılım Geliştirme Mühendisi", "Veri Mühendisi", "Hesaplamalı Matematik Uzmanı"]
    },
    "MAT2255": {
        "ad": "Analiz III (Analysis III)", "sinif": 2, "yariyil": 1, "kategori": "Analiz", "tur": "ZORUNLU",
        "icerik": "Bu ders; tek değişkenli analizden n uzayındaki çok değişkenli fonksiyonlara geçişi, kısmi türevleri, yönlü türevleri, gradyan vektörünü ve Jakobiyen matrislerini kapsar. Çok değişkenli fonksiyonlarda kısıtlı ve kısıtsız ekstremum problemlerini Lagrange çarpanları yöntemiyle çözmeyi, çift ve üçlü katlı integralleri ele alır. Yapay zekadaki çok katmanlı yapay sinir ağlarının geri yayılım (backpropagation) algoritmalarından iktisattaki fayda maksimizasyonuna kadar çok boyutlu sistemlerin temelini oluşturur.",
        "meslekler": ["Yapay Zeka ve Derin Öğrenme Mühendisi", "Ekonometri Uzmanı", "Otonom Araç Çevre Algılama Uzmanı"]
    },
    "IST2226": {
        "ad": "İstatistik II (Statistics II)", "sinif": 2, "yariyil": 2, "kategori": "İstatistik", "tur": "ZORUNLU",
        "icerik": "Bu ders; nokta ve aralık tahmini yöntemlerini (Maksimum Olabilirlik - MLE, Momentler Yöntemi), güven aralıklarını ve hipotez testi kuramını (Tip I/II hatalar, p-değeri, Neyman-Pearson Lemması) kapsar. Ki-Kare testleri, uyum iyiliği testleri, varyans analizi (ANOVA) ve basit doğrusal regresyon ile örneklem verisinden kitle parametrelerine dair matematiksel çıkarım yapma tekniklerini işler. Veri bilimindeki hipotez doğrulamadan dijital ürünlerdeki A/B testlerine, makine öğrenmesindeki model parametre kestiriminden finansal tahminleme sistemlerine kadar tüm kanıta dayalı karar süreçlerinin temelini oluşturur.",
        "meslekler": ["A/B Test ve Büyüme Analisti", "İstatistiksel Modelleyici (ML)", "Risk ve Kredi Tahmin Analisti"]
    },
    "MAT2206": {
        "ad": "Topoloji II (Topology II)", "sinif": 2, "yariyil": 2, "kategori": "Topoloji", "tur": "ZORUNLU",
        "icerik": "Bu ders; çarpım uzaylarını, bölüm uzaylarını, ileri ayırma aksiyomlarını, Urysohn Lemması ve Tietze Genişletme Teoremi'ni kapsar. Metrikleşebilirlik teoremlerini, metrik uzaylarda tamlık kavramını, Tychonoff Teoremi ile tıkızlaştırma yöntemlerini ve temel grup (homotopi) kavramına girişi detaylıca ele alır. Robotik sistemlerdeki durum/hareket uzayı tanımlamalarından kuantum alan teorisindeki durum manifoldlarına ve veri bilimindeki karmaşık uzay indirgemelerine kadar soyut matematiğin en üst düzey geometrik araçlarını sunar.",
        "meslekler": ["Robotik Hareket Planlama Mühendisi", "Yüksek Boyutlu Veri Analisti", "Kuantum Bilişim Araştırmacısı"]
    },
    "MAT2254": {
        "ad": "Bilgisayar Programlama II (Computer Programming II)", "sinif": 2, "yariyil": 2, "kategori": "Uygulamalı Matematik / Yazılım", "tur": "ZORUNLU",
        "icerik": "Bu ders; Nesne Yönelimli Programlama (OOP) ilkelerini (sınıflar, nesneler, kalıtım, kapsülleme), gelişmiş veri yapılarını, dosya yönetimini ve hata yakalama mekanizmalarını kapsar. Modüler yazılım geliştirme prensipleri ile bilimsel hesaplama kütüphanelerini kullanarak karmaşık matematiksel algoritmaları ve veri işleme süreçlerini nesne tabanlı yapıda tasarlama becerisini işler. Yazılım mimarisinden nesne tabanlı sistem tasarımına, hesaplamalı bilim simülasyonlarından büyük veri analitiğine kadar modern yazılım ve teknoloji dünyasının omurgasını oluşturur.",
        "meslekler": ["Backend / Yazılım Mimarisi Mühendisi", "Veri Analisti ve ML Geliştiricisi", "Oyun ve Simülasyon Yazılımcısı"]
    },
    "MAT2256": {
        "ad": "Analiz IV (Analysis IV)", "sinif": 2, "yariyil": 2, "kategori": "Analiz", "tur": "ZORUNLU",
        "icerik": "Bu ders; vektör alanlarını, eğrisel integralleri, yüzey integrallerini ve akı (flux) hesaplarını kapsar. Green, Stokes ve Gauss (Iraksama) teoremleri ile vektör kalkülüsünün temel korunum yasalarını derinlemesine işler. Fonksiyon dizileri, fonksiyon serileri ve düzgün yakınsaklık kavramlarını inceleyerek akışkanlar mekaniği, elektromanyetizma, alan teorileri ve veri bilimindeki manifold analizine doğrudan zemin hazırlar.",
        "meslekler": ["Akışkanlar Mekaniği (CFD) Simülasyon Mühendisi", "Elektromanyetik Sistemler Mühendisi", "Geometrik Derin Öğrenme Uzmanı"]
    },
    "MAT2229": {
        "ad": "Matematik Laboratuvarı I (Mathematics Laboratory I)", "sinif": 2, "yariyil": 1, "kategori": "Uygulamalı Matematik / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Analiz, Lineer Cebir ve Bilgisayar Programlama derslerine ilgi duyan, soyut matematiksel kavramları bilgisayar yazılımlarıyla görselleştirip algoritmik olarak çözmek isteyen öğrenciler için tasarlanmıştır. Bilgisayarlı cebir ve hesaplama sistemlerini (MATLAB, SageMath, Mathematica veya Python ekosistemi) kullanarak sembolik ve nümerik hesaplamaları, matris operasyonlarını, 2B/3B fonksiyon grafiklerinin çizimini ve kök bulma algoritmalarını kapsar. Teorik problemleri bilgisayar ortamında modelleme ve veri görselleştirme becerisi kazandırarak hesaplamalı bilim, veri analitiği ve nümerik simülasyon çalışmalarının pratik uygulama temelini oluşturur.",
        "meslekler": ["Hesaplamalı Matematik Uzmanı", "Bilimsel Yazılım Geliştiricisi", "Veri ve Algoritma Analisti"]
    },
    "MAT2267": {
        "ad": "Matematik Tarihi (History of Mathematics)", "sinif": 2, "yariyil": 1, "kategori": "Matematik Tarihi", "tur": "SEÇMELİ",
        "icerik": "Bu ders; matematiğin felsefi, tarihsel ve kavramsal gelişimine ilgi duyan, soyut kuramların arkasındaki tarihsel kırılma noktalarını ve insanlık düşünce tarihini anlamak isteyen öğrenciler için tasarlanmıştır. Antik Mısır, Babil ve Yunan matematiğinden İslam Dünyası'nın altın çağına ve modern analizin doğuşuna kadar sayı sistemlerinin, geometrinin, cebirin ve kalkülüsün evrimini kapsar. Matematiksel kavramların tarihsel bağlamını kavramak; akademik araştırmalardan bilim iletişimi ve yayıncılığına, matematik eğitiminden bilim felsefesi ve teknik yazarlığa kadar analitik düşüncenin köklerini anlamada temel oluşturur.",
        "meslekler": ["Bilim İletişimcisi ve Yazarı", "Akademisyen / Bilim Historikeri", "Matematik Eğitimi ve Müfredat Uzmanı"]
    },
    "MAT2333": {
        "ad": "Tasarı Geometri (Design Geometry)", "sinif": 2, "yariyil": 1, "kategori": "Geometri", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Geometri, Bilgisayar Grafikleri, Mimarlık, CAD/CAM sistemleri ve 3B Görsel Tasarıma ilgi duyan, üç boyutlu uzay nesnelerini iki boyutlu düzlem üzerinde teknik olarak ifade etmek isteyen öğrenciler için tasarlanmıştır. Dik ve eğik izdüşüm yöntemlerini, Monge (çift dik izdüşüm) metodunu, uzayda nokta, doğru ve düzlem elemanlarının izdüşümsel durumlarını, ara kesit hesaplarını, dönme-yatırma dönüşümlerini ve cisimlerin açınımlarını kapsar. Üç boyutlu uzaysal düşünme yeteneği kazandırarak bilgisayar destekli tasarım (CAD) yazılımlarından mimari/mühendislik çizimlerine, 3B baskı teknolojilerinden oyun/animasyon motorlarındaki hacimsel modellemelere kadar görsel teknolojilerin geometrik altyapısını oluşturur.",
        "meslekler": ["CAD/CAM ve 3B Modelleme Yazılımcısı", "3B Rendering Uzmanı", "Hesaplamalı Tasarım Analisti"]
    },
    "MAT2230": {
        "ad": "Matematik Laboratuvarı II (Mathematics Laboratory II)", "sinif": 2, "yariyil": 2, "kategori": "Uygulamalı Matematik / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Diferensiyel Denklemler, Nümerik Analiz, Optimizasyon ve Veri Bilimi derslerine ilgi duyan, teorik matematik modellerini ileri seviye yazılım algoritmalarıyla bilgisayar ortamında simüle etmek isteyen öğrenciler için tasarlanmıştır. Bilgisayarlı matematik ve programlama dilleri (MATLAB, Python, Mathematica vb.) kullanılarak diferansiyel denklem sistemlerinin sayısal çözümlerini, eğri uydurma (curve fitting) analizlerini, optimizasyon problemlerini ve stokastik (Monte Carlo) simülasyon tekniklerini kapsar. Gelişmiş analitik problemleri bilgisayar kodlarına dökme becerisi kazandırarak, makine öğrenmesi çekirdek algoritmalarından mühendislik simülasyonlarına ve yüksek başarımlı hesaplama (HPC) projelerine kadar modern teknoloji alanlarının uygulama altyapısını oluşturur.",
        "meslekler": ["Makine Öğrenmesi Mühendisi", "Hesaplamalı Simülasyon Uzmanı", "Algoritma Geliştirici"]
    },
    "MAT2270": {
        "ad": "Sayılar Teorisi (Number Theory)", "sinif": 2, "yariyil": 2, "kategori": "Sayılar Teorisi", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Cebir, Kriptografi ve Ayrık Matematik alanlarına ilgi duyan, tam sayıların gizemli dünyasını ve asal sayıların şifreleme algoritmalarındaki rolünü keşfetmek isteyen öğrenciler için tasarlanmıştır. Bölünebilme kurallarını, asal sayıları, EBOB/EKOK algoritmalarını (Öklid algoritması), modüler aritmetiği, lineer kongrüansları, Çin Kalan Teoremi'ni, Fermat, Euler ve Wilson teoremleri ile ilkel kökleri (primitive roots) kapsar. Binlerce yıllık soyut sayı problemlerini çözmenin yanı sıra, günümüzde internet bankacılığını, dijital imzaları, blokzincir mimarisini ve RSA gibi modern siber güvenlik protokollerini ayakta tutan en temel matematiksel omurgayı oluşturur.",
        "meslekler": ["Kriptografi ve Siber Güvenlik Uzmanı", "Blokzincir Geliştiricisi", "Algoritma ve Veri Güvenliği Analisti"]
    },
    "MAT2272": {
        "ad": "Kombinatorik (Combinatorics)", "sinif": 2, "yariyil": 2, "kategori": "Ayrık Matematik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Olasılık, İstatistik, Ayrık Matematik ve Bilgisayar Bilimlerine ilgi duyan, sonlu kümeler üzerindeki yapıları sayma, düzenleme ve optimize etme problemleriyle uğraşmak isteyen öğrenciler için tasarlanmıştır. Güvercin yuvası ilkesi, saymanın temel ilkeleri, permütasyon, kombinasyon, içerme-dışarma prensibi, üretici fonksiyonlar ve yineleme bağıntılarını kapsar. Karmaşık sıralama ve seçme problemlerini formüle etme yeteneği kazandırarak, yazılım algoritmalarının zaman karmaşıklığı analizinden (Big-O) veri yapılarına, şifreleme ihtimallerinin hesaplanmasından yöneylem araştırmalarındaki ağ optimizasyonlarına kadar bilgisayar ve mühendislik bilimlerinin sayma altyapısını oluşturur.",
        "meslekler": ["Algoritma Mühendisi", "Veri Bilimcisi ve Olasılık Analisti", "Ağ ve Optimizasyon Uzmanı"]
    },
    "MAT2276": {
        "ad": "İngilizce Matematiksel Kavramlar (Mathematical Concepts in English)", "sinif": 2, "yariyil": 2, "kategori": "Dil ve İletişim", "tur": "SEÇMELİ",
        "icerik": "Bu ders; uluslararası akademik kaynakları takip etmek, küresel düzeyde bilimsel iletişim kurmak ve İngilizce matematiksel terminolojiye hâkim olmak isteyen öğrenciler için tasarlanmıştır. Temel analiz, cebir, geometri ve uygulamalı matematik kavramlarının İngilizce karşılıklarını, formal tanım kalıplarını, teorem ispatı ifade biçimlerini ve akademik makale okuma/yazma tekniklerini kapsar. Yurt dışında lisansüstü eğitim (master/doktora) planlayan, uluslararası Ar-Ge projelerinde yer alacak veya global teknoloji şirketlerinde çalışacak matematikçiler için kritik bir dilsel ve akademik altyapı oluşturur.",
        "meslekler": ["Uluslararası Ar-Ge Araştırmacısı", "Küresel Teknik Yazar ve Çevirmen", "Global Veri Analisti"]
    },
    "MAT3301": {
        "ad": "Cebir I (Algebra I)", "sinif": 3, "yariyil": 1, "kategori": "Cebir", "tur": "ZORUNLU",
        "icerik": "Bu ders; grup kavramını, alt grupları, devirli (siklik) grupları, permütasyon ve simetri gruplarını, Lagrange Teoremi'ni, normal alt grupları ve bölüm gruplarını kapsar. Grup homomorfizmaları, izomorfizm teoremleri ve otomorfizmalar yardımıyla soyut matematiksel yapıların simetri özelliklerini aksiyomatik boyutta derinlemesine inceler. Modern kriptolojideki açık anahtarlı şifreleme sistemlerinden (RSA, Eliptik Eğriler) kuantum bilişimdeki kuantum kapılarına, blokzincir protokollerinden veri iletimindeki hata düzeltme kodlarına kadar siber güvenliğin ve soyut yazılım mimarilerinin çekirdeğini oluşturur.",
        "meslekler": ["Kriptoloji ve Siber Güvenlik Mimarı", "Blokzincir Protokol Mühendisi", "Kuantum Bilişim Analisti"]
    },
    "MAT3313": {
        "ad": "Nümerik Analiz I (Numerical Analysis I)", "sinif": 3, "yariyil": 1, "kategori": "Uygulamalı Matematik", "tur": "ZORUNLU",
        "icerik": "Bu ders; hata analizini (yuvarlama ve kesme hataları), tek değişkenli doğrusal olmayan denklemlerin kök bulma yöntemlerini (Bisection, Newton-Raphson, Kiriş) ve doğrusal denklem sistemlerinin sayısal çözümlerini (Gauss eleme, LU ayrışımı, Jacobi, Gauss-Seidel) kapsar. Polinomsal interpolasyon (Lagrange, Newton, Spline) ile sayısal türev ve integral (Trapez, Simpson kuralları) hesaplama tekniklerini matematiksel ve algoritmik yaklaşımlarla ele alır. Analitik çözümü bulunamayan karmaşık matematiksel modellerin bilgisayar ortamında yüksek hassasiyet ve minimum hatayla simüle edilmesini sağlayarak mühendislik yazılımlarından finansal hesaplamalara, veri analitiğinden yapay zekaya kadar sayısal kodlamanın temelini oluşturur.",
        "meslekler": ["Hesaplamalı Mühendislik Yazılımcısı", "Quant Finansal Risk Analisti", "Veri Bilimci / Algoritma Optimizasyon Uzmanı"]
    },
    "MAT3315": {
        "ad": "Diferensiyel Denklemler I (Differential Equations I)", "sinif": 3, "yariyil": 1, "kategori": "Diferansiyel Denklemler", "tur": "ZORUNLU",
        "icerik": "Bu ders; birinci basamaktan diferensiyel denklemleri (ayrılabilir, tam, lineer, Bernoulli/Riccati), yüksek basamaktan sabit katsayılı lineer denklemleri, belirsiz katsayılar ve parametrelerin değişimi yöntemleri ile Laplace dönüşümlerini kapsar. Zamanla değişen fiziksel, biyolojik ve finansal sistemlerin anlık değişim oranlarını denklemleştirerek dinamik süreçlerin matematiksel modellemesini ele alır. Kontrol sistemleri mühendisliğinden borsa ve opsiyon fiyatlama modellerine, oyun motorlarındaki fizik simülasyonlarından sürekli zamanlı yapay sinir ağlarına (Neural ODEs) kadar uzanan geniş bir mühendislik ve yazılım yelpazesinin hesaplama motorunu oluşturur.",
        "meslekler": ["Kontrol ve Otonom Sistemler Mühendisi", "Algoritmik Ticaret Analisti", "Fiziksel Simülasyon Yazılımcısı"]
    },
    "MAT3317": {
        "ad": "Kompleks Fonksiyonlar Teorisi I (Theory of Complex Functions I)", "sinif": 3, "yariyil": 1, "kategori": "Analiz", "tur": "ZORUNLU",
        "icerik": "Bu ders; karmaşık sayılar kümesini, karmaşık düzlemdeki topolojiyi, Cauchy-Riemann denklemlerini ve analitik (holomorf) fonksiyon kavramını kapsar. Karmaşık düzlemde eğrisel integralleri, Cauchy İntegral Teoremi ve Formülü'nü, Taylor ve Laurent seri açılımları ile aykırı (singüler) noktaları ve Kalan (Residue) Teoremi'ni derinlemesine ele alır. Gerçel analizde hesaplanması imkansıza yakın integrallerin kolayca çözülmesinden sinyal işlemedeki frekans alanı analizine, kontrol sistemlerindeki kutup-sıfır (pole-zero) kararlılık modellerinden kuantum elektroniğine kadar mühendislik ve fiziksel simülasyonların teorik temelini oluşturur.",
        "meslekler": ["Sinyal İşleme ve Haberleşme Mühendisi", "Akışkanlar Dinamiği Simülasyon Yazılımcısı", "Kuantum Sistemler Mühendisi"]
    },
    "MAT3319": {
        "ad": "Diferensiyel Geometri I (Differential Geometry I)", "sinif": 3, "yariyil": 1, "kategori": "Geometri", "tur": "ZORUNLU",
        "icerik": "Bu ders; 3-boyutlu Öklid uzayında uzay eğrilerinin geometrisini, teğet vektör alanlarını, parametreleştirmeyi ve yay uzunluğu (arc length) kavramını kapsar. Frenet-Serret çatılarını (teğet, normal, binormal vektörler), eğrilik (curvature) ve burulma (torsion) kavramları ile Eğrilerin Temel Teoremi'ni derinlemesine ele alır. Otonom araçların virajlarda sarsıntısız yörünge planlamasından bilgisayar grafiklerindeki 3B Bézier/Spline eğri modellemelerine, robot kollarının uzay hareket kinematiğinden aerodinamik hat tasarımlarına kadar tüm uzaysal geometrik yazılımların matematiksel omurgasını oluşturur.",
        "meslekler": ["Otonom Araç Yörünge Mühendisi", "3B CAD/VFX Yazılım Mühendisi", "Robotik Kinematik Uzmanı"]
    },
    "MAT3302": {
        "ad": "Cebir II (Algebra II)", "sinif": 3, "yariyil": 2, "kategori": "Cebir", "tur": "ZORUNLU",
        "icerik": "Bu ders; halka (ring) yapısını, alt halkaları, idealleri, bölüm halkalarını, halka homomorfizmalarını, tamlık bölgelerini ve polinom halkalarını kapsar. Cisim genişlemelerini, asal ve maksimal idealleri ile sonlu cisimleri (Galois alanları) aksiyomatik ve yapısal boyutlarıyla ele alır. Post-kuantum kriptografiden blokzincirdeki sıfır-bilgi ispatlarına (zk-SNARKs), 5G/6G haberleşmesindeki Reed-Solomon hata düzeltme kodlarından simetrik şifreleme standartlarına (AES) kadar ileri seviye siber güvenlik ve kodlama teknolojilerinin matematiksel omurgasını oluşturur.",
        "meslekler": ["Post-Kuantum Kriptoloji Mühendisi", "Sıfır Bilgi İspatı (ZK) Protokol Mühendisi", "Hata Düzeltme Kodları Uzmanı"]
    },
    "MAT3314": {
        "ad": "Nümerik Analiz II (Numerical Analysis II)", "sinif": 3, "yariyil": 2, "kategori": "Uygulamalı Matematik", "tur": "ZORUNLU",
        "icerik": "Bu ders; matrislerin özdeğer ve özvektörlerinin sayısal hesaplanmasını (Güç yöntemi, QR ayrışımı, SVD), adi diferensiyel denklemlerin (ODE) başlangıç ve sınır değer problemlerinin sayısal çözümlerini (Euler, Runge-Kutta, Çok adımlı yöntemler) ve kısmi türevli denklemlere (PDE) sayısal yaklaşım tekniklerini (Sonlu Farklar Yöntemi - FDM) kapsar. Doğrusal olmayan denklem sistemlerinin bilgisayar ortamında yüksek hassasiyetli sayısal çözümlerini ve bu yöntemlerin kararlılık/yakınsaklık analizlerini derinlemesine ele alır. Yapay zekadaki matris ayrıştırma algoritmalarından mühendislik simülasyon yazılımlarına, finansal diferansiyel denklem çözücülerinden iklim ve akışkanlar dinamiği modellerine kadar yüksek başarımlı hesaplamalı bilimlerin altyapısını oluşturur.",
        "meslekler": ["HPC / Hesaplamalı Bilim Uzmanı", "Yapay Zeka Çekirdek Algoritma Mühendisi", "Quant PDE Çözücü Analisti"]
    },
    "MAT3316": {
        "ad": "Diferensiyel Denklemler II (Differential Equations II)", "sinif": 3, "yariyil": 2, "kategori": "Diferansiyel Denklemler", "tur": "ZORUNLU",
        "icerik": "Bu ders; lineer diferensiyel denklem sistemlerini, varlık ve teklik teoremlerini (Picard-Lindelöf), seri çözümlerini (Frobenius yöntemi) ve lineer olmayan sistemlerde kararlılık (Liapunov anlamında kararlılık, faz portreleri, kritik noktalar) analizini kapsar. Zamana bağlı birden fazla değişkenin birbirine bağlı değişim dinamiklerini ve sistemlerin uzun vadeli kararlılık/dönüm noktalarını matematiksel olarak modeller. Robotik kontrol sistemlerinin durum-uzay (state-space) yazılımlarından ekolojik/biyolojik popülasyon simülasyonlarına, çok değişkenli makroekonomik risk modellerinden kaotik sistem analizlerine kadar karmaşık mühendislik süreçlerinin temelini oluşturur.",
        "meslekler": ["Robotik Kontrol ve Sistem Mühendisi", "Hesaplamalı Biyoloji Analisti", "Sistemik Risk ve Finans Analisti"]
    },
    "MAT3318": {
        "ad": "Kompleks Fonksiyonlar Teorisi II (Theory of Complex Functions II)", "sinif": 3, "yariyil": 2, "kategori": "Analiz", "tur": "ZORUNLU",
        "icerik": "Bu ders; konform (açı koruyan) dönüşümleri, Schwarz-Christoffel dönüşümünü, Riemann Kaplama Teoremi'ni, harmonik fonksiyonları ve Dirichlet problemini kapsar. Analitik devam (analytic continuation) kavramını, sonsuz çarpımları, Weierstrass ve Mittag-Leffler açılım teoremleri ile meromorf fonksiyonları ve Riemann Yüzeyleri'ne girişi derinlemesine ele alır. Düzensiz geometrik sınırları basit alanlara eşleyerek akışkanlar dinamiğindeki aerodinamik hesaplamalardan elektrostatik potansiyel alan simülasyonlarına, 3B bilgisayar grafiklerindeki doku kaplamadan (texture mapping) kuantum fiziğine kadar ileri matematiksel modelleme tekniklerinin altyapısını oluşturur.",
        "meslekler": ["CFD ve Aerodinamik Simülasyon Yazılımcısı", "Elektromanyetik Potansiyel Alan Mühendisi", "Hesaplamalı Geometri Mühendisi"]
    },
    "MAT3320": {
        "ad": "Diferensiyel Geometri II (Differential Geometry II)", "sinif": 3, "yariyil": 2, "kategori": "Geometri", "tur": "ZORUNLU",
        "icerik": "Bu ders; 3-boyutlu Öklid uzayında yüzeyler teorisini, teğet düzlemleri, I. ve II. Temel Formları, Şekil Operatörünü (Weingarten dönüşümü) ile Gauss ve Ortalama Eğrilik kavramlarını kapsar. Yüzeyler üzerindeki en kısa yollar olan Jeodezikleri, doğrultu çizgilerini ve Gauss'un Theorema Egregium (Muhteşem Teorem) ilkesiyle yüzeylerin içsel (intrinsic) geometrik korunum özelliklerini derinlemesine ele alır. Bilgisayar grafiklerindeki 3B yüzey modelleme (mesh processing) algoritmalarından otonom sistemlerde eğri yüzeyler üzerindeki jeodezik rota planlamasına, Genel Görelilik kuramındaki uzay-zaman bükülmesinden mimari kabuk yapı tasarımlarına kadar modern geometrik mühendisliğin temelini oluşturur.",
        "meslekler": ["3B Yüzey Modelleme Yazılımcısı", "Jeodezik Rota ve Seyir Uzmanı", "Hesaplamalı Mimari Tasarımcısı"]
    },
    "MAT3329": {
        "ad": "Matematik Laboratuvarı III (Mathematics Laboratory III)", "sinif": 3, "yariyil": 1, "kategori": "Uygulamalı Matematik / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Özellikle Nümerik Analiz, Bilgisayar Programlama ve Uygulamalı Matematik alanlarına ilgi duyan, ileri düzey soyut ve sayısal problemleri yazılım araçlarıyla modellemek isteyen öğrenciler için tasarlanmıştır. Bu ders; gelişmiş bilgisayarlı cebir sistemlerini ve programlama dillerini (Python, MATLAB, Mathematica) kullanarak karmaşık analitik ve sayısal modellerin bilgisayar simülasyonlarını gerçekleştirmeyi kapsar. Kısmi türevli denklemlerin (PDE) sayısal çözümlerini, optimizasyon algoritmalarını, görselleştirme araçlarını ve büyük veri setlerinin matematiksel analizini derinlemesine ele alarak ileri düzey teorik matematiği endüstriyel yazılımlara dönüştürme yeteneği kazandırır.",
        "meslekler": ["HPC ve Bilimsel Simülasyon Mühendisi", "Kıdemli Algoritma Mühendisi", "Yapay Zeka Çekirdek Uzmanı"]
    },
    "MAT3331": {
        "ad": "Kinematik (Kinematics)", "sinif": 3, "yariyil": 1, "kategori": "Uygulamalı Matematik / Fizik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Mekanik, Fizik, Diferensiyel Geometri ve Robotik alanlarına ilgi duyan, hareket eden cisimlerin nedenlerine inmeden yalnızca uzaydaki yörünge, konum, hız ve ivme dinamiklerini incelemek isteyen öğrenciler için tasarlanmıştır. Vektörel kinematik, eğrisel hareketler, hız ve ivme bileşenleri, dönme hareketleri, Euler açıları ve mekanizmaların hareket denklemlerini kapsar. Otonom robot kollarının eklem yörünge planlamasından havacılık simülasyonlarına, animasyon karakterlerinin iskelet kinematiğinden mekanik sistemlerin uzaysal analizine kadar hareket gerektiren tüm mühendislik disiplinlerinin matematiksel altyapısını oluşturur.",
        "meslekler": ["Robotik Kinematik Mühendisi", "Fizik Simülasyonu Yazılımcısı", "Uçuş Yörünge Analisti"]
    },
    "MAT3335": {
        "ad": "Kriptoloji (Cryptology)", "sinif": 3, "yariyil": 1, "kategori": "Siber Güvenlik / Kriptoloji", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Sayılar Teorisi, Cebir, Siber Güvenlik ve Bilgisayar Bilimlerine ilgi duyan, dijital verilerin gizliliğini sağlamak ve şifreleme/şifre çözme algoritmalarının matematiksel altyapısını öğrenmek isteyen öğrenciler için tasarlanmıştır. Klasik şifreleme yöntemlerini (Sezar, Vigenere), simetrik şifreleme blok algoritmalarını (AES, DES), açık anahtarlı kriptografi sistemlerini (RSA, ElGamal, Eliptik Eğri Kriptografisi - ECC) ve anahtar değişim protokollerini kapsar. Sayıların ve sonlu cisimlerin şifrelemedeki kritik rollerini inceleyerek internet bankacılığından e-ticarete, siber güvenlik protokollerinden blokzincir mimarilerine kadar modern dijital dünyanın matematiksel güvenliğini sağlar.",
        "meslekler": ["Kriptolog ve Siber Güvenlik Uzmanı", "Blokzincir Güvenlik Mühendisi", "Veri Gizliliği Mimarı"]
    },
    "MAT3337": {
        "ad": "Fraktal Geometri (Fractal Geometry)", "sinif": 3, "yariyil": 1, "kategori": "Geometri / Dinamik Sistemler", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Topoloji, Dinamik Sistemler, Bilgisayar Grafikleri ve Doğrusal Olmayan Analiz alanlarına ilgi duyan, klasik Öklid geometrisinin yetersiz kaldığı düzensiz, ölçek-bağımsız (self-similar) doğa formlarını ve karmaşık matematiksel yapıları incelemek isteyen öğrenciler için tasarlanmıştır. Hausdorff boyutu, kendi kendine benzerlik, yinelenen fonksiyon sistemleri (IFS) ile Julia ve Mandelbrot kümeleri gibi non-lineer dinamik sistem kavramlarını kapsar. Doğadaki karmaşık ve girift yapıları matematiksel olarak modelleme yeteneği kazandırarak bilgisayar grafiklerindeki gerçekçi doğa simülasyonlarından fraktal anten tasarımlarına, sıkıştırma algoritmalarından kaos teorisine kadar modern teknolojinin pek çok alanında uygulama altyapısı oluşturur.",
        "meslekler": ["Prosedürel Grafik Mühendisi", "Fraktal Anten Tasarımcısı", "Kaotik Sistemler Analisti"]
    },
    "MAT3339": {
        "ad": "Doğrusal Programlama (Linear Programming)", "sinif": 3, "yariyil": 1, "kategori": "Optimizasyon / Uygulamalı Matematik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Optimizasyon, Yöneylem Araştırması, Uygulamalı Matematik ve İktisadi Veri Analizine ilgi duyan, kısıtlar altında en iyi sonucu (maksimum kar veya minimum maliyet) bulma problemlerini matematiksel olarak modellemek isteyen öğrenciler için tasarlanmıştır. Doğrusal programlama modellerini kurma, Simpleks (Simplex) yöntemi, ikilik (duality) teorisi, duyarlılık (sensitivity) analizi ve taşıma/atama (transportation & assignment) problemlerinin çözüm algoritmalarını kapsar. Karmaşık kaynak dağılımı problemlerini formüle etme yeteneği kazandırarak lojistik ağ optimizasyonundan tedarik zinciri yönetimine, finansal portföy planlamasından yapay zeka maliyet minimizasyonuna kadar endüstriyel karar alma süreçlerinin temelini oluşturur.",
        "meslekler": ["Optimizasyon Uzmanı", "Tedarik Zinciri Analisti", "Kaynak Planlama Uzmanı"]
    },
    "MAT3321": {
        "ad": "Algoritmalar ve Veri Yapıları (Algorithms and Data Structures)", "sinif": 3, "yariyil": 1, "kategori": "Bilgisayar Bilimleri", "tur": "SEÇMELİ",
        "icerik": "Özellikle Bilgisayar Bilimleri, Yazılım Geliştirme ve Uygulamalı Matematik alanlarına ilgi duyan, verileri bilgisayar belleğinde en verimli şekilde saklama, arama ve işleme algoritmalarını öğrenmek isteyen öğrenciler için tasarlanmıştır. Doğrusal ve doğrusal olmayan veri yapılarını (diziler, bağlı listeler, yığınlar, kuyruklar, ağaçlar ve graflar), arama/sıralama algoritmalarını ve bu algoritmaların Big-O notasyonu ile zaman/bellek karmaşıklığı analizini kapsar. Büyük veri kümelerini işleme, optimize kod yazma ve modern yazılım mühendisliğinin temel hesaplama mimarisini kurma yeteneği kazandırarak bilgisayar bilimlerinin çekirdek altyapısını oluşturur.",
        "meslekler": ["Yazılım ve Algoritma Geliştiricisi", "Backend Sistem Mimarisi Mühendisi", "AI Veri Yapıları Mühendisi"]
    },
    "MAT3345": {
        "ad": "Sembolik Programlama Dilleri (Symbolic Programming Languages)", "sinif": 3, "yariyil": 1, "kategori": "Yazılım / Bilgisayarlı Cebir", "tur": "SEÇMELİ",
        "icerik": "Özellikle Bilgisayar Bilimleri, Yapay Zeka, Bilgisayarlı Cebir ve Uygulamalı Matematik alanlarına ilgi duyan, sayısal değerler yerine sembolik ifadelerle cebirsel manipülasyonlar yapmak ve mantıksal programlama dillerini öğrenmek isteyen öğrenciler için tasarlanmıştır. Bu ders; bilgisayarlı cebir sistemlerini (Mathematica, SageMath, SymPy), LISP veya Prolog benzeri sembolik/mantıksal programlama paradigmalarını, analitik türev ve integral işlemlerinin harfsel çözüm algoritmalarını ile kural tabanlı sistemleri kapsar. Karmaşık matematiksel formülleri bilgisayar ortamında otomatik olarak sadeleştirme, türetme ve kanıtlama yeteneği kazandırarak bilgisayarlı cebir yazılımlarının geliştirilmesinden uzman sistemler ve otomatik teorem kanıtlama projelerine kadar modern yapay zeka altyapısını oluşturur.",
        "meslekler": ["Bilgisayarlı Cebir Yazılımcısı", "Uzman Sistemler Mühendisi", "Bilimsel Yazılım Otomasyon Uzmanı"]
    },
    "MAT3322": {
        "ad": "Makine Öğrenmesi İçin Matematik (Mathematics for Machine Learning)", "sinif": 3, "yariyil": 2, "kategori": "Yapay Zeka / Veri Bilimi", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Yapay Zeka, Veri Bilimi, Derin Öğrenme ve İstatistiksel Modelleme alanlarına ilgi duyan, modern makine öğrenmesi algoritmalarının arkasındaki matematiksel teoriyi kavramak isteyen öğrenciler için tasarlanmıştır. Çok değişkenli diferansiyel hesap (gradyanlar, Jakobiyen, Hesse matrisi), lineer cebir ayrışımları (SVD, Özdeğer/Özvektörler, PCA), olasılık ve istatistiksel kestirim (Maximum Likelihood, Bayesyen çıkarım) ile konveks optimizasyon (Gradyan İnişi, Lagrange çarpanları) konularını kapsar. Algoritmaların hazır kütüphanelerini kullanmanın ötesine geçerek modelleri matematiksel olarak sıfırdan kurgulama, optimizasyon hatalarını teşhis etme ve yeni nesil yapay zeka mimarileri tasarlama yeteneği kazandırarak veri bilimi ve yapay zeka mühendisliğinin matematiksel omurgasını oluşturur.",
        "meslekler": ["Makine Öğrenmesi Araştırmacısı", "Kıdemli Veri Bilimci", "Derin Öğrenme Mühendisi"]
    },
    "MAT3330": {
        "ad": "Matematik Laboratuvarı IV (Mathematics Laboratory IV)", "sinif": 3, "yariyil": 2, "kategori": "Uygulamalı Matematik / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle İleri Nümerik Analiz, Bilimsel Hesaplama, Paralel Programlama ve Uygulamalı Matematik alanlarına ilgi duyan, devasa ölçekli karmaşık matematiksel modelleri yüksek başarımlı bilgisayar sistemlerinde kodlamak ve simüle etmek isteyen öğrenciler için tasarlanmıştır. Kısmi türevli denklemlerin (PDE) sonlu elemanlar (FEM) veya sonlu farklar (FDM) yöntemleriyle sayısal çözüm simülasyonlarını, paralel matris hesaplama kütüphanelerini ve gerçek dünya fiziksel/mühendislik problemlerinin yazılımsal optimizasyonunu kapsar. Teorik matematiği endüstriyel boyutta ve yüksek performanslı hesaplama (HPC) altyapısında çalıştırabilme becerisi kazandırarak süper bilgisayar simülasyonlarından büyük veri analitiği mimarilerine kadar ileri düzey teknolojik Ar-Ge çalışmalarının uygulama omurgasını oluşturur.",
        "meslekler": ["HPC Mühendisi", "Bilimsel Simülasyon Yazılımcısı", "Performans Optimizasyon Uzmanı"]
    },
    "MAT3336": {
        "ad": "Optimizasyon (Optimization)", "sinif": 3, "yariyil": 2, "kategori": "Optimizasyon / Uygulamalı Matematik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Doğrusal Programlama, Uygulamalı Matematik, Veri Bilimi ve Mühendislik alanlarına ilgi duyan, kısıtlar altında en iyi kararı vermeyi, maliyeti minimize etmeyi veya verimi maksimize etmeyi amaçlayan matematiksel modelleri incelemek isteyen öğrenciler için tasarlanmıştır. Lineer olmayan optimizasyon, konveks küme ve fonksiyonlar, KKT (Karush-Kuhn-Tucker) koşulları, Lagrange çarpanları, gradyan iniş yöntemleri ve temel optimizasyon algoritmalarını kapsar. Karmaşık sistemlerin eniyileme problemlerini çözme yeteneği kazandırarak yapay zeka maliyet fonksiyonlarının optimize edilmesinden lojistik ağ yönetimine ve finansal portföy planlamasına kadar modern endüstriyel kararların analitik temelini oluşturur.",
        "meslekler": ["Optimizasyon Mühendisi", "Yapay Zeka Optimizasyon Uzmanı", "Portföy Optimizasyon Analisti"]
    },
    "MAT3340": {
        "ad": "Spektral Teori (Spectral Theory)", "sinif": 3, "yariyil": 2, "kategori": "Analiz / Operatör Teorisi", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Fonksiyonel Analiz, Kuantum Mekaniği, Diferensiyel Denklemler ve Operatör Teorisi alanlarına ilgi duyan, sonsuz boyutlu vektör uzaylarındaki lineer operatörlerin spektral özelliklerini ve matris özdeğer teorisinin genelleştirilmiş halini incelemek isteyen öğrenciler için tasarlanmıştır. Normlu ve Hilbert uzaylarında lineer operatörlerin spektrumu, rezolvent kümesi, kompakt operatörler, izdüşüm operatörleri ile öz-eşlenik (self-adjoint) operatörlerin spektral teoremlerini kapsar. Kuantum mekaniğindeki fiziksel gözlenebilirlerin matematiksel altyapısını oluşturarak diferansiyel denklemlerin çözüm teorisinden kuantum bilişime ve veri analitiğindeki gelişmiş matris ayrıştırma (SVD/spektral kümeleme) yöntemlerine kadar ileri düzey teorik ve uygulamalı matematiğin omurgasını oluşturur.",
        "meslekler": ["Kuantum Bilişim Araştırmacısı", "Matematiksel Fizik Modelleme Uzmanı", "Spektral Veri Analitiği Mühendisi"]
    },
    "MAT3344": {
        "ad": "Dönüşümler ve Geometriler (Transformations and Geometries)", "sinif": 3, "yariyil": 2, "kategori": "Geometri", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Geometri, Soyut Cebir, Topoloji ve Bilgisayar Grafiklerine ilgi duyan, düzlem ve uzay üzerindeki geometrik dönüşüm gruplarını ve Felix Klein'ın Erlangen Programı perspektifini incelemek isteyen öğrenciler için tasarlanmıştır. İzometriler, benzerlikler, afin dönüşümler, projektif dönüşümler, çemberlere göre ters dönüşüm (inversiyon) ve dönüşüm gruplarının değişmezleri (invariants) teorisini kapsar. Farklı geometri türlerini dönüşüm grupları aracılığıyla birleştirme yeteneği kazandırarak bilgisayar grafikleri ve 3B modellemedeki koordinat dönüşümlerinden robotik uzaysal hareket matrislerine ve modern geometri araştırmalarına kadar geniş bir uygulama alanı sunar.",
        "meslekler": ["Bilgisayar Grafikleri Yazılımcısı", "Robotik Koordinat Dönüşümleri Uzmanı", "Uzaysal Modelleme Araştırmacısı"]
    },
    "MAT3348": {
        "ad": "İntegral Denklemler (Integral Equations)", "sinif": 3, "yariyil": 2, "kategori": "Diferansiyel Denklemler / Analiz", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Diferensiyel Denklemler, Fonksiyonel Analiz, Matematiksel Fizik ve Uygulamalı Matematik alanlarına ilgi duyan, bilinmeyenin integral işareti altında yer aldığı denklemleri çözme teorisini öğrenmek isteyen öğrenciler için tasarlanmıştır. Fredholm ve Volterra tipi lineer integral denklemlerini, çekirdek (kernel) fonksiyonlarını, ardışık yaklaşımlar (Neumann serileri) metodunu, tekil integral denklemlerini ve Green fonksiyonları yardımıyla diferensiyel denklemlerin integral denklemlerine dönüştürülmesini kapsar. Fiziksel ve mühendislik problemlerinde sınır değer sorunlarının çözümünden potansiyel teorisine, kuantum mekaniğindeki saçılma problemlerinden mühendislik modellemelerine kadar gelişmiş analitik analizin temelini oluşturur.",
        "meslekler": ["Matematiksel Fizik Araştırmacısı", "Sınır Elemanları Simülasyon Mühendisi", "İleri Analiz Algoritma Uzmanı"]
    },
    "MAT3362": {
        "ad": "Projektif Geometri (Projective Geometry)", "sinif": 3, "yariyil": 2, "kategori": "Geometri", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Geometri, Cebirsel Geometri, Bilgisayar Grafikleri ve Bilgisayar Görüşü alanlarına ilgi duyan, Öklid geometrisindeki paralellik kısıtını ortadan kaldırarak sonsuzdaki noktaları ve perspektif izdüşümleri incelemek isteyen öğrenciler için tasarlanmıştır. Homojen koordinatlar, projektif düzlem, Desargues ve Pappus teoremleri, çift oran (cross-ratio), konikler ve projektif dönüşüm gruplarını kapsar. Paralel doğruların uzayda kesiştiği perspektif ilişkilerini matematiksel olarak modelleme yeteneği kazandırarak bilgisayar görüşündeki kamera kalibrasyonundan 3B bilgisayar grafiklerine ve modern cebirsel geometriye kadar geniş bir uygulama alanı oluşturur.",
        "meslekler": ["Bilgisayar Görüşü Mühendisi", "3B Bilgisayar Grafikleri Geliştiricisi", "Cebirsel Geometri Araştırmacısı"]
    },
    "MAT3366": {
        "ad": "Kodlama Teorisi (Coding Theory)", "sinif": 3, "yariyil": 2, "kategori": "Uygulamalı Matematik / İletişim Teorisi", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Soyut Cebir, Sayılar Teorisi, Haberleşme Mühendisliği ve Bilgisayar Bilimlerine ilgi duyan, gürültülü kanallar üzerinden yapılan dijital veri iletimi sırasında oluşan hataları tespit ve düzeltme matematiksel algoritmalarını incelemek isteyen öğrenciler için tasarlanmıştır. Sonlu cisimler (Galois Fields), doğrusal kodlar, Hamming kodları, devirli (cyclic) kodlar ve Reed-Solomon hata düzeltme kodlama tekniklerini kapsar. Veri iletiminin güvenilirliğini matematiksel olarak garanti etme yeteneği kazandırarak uydu haberleşmesinden QR kod okuyuculara, depolama sistemlerinden (SSD/HDD) modern siber güvenlik protokollerine kadar bilgi teknolojilerinin altyapısını oluşturur.",
        "meslekler": ["Kanal Kodlama Mühendisi", "Depolama Sistemleri Uzmanı", "Kod Tabanlı Kriptografi Araştırmacısı"]
    },
    "MAT3376": {
        "ad": "Özel Fonksiyonlar (Special Functions)", "sinif": 3, "yariyil": 2, "kategori": "Analiz / Diferansiyel Denklemler", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle Diferensiyel Denklemler, Matematiksel Fizik ve Analiz alanlarına ilgi duyan, klasik analitik yöntemlerle çözülemeyen karmaşık diferensiyel denklemlerin çözümlerini sağlayan özel fonksiyon sınıflarını incelemek isteyen öğrenciler için tasarlanmıştır. Gama ve Beta fonksiyonları, Bessel fonksiyonları, Legendre polinomları, Hermite ve Laguerre polinomları ile Hipergeometrik fonksiyonların seri çözümleri ve ortogonallik özelliklerini kapsar. Fiziksel ve mühendislik problemlerindeki potansiyel teorisi, dalga denklemleri ve kuantum mekaniği simülasyonlarının analitik çözümlerini yapabilme yeteneği kazandırarak ileri düzey matematiksel modelleme ve fiziksel analizlerin temelini oluşturur.",
        "meslekler": ["Matematiksel Fizik Araştırmacısı", "Simülasyon ve Analiz Mühendisi", "Bilimsel Hesaplama Geliştiricisi"]
    },
    "MAT3378": {
        "ad": "Fonksiyonel Analize Giriş (Introduction to Functional Analysis)", "sinif": 3, "yariyil": 2, "kategori": "Analiz", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle İleri Analiz, Topoloji, Kuantum Mekaniği ve Diferensiyel Denklemler alanlarına ilgi duyan, sonlu boyutlu vektör uzaylarının ötesine geçerek sonsuz boyutlu uzayları ve üzerlerindeki lineer operatörleri incelemek isteyen öğrenciler için tasarlanmıştır. Metriklendirilmiş uzaylar, normlu uzaylar, Banach uzayları, Hilbert uzayları, sınırlı lineer operatörler ile Hahn-Banach ve Banach-Steinhaus gibi temel teoremleri kapsar. Fiziksel ve soyut sistemlerin matematiksel modellerini sonsuz boyutlu uzaylarda formüle etme yeteneği kazandırarak kuantum mekaniğinin uzay teorisinden kısmi diferensiyel denklemlerin çözüm uzaylarına ve veri bilimindeki çekirdek (kernel) metotlarına kadar modern matematiğin en temel altyapısını oluşturur.",
        "meslekler": ["Kuantum Bilişim Araştırmacısı", "Matematiksel Fizik Uzmanı", "Çekirdek Metotları Veri Uzmanı"]
    },
    "MAT4001": {
        "ad": "Bitirme Projesi (Graduation Project)", "sinif": 4, "yariyil": 1, "kategori": "Genel Matematik", "tur": "ZORUNLU",
        "icerik": "Bu ders; öğrencinin lisans eğitimi boyunca edindiği teorik matematiksel birikimi ve algoritmik düşünme becerilerini bağımsız bir araştırma, geliştirme veya uygulama projesinde sentezlemesini kapsar. Belirlenen bir uzmanlaşma alanında (soyut matematik, veri bilimi, kriptoloji, nümerik simülasyon, optimizasyon vb.) literatür taraması yapma, problem tanımlama, teorik kanıt sunma veya koda aktarma süreçlerini bilimsel metodolojiyle ele alır. Proje raporunun akademik yazım standartlarında hazırlanması, jüri önünde sunumu ve savunulması aşamalarıyla akademiden endüstriyel Ar-Ge merkezlerine kadar profesyonel kariyer geçişinin en kritik halkasını oluşturur.",
        "meslekler": ["Ar-Ge ve Modelleme Uzmanı", "Akademisyen / Araştırma Görevlisi", "Teknik Proje Yöneticisi"]
    },
    "MAT4401": {
        "ad": "Fonksiyonel Analiz (Functional Analysis)", "sinif": 4, "yariyil": 1, "kategori": "Analiz", "tur": "SEÇMELİ",
        "icerik": "Bu ders; özellikle İleri Analiz, Topoloji, Kuantum Mekaniği ve Diferensiyel Denklemler alanlarına ilgi duyan, fonksiyonel analizin temellerini daha da derinleştirerek topolojik vektör uzaylarını ve gelişmiş operatör teorisini incelemek isteyen öğrenciler için tasarlanmıştır. Genelleştirilmiş fonksiyonlar (dağılımlar teorisi), zayıf yakınsama, spektral ayrışımlar, Hahn-Banach teoreminin ileri uygulamaları ve Banach cebirlerini kapsar. Fiziksel ve soyut sistemlerin sonsuz boyutlu uzaylardaki davranışlarını tam kapsamlı olarak modelleme yeteneği kazandırarak ileri kuantum mekaniğinden kısmi diferensiyel denklemlerin zayıf çözüm uzaylarına (Sobolev uzayları) ve modern analitik Ar-Ge projelerine kadar en üst düzey matematiksel altyapıyı oluşturur.",
        "meslekler": ["Kuantum Bilişim Araştırmacısı", "Matematiksel Modelleme Uzmanı", "İleri Analiz Ar-Ge Mühendisi"]
    },
    "MAT4405": {
        "ad": "Matematiksel Yöntemler ve Uygulamaları (Mathematical Methods and Applications)", "sinif": 4, "yariyil": 1, "kategori": "Uygulamalı Matematik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; fen ve mühendislik bilimlerinde sıklıkla karşılaşılan karmaşık matematiksel modelleri çözmek için ileri analitik yöntemleri öğrenmek isteyen öğrenciler için tasarlanmıştır. Kompleks değişkenler teorisi, adi ve kısmi diferensiyel denklemlerin analitik çözümleri, sınır değer problemleri, perturbasyon (bozuntu) teorisi ve integral dönüşümleri (Fourier/Laplace) konularını kapsar. Fiziksel sistemlerin matematiksel denklemlerini formüle etme ve çözme yeteneği kazandırarak aerodinamik simülasyonlardan ısı transferi analizine ve ileri teknoloji Ar-Ge modellemelerine kadar geniş bir uygulama alanı sunar.",
        "meslekler": ["Matematiksel Modelleme Mühendisi", "Ar-Ge Hesaplamalı Analiz Uzmanı", "Bilimsel Simülasyon Geliştiricisi"]
    },
    "MAT4407": {
        "ad": "Reel Analiz (Real Analysis)", "sinif": 4, "yariyil": 1, "kategori": "Analiz", "tur": "SEÇMELİ",
        "icerik": "Riemann integrasyonunun eksikliklerini gidererek daha geniş fonksiyon sınıfları üzerinde Lebesgue ölçüsü ve integrali kavramlarını incelemek isteyen öğrenciler için tasarlanmıştır. Lebesgue ölçülebilir kümeler, ölçülebilir fonksiyonlar, Lebesgue integrali, yakınsama teoremleri (Monoton Yakınsama ve Lebesgue Domine Yakınsama) ile Lp uzaylarını kapsar. Modern analiz, olasılık teorisinin matematiksel temelleri ve ileri düzey nicel finans modellemelerinde kullanılan güçlü analitik altyapıyı kazandırarak teorik matematiğin en temel taşlarından birini oluşturur.",
        "meslekler": ["Kantitatif Finans Uzmanı", "Stokastik Modelleme Araştırmacısı", "İleri Analiz Ar-Ge Uzmanı"]
    },
    "MAT4409": {
        "ad": "Saçılım Teorisi (Scattering Theory)", "sinif": 4, "yariyil": 1, "kategori": "Matematiksel Fizik", "tur": "SEÇMELİ",
        "icerik": "Dalgaların veya parçacıkların bir potansiyel engel ya da hedefle etkileşime girerek yön değiştirmesini inceleyen matematiksel süreçleri öğrenmek isteyen öğrenciler için tasarlanmıştır. Schrödinger denklemi için saçılım amplitüdü, faz kayması, Lippmann-Schwinger denklemi, Born yaklaşımı ve ters saçılım problemlerini kapsar. Kuantum sistemlerindeki saçılma olaylarının matematiksel modellemesinden radar/sonar sinyal analizine, akustik dalga yayılımından jeofiziksel tomografiye kadar ileri düzey fiziksel uygulamaların temelini oluşturur.",
        "meslekler": ["Kuantum Saçılım Araştırmacısı", "Radar ve Sinyal Yayılım Mühendisi", "Ters Çözüm Tomografi Uzmanı"]
    },
    "MAT4411": {
        "ad": "Diferensiyellenebilir Manifoldlar (Differentiable Manifolds)", "sinif": 4, "yariyil": 1, "kategori": "Diferansiyel Geometri / Topoloji", "tur": "SEÇMELİ",
        "icerik": "Öklid uzayının ötesine geçerek soyut topolojik uzaylar üzerinde diferansiyel hesap yapmayı sağlayan manifold kavramını incelemek isteyen öğrenciler için tasarlanmıştır. Türevlenebilir manifoldlar, teğet uzaylar, vektör alanları, tensör alanları, diferensiyel formlar ve genel Stokes teoremini kapsar. Fiziksel uzay-zaman modellerinden robotik konfigürasyon uzaylarına ve modern fizik teorilerine kadar ileri düzey geometrinin teorik omurgasını oluşturur.",
        "meslekler": ["Geometrik Modelleme Araştırmacısı", "Uzay-Zaman Fizik Uzmanı", "Robotik Konfigürasyon Uzmanı"]
    },
    "MAT4413": {
        "ad": "Diferensiyel Denklem Sistemleri (Systems of Differential Equations)", "sinif": 4, "yariyil": 1, "kategori": "Diferansiyel Denklemler / Dinamik Sistemler", "tur": "SEÇMELİ",
        "icerik": "Tek bir türevsel denklem yerine birden fazla değişkenin birbirine bağlı değişim oranlarını inceleyen denklem sistemlerini çözmek isteyen öğrenciler için tasarlanmıştır. Lineer diferensiyel denklem sistemleri, matris üstelleri, özdeğer ve özvektör yöntemleri, kararlılık analizi, faz portreleri ve non-lineer sistemlerin lineerleştirilmesi konularını kapsar. Mühendislik sistemlerinin kararlılık analizinden ekolojideki av-avcı modellerine ve ekonomi dinamiklerine kadar çoklu değişkenli sistemlerin davranışlarını öngörme yeteneği kazandırır.",
        "meslekler": ["Dinamik Sistemler Mühendisi", "Matematiksel Modelleme Uzmanı", "Otonom Sistemler Ar-Ge Mühendisi"]
    },
    "MAT4415": {
        "ad": "Kompleks Analiz (Complex Analysis)", "sinif": 4, "yariyil": 1, "kategori": "Analiz", "tur": "SEÇMELİ",
        "icerik": "Reel sayıların ötesine geçerek kompleks düzlem üzerindeki fonksiyonların türev, integral ve seri açılımlarını incelemek isteyen öğrenciler için tasarlanmıştır. Kompleks sayılar, analitik fonksiyonlar, Cauchy-Riemann denklemleri, Cauchy integral teoremi ve formülü, Taylor ve Laurent serileri ile Rezidü teoremini kapsar. Fiziksel potansiyel alanlarının ve akışkan hareketlerinin modellemesinden sinyal işlemedeki konformal dönüşümlere kadar ileri düzey analizin en temel taşını oluşturur.",
        "meslekler": ["Kompleks Sistemler Uzmanı", "Simülasyon Mühendisi", "Kantitatif Finans Analisti"]
    },
    "MAT4417": {
        "ad": "İleri Topoloji (Advanced Topology)", "sinif": 4, "yariyil": 1, "kategori": "Topoloji", "tur": "SEÇMELİ",
        "icerik": "Metrik uzayların ötesine geçerek genel topolojik uzayların daha derin yapılarını, kompaktlık, bağlantılılık, ayrılma aksiyomları ve homotopi kavramlarını incelemek isteyen öğrenciler için tasarlanmıştır. Tychonoff teoremi, Urysohn Lemma, Tietze Genişleme Teoremi, kompaktlaştırma yöntemleri, temel grup ve homotopi teorisinin temellerini kapsar. Soyut uzayların küresel yapılarını sınıflandırma yeteneği kazandırarak modern cebirsel topolojiden gelişmiş veri analitiğindeki topolojik veri analizi (TDA) yöntemlerine kadar geniş bir uygulama alanı sunar.",
        "meslekler": ["Topolojik Veri Analizi Uzmanı", "Cebirsel Topoloji Araştırmacısı", "Robotik Konfigürasyon Uzmanı"]
    },
    "MAT4421": {
        "ad": "Kısmi Türevli Denklemlere Giriş (Introduction to PDEs)", "sinif": 4, "yariyil": 1, "kategori": "Diferansiyel Denklemler / Uygulamalı Matematik", "tur": "SEÇMELİ",
        "icerik": "Birden fazla bağımsız değişkene bağlı türevsel denklemleri çözme ve modelleme tekniklerini öğrenmek isteyen öğrenciler için tasarlanmıştır. Birinci ve ikinci mertebeden kısmi türevli denklemler, karakteristikler yöntemi, dalga denklemi, ısı (difüzyon) denklemi, Laplace ve Poisson denklemleri ile değişkenlerine ayırma (Fourier serileri) yöntemini kapsar. Doğal olayları, ısı yayılımını, dalga hareketlerini ve mühendislik sistemlerini uzay-zaman ekseninde formüle etme yeteneği kazandırır.",
        "meslekler": ["Matematiksel Modelleme Mühendisi", "Akışkanlar Dinamiği (CFD) Uzmanı", "Bilimsel Hesaplama Uzmanı"]
    },
    "MAT4429": {
        "ad": "Matematik Laboratuvarı V (Mathematics Laboratory V)", "sinif": 4, "yariyil": 1, "kategori": "Bilgisayarlı Matematik / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Teorik matematiksel modellerin bilgisayar ortamında Python, MATLAB veya Mathematica gibi modern araçlar kullanılarak simüle edilmesini ve çözülmesini öğrenmek isteyen öğrenciler için tasarlanmıştır. İleri düzey matris hesaplamaları, diferensiyel denklemlerin nümerik çözümleri, optimizasyon algoritmaları, sembolik hesaplama ve matematiksel veri görselleştirme tekniklerini kapsar. Soyut matematik kavramlarını pratik yazılım becerileriyle birleştirme yeteneği kazandırır.",
        "meslekler": ["Bilimsel Yazılım Geliştiricisi", "Nümerik Analiz Uzmanı", "Optimizasyon Uzmanı"]
    },
    "MAT4433": {
        "ad": "İleri Programlama (Advanced Programming)", "sinif": 4, "yariyil": 1, "kategori": "Bilgisayar Bilimleri / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Temel programlama bilgisini ileri düzey yazılım mühendisliği prensipleri ve performans optimizasyonuyla birleştirmek isteyen öğrenciler için tasarlanmıştır. Nesne yönelimli programlama (OOP) mimarileri, gelişmiş veri yapıları ve algoritmalar, bellek yönetimi, tasarım kalıpları (design patterns) ve büyük ölçekli matematiksel simülasyon kodlarının optimizasyonunu kapsar. Soyut matematiksel algoritmaları endüstriyel standartlara uygun yazılım ürünlerine dönüştürme yeteneği kazandırır.",
        "meslekler": ["Kıdemli Yazılım Mühendisi", "Bilimsel Yazılım Geliştiricisi", "Sistem Mimarisi Uzmanı"]
    },
    "MAT4437": {
        "ad": "Harmonik Analiz (Harmonic Analysis)", "sinif": 4, "yariyil": 1, "kategori": "Analiz / Sinyal İşleme", "tur": "SEÇMELİ",
        "icerik": "Karmaşık fonksiyonları daha basit dalga boyları veya temel harmonik bileşenler cinsinden ifade etme teorisini incelemek isteyen öğrenciler için tasarlanmıştır. Fourier serileri, Fourier dönüşümleri, Plancherel teoremi, dağılımlar teorisi, konvolüsyon operatörleri ve dalgacık (wavelet) analizinin temellerini kapsar. Sinyal ve görüntü işlemeden telekomünikasyon ve kısmi diferensiyel denklemlerin çözümüne kadar teknolojinin arkasındaki dönüşüm altyapısını oluşturur.",
        "meslekler": ["Sinyal İşleme Mühendisi", "Görüntü Analitiği Uzmanı", "Dalga Yayılımı Araştırmacısı"]
    },
    "MAT4441": {
        "ad": "Kesirli Diferensiyel Denklemler (Fractional Differential Equations)", "sinif": 4, "yariyil": 1, "kategori": "Diferansiyel Denklemler / Biyomatematik", "tur": "SEÇMELİ",
        "icerik": "Klasik türevin ötesine geçerek kesirli (non-integer) mertebeden türev ve integralleri içeren diferensiyel denklemleri incelemek isteyen öğrenciler için tasarlanmıştır. Riemann-Liouville ve Caputo türev tanımları, kesirli diferensiyel denklemler, bellek etkileri, anomal difüzyon modelleri ile çözüm yöntemlerini kapsar. Fiziksel sistemlerin geçmişe bağımlı (hereditary) davranışlarını modelleme yeteneği kazandırarak viskoelastik malzemelerden biyomedikal modellemeye kadar ileri uygulama alanı sunar.",
        "meslekler": ["Anomal Difüzyon Uzmanı", "Viskoelastik Malzeme Mühendisi", "Biyomedikal Modelleme Uzmanı"]
    },
    "MAT4443": {
        "ad": "Fark Denklemleri (Difference Equations)", "sinif": 4, "yariyil": 1, "kategori": "Ayrık Matematik / Dinamik Sistemler", "tur": "SEÇMELİ",
        "icerik": "Sürekli zamanlı değişimler yerine zamanın kesikli (discrete) adımlarla ilerlediği süreçleri inceleyen fark denklemlerini öğrenmek isteyen öğrenciler için tasarlanmıştır. Lineer ve non-lineer fark denklemleri, denge noktaları, kararlılık analizi, Z-dönüşümü, üreteç fonksiyonları ve finans/biyolojideki uygulamalarını kapsar. Zaman serisi analizinden nüfus dinamiklerine ve ekonomik dalgalanma modellerine kadar kesikli sistemlerin modellemesini yapabilme yeteneği kazandırır.",
        "meslekler": ["Zaman Serileri Analisti", "Kantitatif Risk Uzmanı", "Algoritmik Ticaret Mühendisi"]
    },
    "MAT4447": {
        "ad": "Öklid Dışı Geometriler (Non-Euclidean Geometries)", "sinif": 4, "yariyil": 1, "kategori": "Geometri", "tur": "SEÇMELİ",
        "icerik": "Öklid'in paralellik aksiyomunun değiştirilmesiyle ortaya çıkan alternatif geometrik sistemleri incelemek isteyen öğrenciler için tasarlanmıştır. Hiperbolik geometri, eliptik geometri, Poincaré disk ve yarı düzlem modelleri, eğrilik kavramları ve bu uzaylardaki trigonometrik bağıntıları kapsar. Uzay-zamanın eğrisel yapısını anlamaktan modern kozmolojiye, haritalandırma sistemlerinden bilgisayarlı grafik ve 3D modelleme algoritmalarına kadar uzaysal analizin temelini oluşturur.",
        "meslekler": ["Kozmoloji Araştırmacısı", "3D Grafik Mühendisi", "Konumsal Modelleme Uzmanı"]
    },
    "MAT4451": {
        "ad": "Ortogonal Polinomlar (Orthogonal Polynomials)", "sinif": 4, "yariyil": 1, "kategori": "Uygulamalı Matematik / Nümerik Analiz", "tur": "SEÇMELİ",
        "icerik": "Fonksiyon uzaylarında iç ürün kavramını genişleterek belirli ağırlık fonksiyonlarına göre birbirine ortogonal olan polinom ailelerini incelemek isteyen öğrenciler için tasarlanmıştır. Legendre, Chebyshev, Hermite, Laguerre polinomları, Sturm-Liouville teorisi ile bu polinomların nümerik entegrasyon uygulamalarını kapsar. Karmaşık matematiksel fonksiyonların bilgisayar ortamında yüksek doğrulukla ifade edilmesinden fiziksel alan denklemlerinin spektral çözümlerine kadar uygulama alanı sunar.",
        "meslekler": ["Nümerik Analiz Uzmanı", "Algoritma Geliştiricisi", "Sinyal İşleme Mühendisi"]
    },
    "MAT4461": {
        "ad": "Gruplar Teorisi (Theory of Groups)", "sinif": 4, "yariyil": 1, "kategori": "Cebir", "tur": "SEÇMELİ",
        "icerik": "Simetri kavramını ve cebirsel yapıların temel taşı olan grup yapısını detaylıca incelemek isteyen öğrenciler için tasarlanmıştır. Gruplar, altgruplar, devirli gruplar, Lagrange teoremi, normal altgruplar, bölüm grupları, homomorfizmler, permütasyon grupları ve Sylow teoremlerini kapsar. Simetri analizi gerektiren moleküler yapılardan modern şifreleme algoritmalarına ve kuantum mekaniğindeki dönüşüm gruplarına kadar bilgi güvenliğinin soyut omurgasını oluşturur.",
        "meslekler": ["Kriptografi Uzmanı", "Post-Kuantum Güvenlik Araştırmacısı", "Cebirsel Kodlama Uzmanı"]
    },
    "MAT4463": {
        "ad": "Tensör Cebiri (Tensor Algebra)", "sinif": 4, "yariyil": 1, "kategori": "Doğrusal Cebir / Fiziksel Modelleme", "tur": "SEÇMELİ",
        "icerik": "Vektör uzaylarının ve doğrusal dönüşümlerin ötesine geçerek çok-doğrusal (multilinear) yapıları incelemek isteyen öğrenciler için tasarlanmıştır. Vektör uzaylarının direkt çarpımı, tensör çarpımı, kovaryant ve kontravaryant tensörler, dönüşüm kanunları ve dış çarpım konularını kapsar. Fiziksel gerilme analizlerinden genel göreliliğin matematiksel altyapısına ve makine öğrenmesindeki çok boyutlu veri dizilerinin işlenmesine kadar cebirin güçlü araçlarını oluşturur.",
        "meslekler": ["Sürekli Ortam Analisti", "Bilgisayarlı Görü Uzmanı", "Uzay-Zaman Araştırmacısı"]
    },
    "MAT4487": {
        "ad": "Matematiksel Modelleme (Mathematical Modelling)", "sinif": 4, "yariyil": 1, "kategori": "Genel Matematik / Modelleme", "tur": "SEÇMELİ",
        "icerik": "Fiziksel, biyolojik, ekonomik veya sosyal sistemlerdeki gerçek dünya problemlerini matematiksel dillere dönüştürme süreçlerini incelemek isteyen öğrenciler için tasarlanmıştır. Model kurma aşamaları, boyut analizi, analitik ve sayısal çözüm yaklaşımları, model doğrulama ve duyarlılık analizi konularını kapsar. Karmaşık sistemlerin davranışlarını öngörme ve optimize etme yeteneği kazandırarak endüstriyel Ar-Ge'den finans, ekoloji ve teknoloji sektörlerine kadar uygulama alanı sunar.",
        "meslekler": ["Simülasyon Mühendisi", "Süreç Optimizasyon Uzmanı", "Kantitatif Analist"]
    },
    "MAT4489": {
        "ad": "Operatör Teoriye Giriş (Introduction to Operator Theory)", "sinif": 4, "yariyil": 1, "kategori": "Fonksiyonel Analiz", "tur": "SEÇMELİ",
        "icerik": "Sonsuz boyutlu vektör uzayları üzerindeki doğrusal dönüşümleri (operatörleri) incelemek isteyen öğrenciler için tasarlanmıştır. Banach ve Hilbert uzayları üzerinde sınırlı ve sınırsız operatörler, spektral teori, kompakt operatörler ve öz-eşlenik operatörleri kapsar. Kuantum mekaniğinin matematiksel formülasyonundan diferensiyel denklemlerin spektral çözümlerine kadar modern analizin soyut araçlarını sunar.",
        "meslekler": ["Kuantum Bilişim Uzmanı", "Spektral Analiz Uzmanı", "Nümerik Algoritma Mühendisi"]
    },
    "MAT4497": {
        "ad": "Kategori (Category)", "sinif": 4, "yariyil": 1, "kategori": "Soyut Matematik / Mantık", "tur": "SEÇMELİ",
        "icerik": "Cebir, topoloji, mantık ve bilgisayar bilimleri gibi disiplinler arasındaki ortak yapıları, soyutlamaları ve evrensel özellikleri incelemek isteyen öğrenciler için tasarlanmıştır. Nesneler, morfizmler, funktorlar, doğal dönüşümler ve limitler kavramlarını kapsar. Kategorik veri modellerine ve programlama dillerindeki tip teorisine uzanan birleştirici altyapıyı sunar.",
        "meslekler": ["Tip Teorisi Mimarı", "Kategorik Veri Modeli Uzmanı", "Soyut Matematik Araştırmacısı"]
    },
    "MAT4499": {
        "ad": "Ayrık Matematikte Özel Konular", "sinif": 4, "yariyil": 1, "kategori": "Ayrık Matematik / Kombinatorik", "tur": "SEÇMELİ",
        "icerik": "Standart ayrık matematik müfredatının ötesine geçerek ileri düzey özel problemleri ve teorik yapıları incelemek isteyen öğrenciler için tasarlanmıştır. Ramsey teorisi, matroit teorisi, sonlu cisimler üzerindeki kombinatorik yapılar, ağ akışları ve algoritma karmaşıklığı konularını kapsar. Veri optimizasyonundan ağ topolojisi analizine ve kodlama teorisine kadar güncel bir uygulama alanı sunar.",
        "meslekler": ["Algoritma Mühendisi", "Ağ Topolojisi Analisti", "Kriptografi Uzmanı"]
    },
    "AST321": {
        "ad": "Astronomi Tarihi (History of Astronomy)", "sinif": 4, "yariyil": 1, "kategori": "Disiplinlerarası / Astronomi", "tur": "SEÇMELİ",
        "icerik": "Gökyüzü gözlemlerinin ilk çağlardan günümüze kadar geçirdiği evrimi, kozmolojik modellerin değişimini ve evren anlayışının gelişimini incelemek isteyen öğrenciler için tasarlanmıştır. Antik çağlardan modern astrofiziğe geçiş süreçlerini kapsar. Bilimsel düşüncenin tarihsel kökenlerini anlama ve teorilerin nasıl şekillendiğini kavram yeteneği kazandırır.",
        "meslekler": ["Bilim Tarihçisi", "Bilim İletişimcisi", "Arkeoastronomi Araştırmacısı"]
    },
    "AST213": {
        "ad": "Astronomi I (Astronomy I)", "sinif": 4, "yariyil": 1, "kategori": "Disiplinlerarası / Astronomi", "tur": "SEÇMELİ",
        "icerik": "Gökyüzünün geometrisini, gök cisimlerinin konumlarını ve hareketlerini matematiksel ve fiziksel temellerle incelemek isteyen öğrenciler için tasarlanmıştır. Gök küresi, koordinat sistemleri, Kepler yasaları ve gök mekaniğinin temellerini kapsar. Astrofizik, uydu yörünge mekaniği ve gözlemsel astronomi çalışmalarının temelini oluşturur.",
        "meslekler": ["Uydu Yörünge Uzmanı", "Astrofizik Araştırmacısı", "Astronomi Veri Bilimcisi"]
    },
    "BIY415": {
        "ad": "İklim Bilgisi (Climatology)", "sinif": 4, "yariyil": 1, "kategori": "Disiplinlerarası / Çevre", "tur": "SEÇMELİ",
        "icerik": "Atmosferin genel yapısını, iklim elemanlarını ve küresel ölçekteki değişim mekanizmalarını incelemek isteyen öğrenciler için tasarlanmıştır. Sıcaklık, basınç ve rüzgar sistemleri, iklim sınıflandırmaları ve güncel iklim değişikliği dinamiklerini kapsar. İstatistiksel iklim analizi ve çevresel risk değerlendirmesi konularında güçlü bir analitik altyapı sunar.",
        "meslekler": ["İklim Değişikliği Uzmanı", "Meteorolojik Veri Analisti", "Çevresel Risk Uzmanı"]
    },
    "BIY417": {
        "ad": "Çevre Kirliliği (Environmental Pollution)", "sinif": 4, "yariyil": 1, "kategori": "Disiplinlerarası / Çevre", "tur": "SEÇMELİ",
        "icerik": "Hava, su ve toprak kirliliğinin kaynaklarını, atmosferik ve hidrolojik taşınım mekanizmalarını incelemek isteyen öğrenciler için tasarlanmıştır. Kirletici bozunum kinetiği, adveksiyon-difüzyon denklemleri ve çevresel risk analizi stratejilerini kapsar. Karmaşık kirlilik süreçlerini matematiksel olarak modelleme yeteneği kazandırarak ekolojik planlama için altyapı sunar.",
        "meslekler": ["Çevre Modelleme Uzmanı", "ÇED ve Risk Analisti", "Atık Yönetimi Mühendisi"]
    },
    "MAT4402": {
        "ad": "Fark Denklem Sistemleri (Systems of Difference Equations)", "sinif": 4, "yariyil": 2, "kategori": "Uygulamalı Matematik / Dinamik Sistemler", "tur": "SEÇMELİ",
        "icerik": "Bu ders; tek bir fark denklemi yerine birden fazla değişkenin karşılıklı etkileşim içinde kesikli zaman adımlarıyla değiştiği sistemleri incelemek isteyen öğrenciler için tasarlanmıştır. Lineer fark denklem sistemleri, matris formülasyonları, özdeğer ve özvektör analizleri, denge durumları (equilibrium points), kararlılık kriterleri, non-lineer sistemlerin doğrusallaştırılması ve çoklu değişkenli zaman serisi modellerini kapsar. Çok türli ekolojik rekabet modellerinden makroekonomik girdi-çıktı analizlerine ve çok değişkenli finansal öngörü süreçlerine kadar karmaşık kesikli sistemlerin analitik altyapısını sunar.",
        "meslekler": ["Kantitatif Finans Analisti", "Dinamik Sistemler Uzmanı", "Makroekonomik Projeksiyon Uzmanı"]
    },
    "MAT4404": {
        "ad": "Cisim Genişlemeleri (Field Extensions)", "sinif": 4, "yariyil": 2, "kategori": "Cebir", "tur": "SEÇMELİ",
        "icerik": "Bu ders; halkalar ve cisimler teorisinde bir adım öteye geçerek cebirsel uzayların genişleme yapılarını incelemek isteyen öğrenciler için tasarlanmıştır. Basit genişlemeler, cebirsel ve aşkın elemanlar, derecesi sonlu genişlemeler, parçalanma cisimleri (splitting fields), cebirsel kapanış ve Galois teorisinin temellerini oluşturan otomorfizma gruplarını kapsar. Polinomların köklerinin yapısını anlamaktan sonlu cisimler üzerindeki modern şifreleme algoritmalarına ve hata düzelten kodların tasarımına kadar soyut cebirin en zarif ve güçlü altyapısını sunar.",
        "meslekler": ["Kriptografi Uzmanı", "Cebirsel Kodlama Uzmanı", "Sayılar Teorisi Araştırmacısı"]
    },
    "MAT4406": {
        "ad": "Uygulamalı Matematik (Applied Mathematics)", "sinif": 4, "yariyil": 2, "kategori": "Uygulamalı Matematik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; soyut matematiksel teorileri ve analitik yöntemleri fiziksel, mühendislik, finansal ve endüstriyel gerçek dünya problemlerine uyarlamak isteyen öğrenciler için tasarlanmıştır. Perturbasyon (tedirgisme) teorisi, asimptotik analiz, varyasyonlar hesabı, integral denklemler ve matematiksel fizik problemlerinin çözüm yöntemlerini kapsar. Teorik matematik altyapısını somut modelleme becerileriyle birleştirerek endüstriyel Ar-Ge'den bilimsel simülasyona ve teknolojik optimizasyona kadar geniş bir analitik uygulama alanı sunar.",
        "meslekler": ["Ar-Ge Mühendisi", "Simülasyon Uzmanı", "Operasyonel Araştırma Uzmanı"]
    },
    "MAT4408": {
        "ad": "Fourier Analizi (Fourier Analysis)", "sinif": 4, "yariyil": 2, "kategori": "Analiz / Sinyal İşleme", "tur": "SEÇMELİ",
        "icerik": "Bu ders; karmaşık periyodik fonksiyonların ve sinyallerin daha basit harmonik bileşenlere (sinüs ve kosinüslere) nasıl ayrılabileceğini incelemek isteyen öğrenciler için tasarlanmıştır. Fourier serileri, trigonometrik yaklaşım, yakınsama teoremleri (Dirichlet ve Fejér), Fourier dönüşümü (Fourier Transform), ters dönüşüm, konvolüsyon teoremi, Parseval özdeşliği ve ısı/dalga denklemlerinin sınır değer problemlerine uygulanmasını kapsar. Fiziksel sistemlerin frekans domeninde analiz edilmesinden ses/görüntü sıkıştırma algoritmalarına ve mühendislik simülasyonlarına kadar modern analizin en temel ve yaygın araçlarından birini sunar.",
        "meslekler": ["Sinyal İşleme Mühendisi", "Akustik Analisti", "Zaman Serileri Analisti"]
    },
    "MAT4412": {
        "ad": "Geometriler ve Topoloji (Geometries and Topology)", "sinif": 4, "yariyil": 2, "kategori": "Geometri / Topoloji", "tur": "SEÇMELİ",
        "icerik": "Bu ders; klasik Öklid geometrisinin ötesine geçerek uzayın genel yapılarını, eğrilik kavramlarını ve sürekli deformasyonlar altında değişmeyen özelliklerini (topolojik değişmezleri) incelemek isteyen öğrenciler için tasarlanmıştır. Öklid dışı geometriler (Hiperbolik ve Eliptik geometriler), metrik uzaylar, topolojik uzaylar, kompaktlık, bağlantılılık, temel grup (fundamental group) ve yüzeylerin sınıflandırılması konularını kapsar. Evrenin genel görelilikteki geometrik yapısından modern veri analitiğindeki topolojik formülasyonlara kadar soyut uzayların matematiksel altyapısını kurar.",
        "meslekler": ["Topolojik Veri Uzmanı", "3D Geometri Mühendisi", "Geometrik Kozmoloji Araştırmacısı"]
    },
    "MAT4414": {
        "ad": "Dinamik Sistemler (Dynamical Systems)", "sinif": 4, "yariyil": 2, "kategori": "Uygulamalı Matematik / Diferansiyel Denklemler", "tur": "SEÇMELİ",
        "icerik": "Bu ders; zamanla değişen fiziksel, biyolojik veya ekonomik sistemlerin uzun vadeli evrimini incelemek isteyen öğrenciler için tasarlanmıştır. Faz uzayı (phase space), akışlar (flows), denge noktalarının kararlılık analizi (Lyapunov kararlılığı, doğrusallaştırma), çatallanma (bifurcation) teorisi, limit çevrimleri (limit cycles) ve kaos teorisinin temellerini (garip çekiciler ve Lorenz sistemi) kapsar. Doğrusal olmayan karmaşık sistemlerin doğasını anlamaktan hava durumu tahminlerine, robotik kontrol sistemlerinden ekolojik popülasyon dalgalanmalarına kadar modern bilimin en büyüleyici analitik araçlarını sunar.",
        "meslekler": ["Simülasyon Mühendisi", "Piyasa Dinamikleri Analisti", "Kompleks Sistemler Araştırmacısı"]
    },
    "MAT4430": {
        "ad": "Matematik Laboratuvarı VI (Mathematics Laboratory VI)", "sinif": 4, "yariyil": 2, "kategori": "Bilgisayarlı Matematik / Yazılım", "tur": "SEÇMELİ",
        "icerik": "Bu ders; teorik matematik bilgilerini bilgisayar ortamında ileri düzey sayısal yöntemler, simülasyonlar ve modern programlama araçlarıyla hayata geçirmek isteyen öğrenciler için tasarlanmıştır. Diferensiyel denklemlerin ve denklem sistemlerinin sayısal çözümleri, büyük boyutlu matris hesaplama algoritmaları, optimizasyon rutinleri, gelişmiş grafik görselleştirme teknikleri ve bilimsel hesaplama kütüphanelerinin ileri düzey projelerde uygulanmasını kapsar. Soyut matematiksel modelleri somut yazılımlara dönüştürme, algoritma optimizasyonu yapma ve veri odaklı simülasyonlar kurma yeteneği kazandırarak bilimsel hesaplama, yazılım mühendisliği ve endüstriyel Ar-Ge alanlarında güçlü bir pratik altyapı sunar.",
        "meslekler": ["Bilimsel Hesaplama Mühendisi", "Veri Bilimi Yazılım Uzmanı", "Nümerik Algoritma Geliştirici"]
    },
    "MAT4432": {
        "ad": "Uygulamalı Kısmi Türevli Denklemler (Applied Partial Differential Equations)", "sinif": 4, "yariyil": 2, "kategori": "Diferansiyel Denklemler", "tur": "SEÇMELİ",
        "icerik": "Bu ders; fizik, mühendislik, finans ve diğer fen bilimlerindeki çok değişkenli süreçleri modellemek için kullanılan kısmi türevli denklemlerin (KTD) analitik çözüm yöntemlerini incelemek isteyen öğrenciler için tasarlanmıştır. Birinci ve ikinci mertebeden KTD'ler, karakteristikler yöntemi, dalga denklemi, ısı (difüzyon) denklemi, Laplace denklemi, değişkenlerine ayırma metodu, Fourier serileri ve Green fonksiyonları konularını kapsar. Isı iletimi, dalga yayılımı, akışkanlar mekaniği ve potansiyel teorisi gibi fiziksel olayların matematiksel modellemesinden finansal opsiyon fiyatlandırma denklemlerine kadar geniş bir uygulama alanı sunar.",
        "meslekler": ["Simülasyon Mühendisi", "Kantitatif Finans Analisti", "CFD Uzmanı"]
    },
    "MAT4436": {
        "ad": "Modüller Teorisi (Theory of Modules)", "sinif": 4, "yariyil": 2, "kategori": "Cebir", "tur": "SEÇMELİ",
        "icerik": "Bu ders; doğrusal cebirdeki vektör uzayı kavramını bir cisim yerine genel bir halka üzerine genelleştiren, soyut cebirin en temel ve birleştirici yapı taşlarından biri olan modülleri incelemek isteyen öğrenciler için tasarlanmıştır. Modül kavramı, altmodüller, bölüm modülleri, modül homomorfizmleri, serbest modüller, projeksiyon ve enjektif modüller, temel ideal bölgeleri (PID) üzerindeki sonlu üretilmiş modüllerin yapısı ve tensör çarpımları konularını kapsar. Halkalar teorisi ile doğrusal cebir arasındaki köprüyü kurarak homolojik cebir, cebirsel topoloji ve ileri düzey sayısal yapılar için derinlemesine bir analitik altyapı sunar.",
        "meslekler": ["Soyut Cebir Araştırmacısı", "Kriptografi Uzmanı", "Akademik Ar-Ge Uzmanı"]
    },
    "MAT4440": {
        "ad": "Yarı Riemann Geometrisi (Semi-Riemannian Geometry)", "sinif": 4, "yariyil": 2, "kategori": "Geometri / Fizik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; standart Riemann geometrisinin pozitif definit metrik koşulunu esneterek metrik tensörün işaret değiştirilmesine (indeksine) izin veren yapıları incelemek isteyen öğrenciler için tasarlanmıştır. Yarı Riemann manifoldları (özellikle Lorentzian manifoldları), Levi-Civita bağlantısı, eğrilik tensörleri (Riemann, Ricci, skaler eğrilik), jeodezik eğriler ve Einstein alan denklemlerinin geometrik altyapısını kapsar. Evrenin uzay-zaman dokusunu, karadeliklerin etrafındaki kütleçekim alanlarını ve modern fiziksel geometri problemlerini modellemek için güçlü bir matematiksel altyapı sunar.",
        "meslekler": ["Uzay-Zaman Araştırmacısı", "Gravitasyonel Fizik Uzmanı", "İleri Geometri Uzmanı"]
    },
    "MAT4442": {
        "ad": "Lie Grupları (Lie Groups)", "sinif": 4, "yariyil": 2, "kategori": "Geometri / Cebir", "tur": "SEÇMELİ",
        "icerik": "Bu ders; sürekli simetrileri matematiksel olarak incelemek isteyen öğrenciler için tasarlanmıştır. Düzgün manifoldlar ile grup yapısının birleştiği Lie gruplarını, Lie cebirlerini, birim elemandaki teğet uzayları, üstel dönüşümü, matris Lie gruplarını ve temel temsil teorisini kapsar. Fiziksel sistemlerdeki korunum yasalarından modern kuantum mekaniğine, robotik kinematikten diferansiyel denklemlerin simetri analizlerine kadar geniş ve derinlikli bir analitik altyapı sunar.",
        "meslekler": ["Kuantum Bilişim Uzmanı", "Robotik Kinematik Mühendisi", "Geometri Araştırmacısı"]
    },
    "MAT4448": {
        "ad": "Kesirli Fark Denklemleri (Discrete Fractional Equations)", "sinif": 4, "yariyil": 2, "kategori": "Ayrık Matematik", "tur": "SEÇMELİ",
        "icerik": "Bu ders; geçmişteki durumların güncel durumu hafıza etkisiyle etkilediği kesikli (discrete) süreçleri incelemek isteyen öğrenciler için tasarlanmıştır. Nabla ve Delta kesirli fark operatörleri, kesirli toplam ve fark formülasyonları, kesirli mertebeli fark denklemlerinin analitik ve sayısal çözüm yöntemleri, Mittag-Leffler tipi kesikli fonksiyonlar ile bu sistemlerin kararlılık analizini kapsar. Ekonomik dalgalanmalardan biyolojik popülasyon dinamiklerine ve hafıza bağımlı fiziksel süreçlerin modellenmesine kadar modern uygulamalı matematiğin en güncel analitik araçlarını sunar.",
        "meslekler": ["Matematiksel Modelleme Uzmanı", "Kantitatif Risk Analisti", "Dinamik Sistemler Araştırmacısı"]
    },
    "MAT4452": {
        "ad": "Topolojik Vektör Uzaylarına Giriş (Introduction to Topological Vector Spaces)", "sinif": 4, "yariyil": 2, "kategori": "Topoloji / Analiz", "tur": "SEÇMELİ",
        "icerik": "Bu ders; doğrusal cebirdeki vektör uzayı kavramı ile genel topolojinin yapılarını birleştirerek, toplama ve skalerle çarpma işlemlerinin sürekli olduğu uzayları (Topolojik Vektör Uzayları - TVS) incelemek isteyen öğrenciler için tasarlanmıştır. Lokal konveks uzaylar, yarı norm aileleri (seminorms), Hahn-Banach teoreminin analitik ve geometrik versiyonları, lineer dönüşümlerin sürekliliği, Fréchet uzayları ve Banach uzaylarının temellerini kapsar. Sonsuz boyutlu uzaylardaki analiz problemlerini çözmekten kuantum mekaniğinin matematiksel temellerine ve kısmi diferensiyel denklemlerin dağılım (distribution) teorisine kadar modern analizin en güçlü altyapısını sunar.",
        "meslekler": ["Fonksiyonel Analiz Araştırmacısı", "Kuantum Sistemleri Uzmanı", "İleri Analiz Uzmanı"]
    },
    "MAT4472": {
        "ad": "Uygulamalı Kompleks Analiz (Applied Complex Analysis)", "sinif": 4, "yariyil": 2, "kategori": "Analiz", "tur": "SEÇMELİ",
        "icerik": "Bu ders; karmaşık sayılar düzlemindeki analitik fonksiyon teorisini gerçek dünya problemlerine ve mühendislik uygulamalarına uyarlamak isteyen öğrenciler için tasarlanmıştır. Kompleks türev ve integral, Cauchy-Riemann denklemleri, harmonik fonksiyonlar, Cauchy integral teoremi, rezidü teoremi (residue theorem) ve kontür integralleri, konformal tasvirler (conformal mappings) ile Laplace denkleminin sınır değer problemlerine uygulanmasını kapsar. Akışkanlar mekaniği, ısı iletimi, elektrostatik potansiyel alanları ve sinyal işleme süreçlerindeki karmaşık analitik çözümleri modellemek için güçlü bir matematiksel altyapı sunar.",
        "meslekler": ["Akışkanlar Modelleme Mühendisi", "Anten Tasarım Uzmanı", "Kantitatif Finans Analisti"]
    },
    "MAT4490": {
        "ad": "Halkalar Teorisi (Theory of Rings)", "sinif": 4, "yariyil": 2, "kategori": "Cebir", "tur": "SEÇMELİ",
        "icerik": "Bu ders; gruplar teorisinden sonra cebirsel yapıların en temel ve zengin halkalarından biri olan, iki ikili işleme (toplama ve çarpma) sahip cebirsel sistemleri incelemek isteyen öğrenciler için tasarlanmıştır. Halka kavramı, altrakalar, idealler, bölüm halkaları, halka homomorfizmleri, asal ve maksimal idealler, polinom halkaları, tamlık bölgeleri (integral domains), esas ideal bölgeleri (PID), tek türlü çarpanlara ayrılma bölgeleri (UFD) ve Noetherci halkalar konularını kapsar. Modern cebirsel yapıların anlaşılmasından cebirsel geometriye ve modern kriptografik algoritmaların arka planındaki cebirsel temellere kadar derinlemesine bir analitik altyapı sunar.",
        "meslekler": ["Kriptografi Uzmanı", "Cebirsel Kodlama Uzmanı", "Cebir Araştırmacısı"]
    },
    "BLM446": {
        "ad": "Bulanık Mantık (Fuzzy Logic)", "sinif": 4, "yariyil": 2, "kategori": "Bilgisayar Bilimleri / Mantık", "tur": "SEÇMELİ",
        "icerik": "Bu ders; kesin doğru veya yanlış (0 veya 1) temeline dayanan klasik mantık anlayışının ötesine geçerek, insan mantığındaki dereceli ve belirsiz (muğlak) bilgileri matematiksel olarak modellemek isteyen öğrenciler için tasarlanmıştır. Kesin kümeler ve bulanık kümeler arasındaki farklar, üyelik fonksiyonları (membership functions), bulanık küme işlemleri (kesişim, birleşim, tümleyen), dilsel değişkenler (linguistic variables), bulanık kural tabanlı sistemler, Mamdani ve Sugeno çıkarım mekanizmaları ile bulanık kontrol ve karar verme süreçlerini kapsar. Gerçek dünya problemlerindeki belirsizliklerin ve sübjektif verilerin yapay zeka, kontrol sistemleri ve karar destek mekanizmalarında işlenmesi için güçlü bir analitik altyapı sunar.",
        "meslekler": ["Yapay Zeka Mühendisi", "Otomasyon Uzmanı", "Karar Destek Uzmanı"]
    }
}

st.title("🎓 Matematik Bölümü Kariyer ve Ders Rehberi")
st.write("Derslerin teorik içeriklerini ve seni hazırladığı kariyer yollarını bu ekrandan interaktif olarak inceleyebilirsin.")

tab1, tab2 = st.tabs(["📚 Müfredat Listesi", "🔍 Detaylı Ders Sorgula"])

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