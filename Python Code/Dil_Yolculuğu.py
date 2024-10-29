import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from PIL import Image, ImageTk


arka_plan_renk="#E3F2FD"
baslık_renk="#1E88E5"
buton_alt="#66BB6A"
buton_başla="#FF7043"
buton_sil="#FF3232"
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
        with open("Asset/Database/kullanici.txt", "w") as f:
            f.write(kullanici_adi)
        window.quit()
        subprocess.Popen(["python","Asset/Library/main.py"])

# Veritabanını gösteren bir pencere aç
def veritabani_goster():
    global result_window  # result_window'u global olarak tanımla
    conn = sqlite3.connect('Asset/Database/oyuncu_skor.db')
    c = conn.cursor()

    # En iyi 10 kullanıcıyı al (doğru sayısına göre sıralı)
    c.execute("SELECT * FROM oyun_sonuclari ORDER BY dogru_sayisi DESC LIMIT 10")
    sonuclar = c.fetchall()
    conn.close()

    # Sonuçları yeni bir pencerede göster
    result_window = tk.Toplevel(window)
    result_window.title("En İyi 10")
    result_window.config(bg=arka_plan_renk,bd=-1)
    text_area = tk.Text(result_window, width=60, height=10,bd=-1,bg=arka_plan_renk)
    text_area.pack()



    if not sonuclar:  
        sonuc_yok = tk.Label(result_window, text="Kayıt Bulunamadı", font=("Verdana", 16, "roman"), width=20, height=2,bg=arka_plan_renk)
        sonuc_yok.pack(pady=5)
    else:
        for sonuc in sonuclar:
            text_area.insert(tk.END, f"İsim: {sonuc[1]} Doğru: {sonuc[2]} Yanlış: {sonuc[3]} Boş: {sonuc[4]}\n")

    # Tüm kayıtları silme butonunu ekle
    silme_buton = tk.Button(result_window, text="Tüm Kayıtları Sil", command=sil_tum_kayitlar,bg=buton_sil)
    silme_buton.pack(pady=5)

def sil_tum_kayitlar():
    if messagebox.askyesno("Onay", "Tüm kayıtları silmek istediğinize emin misiniz?"):
        conn = sqlite3.connect('Asset/Database/oyuncu_skor.db')
        c = conn.cursor()
        c.execute("DELETE FROM oyun_sonuclari")
        conn.commit()
        conn.close()
        messagebox.showinfo("Başarılı", "Tüm kayıtlar silindi.")
        
        # Açık olan sonucu gösteren pencereyi kapat
        result_window.destroy()  # result_window tanımlı olmalı
        veritabani_goster()  # Yenile

window = tk.Tk()
window.title("Dil Yolculuğu - Giriş")
window.geometry("500x300")

# Ekran boyutunu al
ekran_genislik = window.winfo_screenwidth()
ekran_yukseklik = window.winfo_screenheight()

# Pencereyi ekranda ortala
x = (ekran_genislik // 2) - (500 // 2)
y = (ekran_yukseklik // 2) - (300 // 2)
window.geometry(f"500x300+{x}+{y}")

label_adi = tk.Label(window, text="İsminizi Giriniz", font=("Verdana", 16, "roman"), width=20, height=2,bg=arka_plan_renk)
label_adi.pack(pady=10)

entry_adi = tk.Entry(window, font=("Arial", 14), width=25)
entry_adi.pack(pady=10)

btn_basla = tk.Button(window, text="Oyuna Başla", width=15, height=4, command=oyunu_baslat,bd=0.5,bg=buton_başla)
btn_basla.pack(pady=10)

btn_veritabani = tk.Button(window, text="En iyi 10 Sırala", width=15, height=2, command=veritabani_goster,bd=0.5,bg=buton_alt)
btn_veritabani.pack(pady=10)
window.config(bg=arka_plan_renk)

icon_image = Image.open("Asset/icon/game.jpg")  
icon_photo = ImageTk.PhotoImage(icon_image)
window.iconphoto(True, icon_photo)
veritabani_baglanti()
window.mainloop()
