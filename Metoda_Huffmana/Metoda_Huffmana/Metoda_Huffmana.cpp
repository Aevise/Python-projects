// Metoda_Huffmana.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector> 
#include <queue> 
#include <unordered_map> 
#define wielkosc_tablicy 256

typedef struct Symbol_struktura
{
    char znak = NULL;
    int kod_symbolu = 0;                                                                                     
    int ilosc_symbolu = 0;
}Symbol;

typedef struct Drzewo_Huffmana 
{ 
    Drzewo_Huffmana* prawy = nullptr; 
    Drzewo_Huffmana* lewy = nullptr; 
    char przechowywany_symbol; 
    int ilosc_symboli_w_poddrzewie; 
}Drzewo_kodowe; 

struct porownaj
{
    bool operator()(const Drzewo_kodowe* lewe, const Drzewo_kodowe* prawe) const
    {
        return lewe->ilosc_symboli_w_poddrzewie > prawe->ilosc_symboli_w_poddrzewie;         // symbol o mniejszej czestotliwosci wystepowania ma wiekszy priorytet
    }
};


namespace std {
  typedef basic_string<unsigned char> ustring;
  typedef std::basic_ofstream<unsigned char, std::char_traits<unsigned char> > uofstream;
}

int porownanie_malejaco(const void* a, const void* b);       //funkcja porownania wartosci do qsort
Drzewo_kodowe *buduj(char symbol, int ilosc_symboli, Drzewo_kodowe* lewe_dziecko, Drzewo_kodowe* prawe_dziecko);
int porownanie_rosnaco(const void* a, const void* b);       //funkcja porownania wartosci do qsort
bool czy_jestem_lisciem(Drzewo_kodowe* korzen);
void zakoduj(Drzewo_kodowe* korzen, std::string kod, std::unordered_map<char, std::string>& kod_Huffmana, std::ofstream &plik);
std::string dec_na_bin(int liczba);                         //zamiana wartosci dziesietnej na binarna, przechowywana w zmiennej typu string
int bin_na_dec(int pozycja, int wartosc);                   //zamiana wartosci binarnej na dziesietna

int main()
{    
    int ilosc_wpisanych_symboli = 0;                //licznik wykorzystanych symboli
    int decyzja = 0;                                //znmienna decydujaca o wpisaniu wlasnego tekstu lub wykorzytania wartosci domyslnej
    int miejsce = -1;                               //miejsce danego symbolu w tablicy symboli
    char dana;                             //zmienna do przechowania obecnie czytanego symbolu z pliku
    Symbol tablica_symboli[wielkosc_tablicy];       
    std::string moj_tekst = {"Laboratoria z przedmiotu Teoria Informacji i Kodowania" };                          //zmienna do przechowania wlasnego tekstu
    std::ofstream dane_wejsciowe_tworzenie;         //definicja obiektu klasy ofstream (zapis do pliku)
    std::ofstream model_informacji_chaos;           //definicja obiektu klasy ofstream (zapis do pliku)
    std::ofstream model_informacji_posortowany;     //definicja obiektu klasy ofstream (zapis do pliku)
    std::ofstream wpisanie_kodu_do_pliku;            //definicja obiektu klasy ofstream (zapis do pliku)
    std::ofstream wpisanie_drzewa_do_pliku;         //definicja obiektu klasy ofstream (zapis do pliku)
    std::unordered_map<char, int> mapowanie;
    std::unordered_map<char, std::string> kod_huffmana;
    std::ifstream dane_wejsciowe_odczyt;            //definicja obiektu klasy ifstream (odczyt z pliku)

    std::cout << "Jezeli chcesz wpisac wlasny tekst wpisz 1 w przeciwnym wypadku wpisz 0" << std::endl;
    std::cin >> decyzja;                            

        if (decyzja > 1) decyzja = 1;               //korekta blednie wpisanych wartosci liczbowych
        else if (decyzja < 0) decyzja = 0;

    dane_wejsciowe_tworzenie.open("plik1.txt", std::ios_base::trunc);     //poinformowanie do jakiego pliku ma wplynac bufor danych                                          
    if (decyzja == 0)
    {
        
        dane_wejsciowe_tworzenie << moj_tekst;     //wartosc domyslna                
    }
    else
    {
        std::cin.get();                             //przechwycenie znaku bialego po nacisnieciu "ENTER"
        std::cout << "Podaj tekst: " << std::endl;
        std::getline(std::cin, moj_tekst);          //wpisane wlasnego tekstu             
        dane_wejsciowe_tworzenie << moj_tekst;      //przekazanie bufora danych do strumienia
    }
    dane_wejsciowe_tworzenie.close();               //zamkniecie strumienia

    dane_wejsciowe_odczyt.open("plik1.txt", std::ios_base::in);         //otwarcie strumienia danych w trybie tylko do czytania
    while (dane_wejsciowe_odczyt.get(dana))         //czytanie strumienia danych                     
    {
        for (int i = 0; i <= ilosc_wpisanych_symboli; i++)              //przeszukiwanie tablicy symboli 
        {
            //jezeli znaleziono znak przerwij dalsze szukanie i przejdz dalej
            if (tablica_symboli[i].znak == dana) {break;}
            else{miejsce++;}
            //jezeli nie znaleziono znaku, iteruj miejsce, w ktorym moglby wystepowac znak i kontynuuj
            //zmienna miejsce sluzy do przechowania wartosci i
        }
        if (tablica_symboli[miejsce].ilosc_symbolu == 0)   //jezeli symbol wczesniej nie wystapil
        {
            tablica_symboli[miejsce].kod_symbolu = dana;   //wpisanie danych do odpowiedniej struktury z tablicy
            tablica_symboli[miejsce].znak = dana;
            tablica_symboli[miejsce].ilosc_symbolu++;
            ilosc_wpisanych_symboli++;                     //iteracja ilosci wystapujacych symboli
        }
        else{tablica_symboli[miejsce].ilosc_symbolu++;}    //jezeli symbol wczesniej wystapil to zwieksz ilosc wystapien o 1
        miejsce = 0;                                       //ustawienie wartosci miejsca na 0
    }
    dane_wejsciowe_odczyt.close();                         //zamkniecie strumienia
//-------------------wypisanie przed sortowaniem-------------------------------------------
    model_informacji_chaos.open("plik2.txt", std::ios_base::trunc);                     //poinformowanie do jakiego pliku ma wplynac bufor danych
    model_informacji_chaos << "Ilosc uzytych symboli: " << ilosc_wpisanych_symboli << "\n";
    for (int i = 0; i <= ilosc_wpisanych_symboli; i++)
    {
        //wpisanie wartosci tablicy struktur o nazwie Symbol do pliku
        if (tablica_symboli[i].znak != NULL)
        {
            model_informacji_chaos << "znak: " << tablica_symboli[i].znak << " kod symbolu: " << tablica_symboli[i].kod_symbolu;
            model_informacji_chaos << " ilosc wystapien: " << tablica_symboli[i].ilosc_symbolu << std::endl;
        }
    }
    model_informacji_chaos.close();                      //zamkniecie strumienia
//------------------wypisanie z sortowaniem--------------------------------------------------
    qsort(tablica_symboli, ilosc_wpisanych_symboli+1, sizeof(Symbol), porownanie_malejaco);      //sortowanie tablicy
    model_informacji_posortowany.open("plik3.txt", std::ios_base::trunc);               //poinformowanie do jakiego pliku ma wplynac bufor danych 
    model_informacji_posortowany << "Ilosc uzytych symboli: " << ilosc_wpisanych_symboli << "\n";
    for (int i = 0; i <= ilosc_wpisanych_symboli; i++)
    {
        //wpisanie posortowanych wartosci tablicy struktur o nazwie Symbol do pliku
        if (tablica_symboli[i].znak != NULL)
        {
            model_informacji_posortowany << "znak: " << tablica_symboli[i].znak << " kod symbolu: " << tablica_symboli[i].kod_symbolu;
            model_informacji_posortowany << " ilosc wystapien: " << tablica_symboli[i].ilosc_symbolu << std::endl;
        }
    }
    model_informacji_posortowany.close();               //zamkniecie strumienia

    qsort(tablica_symboli, ilosc_wpisanych_symboli + 1, sizeof(Symbol), porownanie_rosnaco); //zamiana kolejnosci posortowania tablicy na odwrotna
  
    for (char znak : moj_tekst) 
    { 
        mapowanie[znak]++; 
    } 
    
    // tworzenie kolejki priorytetowej do przechowywania elementow drzewa  
    std::priority_queue<Drzewo_kodowe*, std::vector<Drzewo_kodowe*>, porownaj> kolejka; 

    for (auto lisc : mapowanie)  //wpisanie kazdego symbolu jako lisc i dodanie go do kolejki priorytetowej
    { 
        kolejka.push(buduj(lisc.first, lisc.second, nullptr, nullptr)); 
    }

    while (kolejka.size() != 1)
    {
        Drzewo_kodowe* lewy = kolejka.top();
        kolejka.pop();
        Drzewo_kodowe* prawy = kolejka.top();
        kolejka.pop();
        int laczne_wystepowanie = lewy->ilosc_symboli_w_poddrzewie + prawy->ilosc_symboli_w_poddrzewie; //obliczenie lacznej ilosci wystepujacych symboli dla laczonych lisci/punktow
        kolejka.push(buduj(NULL, laczne_wystepowanie, lewy, prawy)); //polaczenie dwoch lisci o najmniejszej czestotliwosci wystepowania i dodanie go z powrotem do kolejki priorytetowej
    }

    Drzewo_kodowe* korzen = kolejka.top();          //ustawienie wskaznika na korzen drzewa
    wpisanie_drzewa_do_pliku.open("Drzewo_Huffmana.txt", std::ios_base::trunc);                     //poinformowanie do jakiego pliku ma wplynac bufor danych

    zakoduj(korzen, "", kod_huffmana, wpisanie_drzewa_do_pliku); //przejscie przez drzewo od korzenia i zakodowanie symboli

    wpisanie_kodu_do_pliku.open("Kod_Huffmana.txt", std::ios_base::trunc);     //poinformowanie do jakiego pliku ma wplynac bufor danych
    for (auto dane_z_funkcji_zakoduj : kod_huffmana) 
    {
        wpisanie_kodu_do_pliku << "Znak: " << dane_z_funkcji_zakoduj.first << " Kod: " << dane_z_funkcji_zakoduj.second<<std::endl;
    }

    wpisanie_kodu_do_pliku.close();                //zamkniecie strumienia
    wpisanie_drzewa_do_pliku.close();                //zamkniecie strumienia

    //wypisanie kodowania poszczegolnych symboli
    std::cout << "Otrzymane slowa kodowe:\n" << std::endl;
    for (auto para : kod_huffmana) 
    {
        std::cout << para.first << " " << para.second << std::endl;
    }


    // wpisanie kodu do zakodowania do nowej zmiennej
    std::string str;
    for (char ch : moj_tekst) 
    {
        str += kod_huffmana[ch];
    }

    std::ofstream przed_kompresja;                                              //definicja obiektu klasy ofstream (zapis do pliku)
    przed_kompresja.open("bit_przed_kompresja.txt", std::ios_base::trunc);              //poinformowanie do jakiego pliku ma wplynac bufor danych
    przed_kompresja << str;
    przed_kompresja.close();

    //-------------------------Kompresja danych wejsciowych-----------------------------------------------//
    std::ifstream odczyt_przed_kompresja("bit_przed_kompresja.txt", std::ios_base::in);
    std::uofstream po_kompresji;
    po_kompresji.open("po_kompresji", std::ios_base::trunc);
    unsigned char pobrany_symbol;
    int licznik_pelnych_bajtow = 0; //zlicza ilosc pelnych bajtow ktore zostana zapisane do zakodowanego pliku
    std::ustring bajt_binarnie;             //przechowuje dany bajt zapisany w sposob binarny
    unsigned char zakodowany_znak;          //przechowuje zakodowany znak
    int wartosc_liczbowa = 0;               //wartosc dziesietna odczytanego kodu
    int pozycja_bitu = 0;                   //okresla pozycje odczytanego bitu w bajcie

    while (odczyt_przed_kompresja >> pobrany_symbol) //czytanie z pliku bit_przed_kompresja.txt
    {
        if (bajt_binarnie.size() < 7)               //budowanie bajtu przechowywanego jako 8 bitow w stringu
        {
            bajt_binarnie.push_back(pobrany_symbol);
        }
        else                                                //wykonuje sie gdy w stringu jest 7 elementow
        {
            bajt_binarnie.push_back(pobrany_symbol);        //dopisanie 8 elementu
            while (bajt_binarnie.size() != 0)               //wykonuje sie dopoki string nie bedzie pusty
            {
                zakodowany_znak = bajt_binarnie.back();     //odczytanie znaku przechowanego na koncu stringu
                if (zakodowany_znak == '1')                 //okreslenie czy przechowywany znak to 0 czy 1
                {
                    wartosc_liczbowa = wartosc_liczbowa + bin_na_dec(pozycja_bitu, 1);
                }
                else
                {
                    wartosc_liczbowa = wartosc_liczbowa + bin_na_dec(pozycja_bitu, 0);
                }
                
                pozycja_bitu = pozycja_bitu + 1;            //zmiana znaczenia bitu
                bajt_binarnie.pop_back();                   //usuniecie obsluzonego bitu
            }
            zakodowany_znak = wartosc_liczbowa;             //wpisanie do zmiennej typu char wartosci obliczonej powyzej
            po_kompresji << zakodowany_znak;                //wpisanie zakodowanego znaku do pliku

            pozycja_bitu = 0;                               //reset wartosci poczatkowych
            wartosc_liczbowa = 0;
            bajt_binarnie.clear();
            licznik_pelnych_bajtow++;                       
        }
    }
    int uzupelnienie_zerami = bajt_binarnie.size();         
    if (bajt_binarnie.size() != 0)                          //wykona sie jezeli bajt_binarnie ma wartosc wiêksza od 0 i mniejsza od 8
    {
        pozycja_bitu = 0;                                   //reset wartosci poczatkowych
        wartosc_liczbowa = 0;
        while (bajt_binarnie.size() != 0)                   
        { 
            zakodowany_znak = bajt_binarnie.back();         //odczytanie ostatniego przechowywanego elementu w stringu
            if (zakodowany_znak == '1')                     //obliczenie wartosci 
            {
                wartosc_liczbowa = wartosc_liczbowa + bin_na_dec(pozycja_bitu, 1);
            }
            else
            {
                wartosc_liczbowa = wartosc_liczbowa + bin_na_dec(pozycja_bitu, 0);
            }
            
            pozycja_bitu = pozycja_bitu + 1;
            bajt_binarnie.pop_back();                       //usuniecie obsluzonego elementu
        }
        zakodowany_znak = wartosc_liczbowa;                 //wpisanie do zmiennej typu char wartosci obliczonej powyzej           
        po_kompresji << zakodowany_znak;                    //wpisanie zakodowanego znaku do pliku
        pozycja_bitu = 0;
        wartosc_liczbowa = 0;
        bajt_binarnie.clear();
    }
    po_kompresji.close();
    odczyt_przed_kompresja.close();
    //---------------------------------------------------------------------------------------------------------//
    
    //----------------odczytanie skompresowanego kodu i zamiana go na wartosci binarne-------------------------//
    std::ifstream odczyt_po_kompresji("po_kompresji", std::ios_base::in);
    std::ofstream dekompresja_kod;
    dekompresja_kod.open("dekompresja_kod.txt", std::ios_base::trunc);
    int wartosc_symbolu = 0;
    std::string przechowanie_liczby_w_formie_binarnej;
    bool wykonaj = 1;
    int obieg_petli = 1;
    int pamietaj = licznik_pelnych_bajtow;

    while (licznik_pelnych_bajtow)
    {
        while (odczyt_po_kompresji >> pobrany_symbol)                                       //pobranie symbolu z pliku po_kompresji
        {
            wartosc_symbolu = pobrany_symbol;                                               //zamiana char na wartosc binarna
            przechowanie_liczby_w_formie_binarnej = dec_na_bin(wartosc_symbolu);            //zamiana odczytanego symbolu na wartosc binarna, ktora jest zapisana na stringu
            if (licznik_pelnych_bajtow != 0 && wykonaj == 1)
            {
                
                if (pamietaj >= obieg_petli) 
                {
                    while (przechowanie_liczby_w_formie_binarnej.size() != 8)               //uzupelnienie brakujacych zer w zapisie binarnym
                    {
                        przechowanie_liczby_w_formie_binarnej = "0" + przechowanie_liczby_w_formie_binarnej;
                    }
                    dekompresja_kod << przechowanie_liczby_w_formie_binarnej;
                    przechowanie_liczby_w_formie_binarnej.clear();
                }
                else 
                {
                    while(przechowanie_liczby_w_formie_binarnej.size() != uzupelnienie_zerami)    //uzupelnienie brakujacych zer w zapisie binarnym     
                    {
                        przechowanie_liczby_w_formie_binarnej = "0" + przechowanie_liczby_w_formie_binarnej;
                    }
                    dekompresja_kod << przechowanie_liczby_w_formie_binarnej;               //zapisanie odkodowanych znakow w formie 0 i 1 do pliku o nazwie dekompresja_kod.txt
                    przechowanie_liczby_w_formie_binarnej.clear();
                }
            }
            obieg_petli++;
        }
        licznik_pelnych_bajtow--;
        if (licznik_pelnych_bajtow == 0)
        {
            wykonaj = 0;
        }
    }
    if (wykonaj == 1)           //wykona sie jezeli zaden string nie mial dlugosci 8
    {
        odczyt_po_kompresji >> pobrany_symbol;
        wartosc_symbolu = pobrany_symbol;
        przechowanie_liczby_w_formie_binarnej = dec_na_bin(wartosc_symbolu);
        while (przechowanie_liczby_w_formie_binarnej.size() != uzupelnienie_zerami)
        {
            przechowanie_liczby_w_formie_binarnej = "0" + przechowanie_liczby_w_formie_binarnej;
        }
        dekompresja_kod << przechowanie_liczby_w_formie_binarnej;
        przechowanie_liczby_w_formie_binarnej.clear();
    }

    odczyt_po_kompresji.close();
    dekompresja_kod.close();
    //---------------------------------------------------------------------------------------------------------//

    //dekodowanie znakow
    std::string pomocnik;
    std::ifstream czytanie_kodu("dekompresja_kod.txt", std::ios_base::in);
    std::ofstream dekompresja_tekst;
    dekompresja_tekst.open("dekompresja_tekst.txt", std::ios_base::trunc);
    pomocnik.clear();
    while (czytanie_kodu >> pobrany_symbol)
    {
            pomocnik.push_back(pobrany_symbol);
            for (auto pair : kod_huffmana)
            {
                if (pomocnik == pair.second)
                {
                    std::cout << std::endl << "Odczytany kod: " << pair.second << " znak: " << pair.first;
                    dekompresja_tekst << pair.first;
                    pomocnik.clear();
                }
            }
    }
    czytanie_kodu.close();
    dekompresja_tekst.close();

    std::cout << std::endl<< "Utworzone pliki znajduja sie w folderze z projektem";
}

int porownanie_malejaco(const void* a, const void* b)
{
    Symbol* symbol1 = (Symbol*)a;
    Symbol * symbol2 = (Symbol*)b;

    int wynik_porownania = symbol1->ilosc_symbolu - symbol2->ilosc_symbolu;

    //jezeli oba symbole maja taka sama czestosc wystepowania, to sortowane sa po wartosci kodu symbolu
    if (wynik_porownania == 0)
    {
        wynik_porownania = symbol1->kod_symbolu - symbol2->kod_symbolu;
    }

    return -wynik_porownania; //odwrocenie logiki sprawdzania
}


int porownanie_rosnaco(const void* a, const void* b)
{
    Symbol* symbol1 = (Symbol*)a;
    Symbol* symbol2 = (Symbol*)b;

    int wynik_porownania = symbol1->ilosc_symbolu - symbol2->ilosc_symbolu;

    //jezeli oba symbole maja taka sama czestosc wystepowania, to sortowane sa po wartosci kodu symbolu
    if (wynik_porownania == 0)
    {
        wynik_porownania = symbol1->kod_symbolu - symbol2->kod_symbolu;
    }

    return wynik_porownania; 
}

Drzewo_kodowe *buduj(char symbol, int ilosc_symboli, Drzewo_kodowe* lewe_dziecko, Drzewo_kodowe* prawe_dziecko)
{  
    Drzewo_kodowe* drzewo = new Drzewo_kodowe(); 
     
    drzewo->ilosc_symboli_w_poddrzewie = ilosc_symboli; 
    drzewo->przechowywany_symbol = symbol; 
    drzewo->lewy = lewe_dziecko; 
    drzewo->prawy = prawe_dziecko; 
     
    return drzewo; 
}

bool czy_jestem_lisciem(Drzewo_kodowe* korzen)  //sprawdzenie czy dany element jest lisciem
{
    return korzen->lewy == nullptr && korzen->prawy == nullptr;
}

void zakoduj(Drzewo_kodowe* korzen, std::string kod, std::unordered_map<char, std::string>& kod_Huffmana, std::ofstream& plik)
{
    if (korzen == nullptr) 
    {
        return; //jezli wskaznik bedzie pokazywal na niezaalokowana pamiec to funkcja natychmiast konczy dzialanie
    }

    if (czy_jestem_lisciem(korzen))
    {
        kod_Huffmana[korzen->przechowywany_symbol] = (kod != "") ? kod : "1"; //wyrazenie warunkowe
    }

    //wpisanie tekstu do pliku odnosnie powstalego drzewa
    plik << std::endl << "Laczna ilosc symboli: (" << korzen->ilosc_symboli_w_poddrzewie << ")";
    if (korzen->przechowywany_symbol == NULL)
    {
        plik << " Jestem wezlem bez przechowywanego symbolu :(";
    }
    else
    {
        plik << " Przechowywany symbol: (" << korzen->przechowywany_symbol<<")";
    }

    plik << " Lewe dziecko: (" << &korzen->lewy << ") Prawe dziecko: (" << &korzen->prawy << ") Moj adres: (" << &korzen<<")";
    zakoduj(korzen->lewy, kod + "0", kod_Huffmana, plik); //rekurencyjne przejscie do lewego wezla
    zakoduj(korzen->prawy, kod + "1", kod_Huffmana, plik); //rekurencyjne przejscie do prawego wezla
}

std::string dec_na_bin(int liczba)
{
    std::string wartosc;
    std::string tymczasowy;
    wartosc.clear();
    tymczasowy.clear();
    int kontener1;
    while (liczba)
    {
        kontener1 = liczba % 2;
        liczba = liczba / 2;
        tymczasowy = std::to_string(kontener1);
        wartosc = tymczasowy + wartosc;
    }
    return wartosc;
}

int bin_na_dec(int pozycja, int wartosc)
{
    int wynik = 0;
    if (pozycja == 0)
    {
        if (wartosc == 0)
        {
            return 0;
        }
        else
        {
            return 1;
        }
    }
    else
    {
        int dwa = 2;
        int wynik = 0;
        for (int i = 1; i < pozycja; i++)
        {
            dwa *= 2;
        }
        return wartosc * dwa;
    }
}