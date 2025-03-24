import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

seed = 0
random.seed(seed)
np.random.seed(seed)

G = nx.Graph()

def graph_function(G):
    # İstasyon kodları, isimleri ve hatları
    istasyonlar = {
        "K1": ("Kızılay", "Kırmızı Hat"),
        "K2": ("Ulus", "Kırmızı Hat"),
        "K3": ("Demetevler", "Kırmızı Hat"),
        "K4": ("OSB", "Kırmızı Hat"),
        "M1": ("AŞTİ", "Mavi Hat"),
        "M2": ("Kızılay", "Mavi Hat"),
        "M3": ("Sıhhiye", "Mavi Hat"),
        "M4": ("Gar", "Mavi Hat"),
        "T1": ("Batıkent", "Turuncu Hat"),
        "T2": ("Demetevler", "Turuncu Hat"),
        "T3": ("Gar", "Turuncu Hat"),
        "T4": ("Keçiören", "Turuncu Hat")
    }

    # Düğümleri ekle
    G.add_nodes_from(istasyonlar.keys())

    # Hat bağlantıları
    G.add_edge("K1", "K2", weight=4)
    G.add_edge("K2", "K3", weight=6)
    G.add_edge("K3", "K4", weight=8)
    G.add_edge("M1", "M2", weight=5)
    G.add_edge("M2", "M3", weight=3)
    G.add_edge("M3", "M4", weight=4)
    G.add_edge("T1", "T2", weight=7)
    G.add_edge("T2", "T3", weight=9)
    G.add_edge("T3", "T4", weight=5)

    # Aktarmalar
    G.add_edge("K1", "M2", weight=2)
    G.add_edge("K3", "T2", weight=3)
    G.add_edge("M4", "T3", weight=2)

    # Düğüm pozisyonlarını ayarla
    pos = nx.spring_layout(G, seed=42)

    # Kenar etiketleri (dakika)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    node_labels = {node: node for node in G.nodes()}

    isim_labels = {
        node: f"{isim} ({hat})" for node, (isim, hat) in istasyonlar.items()
    }


    offset_y = 0.15
    label_pos = {node: (x, y + offset_y) for (node, (x, y)) in pos.items()}

    # Çizim Başlıyor
    plt.figure(figsize=(11, 7))

    # Düğümleri çiz (içinde sadece kod yazacak)
    nx.draw(
        G, pos, with_labels=True, labels=node_labels,
        node_color="red", node_size=3000,
        font_size=10, font_color="white", font_weight="bold"
    )

    # ⏱ Kenarlardaki süreleri yaz
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # 🟢 Düğüm dışı (üstteki) yazıları çiz
    nx.draw_networkx_labels(G, label_pos, labels=isim_labels,
                            font_size=9, font_color="black", font_family="serif")

    # Başlık ve görsel ayarlar
    plt.title("Metro Ağı Grafiği (Kodlar Düğümde, Durak + Hat İsmi Üstte)", fontsize=13)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
