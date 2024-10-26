import sqlite3

def save_database(true, false, non):
    conn = sqlite3.connect('Asset/Database/oyuncu_skor.db')
    c = conn.cursor()
    with open("Asset/Database/kullanici.txt", "r") as file:
        kullanıcı_adı = file.read().strip()

    # Sorguda üç tane değer bekleniyor, non değerini ekle
    c.execute('''INSERT INTO oyun_sonuclari (kullanici_adi, dogru_sayisi, yanlis_sayisi, bos_sayisi) 
                 VALUES (?, ?, ?,?)''', (kullanıcı_adı, true, false, non))  
    conn.commit()
    conn.close()