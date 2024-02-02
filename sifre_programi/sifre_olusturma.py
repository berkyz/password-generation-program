import random
import os
dosya_yolu = os.getcwd()
os.chdir(os.path.expanduser(dosya_yolu))
def sifre_olustur(dosya_ismi):
    """Bir dosya içerisine 8 ile 10 arasında birden fazla şifre oluşturur."""
    lst_harf = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","q","w","e","r","t","y","u","o","p","a","s","d","f","g","h","j","k","l","i","z","x","c","v","b","n","m"]
    lst_sayi = [0,1,2,3,4,5,6,7,8,9]
    lst_sembol = ["!","+","%","&","/","=","?","_","-","*","^","#","$","|","@","€",".",":",",",";","`"]
    lst_birlesik = lst_harf + lst_sayi

    while True:
            dosya = open("dosya.txt","r+")
            icerik = dosya.read()
            i = random.randint(8,10)
            j = 0
            abc = random.randint(1,2)
            kelime = ""
            while j < i:
                if abc == 1:
                    a = random.randint(0,61)
                    kelime = kelime + str(lst_birlesik[a])
                elif abc == 2:
                    efg = random.randint(1,2)
                    a = random.randint(0,61)
                    b = random.randint(0,20)
                    if efg == 1:
                        kelime = kelime + str(lst_birlesik[a])
                    elif efg == 2:
                        kelime = kelime + lst_sembol[b]
                j+=1
            if kelime not in icerik:
                dosya.write(kelime + "\n")
                print("Eklendi.")
            elif kelime in icerik:
                print("Zaten var.")
            dosya.close()