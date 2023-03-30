#!/usr/bin/env python
# coding: utf-8

# In[58]:


import math
print ("1. Menghitung bangun 2 Dimensi")
print ("2. Menghitung bangun 3 dimensi")
print("")
bangun = int(input("Pilih opsi: "))
if bangun == 1:
    print ("pilih bangun 2 dimensi yang ingin dihitung")
    print ("{}\n{}\n{}\n{}\n{}\n{}\n".format("1. Persegi", "2. Persegi Panjang", "3. Segitiga", "4. Lingkaran", "5. Jajar Genjang", "6. Trapesium"))
    duaD = int(input("pilih bangun yang ingin dihitung: "))
    if duaD == 1:
        print("")
        print ("proses menghitung persegi")
        L = int(input("masukkan lebar persegi: "))
        luas1 = 4 * L
        print (luas1)
    elif duaD == 2:
        print("")
        print ("proses menghitung persegi panjang")
        P = int(input("masukkan Panjang persegi Panjang: "))
        L = int(input("masukkan lebar persegi Panjang: "))
        luas2 = P * L
        print (luas2)
    elif duaD == 3:
        print("")
        print ("proses menghitung segitiga")
        A = int(input("masukkan alas segitiga: "))
        T = int(input("masukkan tinggi segitiga: "))
        luas3 = 1/2 * A * T
        print (luas3)
    elif duaD == 4:
        print("")
        print("")
        print ("proses menghitung Lingkaran")
        r = int(input("masukkan jari - jari lingkaran: "))
        luas4 = math.pi * r * r
        print (luas4)
    elif duaD == 5:
        print ("proses menghitung Jajar Genjang")
        alas = float(input("Masukan alas: "))
        tinggi = float(input("Masukan tinggi: "))
        luas5 = alas * tinggi
        print(luas5)
    elif duaD == 6:
        print ("proses menghitung Trapesium")
        a = float(input("Masukan sisi A: "))
        b = float(input("Masukan sisi B: "))
        tinggi = float(input("Masukan tinggi: "))
        luas = 0.5 * (a + b) * tinggi
        print (luas)
    
    else:
        print("Maaf, bentuk  yang dapat dihitung hanya terbatas sampai 6 saja")
        
        
elif bangun == 2:
    print ("pilih bangun 3 dimensi yang ingin dihitung")
    print ("{}\n{}\n{}\n{}\n{}\n{}\n".format("1. Kubus", "2. Balok", "3. Tabung", "4. Kerucut", "5. Limas", "6. Prisma"))
    tigaD = int(input("pilih bangun yang ingin dihitung: "))
    if tigaD == 1:
        print("")
        print ("proses menghitung Volume Kubus")
        sisi = float(input("Masukan panjang sisi: "))
        volume1 = sisi**3
        print(volume1)
        print (volume1)
    elif tigaD == 2:
        print("")
        print ("proses menghitung Volume Balok")
        panjang =float(input("Masukan panjang balok: "))
        lebar =float(input("Masukan lebar balok: "))
        tinggi =float(input("Masukan tinggi balok: "))
        volume2 = panjang * lebar * tinggi
        print("Volume balok dengan panjang", panjang, ",lebar", lebar, ", dan tinggi", tinggi, "adalah", volume2)
    elif tigaD == 3:
        print("")
        print ("proses menghitung Volume Tabung")
        jari_jari =float(input("Masukan jari-jari tabung: "))
        tinggi = float(input("Masukan tinggi tabung: "))
        volume3 = math.pi * jari_jari * tinggi
        print("Volume tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah", volume3)
    elif tigaD == 4:
        print("")
        print ("proses menghitung Volume Kerucut")
        jari_jari =float(input("Masukan jari-jari kerucut: "))
        tinggi =float(input("Masukan tinggi kerucut: "))
        volume4 = 1/3 * math.pi * jari_jari **2 * tinggi
        print("Volume kerucut dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah", volume4)
    elif tigaD == 5:
        print("")
        print ("proses menghitung Limas")
        alas =float(input("Masukan alas limas: "))
        tinggi =float(input("Masukan tinggi limas: "))
        volume5 = 1/3 * alas * tinggi
        print("Volume limas dengan luas alas", alas, "dan tinggi", tinggi, "adalah", volume5)
    elif tigaD == 6:
        print ("proses menghitung Prisma")
        alas =float(input("Masukan alas prisma: "))
        tinggi =float(input("Masukan tinggi prisma: "))
        tinggi_prisma =float(input("Masukan tinggi prisma: "))
        volume6 = 1/2 * alas * tinggi * tinggi_prisma
        print("Volume prisma segita dengan alas", alas, ", tinggi", ", dan tinggi prisma", tinggi_prisma, "adalah", volume6)

    
    else:
        print("Maaf, bentuk  yang dapat dihitung hanya terbatas sampai 6 saja")
else:
    bangun >= 3
    print ("ALERT BANGUN HANYA TERSEDIA SAMPAI 3 DIMENSI SAJA")
    


# In[ ]:





# In[ ]:




