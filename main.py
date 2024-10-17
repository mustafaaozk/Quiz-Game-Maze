import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame
import sqlite3  
import subprocess    

from quiz_data import sorular_ve_cevaplar
from database_save import save_database

window = tk.Tk()
window.title("Labirent Quiz Oyunu")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
background_color = "#ADD8E6"
window.config(bg=background_color)


pygame.mixer.init()
alkis_sesi = pygame.mixer.Sound("Asset/Voice/alkis_sesi.mp3")
yanlis_cevap = pygame.mixer.Sound("Asset/Voice/yanlis_cevap.mp3")

etiket1 = Label(window, text="Oyunu kazanmak için ödüle ulaş \n Timsahlara yaklaşırsan Ölürsün.",
                 fg="black", bg=background_color, font=("Times New Roman", 16))
etiket1.pack(pady=20)

random.shuffle(sorular_ve_cevaplar)
sorular_ve_cevaplar = sorular_ve_cevaplar[:20]  # 20 soru ile çalışıyoruz

soru_indeks = 0  # İlk sorudan başla

# Doğru ve yanlış cevap sayaçları
dogru_sayac = 0
yanlis_sayac = 0
check_point = 0


image = Image.open("Asset/Background/labirent.png")
image = image.resize((800, 500))
photo = ImageTk.PhotoImage(image)

white = "f0f6f2"
canvas = tk.Canvas(window, width=805, height=500)
canvas.config(bg="white",bd=-2)  

canvas.create_image(400, 250, image=photo)

canvas.pack(side=tk.LEFT, padx=50)

canvas.create_rectangle(1,1,805,500,outline="black",width=12)

karakter_resmi = Image.open("Asset/Images/karakter.png")
karakter_resmi = karakter_resmi.resize((100, 80), Image.Resampling.LANCZOS)  # Resmi uygun boyutlandır
karakter_img = ImageTk.PhotoImage(karakter_resmi)

timsah_resmi = Image.open("Asset/Images/timsah.png")
timsah_resmi = timsah_resmi.resize((60, 60), Image.Resampling.LANCZOS)  # Timsah resmini boyutlandır
timsah_img = ImageTk.PhotoImage(timsah_resmi)


# Karakteri canvas üzerine yerleştir
karakter = canvas.create_image(2, 15, image=karakter_img, anchor=tk.NW)

# Ödül resmi (oyun boyunca görünecek)
odul_resmi = Image.open("Asset/Images/odul.png")  # Ödül resmini yükle
odul_resmi = odul_resmi.resize((100, 100), Image.Resampling.LANCZOS)  # Resmi uygun boyutlandır
odul_img = ImageTk.PhotoImage(odul_resmi)

# Ödülü en başta labirentin sonuna yerleştir
odul_x = 715
odul_y = 400
canvas.create_image(odul_x, odul_y, image=odul_img, anchor=tk.NW)

# Soru ve giriş alanı
frame = tk.Frame(window)
frame.config(bg=background_color)
frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Doğru sayacı ekranı
label_dogru = tk.Label(window, text=f"Doğru: {dogru_sayac}", font=("Times New Roman", 20, "bold"), fg="green", bg=background_color)
label_dogru.place(x=width-370, y=200)  # Ekranın sağ üst köşesine yerleştir

# Yanlış sayacı ekranı
label_yanlis = tk.Label(window, text=f"Yanlış: {yanlis_sayac}", font=("Times New Roman", 20, "bold"), fg="red", bg=background_color)
label_yanlis.place(x=width-200, y=200)  # Doğru sayaç yanına yerleştir

# Soru etiketi için bir Text alanı ekleyelim
label_soru = Text(frame, width=40, height=2, font=("Times New Roman",30, "bold"), wrap=tk.WORD,bd=0,bg=background_color)
label_soru.pack(pady=0)  # Yukarıdan boşluk bırakmak için pady ekledik
label_soru.config(state=tk.NORMAL)

# Cevap seçimi için değişken
cevap_var = tk.StringVar()
cevap_var.set(None)

radiobuttons = []

def karakteri_hareket_et():
    # Karakteri belirli bir adım (örneğin 50 piksel) sağa doğru hareket ettir
    canvas.move(karakter, 50, 0)

    # Karakter ödüle ulaştı mı kontrol et (X ve Y koordinatlarına göre)
    karakter_pos = canvas.coords(karakter)
    if karakter_pos[0] >= odul_x and karakter_pos[1] >= odul_y:
        messagebox.showinfo("Tebrikler!", "Karakter ödüle ulaştı! Oyunu kazandınız.")
        window.quit()

# Karakterin her doğru cevap sonrası gideceği koordinatlar listesi
hareket_koordinatlari = [
    (0, 0), (2, 120), (odul_x, odul_y),(2, 220), (400, 250), 
    (500, 300), (600, 350), (500, 400), (400, 450), 
    (300, 500), (odul_x, odul_y)  # Son doğru cevapta ödüle ulaşacak
]

# Timsahların bulunduğu koordinatlar
timsah_koordinatlari = [(120, 100), (260, 217), (510, 320),(475,420),(560,140),(730,230)]  # Örnek timsah koordinatları
  #                                                         en alt      sağ üst  en sol
# Timsahları doğru resimle yerleştir
for timsah_x, timsah_y in timsah_koordinatlari:
    canvas.create_image(timsah_x, timsah_y, image=timsah_img, anchor=tk.NW)

# At the beginning of your code
son_dogru_koordinat = (2, 15)  # Initialize with the starting position of the character

def karakteri_hareket_et(dogru_mu):
    global dogru_sayac, yanlis_sayac, son_dogru_koordinat  # Include son_dogru_koordinat here

    # Doğru cevap verilirse karakteri belirtilen koordinatlara taşı
    if dogru_mu:  
        if dogru_sayac < len(hareket_koordinatlari):
            hedef_koordinat = hareket_koordinatlari[dogru_sayac]  # Doğru sayısına göre koordinatı al
            animasyon_hareketi(canvas, karakter, hedef_koordinat[0], hedef_koordinat[1])
            
            # Update last correct position after moving
            son_dogru_koordinat = (hedef_koordinat[0], hedef_koordinat[1])  # Update last correct position
            
            # Kontrol et, eğer ödüle ulaşılmışsa
            if odul_yaklasti_mi(canvas.coords(karakter)):
                messagebox.showinfo("Tebrikler!", "Karakter ödüle ulaştı! Oyunu kazandınız.")
                save_database(dogru_sayac, yanlis_sayac)
                window.quit()  # Oyunu kapat
                subprocess.Popen(["python", "son_odul.py"])

    else:  # Yanlış cevap verilirse
        # Yanlış sayaca göre timsah konumlarını kontrol et
        if yanlis_sayac < len(timsah_koordinatlari):
            hedef_koordinat = timsah_koordinatlari[yanlis_sayac]  # Şu anki yanlış sayısına göre timsah konumunu al
            animasyon_hareketi(canvas, karakter, hedef_koordinat[0], hedef_koordinat[1])

        # Kontrol et, eğer timsaha yaklaşıldıysa
        if timsah_yaklasti_mi(canvas.coords(karakter)):
            messagebox.showinfo("Oyun Bitti!", "Timsaha yaklaştınız! Oyun bitti.")
            save_database(dogru_sayac, yanlis_sayac)
            window.quit()  # Oyunu kapat

# Tek bir cevabi_kontrol_et fonksiyonu
def cevabi_kontrol_et():
    global dogru_sayac, yanlis_sayac, soru_indeks, son_dogru_koordinat  # Declare soru_indeks as global

    secilen_cevap = cevap_var.get()
    dogru_cevap = sorular_ve_cevaplar[soru_indeks][2]

    if secilen_cevap == "":
        messagebox.showwarning("Uyarı", "Lütfen bir cevap seçin.")
        return

    if secilen_cevap == dogru_cevap:
        dogru_sayac += 1
        label_dogru.config(text=f"Doğru: {dogru_sayac}")
        alkis_sesi.play()
        messagebox.showinfo("Sonuç", "Doğru cevap!")

        # Doğru cevaptan sonra karakteri hareket ettir
        karakteri_hareket_et(dogru_mu=True)

        # Eğer yanlış cevap verdikten sonra doğru cevap verildiyse karakter geri eski pozisyonuna gider
        if yanlis_sayac > 0:
            # Move character back to last correct position
            x_fark = son_dogru_koordinat[0] - canvas.coords(karakter)[0]
            y_fark = son_dogru_koordinat[1] - canvas.coords(karakter)[1]
            canvas.move(karakter, x_fark, y_fark)

    else:
        yanlis_sayac += 1
        label_yanlis.config(text=f"Yanlış: {yanlis_sayac}")
        yanlis_cevap.play()
        messagebox.showerror("Sonuç", f"Yanlış cevap! Doğru cevap: {dogru_cevap}")

        # Yanlış cevaptan sonra karakter timsaha doğru hareket eder
        karakteri_hareket_et(dogru_mu=False)

    # Sorular bitene kadar devam et
    soru_indeks += 1
    if soru_indeks < len(sorular_ve_cevaplar):
        soru_goster()  # Yeni soruyu göster
    else:
        # Oyun sona erdiğinde karakterin ödüle ulaşıp ulaşmadığını kontrol et
        karakter_pos = canvas.coords(karakter)
        if odul_yaklasti_mi(karakter_pos):
            messagebox.showinfo("Tebrikler!", "Karakter ödüle ulaştı! Oyunu kazandınız.")
            save_database(dogru_sayac, yanlis_sayac)
            window.quit()  # Oyunu kapat
            

def odul_yaklasti_mi(karakter_pos):
    """Karakter ödüle ulaştı mı?"""
    x, y = karakter_pos
    return abs(x - odul_x) < 10 and abs(y - odul_y) < 10  # Ödüle yakın olup olmadığını kontrol et

def timsah_yaklasti_mi(karakter_pos):
    """Karakter bir timsahın koordinatına ulaştı mı?"""
    for timsah_x, timsah_y in timsah_koordinatlari:
        if abs(karakter_pos[0] - timsah_x) < 10 and abs(karakter_pos[1] - timsah_y) < 10:
            return True  # Timsah koordinatına yakınsa True döndür
    return False
def animasyon_hareketi(canvas, obj, hedef_x, hedef_y, adim=5):
    """Karakteri belirlenen koordinatlara adım adım hareket ettirir."""
    x, y = canvas.coords(obj)

    if abs(hedef_x - x) > adim or abs(hedef_y - y) > adim:  # Hedefe ulaşılmadıysa
        x_fark = hedef_x - x
        y_fark = hedef_y - y
        x_adim = adim if x_fark > 0 else -adim
        y_adim = adim if y_fark > 0 else -adim

        # Eğer x veya y farkı küçükse o eksende hareketi bitir
        if abs(x_fark) < adim:
            x_adim = x_fark
        if abs(y_fark) < adim:
            y_adim = y_fark

        # Karakteri yeni konuma adım adım taşı
        canvas.move(obj, x_adim, y_adim)
        # Bir süre sonra tekrar hareket ettir (animasyonu devam ettirmek için)
        canvas.after(50, animasyon_hareketi, canvas, obj, hedef_x, hedef_y)
son_dogru_koordinat = (0, 15)   

def siklari_olustur():
    global radiobuttons
    for rb in radiobuttons:
        rb.destroy()  # Eski şıkları temizle

    radiobuttons = []

    siklar = sorular_ve_cevaplar[soru_indeks][1]  # Şıkları al
    for sik in siklar:
        rb = tk.Radiobutton(frame, text=sik, variable=cevap_var, value=sik, font=("Times New Roman", 30),bg=background_color)
        rb.pack(anchor='w')  # Şıkları sola yasla
        radiobuttons.append(rb)

def soru_goster():
    global soru_indeks
    label_soru.delete(1.0, tk.END)  # Eski soruyu temizle
    label_soru.insert(tk.END, sorular_ve_cevaplar[soru_indeks][0])  # Yeni soruyu ekle
    siklari_olustur()  # Şıkları oluştur

soru_goster()

# Cevap kontrol butonu
btn_kontrol = tk.Button(frame, text="Cevabı Kontrol Et", command=cevabi_kontrol_et, font=("Times New Roman", 14),bg="#E6A8AD", bd=-1)
btn_kontrol.pack(side=tk.BOTTOM, pady=10)


window.mainloop()
