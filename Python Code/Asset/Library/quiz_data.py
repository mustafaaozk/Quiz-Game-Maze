sorular_ve_cevaplar = [
    ("Kitaplığındaki kitaplar çok düzenliydi.\n\nYukarıdaki cümlede altı çizgili sözcük hangi tür isimdir?", 
     ["Özel isim", "Cins isim", "Soyut isim", "Tekil isim"], 
     "Cins isim", ["kitaplar"]),  
    
    ("“Bahçede güzel çiçekler açmıştı.”\n\nYukarıdaki cümlede hangi sözcük sıfattır?", 
     ["Bahçede", "Güzel", "Çiçekler", "Açmıştı"], 
     "Güzel", ["sıfattır"]),  

    ("“Bu kitabı o bana hediye etti.”\n\nYukarıdaki cümlede zamir olarak kullanılan sözcüğü bulun.", 
     ["Bu", "Kitabı", "O", "Bana"], 
     "O", ["zamir"]),  

    ("“Bu soruyu hızlıca çözdü.”\n\nYukarıdaki cümlede zarf olan sözcüğü bulun.", 
     ["Bu", "Soruyu", "Hızlıca", "Çözdü"], 
     "Hızlıca", ["zarf"]),  

    ("“Tatilden sonra ödevlerimi bitireceğim.”\n\nYukarıdaki cümlede edat (ilgeç) olarak kullanılan sözcüğü bulun.", 
     ["Tatilden", "Sonra", "Ödevlerimi", "Bitireceğim"], 
     "Sonra", []),  

    ("“Hem çalışmalı hem de dinlenmelisin.”\n\nYukarıdaki cümlede bağlaç olan sözcüğü bulun.", 
     ["Hem", "Çalışmalı", "De", "Dinlenmelisin"], 
     "Hem", []),  

    ("“Aman! Dikkat et, düşeceksin!”\n\nYukarıdaki cümlede ünlem olan sözcüğü bulun.", 
     ["Aman", "Dikkat", "Et", "Düşeceksin"], 
     "Aman", []),  

    ("“O, her sabah koşuya çıkar.”\n\nYukarıdaki cümledeki fiili bulun.", 
     ["O", "Her", "Koşuya", "Çıkar"], 
     "Çıkar", ["fiili"]),  

    ("Aşağıdaki cümlelerden hangisinde niteleme sıfatı kullanılmıştır?", 
     ["Gideceğimiz yer uzakta.", "Bugün Ayşe kırmızı elbisesini giymişti.", "Dün hava yağmurluydu.", "Ağladığımı sadece Ali gördü."], 
     "Bugün Ayşe kırmızı elbisesini giymişti.", []),  

    ("Aşağıdaki cümlelerden hangisinde kişi zamiri ve dönüşlülük zamiri beraber kullanılmıştır?", 
     ["O bunu kendi seçti.", "Ali bugün okula gelmedi.", "Bu sabah kendimi yorgun hissediyorum.", "Gideceğimden Hilalin haberi yoktu."], 
     "O bunu kendi seçti.", []),  

    ("Aşağıdaki cümlelerden hangisinde edat kullanılmıştır?", 
     ["Bu çok zahmetli bir işti.", "Beni senin gibi anlayan başka kimse olmadı.", "Yeni yapılan bina göz alıcıydı.", "Galiba kış sert geçecek."], 
     "Beni senin gibi anlayan başka kimse olmadı.", []),  

    ("“ Ya kendin gel ya da haber yolla. ” cümlesinde geçen sözcüklerin türü nedir?", 
     ["Edat", "Sıfat", "İsim", "Bağlaç"], 
     "Bağlaç", ["Ya", "ya"]),  

    ("“Hey! Yabancı nereye böyle sessiz sedasız.” \n\nAltı çizili sözcüğün türü nedir?", 
     ["İsim", "Ünlem", "Eylem", "Bağlaç"], 
     "Ünlem", ["Hey", "Hey!"]),  

    ("Aşağıdaki sözcüklerden hangisinde zaman zarfında kullanılmıştır?", 
     ["Yarın İstanbul'a gidecek.", "Hiç durmadan çalıştılar.", "Niçin söylediklerimi dinlemiyorsunuz?", "Sessizce yürüdüler."], 
     "Yarın İstanbul'a gidecek.", []),  

    ("“Okula giderken yoluma koyun sürüsü çıktı.” \n\nCümlesinde altı çizili sözcükte hangi isim türü kullanılmıştır?", 
     ["Bağlaç", "Ünlem", "İsim", "Eylem"], 
     "İsim", ["sürüsü"]),  

    ("“Seni çok seviyorum.”\n\nCümlesindeki altı çizili sözcüğün türü nedir?", 
     ["İsim", "Ünlem", "Bağlaç", "Eylem"], 
     "Eylem", ["seviyorum"]),

    ("“Tahta merdivenleri hızla çıktım.” \n\nCümlesindeki altı çizili sözcükler sırasıyla hangi şıkta doğru verilmiştir?", 
     ["Fiil-sıfat", "Sıfat-sıfat", "Zarf-sıfat", "Sıfat-Zarf"], 
     "Sıfat-Zarf", ["Tahta", "hızla"]),  

    ("“Çağlar çok güzel bir hediye almıştı.” \n\nCümlesindeki altı çizili sözcükler sırasıyla hangi şıkta doğru verilmiştir?", 
     ["Zarf- sıfat-sıfat-isim", "Sıfat-sıfat-sıfat-isim", "Sıfat-zarf-sıfat-isim", "Zarf-zarf-isim-sıfat"], 
     "Zarf- sıfat-sıfat-isim", ["çok", "güzel", "bir", "hediye"]),  

    ("Konsere gidebilirsin yalnız evden izin almalısın.\nKüçük kedicik annesini kaybedince yalnız kaldı.\nSelim yalnız kalınca aklı başına geldi.\nNur tabağındaki yemeklerden yalnız etleri yememiş.\nYukarıda verilen sözcüklerde “yalnız” sözcüğü kaç türde kullanılmıştır?", 
     ["3", "2", "1", "0"], 
     "3", ["yalnız"]),  

    ("Kutudaki bir bardak kırık gelmiş.\nAbimle bir bu konuda anlaşamıyoruz.\nOnu kimseyle bir tutmazdı.\nBeni biri aramış.\nYukarıda verilen sözcüklerde “bir” sözcüğü sırasıyla hangi türlerde kullanılmıştır?", 
     ["Zarf-sıfat-sıfat-zarf", "Sıfat-sıfat-zarf-isim", "Sıfat-edat-zarf-zamir", "Zamir-edat-sıfat-sıfat"], 
     "Sıfat-edat-zarf-zamir", ["bir"]),

    ("“Masaya güzel bir cila yaptık.” \n\nCümlesindeki altı çizili sözcük türü bakımından nedir?", 
     ["Sıfat", "Zarf", "Fiil", "İsim"], 
     "Fiil", ["yaptık"]),

    ("“Sarı saçlarını savurarak sinirle yürüdü.”\n\n Cümlesindeki altı çizili sözcük türü bakımından nedir?", 
     ["İsim", "Sıfat", "Bağlaç", "Zarf"], 
     "Sıfat", ["Sarı"]),

    ("“Paketi eve kadar taşıdık.”\n\n Cümlesindeki altı çizili sözcük türü bakımından nedir?", 
     ["İsim", "Sıfat", "Fiil", "Zarf"], 
     "Fiil", ["taşıdık"]),

    ("“Halbuki iste ömrümü,\nİste gönlümü,\nİste, yoluna sereyim.\n\nYukarıda verilen dizedeki altı çizili sözcük türü bakımından nedir?", 
     ["İsim", "Edat", "Bağlaç", "Zamir"], 
     "Bağlaç", ["Halbuki"]),

    ("“Sabahleyin  .....  elbisesini giyip dışarı çıktı.”\n\nBu cümlede boş bırakılan yere aşağıdaki sözcüklerden hangisi getirilirse “ elbise” sözcüğünün niteliği belirtilmiş olmaz?", 
     ["Çizgili", "Yeşil", "İş", "Yeni"], 
     "İş", ["belirtilmiş olmaz"]), 

    ("“Masmavi gökyüzünü ve neşeli kuşları gördüğüm için çok sevindim.” \n\nCümlesindeki isimler aşağıdakilerin hangisinde doğru verilmiştir?", 
     ["Masmavi - Neşeli", "Gökyüzü - Kuşlar", "Neşeli - Gökyüzü", "Kuşlar - Çok"], 
     "Gökyüzü - Kuşlar", []),  

    ("Aşağıdaki cümlelerin hangisinde bağlaç yoktur?", 
     ["Mezuniyetine ne annem geldi ne babam.", "Kalemini ve silgisini evde unutmuş.", "Sinemaya veya tiyatroya gidelim.", "Akşamki yemek mideme dokundu."], 
     "Akşamki yemek mideme dokundu.", []),   

    ("Aşağıdaki cümlelerin hangisinde ünlem, cümleye şaşma anlamı kalmıştır?", 
     ["Ah, ne güzeldi o eski Ramazanlar!", "Oh be, dünya varmış!", "Aa, onlarda burdaymış!", "Hey, bana baksana!"], 
     "Aa, onlarda burdaymış!", []),  

    ("Evlerini yüksek kurdular\nÖnlerinde uzun balkon\nSular aşağıda kaldı\nAşağıda kaldı ağaçlar\n\nYukarıdaki altı çizili kelimelerden hangisi zarf görevindendir?", 
     ["Yüksek", "Uzun", "Aşağıda", "Ağaçlar"], 
     "Yüksek", ["yüksek", "uzun", "aşağıda", "ağaçlar"]),  

    ("Aşağıdaki cümlelerden hangisinde “ile” edat olarak kullanılmamıştır?", 
     ["Arkadaşım ile sinemaya gideceğiz.", "Tren ile yolculuk yapacağız.", "Zeynep ile Fatma ders çalışacak.", "Babamla maça gittik."], 
     "Zeynep ile Fatma ders çalışacak.", ["kullanılmamıştır"]),  

    ("Gökyüzünde yalnız gezen yıldızlar \nYeryüzünde sizin kadar yalnızım \nBir haykırsam belki duyulur sesim \nBen yalnızım, ben yalnızım, yalnızım \n\nBu dörtlüğün hangi mısralarında zamir yoktur?", 
     ["1-2", "2-4", "3-4", "1-3"], 
     "1-3", ["yoktur"]),  

    ("Hangisinde çekimli fiil vardır?", 
     ["Parktaki çocuk, akıllı biriydi.", "Çalışırsa iyi yapacağını bilen biriydi.", "Atatürk'ün atı çok güzeldi.", "O, sınıfımızın en akıllı çocuğudur."], 
     "Çalışırsa iyi yapacağını bilen biriydi.", []),

    ("“Kınamazlar güzel sevse yiğidi,\n güzel sevmek koç yiğide ar değil.”\n\nKaracaoğlan’a ait olan yukarıdaki dizelerde “güzel” kelimesinin görevi nedir?", 
     ["İsim", "Sıfat", "Zarf", "Edat"], 
     "İsim", ["“güzel”"]),

    ("“Geniş kar ayakkabıları giymiş bir adam yürüyordu. Zorlu yaşam şartları bu adamı yormuştu.”\n\nYukarıdaki paragrafta aşağıdaki sıfat türlerinden hangisine örnek verilmemiştir?", 
     ["Belgisiz sıfat", "Niteleme sıfatı", "İşaret sıfatı", "Soru sıfatı"], 
     "Soru sıfatı", []),

    ("I.Bunların hepsini satsan ne kazanırsın?\nII.Bu uçuşların ardından bir daha sefer yapılmadı.\nIII.Çömlekçi Baba da buralarda yaşamış.\nIV.Bunun ardından insanlarda bir merak başladı.\nYukarıdaki cümlelerin hangilerinde zamir kullanılmıştır?", 
     ["I, II ve III", "I, III ve IV", "II, III ve IV", "I, II ve IV"], 
     "I, III ve IV", []),

    ("I.Sevgi\nII.Barışsever\nIII.Dost\nYukarıda verilen isimler yapılarına göre basit isim, türemiş isim, birleşik isim olarak sıralandığında oluşan sıralama aşağıdakilerden hangisidir?", 
     ["I-II-III", "I-III-II", "III-II-I", "III-I-II"], 
     "III-I-II", []),

    ("Aşağıdaki cümlelerin hangisinde ünlem uyarı anlamında kullanılmıştır?", 
     ["Heyy! Dikkat et düşeceksin.", "Eyvah! Defterimi unuttum.", "Simitçi!","‘Ohhh!’ çekecek diye düşündüm."], 
     "Heyy! Dikkat et düşeceksin.", []),

    ("Aşağıdaki cümlelerin hangisinde eylem diğerlerinden farklıdır?", 
     ["Bir haziran sabahı telaşla mutfaktan içeri girdi.", "Daha önce hiçbir yerde çalışmamıştı.", "Küçük kardeşi bu evin hanımıydı.", "Hanımı kaşlarını çatarak “Yeter!” diye bağırdı."], 
     "Küçük kardeşi bu evin hanımıydı.", []),

    ("“Onun böyle konuşmasına üzülmüştü; içini çekmemek için kendini zor tuttu.”\n\nYukarıdaki cümlede edat görevinde kullanılan kelime hangisidir?",
     ["Böyle", "İçini", "İçin", "Kendi"], 
     "İçin", []),

    ("“Buraya geleli ancak iki ay olmuştu.” cümlesinde bağlaç olan kelimenin yerine aşağıdakilerden hangisi getirilemez?", 
     ["Ve", "Sadece", "Yalnız", "Üstelik"], 
     "Ve", [])
]  

