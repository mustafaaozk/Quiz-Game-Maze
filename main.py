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
cevap_var = tk.StringVar(value="")
geri_sayim_suresi = 30  
zamanlayici = None

pygame.mixer.init()
alkis_sesi = pygame.mixer.Sound("Asset/Voice/alkis_sesi.mp3")
yanlis_sesi = pygame.mixer.Sound("Asset/Voice/yanlis_cevap.mp3")

# etiket1 = Label(window, text="Oyunu kazanmak için ödüle ulaş \n Timsahlara yaklaşırsan Ölürsün.",
#                  fg="black", bg=background_color, font=("Times New Roman", 16))
# etiket1.pack(pady=20)

random.shuffle(sorular_ve_cevaplar)
sorular_ve_cevaplar = sorular_ve_cevaplar[:20]  # 20 soru ile çalışıyoruz

soru_indeks = 0  # İlk sorudan başla

# Doğru ve yanlış cevap sayaçları
dogru_sayac = 0
yanlis_sayac = 0
bos_sayısı=0


image = Image.open("Asset/Background/labirent.png")
image = image.resize((800, 500))
photo = ImageTk.PhotoImage(image)

white = "f0f6f2"
canvas = tk.Canvas(window, width=805, height=500)
canvas.config(bg="white",bd=-2)  

canvas.create_image(400, 250, image=photo)

canvas.pack(side=tk.LEFT, padx=50)

canvas.create_rectangle(1,1,805,500,outline="green",width=12)

karakter_resmi = Image.open("Asset/Images/karakter.png")
karakter_resmi = karakter_resmi.resize((80, 60), Image.Resampling.LANCZOS)  # Resmi uygun boyutlandır

karakter_img = ImageTk.PhotoImage(karakter_resmi.transpose(((Image.FLIP_LEFT_RIGHT))))

timsah_resmi = Image.open("Asset/Images/timsah.png")
timsah_resmi = timsah_resmi.resize((60, 60), Image.Resampling.LANCZOS)  # Timsah resmini boyutlandır
timsah_img = ImageTk.PhotoImage(timsah_resmi)


# Karakteri canvas üzerine yerleştir
karakter = canvas.create_image(2, 15, image=karakter_img, anchor=tk.NW)

# Ödül resmi (oyun boyunca görünecek)
odul_resmi = Image.open("Asset/Images/odul.png")  # Ödül resmini yükle
odul_resmi = odul_resmi.resize((100, 100), Image.Resampling.LANCZOS)  # Resmi uygun boyutlandır
odul_img = ImageTk.PhotoImage(odul_resmi)

# Soru ve giriş alanı
frame = tk.Frame(window)
frame.config(bg=background_color)
frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Doğru sayacı ekranı
label_dogru = tk.Label(window, text=f"Doğru: {dogru_sayac}", font=("Times New Roman", 30, "bold"), fg="green", bg=background_color)
label_dogru.place(x=width-1070, y=70)  # Ekranın sağ üst köşesine yerleştir

# Yanlış sayacı ekranı
label_yanlis = tk.Label(window, text=f"Yanlış: {yanlis_sayac}", font=("Times New Roman", 30, "bold"), fg="red", bg=background_color)
label_yanlis.place(x=width-880, y=70)  # Doğru sayaç yanına yerleştir

label_bos = tk.Label(window, text=f"Boş: {bos_sayısı}", font=("Times New Roman", 30, "bold"), fg="blue", bg=background_color)
label_bos.place(x=width-700, y=70)  # Doğru sayaç yanına yerleştir

label_geri_sayim = tk.Label(window, text=f"Süre: {geri_sayim_suresi} sn", font=("Times New Roman", 30), bg=background_color)
label_geri_sayim.place(x=width-350, y=80) 

# Soru etiketi için bir Text alanı ekleyelim
label_soru = Text(frame, width=55, height=9, font=("Times New Roman", 20, "bold"), wrap=tk.WORD, bd=0, bg=background_color)
label_soru.pack(pady=0)  # Yukarıdan boşluk bırakmak için pady ekledik
label_soru.config(state=tk.NORMAL)

# Cevap seçimi için değişken
cevap_var = tk.StringVar(value="None")
cevap_var.set(None)

radiobuttons = []
timsah_koordinatlari = [(120, 100), (260, 217), (510, 320),(475,420),(560,140),(730,230)]  # Örnek timsah koordinatları
  #                                                         en alt      sağ üst  en sol

for index, (timsah_x, timsah_y) in enumerate(timsah_koordinatlari):
    if index == 0:  # İlk timsahı sağa döndür

        tamsah_img_donmus = ImageTk.PhotoImage(timsah_resmi.transpose((Image.FLIP_LEFT_RIGHT))) # Sağa bakacak şekilde döndür
        canvas.create_image(timsah_x, timsah_y, image=tamsah_img_donmus, anchor=tk.NW)
    else:
        canvas.create_image(timsah_x, timsah_y, image=timsah_img, anchor=tk.NW)

# Karakterin her doğru cevap sonrası gideceği koordinatlar listesi

arry_hareket = [
    (2, 15),
    (2, 130),
    (10, 220),
    (80, 310),
    (48, 400),
    (250, 400),
    (300, 320),
    (360, 270),
    (350, 145),
    (270, 45)
]

arry=[
    [(100, 15),(170, 15), (170, 120), (120, 100)],
    [(2,15),(2, 130),(170, 15), (170, 120), (120, 100)],
    [(10, 220),(2,15) ,(2, 130), (100, 15), (170, 15), (170, 120), (120, 100)]   
]

odul_x = 170
odul_y = 120
canvas.create_image(odul_x, odul_y, image=odul_img, anchor=tk.NW)

point_control =0
check_point = 0
cp2=0
hedef_koordinat=(0,0)
def karakteri_hareket_et(dogru_mu):
    global dogru_sayac, yanlis_sayac, check_point, point_control, hedef_koordinat, cp2

    # Eğer cevap doğruysa
    if dogru_mu:  
        if dogru_sayac and point_control < 1:  
            check_point += 1
            hedef_koordinat = arry_hareket[check_point]  # Doğru cevap için doğru indeksi al
            print(f"hedef: {hedef_koordinat[0], hedef_koordinat[1]}")
            animasyon_hareketi(canvas, karakter, hedef_koordinat[0], hedef_koordinat[1]) 
            point_control = 0
            cp2 = 0  # Reset cp2 to ensure the next movement starts fresh
            print("Doğru hareket")
        elif cp2 > 0:  # Move back to the previous point if cp2 is greater than zero
            cp2 -= 1
            point_control-=1
            hedef_koordinat = arry[check_point][cp2]
            animasyon_hareketi(canvas, karakter, hedef_koordinat[0], hedef_koordinat[1])
            print("Önceki doğru hareket")
    else:
        # Yanlış cevap durumunda karakter hareket etsin
        if point_control < len(arry[check_point]):  # Hareket sınırını kontrol et
            hedef_koordinat = arry[check_point][point_control]
            animasyon_hareketi(canvas, karakter, hedef_koordinat[0], hedef_koordinat[1])  
            point_control += 1  # Yanlış hareket için artır
            cp2 = point_control - 1
            print("Yanlış hareket")

    # Karakter bir timsaha yaklaştı mı kontrol et
    if timsah_yaklasti_mi(hedef_koordinat):
        messagebox.showinfo("Game Over!", "Karakter bir timsaha yaklaştı! Oyun bitti.")
        window.quit()
        save_database(dogru_sayac, yanlis_sayac, bos_sayısı)

    print(f"Check Point: {check_point}, Point Control: {point_control}, CP2: {cp2}, Hedef: {hedef_koordinat[0], hedef_koordinat[1]}")

    

    # Karakter bir timsaha yaklaştı mı kontrol et
    if timsah_yaklasti_mi(hedef_koordinat):
        messagebox.showinfo("Game Over!", "Karakter bir timsaha yaklaştı! Oyun bitti.")
        window.quit()
        save_database(dogru_sayac, yanlis_sayac, bos_sayısı)

    print(f"check:{check_point}, pointyanlış:{point_control}cp2:{cp2} hedef:{hedef_koordinat[0], hedef_koordinat[1]}")

def cevabi_kontrol_et():
    global dogru_sayac, yanlis_sayac, soru_indeks, bos_sayısı  # Gerekli değişkenleri tanımla
    secilen_cevap = cevap_var.get()
    
    # Kullanıcının cevap seçip seçmediğini kontrol et
    if secilen_cevap == "None":  # Kullanıcı cevap seçmediyse
        messagebox.showwarning("Uyarı", "Lütfen bir cevap seçin.")
        return

    dogru_cevap = sorular_ve_cevaplar[soru_indeks][2]  # Doğru cevabı al
    zamanlayiciyi_durdur()
    # Cevap kontrolü
    if secilen_cevap == dogru_cevap:
        dogru_sayac += 1
        label_dogru.config(text=f"Doğru: {dogru_sayac}")
        #alkis_sesi.play()
        messagebox.showinfo("Sonuç", "Doğru cevap!")
        karakteri_hareket_et(dogru_mu=True)
        
    else:
        yanlis_sayac += 1
        label_yanlis.config(text=f"Yanlış: {yanlis_sayac}")
        #yanlis_sesi.play()
        messagebox.showerror("Sonuç", f"Yanlış cevap! Doğru cevap: {dogru_cevap}")
        karakteri_hareket_et(dogru_mu=False)
    
    soru_indeks += 1
    if soru_indeks < len(sorular_ve_cevaplar):
        soru_goster()  # Yeni soruyu göster
    else:
        karakter_pos = canvas.coords(karakter)
        if odul_yaklasti_mi(karakter_pos):
            messagebox.showinfo("Tebrikler!", "Karakter ödüle ulaştı! Oyunu kazandınız.")
            subprocess.Popen(["python", "son_odul.py"])
            save_database(dogru_sayac, yanlis_sayac, bos_sayısı)
            window.quit()
        elif timsah_yaklasti_mi(karakter_pos):
            messagebox.showinfo("Oyun Bitti!", "Timsaha yaklaştınız! Oyun bitti.")
            save_database(dogru_sayac, yanlis_sayac, bos_sayısı)
            window.quit()

def odul_yaklasti_mi(karakter_pos):
    """Karakter ödüle ulaştı mı?"""
    if karakter_pos[0]==odul_x and karakter_pos[1] == odul_y:
        return True
    return False
def timsah_yaklasti_mi(karakter_pos):
    """Karakter bir timsahın koordinatına ulaştı mı?"""
    for timsah_x, timsah_y in timsah_koordinatlari:
        
        if karakter_pos[0] == timsah_x and karakter_pos[1] == timsah_y:
            return True  
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

def siklari_olustur():
    global radiobuttons, cevap_var
    for rb in radiobuttons:
        rb.destroy()  # Eski şıkları temizle

    radiobuttons = []

    siklar = sorular_ve_cevaplar[soru_indeks][1]  # Şıkları al
    random.shuffle(siklar)
    for sik in siklar:
        rb = tk.Radiobutton(frame, text=sik, variable=cevap_var, value=sik, font=("Times New Roman", 25), bg=background_color)
        rb.pack(anchor='w')  # Şıkları sola yasla
        radiobuttons.append(rb)

def geri_sayim():
    global geri_sayim_suresi, zamanlayici,bos_sayısı

    # Süre dolduysa sonraki soruya geç
    if geri_sayim_suresi <= 0:
        bos_sayısı+=1
        label_bos.config(text=f"Boş: {bos_sayısı}")
        messagebox.showinfo("Zaman Doldu", "30 saniye içinde cevap verilmedi. Bir sonraki soruya geçiliyor.")
        bos_sayısı+=1
        sonraki_soruya_gec()
        return

    # Geri sayımı güncelle
    label_geri_sayim.config(text=f"Süre: {geri_sayim_suresi} sn")
    geri_sayim_suresi -= 1

    # Geri sayımı devam ettir
    zamanlayici = window.after(1000, geri_sayim)  # 1000 ms = 1 saniye

def zamanlayiciyi_durdur():
    global zamanlayici
    if zamanlayici is not None:
        window.after_cancel(zamanlayici)  # Mevcut zamanlayıcıyı durdur

def soru_goster():
    global soru_indeks, geri_sayim_suresi,label_soru
    label_soru.delete(1.0, tk.END)  # Eski soruyu temizle
    cevap_var.set(None)
    soru_metni = sorular_ve_cevaplar[soru_indeks][0]
    
    altı_çizili_kelimeler = sorular_ve_cevaplar[soru_indeks][3] if len(sorular_ve_cevaplar[soru_indeks]) > 3 else []
    # Her kelime için altı çizgili hale getir
    for kelime in altı_çizili_kelimeler:
        soru_metni = soru_metni.replace(kelime, f"{kelime}")  # Kelimeyi vurgula

    label_soru.insert(tk.END, soru_metni)  # Yeni soruyu ekle

    # Altı çizili kelimeler için tag'leri ekle
    for kelime in altı_çizili_kelimeler:
        start_index = label_soru.search(kelime, 1.0, tk.END)
        while start_index:  # Tüm örnekleri bul
            end_index = f"{start_index} + {len(kelime)}c"
            label_soru.tag_add("underline", start_index, end_index)
            start_index = label_soru.search(kelime, end_index, tk.END)

    # Tag özelliklerini ayarla
    label_soru.tag_config("underline", underline=True)  # Altı çizgi için tag

    siklari_olustur()  # Şıkları oluştur
    geri_sayim_suresi = 30  # Her yeni soru için süreyi 30 saniyeye ayarla
    zamanlayiciyi_durdur()  # Önceki zamanlayıcıyı durdur
    geri_sayim()

def sonraki_soruya_gec():
    global soru_indeks
    soru_indeks += 1
    if soru_indeks < len(sorular_ve_cevaplar):
        soru_goster()  # Yeni soruyu göster
    else:
        # Oyun sona erdiğinde karakterin ödüle ulaşıp ulaşmadığını kontrol et
        karakter_pos = canvas.coords(karakter)
        if odul_yaklasti_mi(karakter_pos):
            messagebox.showinfo("Tebrikler!", "Karakter ödüle ulaştı! Oyunu kazandınız.")
            save_database(dogru_sayac, yanlis_sayac, bos_sayısı)
            window.quit()  # Oyunu kapat
        if timsah_yaklasti_mi(karakter_pos):
            messagebox.showinfo("Oyun Bitti!", "Timsaha yaklaştınız! Oyun bitti.")
            save_database(dogru_sayac, yanlis_sayac, bos_sayısı)
            window.quit()  # Oyunu kapat
        
soru_goster()

# Cevap kontrol butonu
btn_kontrol = tk.Button(frame, text="Cevabı Kontrol Et", command=cevabi_kontrol_et, font=("Times New Roman", 30),bg="#E6A8AD", bd=-1)
btn_kontrol.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
