import sifre_olusturma
import os
dosyanın_yolu = os.getcwd()
os.chdir(dosyanın_yolu)
os.system("setup.py")
sifre_olusturma.sifre_olustur("dosya.txt")