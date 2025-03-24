Sürücüsüz Metro Simülasyonu - Rota Optimizasyonu

Bu proje, bir şehir metrosunun istasyonları arasında en hızlı ve en az aktarmalı rotayı hesaplayan bir Python uygulamasıdır. Projede, grafik (graph) veri yapısı kullanılarak metro istasyonları modellenmiş, ardından iki farklı algoritma ile yolculuk senaryoları test edilmiştir:

1. BFS (Breadth-First Search): En az durak değiştirerek hedefe ulaşmak için
2. A* (A-Star): Zaman (süre) açısından en hızlı rotayı bulmak için

---

 Projenin Yapısı

- `graft.py`: Metro ağı grafik olarak çizilir. İstasyonlar, hatlar ve bağlantılar görsel olarak modellenir.
- `EdanurDogan_MetroSimulation.py`: Ana algoritmalar ve sınıflar burada yer alır. Kodun çalıştığı ana dosyadır.


Kullanılan Teknolojiler ve Kütüphaneler

`networkx`: Metro ağı grafini modellemek için kullanıldı. 
`matplotlib`:Metro ağı grafini görselleştirmek için kullanıldı. 
`collections`:BFS algoritmasında `deque` veri yapısını kullanmak için. 
`heapq`:A* algoritması için öncelik kuyruğu oluşturmakta kullanıldı. 
`typing`:Kodun tip güvenliğini ve okunabilirliğini artırmak için. 
`random`, `numpy`:Görselin kararlı kalmasını sağlamak için sabit seed kullanımı. 


Sınıfların Tanımları ve Görevleri

`Istasyon` sınıfı
- Her istasyonun ID'si, adı ve hangi hatta olduğu bilgisi tutulur.
- `komsular` listesi ile diğer istasyonlara olan bağlantılar (süre bilgisiyle) tutulur.

`MetroAgi` sınıfı
- Tüm istasyonlar ve hatlar burada kayıt altına alınır.
- `istasyon_ekle`, `baglanti_ekle` gibi fonksiyonlarla metro ağı oluşturulur.
- İki önemli algoritmayı içinde barındırır: `en_az_aktarma_bul` ve `en_hizli_rota_bul`


Algoritmaların Mantığı
BFS (en_az_aktarma_bul):
Amaç: İki istasyon arasında "en az aktarma" yaparak hedefe ulaşmak.

Nasıl çalışır:
- `deque` (çift yönlü kuyruk) kullanılarak katman katman arama yapılır.
- Her seferinde en kısa adım sayısıyla gidilebilecek tüm istasyonlar sıraya alınır.
- Aynı istasyon tekrar ziyaret edilmez.
- Hedef istasyona ulaşıldığında mevcut yol döndürülür.

Adımlar:
1. Başlangıç istasyonu kuyruğa eklenir.
2. Kuyruktan bir istasyon alınır, hedef mi kontrol edilir.
3. Komşuları keşfedilir, ziyaret edilmemişler kuyruk sonuna eklenir.
4. Yol bulunursa durur, bulunamazsa boş döner.

2. A* (en_hizli_rota_bul):

Amaç: İki istasyon arasındaki en kısa sürede (dakika bazlı) ulaşımı bulmak.

Nasıl çalışır:
- Her bağlantıdaki süre bir "maliyet" olarak kabul edilir.
- `heapq` modülü ile öncelik kuyruğu kullanılarak her zaman toplam süresi en kısa olan yol seçilir.
- Hedef istasyona ulaşıldığında rota ve toplam süre döndürülür.

Adımlar:
1. Başlangıç istasyonu öncelik kuyruğuna eklenir.
2. Kuyruktan en düşük maliyetli yol alınır.
3. Eğer hedefse, sonuç döndürülür.
4. Değilse komşularla genişletilir, yeni toplam süreye göre kuyruk güncellenir.
5. Daha önce daha kısa sürede ziyaret edilmiş bir düğüm varsa tekrar işlenmez.

`graft.py` dosyasında:

- Tüm istasyonlar node (düğüm) olarak çizilir.
- Aralarındaki bağlantılar edge (kenar) olarak çizilir.
- Her düğüm üzerinde istasyon kodu, üst kısmında ise istasyon adı ve hat adı gösterilir.
- Kenarlarda dakika cinsinden geçiş süresi yer alır.

Örnek görsel:
python
plt.title("Metro Ağı Grafiği (Kodlar Düğümde, Durak + Hat İsmi Üstte)")
