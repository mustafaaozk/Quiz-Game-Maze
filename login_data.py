import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

# Veritabanı bağlantısı ve tablo oluşturma
def veritabani_baglanti():
    conn = sqlite3.connect('Asset/Database/oyuncu_skor.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS oyun_sonuclari 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                kullanici_adi TEXT, 
                dogru_sayisi INTEGER, 
                yanlis_sayisi INTEGER,
                bos_sayisi INTEGER)''')
    conn.commit()
    conn.close()

# Kullanıcı ismini al ve oyunu başlat
def oyunu_baslat():
    kullanici_adi = entry_adi.get().strip()
    
    if kullanici_adi == "":
        messagebox.showwarning("Uyarı", "Lütfen isminizi girin!")
    else:
        with open("kullanici.txt", "w") as f:
            f.write(kullanici_adi)
        window.quit()
        subprocess.Popen(["python", "main.py"])

# Veritabanını gösteren bir pencere aç
def veritabani_goster():
    conn = sqlite3.connect('Asset/Database/oyuncu_skor.db')
    c = conn.cursor()

    # Veritabanındaki tüm kayıtları al
    c.execute("SELECT * FROM oyun_sonuclari")
    sonuclar = c.fetchall()
    conn.close()

    # Sonuçları yeni bir pencerede göster
    result_window = tk.Toplevel(window)
    result_window.title("Veritabanı Sonuçları")
    
    text_area = tk.Text(result_window, width=60, height=10)
    text_area.pack()

    # Kaydırma çubuğu ekleyin
    scrollbar = tk.Scrollbar(result_window, command=text_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area['yscrollcommand'] = scrollbar.set
    
    if not sonuclar:  
        sonuc_yok = tk.Label(result_window, text="Kayıt Bulunamadı", font=("Verdana", 16, "roman"), width=20, height=2)
        sonuc_yok.pack(pady=5)
    else:
        for sonuc in sonuclar:
            text_area.insert(tk.END, f"Kullanıcı: {sonuc[1]}, Doğru: {sonuc[2]}, Yanlış: {sonuc[3]}, Bos: {sonuc[4]}\n")

window = tk.Tk()
window.title("Labirent Quiz Oyunu - Giriş")

label_adi = tk.Label(window, text="Öğrenci Adı", font=("Verdana", 16, "roman"), width=20, height=2)
label_adi.pack(pady=10)

entry_adi = tk.Entry(window, font=("Arial", 14), width=25)
entry_adi.pack(pady=10)

btn_basla = tk.Button(window, text="Oyuna Başla", width=15, height=4, command=oyunu_baslat)
btn_basla.pack(pady=10)

btn_veritabani = tk.Button(window, text="Veritabanını Göster", width=15, height=2, command=veritabani_goster)
btn_veritabani.pack(pady=10)

window.geometry("500x300")

veritabani_baglanti()

window.mainloop()
