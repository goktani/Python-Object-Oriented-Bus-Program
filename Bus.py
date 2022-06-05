# In[0]:
                             ## PROBLEM 

# ========================
# Kullanıcıların "28 GRU 454" plakalı tek bir otobüs için yolcuları yönetmesini
# sağlayan bir Nesne Tabanlı Program yazacaksınız.
#
# Program, bu otobüsün yolcuları hakkında ad, soyad, cinsiyet, koltuk numarası vb.
# bilgileri saklamalıdır.

# Programın menüsü şu şekilde olmalıdır.
# ========================
#       Menu
# 1- Rezervasyon yap
# 2- Bütün yolcuları görüntüle
# 3- Bütün koltukları görüntüle
# 4- Bütün boş koltukları görüntüle
# 5- Çıkış
# Tercihinizi seçin:
# ========================

# Kodlarınızda gerekli yerlerde açıklamalar yapınız!!!
# Uygun yerlerde, en az 1 try/exept, ve 1 assert kullanmanız gerekli!!!

# Şimdi, bu problem için aşağıdaki özelliklerde sınıflar oluşturun ve daha sonra 
# bir main() metot çağırılarak programınız başlayacak.

# In[0]:
# ========================
# Yolcu() sınıfı:
# Öznitelikler: adı, soyadı, cinsiyeti
# Get/Set metotları (Bütün nitelikler için)
# Yolcu sınıfı için print metodunu yeniden tanımla, Örneğin: "Mert Yılmaz, E"

import time         #time methodunu çağırarak programımızda kullanacağız.
class Yolcu():      #Yolcu sınıfı oluşturuyoruz.
    def __init__(self,name,surname,gender):     #__init__  ile değişkenler tanımlıyoruz.
        self.name=name
        self.surname=surname        #DEĞİŞKENLERİMİZ...
        self.gender=gender  
    def get_name(self):     #Fonksiyonlar oluşturarak ileride fonksiyonlarımızı çalıştırarak programımızı oluşturacağız.
        return self.name
    def get_surname(self):   
        return self.surname
    def get_gender(self):
        return self.gender 
    def set_name(self,name1):
        self.name=name1                 #İSİM SOYİSİM ve CİNSİYET bilgilerini fonksiyonlarla oluşturuyoruz.
        return f"Adınız: {self.name}"
    def set_surname(self,surname1):
        self.surname=surname1
        return f"Soyadınız: {self.surname}"
    def set_gender(self,gender1):
        self.gender=gender1
        return f"Cinsiyetiniz: {self.gender}"
    def write(self):
        return f"{self.name},{self.surname},{self.gender}"      #write fonksiyonu ile tüm alınan bilgileri aynı cümlede göstereceğiz.

passenger=Yolcu(None,None,None)             #Yolcu sınıfını passenger adlı değişkene atıyoruz.


# In[0]:
# ========================
# Koltuk() sınıfı:
# Öznitelikler: int koltukNO, Boolean koltukDurum varsayılan False olsun, ve bir 
# Yolcu() yolcusu varsayılan None olsun
# Get/Set metotları (Bütün nitelikler için)
# get_yolcu ve set_yolcu() metotları tanımla, set_yolcu da koltuk durumunu değiştir.
# print metodu tanımla (Örnek: Koltuk no: 13, Mert Yılmaz, E)

class Koltuk():     #Koltuk sınıfı oluşturuyoruz.
    def __init__(self,seatNumber=None,seatStatus=False,passenger=None):       #__init__  ile değişkenler tanımlıyoruz.
        self.seatNumber=seatNumber
        self.seatStatus=seatStatus      #DEĞİŞKENLERİMİZ...
        self.passenger=passenger
    def get_seatNumber(self):
        return self.seatNumber
    def get_seatStatus(self):
        return self.seatStatus 
    def get_passenger(self):
        return self.passenger               #KOLTUK NUMARASI KOLTUĞUN DOLULUK DURUMU VE YOLCU adındaki değişken ile fonksiyonlar oluşturuyoruz.
    def set_seatNumber(self,seatNumber):
        self.seatNumber=seatNumber
    def set_seatStatus(self,seatStatus):
        self.seatStatus=seatStatus
    def set_passenger(self,passenger):
        self.passenger=passenger
seat=Koltuk()       #Koltuk Sınıfını SEAT adındaki değişkene atıyoruz.

        
# In[0]:
# ========================
# Otobus() sınıfı özellikleri:
# Öznitelikler: str plaka, int KoltukSayısı varsayılan 42 olsun
# Her bir otobüs 42 koltuktan oluşacaktır, öncelike  self.koltukar = [] alıp
# Bu listeyi 42 boş koltukla doldurun (Koltuk() nesneleri ile)
# Get/Set metotları (Plaka ve koltuk sayısı nitelikleri için)

# koltukRezerv(y yolcusu, int koltukNo) metodu ile yolcu rezerve etsin, 
    # önceden rezerve edilmiş bir koltuk rezerve etmeye çalışırsanız
    # bir hata mesajı vermeniz gerekir, 
    # "rezerve edilmiş, koltukta ... kişi oturuyor" şeklinde.

# printYolcular() metodu bütün yolcuları yazdırsın. Örneğin,
    # Koltuk no: 13, Mert Yılmaz, E

# printKoltuklar() metodu bütün koltukları yazdırsın. 
    # 1 False, None
    # ...
    # 13 True, Mert Yılmaz, E 
    # ...
    # gibi
    
# printBosKoltuklar() metodu bütün boş koltukların numarasını yazdırsın. "1 False, None" gibi

class Otobus():         #Otobüs adında Sınıf oluşturuyoruz
    def __init__(self,plate,reservation,allSeatNumber=42):          #__init__  ile değişkenler tanımlıyoruz.
        self.plate=plate
        self.reservation=reservation        #DEĞİŞKENLERİMİZ...
        self.allSeatNumber=allSeatNumber
    def get_plate(self):
        return self.plate
    def get_allSeatNumber(self):
        return self.allSeatNumber           #TÜM KOLTUK NUMARALARI PLAKA VE REZERVASYON bilgilerini fonksiyonlarla oluşturuyoruz.
    def get_reservation(self):
        return passenger.get_passenger()
    def set_plate(self,):
        self.plaka="28 GRU 454"  
    def set_allSeatNumber(self,allSeatNumber):
        self.allSeatNumber=allSeatNumber
bus=Otobus(4,1)         #Otobus sınıfını bus adındaki değişkene atıyoruz.
    
    
# In[0]:
# ========================
# Bir main() metodu yazın
# Bir otobus örnek nesnesi oluşturun
# Menüyü göstersin, print ile ve
# Kullanıcının seçimine göre program kullanıcıdan parametre almalı ve ilgili
    # metotları çağırmalı.
# Örneğin, kullanıcı 1'girerse, yolcu adını, soyadını, cinsiyetini ve koltuk numarası
# alarak ilgili metodu çağırıp koltuk rezerve etsin. Menü'deki diğer rakamlar
# için de benzer işlemler yapmalı. İşlem 5'te çıkış için sys.exit kullanabilirsiniz.

# Programın menüsü şu şekilde olmalı
# ========================
"""
               MENU
        1- Rezervasyon yap
        2- Bütün yolcuları görüntüle
        3- Bütün koltukları görüntüle
        4- Bütün boş koltukları görüntüle
        5- Çıkış
        """

# Tercihinizi seçin:

    
                    #Main adında bir fonksiyon oluşturuyoruz.
def main():         #Bu değişkene sınıflarda kullandığımız fonksiyonları çağırarak programımız bir bütün elde edecek.
    seats=[]        #seats adında bir liste oluşturuyoruz.
    for i in range(1,44):
        seats.append(seat.get_seatNumber())         #for döngüsü ile listeye append methodu ile 42 tane koltuk atıyoruz.
    while True:             #Kullanıcıya yapacağı işlemler için bir Menü göderiyoruz (Print ile)
        print("""========================
       Menu
 1- Rezervasyon yap
 2- Bütün yolcuları görüntüle
 3- Bütün koltukları görüntüle          
 4- Bütün boş koltukları görüntüle
 5- Çıkış""")
        try:
            inp=int(input("Tercihinizi seçin: "))#Kullanıcıdan  bir integer olarak bir değer alıyoruz ve 'inp' adında bir değişkene atıyoruz.
        except:
            print("Lütfen Sadece Tam Sayı Değeri Giriniz.")     #Kullanıcı integer değer vermez ise bu hata ile karşılanacaktır.
        print("========================")
        if inp==1:      #Kullanıcının eğer girdiği değişken 1 ise aşağıdaki komutlar çalışacak.
            try:
                seats1=int(input("Hangi Koltuğu Tercih Etmek İstiyorsunuz: "))
            except:
                print("Lütfen Sadece Tam Sayı değeri giriniz.")
            try:
                if seats1<1:
                        print("Lütfen Koltuk Numarasını 1 ile 42 arsında bir seçim yapınız.")
                        continue #Koltuk numaramızı 1 den küçük seçersek yukarıdaki hata ile karşılaşırız.
                elif seats1>42:
                        print("Lütfen Koltuk Numarasını 1 ile 42 arsında bir seçim yapınız.")                                            
                        continue #Koltuk numarasını 42 den büyük seçersek yukarıdaki hata ile karşılaşırız.
                if seats[seats1]==None:
                        passenger.set_name(input("İsminizi Giriniz: "))  #Program hatasız çalışır ise kullanıcıdan input ile değerler alıyoruz.
                        passenger.set_surname(input("Soyisminizi Giriniz: "))
                        passenger.set_gender(input("Cinsiyetinizi Giriniz: "))
                        print("Yolcu Bilgileri Alındı Doğrulanıyor...")  #Kullanıcıya bir geri bildirim yapıyoruz.
                        time.sleep(1)   #Time sleep ile işlemimizi yavaşlatıyoruz.
                elif seats[seats1]!=None:       #Eğer rezerve edilmiş koltuğu seçerse aşağıdaki bidiriyi alıyor.
                        print("Seçtiğiniz Koltuk başka biri tarafından alınmıştır.")
                seats[seats1]=passenger.write()  #Kullanıcıdan alınan değerleri liste içinde tanımlıyor.
                print(seats)   #Listeyi kullanıcıya gösteriyor.
            finally:
                pass

        elif inp==2:        #Kullanıcının eğer girdiği değişken 2 ise aşağıdaki komutlar çalışacak.
            b=-1            #b adında bir değişken oluşturuyoruz. (Bu değişkeni döngü içinde koltuk numarasını gösterecektir.)
            for i in seats:
                b+=1        #for döngüsü ile listedeki koltuklara bakıyoruz ve None(boş) olan koltukları eleyip None olmayan(Dolu) olan
                if i!=None: #koltuğu buluyoruz.
                    print(f"Koltuk Numarası: {b},{i}")  #Print ile yazdırıyoruz.
        elif inp==3:        #Kullanıcının eğer girdiği değişken 3 ise aşağıdaki komutlar çalışacak.
            for g in range(1,43): #for döngüsü ile koltuktaki tüm listeye bakılacak ve dolu olan koltuğun bilgileri gözükecektirr.
                print(f"{g}-{seats[g]}")
        elif inp==4:        #Kullanıcının eğer girdiği değişken 4 ise aşağıdaki komutlar çalışacak.
            a=-1
            for i in seats:    #for döngüsü ile listeye bakıyoruz.
                a+=1
                if i==None:     #listedeki tüm None(Boş) olanları print ile yazdırıyoruz.
                    print(a,seat.get_seatNumber(),seat.get_seatStatus())
        elif inp==5:                #Kullanıcının eğer girdiği değişken 1 ise aşağıdaki komutlar çalışacak.
            print("İyi Günler Dileriz...")  #Kullanıcıya geri bildirim veriliyor ve Programdan çıkış Yapılıyor...
            print("Çıkış Yapılıyor...")
            time.sleep(1)
            break
        else:       #Eğer kullanıcı 1 ile 5 arasında bir değer girmez ise aşağıdaki hata mesajını alacaktır.
            print("Lütfen Sadece 1'den 5'e Kadar Olan Değerleri Giriniz.")
main()          #main() ile fonksiyonumuzu çağırıyoruz.
