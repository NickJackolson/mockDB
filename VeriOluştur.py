import csv
import numpy as np
import os
import random
import pandas as pd
import string
import re

# id - kullanıcıAdı - Şifre - E-mail - isim - soyisim - kullanıcıTel - kurumadı - kurumAdresi - kurumtel - rol - yetki - veri
# sonuç - gönderme_tarihi - sonuç_tarihi

def kullanıcı_adı(isim,soyisim):
    isim = isim.split(" ")[0]
    num = random.randint(1, 150)
    kullanıcı_adı = (isim[:random.randint(3,len(isim))]+soyisim[:random.randint(0,len(soyisim))]+str(num))
    return kullanıcı_adı

def şifre():
    lower_upper_alphabet = string.ascii_letters
    temp = []
    şifre = ""
    for i in range(0,8):
        temp.append(random.choice(lower_upper_alphabet))
    return şifre.join(temp)

def e_mail(isim):
    isim = re.sub(" ","_",isim)
    mail_seç = ["gmail","outlook","hotmail"]
    num = random.randint(60, 98)
    e_mail_adresi = (isim+str(num)+"@"+random.choice(mail_seç)+".com").lower()
    return e_mail_adresi

def kurum_adı_adresi_telefonu(kurum_listesi,adres_listesi,adet):
    eşleşme = zip(kurum_listesi[:adet],adres_listesi[:adet],[sabit_no() for i in range(0,adet)])
    return list(eşleşme)

def isim_soyisim(isim_listesi, soyisim_listesi):
    isim_soyisim_listesi = []
    i = 0
    for isim,soyisim in zip(isim_listesi,soyisim_listesi):
        isim_soyisim_listesi.append((isim,soyisim))
        if i == 120:
            break
        i += 1
    return isim_soyisim_listesi

def sabit_no():
    num = random.randint(1000000, 9999999)
    sabit_no = (str(num))
    return sabit_no

def tel_no(adet):
    tel_no_listesi = []
    for i in range(0,adet):
        num = random.randint(5000000000, 5599999999)
        tel_no_listesi.append(str(num))
    return tel_no_listesi

def yetki(adet,admin_adeti):
    yetki_listesi = np.zeros(adet,dtype=np.int8)
    yetki_listesi[0:admin_adeti] = 1
    return yetki_listesi

def dosya_oku(dosya_adı):
    with open(dosya_adı,encoding="UTF-8") as dosya:
        liste = dosya.read()
    liste = liste.split("\n")
    liste = [eleman for eleman in liste if eleman != '']
    return liste



isim_listesi = dosya_oku("isim_listesi.txt")
soyisim_listesi = dosya_oku("soyisim.txt")
kurumlar_listesi = dosya_oku("kurumlar.txt")
adresler_listesi = dosya_oku("adresler.txt")
adresler_listesi = [ x+y for x,y in zip(adresler_listesi[0::2], adresler_listesi[1::2]) ]
adres_listesi = []
for adres in adresler_listesi:
    adres_listesi.append(adres.replace(",", ""))
tarih_listesi = dosya_oku("tarihler.txt")

kullanıcı_adı_listesi = [kullanıcı_adı(isim,soyisim) for isim,soyisim in zip(isim_listesi,soyisim_listesi)]

şifre_listesi = [şifre() for i in range(0,120)]

e_mail_listesi = [e_mail(isim) for isim in isim_listesi]

tel_no_listesi = tel_no(120)

kurum_adı_adr_tel = kurum_adı_adresi_telefonu(kurumlar_listesi,adres_listesi,120)
kurum_adı_adr_tel = np.asarray(list(map(list, kurum_adı_adr_tel)))
while kurum_adı_adr_tel.shape[0] < 120:
    kurum_adı_adr_tel = np.vstack([kurum_adı_adr_tel[random.randint(0, len(kurum_adı_adr_tel)-1)], kurum_adı_adr_tel])

yetki_listesi = yetki(120,2)



#boş sütunlar
rol = [None for i in range(0,120)]
veri = [None for i in range(0,120)]
sonuç = [None for i in range(0,120)]
sonuç_tarihi = [None for i in range(0,120)]



db_dict = {"id":np.arange(0,120), "kullanıcıAdı":kullanıcı_adı_listesi[0:120], "şifre":şifre_listesi[0:120],
                  "email":e_mail_listesi[0:120], "isim":isim_listesi[0:120], "soyisim":soyisim_listesi[0:120] ,
                  "kullanıcıTel":tel_no_listesi , "kurumAdı": kurum_adı_adr_tel[:,0], "kurumAdresi":kurum_adı_adr_tel[:,1],
                  "kurumTel":kurum_adı_adr_tel[:,2] ,"rol":rol, "yetki":yetki_listesi, "veri":veri,
                  "sonuç":sonuç, "göndermeTarihi":tarih_listesi,"sonuçTarihi":sonuç_tarihi}


db = pd.DataFrame(data=db_dict)
db = db.set_index("id")

db.to_csv(r'IndexDummyData.csv', index = True, encoding = 'utf-16')
