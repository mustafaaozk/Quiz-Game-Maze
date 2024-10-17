import sqlite3

def save_database(true,false):
    conn = sqlite3.connect('Asset/Database/oyuncu_skor.db')
    c = conn.cursor()
    with open("kullanici.txt", "r") as file:
        kullanıcı_adı = file.read().strip()

    c.execute('''INSERT INTO oyun_sonuclari (kullanici_adi, dogru_sayisi, yanlis_sayisi) 
                 VALUES (?, ?, ?)''', (kullanıcı_adı, true, false)) 
    conn.commit()
    conn.close()
