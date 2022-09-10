
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def odczytaj_tekst(nazwa_pliku):
    odczytanytekst = ""
    with open(nazwa_pliku, "r", encoding="utf-8") as tekst:
        for symbol in tekst:
            odczytanytekst += symbol
    tekst.close()
    return odczytanytekst

def oblicz_znak(zapis_binarny_string):
    liczba = int(zapis_binarny_string, 2)
    znak = chr(liczba)
    return znak

def oblicz_CRC(zapis_binarny, mianownik):
    for x in range(len(mianownik) - 1):
        zapis_binarny = zapis_binarny + '0'
    while len(zapis_binarny) >= len(mianownik):
        pomocnik = zapis_binarny[0: len(mianownik)]
        zapis_binarny = zapis_binarny[len(mianownik):]
        wynik = ""
        for i in range(len(mianownik)):
            if pomocnik[i] == mianownik[i]:
                wynik = wynik + '0'
            else:
                wynik = wynik + '1'
        wynik = str(bin(int(wynik, 2)))[2:]
        zapis_binarny = wynik + zapis_binarny
    while len(zapis_binarny) < (len(mianownik) - 1):
        zapis_binarny = "0" + zapis_binarny
    return zapis_binarny

def Sprawdz_CRC(tekst, mianownik):
    zapis_binarny = ""
    for x in tekst:
        pomocnik = pomocnik2 = bin(ord(x))[2:]
        while len(pomocnik) < 8:
            pomocnik = '0' + pomocnik
        zapis_binarny = zapis_binarny + pomocnik
    while len(pomocnik2) < len(mianownik) - 1:
        pomocnik2 = '0' + pomocnik2
    zapis_binarny = zapis_binarny[:len(zapis_binarny) - 8] + pomocnik2
    return zapis_binarny

def tekst_na_bin(tekst):
    zapis_binarny = ""
    for x in range(len(tekst)):
        pomocnik = bin(ord(tekst[x]))[2:]
        while len(pomocnik) < 8:
            pomocnik = '0' + pomocnik
        zapis_binarny = zapis_binarny + pomocnik
    return zapis_binarny

if __name__ == '__main__':
    # obliczanie CRC
    nazwa_pliku = "Tekst.txt"
    plik_zapis = open(nazwa_pliku, "w")
    tekst = "qaz12345"
    print("Czy chcesz podac wlasny tekst? 1 - tak, 0 - nie. Domyslnie wpisane zostanie qaz12345 ")
    wybor = int(input())
    if wybor >= 1:
        print("Podaj tekst: ")
        tekst = input()
        plik_zapis.write(tekst)
    else:
        plik_zapis.write(tekst)
    plik_zapis.close()
    wczytany_tekst = odczytaj_tekst(nazwa_pliku)
    print(wczytany_tekst)
    W_Binarna = tekst_na_bin(wczytany_tekst)
    print(W_Binarna)
    print("Czy chcesz podac dzielnik CRC? 1 - tak, 0 - nie. Domyslna wartosc to: 111010101")
    wybor = int(input())
    if wybor >= 1:
        print("Podaj dzielnik: ")
        mianownik = input()
    else:
        mianownik = "111010101"
    CRC = oblicz_CRC(W_Binarna, mianownik)
    print("Obliczone CRC: ", CRC)
    znak_CRC = oblicz_znak(CRC)
    print("Znak dopisany do pliku: ", znak_CRC," wartosc: ", ord(znak_CRC))
    with open(nazwa_pliku, "a", encoding="utf-8") as plik_zapis:
        plik_zapis.write(znak_CRC)
    plik_zapis.close()
    print("Wcisnij dowolny klawisz aby kontynuowac")
    pauza = input()
    #sprawdzenie CRC
    print("Sprawdzenie poprawnosci dopisanego CRC do pliku")
    wczytany_tekst = odczytaj_tekst(nazwa_pliku)
    print(wczytany_tekst)
    W_Binarna = Sprawdz_CRC(wczytany_tekst, mianownik)
    print(W_Binarna)
    CRC = int(oblicz_CRC(W_Binarna, mianownik))
    print("Obliczone CRC: ", CRC)
    if CRC == 0:
        print("CRC poprawne - plik poprawny")
    else:
        print("CRC bledne - plik uszkodzony")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
