---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region id="view-in-github" colab_type="text" -->
<a href="https://colab.research.google.com/github/ajankowski/python_tiny_workshop/blob/master/Python_w_10_lat.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<!-- #endregion -->

<!-- #region id="5zk32T8F0Bbj" colab_type="text" -->
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" align="center" width='500'>

# Python
to jeden z najpopularniejszych i najlatwiejszych do nauczenia się języków programowania.  
Kod w języku Python jest krótki i czytelny, nie pozostawia wątpliwości co do sposobu działania.  
Dodatkowy bonus - jest to język nauki i sztucznej inteligencji :-)
<!-- #endregion -->

<!-- #region id="bP9DSAAY0Bbl" colab_type="text" -->
## Syntax (struktura, uporządkowanie słów w zdaniu - gramatyka Pythona)
- Bloki kodu oddzielone są wcięciami (stosuje się 4 spacje, nie jest to konieczne, ale musimy być konsekwentni, tzn. kolejne wcięcia muszą być takie same, linia bez wcięcia znajdować się będzie poza blokiem).
- Wyrażenia które wymagają wcięć zakończone są dwukropkiem **:**
- Ważna jest wielkość liter.
- Komentarze w kodzie zaczynamy od znaku #
<!-- #endregion -->

```python id="zDV7Nwc89PpW" colab_type="code" colab={}
print('hello world')
```

```python id="vzTU16j3HPzB" colab_type="code" colab={}
!wget 
```

<!-- #region id="zX5CSbGx0Bbn" colab_type="text" -->
# Zmienne
Zmienna = miejsce, gdzie komputer przechowuje dane  
Zmienne przypisujemy do nazw znakiem rowności **=** , a testujemy czy dane są równe znakiem **==**
<!-- #endregion -->

```python id="AFeV6xAK0Bbq" colab_type="code" colab={}
kot = 3
pies = 7

```

```python id="_COkZ9ns0Bbz" colab_type="code" colab={}
kot + pies
```

```python id="RMfMdSAk0Bb_" colab_type="code" colab={}
kot == 3
# kot == pies
```

```python id="L5nlcdr10BcI" colab_type="code" colab={}
# wszystko od '#' do końca wiersza to komentarz (Python go pomija)
napis_1 = 'hallo'
napis_2 = "world!"

napis_3 = napis_1 + napis_2 # komentarz może zacząć się nie-na-początku wiersza
```

```python id="nED5KZiX0BcO" colab_type="code" colab={}
print(napis_3)
```

```python id="pEZEZPuiwhYq" colab_type="code" colab={}
#  możemy też wyświetlać dłuższy tekst
print('''dłuższy tekst
w kilku 
linijkach''')
```

```python id="mVi3uSr9vwTi" colab_type="code" colab={}
print('lecimy dalej)
```

```python id="H5gu2ev9v5Zg" colab_type="code" colab={}
# czasem program odmówi działania i pokaże nam błąd :-)
```

<!-- #region id="wqOuEgaX5mx8" colab_type="text" -->
### Symbole do wykonywanie działań matematycznych w Pythonie


Operator | Operation | Example | Evaluates to . . .
---|---|---|---|
** | Exponent | 2 ** 3 | 8
 % | Modulus | 22 % 8 | 6
// | Integer division | 22 // 8 | 2
/  | Division | 22 / 8 | 2.75
* | Multiplication | 3 * 5 | 15
- | Subtraction | 5 - 2 | 3
+ | Addition | 2 + 2 | 4
<!-- #endregion -->

```python id="N7GSXAsQ7-HN" colab_type="code" colab={}
# mozemy sprawdzić czy jakaś liczba dzieli sie przez inną 
8%3
```

```python id="kLz9oacR8YzS" colab_type="code" colab={}
print('reszta z dzielenia 8/3 -> ' + str(8%3))
```

```python id="lc4Gr9zs0BdP" colab_type="code" colab={}
imie = input('jak masz na imie? ')
print('hej '+ imie)
```

<!-- #region id="LQ5gCc740BdW" colab_type="text" -->
### Ćwiczenia e110

Poproś uzytkownika o wprowadzenie jakiejś cyfry i wydrukuj wynik mnożenia jej przez 3
<!-- #endregion -->

```python colab_type="code" id="E5VgrnBQ-5hV" colab={}
# ćwiczenie

```

<!-- #region colab_type="text" id="F8OpGPAlM8nq" -->
### Ćwiczenia e120

Poproś uzytkownika o wprowadzenie imienia i wieku, odpowiedz mu w którym roku będzie miał 100 lat.  

Oczekiwany wynik dla Bartka, 33 lata:  
'Bartek będziesz miał sto lat w 2053 roku'
<!-- #endregion -->

```python colab_type="code" id="hAwIJN6xM9_C" colab={}
# ćwiczenie
```

<!-- #region id="l6kDWT4N0BcZ" colab_type="text" -->
# Typy danych

W pythonie mamy dostępne kilka typów danych, podstawowe z nich to:   
- *int* - (integer) -liczby całkowite:  -99, -98,..., -2, -1, 0, 1, 2, ..., 98  
- *float* - floating point -liczby rzeczywiste (zmiennoprzecinkowe):  0.2, 3.14, -0.8897  
- *str* - tekst (string), tekstem jest dowolne wyrażenie w cudzysłowie pojedynczym lub podwójnym: 'python' lub "python"
<!-- #endregion -->

```python id="JX4WNUeM0Bca" colab_type="code" colab={}
liczba_calkowita = 6
liczba_rzeczywista = 0.56
```

```python id="1qRcU4-Y0Bcg" colab_type="code" colab={}
type(liczba_calkowita)
type(liczba_rzeczywista)
```

```python id="KD9DauLR0Bcq" colab_type="code" colab={}
napis = 'kuble'
```

```python id="4HNZQwTn0Bcx" colab_type="code" colab={}
type(napis)
```

```python id="n94zQQDx0Bc4" colab_type="code" colab={}
napis[1:4]
```

```python id="gd1RHweT0BdA" colab_type="code" colab={}
n = 'ala ma kota'
len(n) # liczba znaków w tekście
```

```python id="3gYnr4l90BdI" colab_type="code" colab={}
n.split()
```

<!-- #region id="nupos-OT_qxM" colab_type="text" -->
### Ćwiczenia e130
Sprawdź co się stanie jeśli dodasz do siebie dwa słowa
<!-- #endregion -->

```python colab_type="code" id="AeKGwHD3AVH-" colab={}
# ćwiczenie

```

<!-- #region colab_type="text" id="KSKRjbLh_9xN" -->
### Ćwiczenia e140
Oddziel typ pliku od jego nazwy np.  
obrazek.jpg > jpg
dane.xlsx > xlsx
<!-- #endregion -->

```python colab_type="code" id="kaIPNIleAVxe" colab={}
# ćwiczenie

```

<!-- #region id="Hq7k1dXT0Bdb" colab_type="text" -->
# Struktury danych w Pythonie
- listy - grupują wartości dowolnego typu (tekst, liczby, inne listy, ....)
    - tworzymy je uzywając kwadratowych nawiasow []
- tuples (krotki) - działają tak jak listy, ale sa niezmienialne (immutable)
    - tworzymy je uzywając nawiasów okrąglych () 

<!-- #endregion -->

<!-- #region id="ucaxKPNJ0Bdd" colab_type="text" -->
- slowniki - grupują wartości typu klucz-wartość
    - tworzymy je używając nawiasów {}
- sety
    - tworzone przy uzyciu słowa kluczowego **set**
    - używamy nawiasów **{}**

Metody dostepne w przypadku struktur danych sa w wiekszosci wypadkow podobne.
Na przydlad len() pokaże nam dlugość zarówno listy, tupli jak i setu.
<!-- #endregion -->

<!-- #region id="AnL8AjLO0Bdg" colab_type="text" -->
## Listy i tuple
<!-- #endregion -->

```python id="3PITxa-L0Bdj" colab_type="code" colab={}
lista = [] #pusta lista
lista_2 = [3, ["inna", "lista"],"a", lista]
```

```python id="Di-_qmOs0Bd_" colab_type="code" colab={}
lista.append(15)
lista.append('slowo')
lista
```

```python id="5STPVhhI0BeQ" colab_type="code" colab={}
# możemy wybrać jeden lub więcej elementów z listy
lista_2[0] 
```

```python id="eZvVl_Kwx1ER" colab_type="code" colab={}
# usuwanie elementu z listy 
print(lista)
del lista[1]
```

```python id="GN_9BL97yT1R" colab_type="code" colab={}
print(lista)
```

```python id="UMfTTbV50Bds" colab_type="code" colab={}
tupla = (3, 7, 9)
```

```python id="h91a1aH00Bdy" colab_type="code" colab={}
#roznice miedzyy listą i tuplą - tupli nie można zmienic
tupla.append(10)
```

```python id="Tqcdn6Z40BeY" colab_type="code" colab={}
"""Dostęp do elementów listy lub tupli mamy uzywając ich indeksow w nawiasach [],  
lub tnąc liste na kawałki używająć indeksów w nawiasach [] i ':' 
"""""
lista_3  = ["zmienna_1", 2, 3.14]

print(lista_3[0])   # elementy listy numerujemy od '0'
print(lista_3[0:2])
print(lista_3[-1])
print(lista_3[1:])
print(lista_3[::2])
print(len(lista_3))  # dlugosc listy
```

```python id="yD3sh6K00Bef" colab_type="code" colab={}
# po liście można też iterować for -- dostajemy wtedy jej elementy
for element in lista_3:
    print(element)
```

```python id="rm3MzcY-0Bem" colab_type="code" colab={}
# lista list
koszyk = [['mleko', 'ser'], ['chleb', 'bulki','rogaliki'], [3, 7, 6]]
```

```python id="XLNoaRum0Bez" colab_type="code" colab={}
koszyk[1][0]
```

<!-- #region id="KZxh_1Ds0Be6" colab_type="text" -->
### Ćwiczenia e150
stwórz listę zadań do wykonania i wydrukuj jej trzeci element
<!-- #endregion -->

```python colab_type="code" id="HkeV-tDt_P1J" colab={}
# ćwiczenie

```

<!-- #region id="4prQP1Gz0BcX" colab_type="text" -->
### Ćwiczenia e160

Napisz listę zakupow z cenami produktów, a nastepnie policz i wyswietl całkowity koszt.  
burak 2  
kaczka 4.5  
total 6.5
<!-- #endregion -->

```python id="QpZbvIja-yVa" colab_type="code" colab={}
# ćwiczenie

```

<!-- #region id="FnRL3SUr0Be7" colab_type="text" -->
## Słowniki

Słownik to kolekcja różnych elementów w którek każdy element ma klucz i odpowiadającą mu wartość.
To tak mini baza danych.
<!-- #endregion -->

```python id="11fd8Id40Be9" colab_type="code" colab={}
slownik= {}  #pusty slownik
slownik = dict()  #pusty slownik

slownik = {"klucz": "zmienna", 2: 3, "pi": 3.14}
slownik['klucz']
```

```python id="nIpN_uiB0BfF" colab_type="code" colab={}
slownik["pi"] = 3.15 #tak zmieniamy wartosc zmiennych w slowniku
slownik['pi']
```

```python id="pfThJVSqCtVD" colab_type="code" colab={}
import requests
response = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/chf/')
response.json()
```

<!-- #region id="j7rxX9x7Cqq4" colab_type="text" -->
### Ćwiczenia e170
wydrukuj symbol waluty, datę i  jej kurs:

USD, 2020-04-02, 3.85

<!-- #endregion -->

```python colab_type="code" id="Zx-6h3S4_OdJ" colab={}
# ćwiczenie

```

<!-- #region id="PwUzKsxi0BfL" colab_type="text" -->
# Instrukcje sterujące

W życiu często podejmujemy decyzje w zależności od sytuacji.  
W programowaniu też mamy taką możliwość i służą do tego instrukcje sterujące.
- if
- for 
- while 
<!-- #endregion -->

```python id="01X2cYCb0Bfy" colab_type="code" colab={}
jestem_glodny = input('jestes glodny?\n')

if jestem_glodny == 'tak':
    print('pizza')
```

```python id="ewkr6wPu36_v" colab_type="code" colab={}
jestem_glodny = input('jestes glodny?\n')

if jestem_glodny == 'tak':
    print('pizza')
    
elif jestem_glodny == 'nie':
    print('to popij')
```

```python id="8dx21QUo37XR" colab_type="code" colab={}
jestem_glodny = input('jestes glodny?\n')

if jestem_glodny == 'tak':
    print('pizza')
    
elif jestem_glodny == 'nie':
    print('to popij')
    
else:
    print('nie odpowiadasz? nie wiem co robić')
```

```python id="BNIjrYYV0BfX" colab_type="code" colab={}
lista_4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in lista_4:             # pętla for powtarza wielokrotnie tę samą operację
    if element in (3, 4, 7, 9):   #if sprawdza czy jakas zaleznosc jest prawdziwa
        print(element)
    else:
        print('co to jest??')
```

```python id="SA0uXNFR0BfN" colab_type="code" colab={}
# możemy użyć funkcji range(n), żeby wygenerować ciąg kolejnych liczb
for liczba in range(5):
    print(liczba)
```

```python id="OvCxtKz40Bfh" colab_type="code" colab={}
i = 0
while i < 6:
    print('dawaj jeszcze')
    i +=1
```

<!-- #region id="b1tva_j10Bf5" colab_type="text" -->
###  Ćwiczenia e180
zapytaj użytkownika o coś i wydrukuj różne komunikaty w zależności od odpowiedzi
<!-- #endregion -->

```python colab_type="code" id="jW8IwCWt_Yz6" colab={}
# ćwiczenie

```

<!-- #region id="_Q2MxC7a0Bf6" colab_type="text" -->
# Funkcje
Funkcje to fragmenty kodu, które nakazują Pythonowi wykonać jakieś zadanie.
Zalety tworzenia funkcji to:
- wieloktorne wykorzystanie tego samego kawałka kodu! 
- budowa złożonych programów, z prostszych do przeanalizowania oraz napisania elementów
- czytelność

Funkcje składają się z trzech elementów:
- nazwy funkcji
- jej parametrów (tego co funkcja od nas otrzyma)
- bloku kodu


<!-- #endregion -->

```python id="VQh5fdrI0Bf9" colab_type="code" colab={}
#definicja funkcji (tworzy funkcje, ale jej nie wywołuje)
def wielkie_litery(napis):
    wielki_napis = napis.upper()
    return wielki_napis

#wywołanie funkcji
wielkie_litery('kot')
```

```python id="FlJdxTur0BgC" colab_type="code" colab={}
def kwadrat(x):
    return x*x

print(kwadrat(5))
```

<!-- #region id="0VGbtr-xFYz6" colab_type="text" -->
### Ćwiczenia e190
Napisz funkcję która zwróci żart z podanym jej słowem ze strony https://api.chucknorris.io/ lub napisze, że żart z tym słowem nie istnieje.
<!-- #endregion -->

```python id="dK93YQqQEcOO" colab_type="code" colab={}
# ćwiczenie
```

<!-- #region id="RUGX-37P0BgH" colab_type="text" -->
### Ćwiczenia e200

stwórz funkcję która pyta o miasto zamieszkania i podaje fikcyjną pogodę
<!-- #endregion -->

```python colab_type="code" id="IbQvVoEM_b1J" colab={}
# ćwiczenie

```

<!-- #region id="bYUidAU20BgJ" colab_type="text" -->
# Moduły

Moduły (biblioteki) to programy pythona które zawierają kodu (funkcje, klasy itp), który możemy wykorzystać.
Najpierw jednak musimy je zaimportować po prostu używająć slowa 'import'.  
Aby wykorzystać jakąś funkcję zdefiniowaną w zaimportowanym module,   musimy
przed nazwą funkcji dołączyć nazwę modułu. 
<!-- #endregion -->

```python id="mH4g90_l0BgK" colab_type="code" colab={}
import random #modul z funkcjami związanymi z losowością (liczby losowe, losowy wybór elementów z listy itp.)

losowa_liczba = random.randint(1, 100)
print(losowa_liczba)
```

<!-- #region colab_type="text" id="XTugz_YkAI1a" -->
### Ćwiczenia e210
Swórz wirtualną kostkę do gry i zasymuluj dwa rzuty.

<!-- #endregion -->

```python colab_type="code" id="rvExwpmlAEoS" colab={}
# ćwiczenie

```

```python colab_type="code" id="VuuhrL2jA4U1" colab={}
# ćwiczenie

```

<!-- #region colab_type="text" id="dFIu7cQUA0lC" -->
### Ćwiczenia e220
Stwórz funkcję liczącą powierzchnie koła o danej średnicy

<!-- #endregion -->

```python colab_type="code" id="BlAnjJXUAxDF" colab={}
# ćwiczenie

```

<!-- #region id="HhvuB2TMF05U" colab_type="text" -->
# Błędy 
<!-- #endregion -->

<!-- #region id="hz131McQO6re" colab_type="text" -->
### Ćwiczenia e230
Co tu jest nie tak?
<!-- #endregion -->

```python id="g6VPZsTwF3Jg" colab_type="code" colab={}
print('blad)
```

```python id="HP554sBrF4rC" colab_type="code" colab={}
pizza(salami)
```

```python id="BbTjSOlCGDvq" colab_type="code" colab={}
def pizza(skladnik):
  return f'dzisiaj pizza z {skladnik}'

```

```python id="g9Y29xy-Gkzn" colab_type="code" colab={}
pizza()
```

```python id="RrLCw3-mGUZ_" colab_type="code" colab={}
def szczekaj()
  return 'hau, hau'


```

```python id="h655bCEpG95l" colab_type="code" colab={}
def dzielenie(a, b):
  return a/b
```

```python id="s01-Wgz2HO7N" colab_type="code" colab={}
dzielenie(4, 0)
```

<!-- #region id="pGtpPGbw0Bgg" colab_type="text" -->
# Zajęcia praktyczne
<!-- #endregion -->

<!-- #region id="Z8inm7yd0Bgi" colab_type="text" -->
## Praca z plikami tekstowymi

Praca z plikami w Pythonie jest bardzo prosta.  
**open(name, mode)** zwraca obiekt z plikiem:
- name - ścieżka do pliku
- mode:  
    'r' (read): otwieramy tylko do odczytu   
    'w' (write): otwieramy tylko do pisania  
    'a' (append): otwieramy do dopisywania (następne linijki)  
<!-- #endregion -->

```python id="MEbgelAZHXda" colab_type="code" colab={}
!wget -O plik.txt https://www.w3.org/TR/PNG/iso_8859-1.txt 
```

```python id="i6DHuN_Q0Bgj" colab_type="code" colab={}
with open('plik.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
```

```python id="RqzO_fDk0Bgr" colab_type="code" colab={}
with open('plik.txt', 'r') as f:
    for linia in f:
        print(linia)
        break
```

```python id="9Ct_e8A20Bg3" colab_type="code" colab={}
with open('plik.txt', 'w') as f:
  f.write('dziala to nasze pisanie, czy nie?')
```

```python id="Use2Bevj0Bg6" colab_type="code" colab={}
with open('plik.txt','r') as f:
    print(f.read())
```

<!-- #region colab_type="text" id="l5pWCOvo-03u" -->
### Ćwiczenia e240

Dodaj jeszcze jakiś tekst do naszego pliku.
<!-- #endregion -->

```python colab_type="code" id="nXeU-BSg_FjO" colab={}
# ćwiczenie

```

<!-- #region id="QCKqhBgdHEmE" colab_type="text" -->
## Praca z plikami
<!-- #endregion -->

```python id="2XjMx9GAOtC1" colab_type="code" colab={}
# zmieniamy nazwy wszystkich plikow w folderze
import os

i = 1
folder = '/content/sample_data/'

for filename in os.listdir(folder):
  plik = folder+filename
  rozszerzenie = filename.split('.')[1]
  new_name ="kurs_" + str(i)+'.'+ rozszerzenie
  os.rename(plik, folder+new_name) 
  i += 1
```

```python colab_type="code" id="sxIwQRK1_JPd" colab={}
# ćwiczenie

```

<!-- #region id="KHlrgx_BS8Y4" colab_type="text" -->
## API
<!-- #endregion -->

```python id="JcXyqUtdS_u5" colab_type="code" colab={}
import requests

r = requests.get("https://api.adviceslip.com/advice")
content = r.json()
print(content)
```

<!-- #region id="DCtAwAXW7wG_" colab_type="text" -->
### Ćwiczenia e250
Wydrukuj porade dotyczącą X
<!-- #endregion -->

```python id="FyawSvv_7wxG" colab_type="code" colab={}
# ćwiczenie

```

<!-- #region id="a2yqt25h0BhT" colab_type="text" -->
# Klasy
Python jest całkowicie zorientowany obiektowo: możemy zarówno korzystać z wbudowanych klas jak i tworzyć własne klasy.

Tworzenie klas w Pythonie jest proste. Po prostu definiujemy klasę i zaczynamy ją stosować.  
Klasa w Pythonie rozpoczyna się słowem kluczowym **class**, po którym następuje nazwa klasy , która zwyczajowo pisana jest z dużej litery.
<!-- #endregion -->

```python id="NSFwOD4y0BhU" colab_type="code" colab={}
class Pies():
    def __init__(self, rasa):
        self.najwiekszy_wrog = 'kot'
        self.nogi = 4
        self.rasa = rasa

    def zaszczekaj(self):
        print('hau, hau')
        
    def zjedz(self, nastroj):
        if nastroj == 'wesoly':
          print('macham ogonem')
        elif nastroj == 'zly':
          print('gryzę')
        else:
          print('idę spać')


```

```python id="N7fuUlzB0BhX" colab_type="code" colab={}
rudy = Pies('wilczur')
rudy.rasa
```

```python id="lcjdbWPl0Bhh" colab_type="code" colab={}
rudy.zaszczekaj()
```

<!-- #region colab_type="text" id="o9Dndv-cdKKK" -->
### Ćwiczenia e260
Stwórz własnego psa i spraw, żeby pomachał ogonem

<!-- #endregion -->

```python colab_type="code" id="BrgR3G_R_NCV" colab={}
# ćwiczenie

```

<!-- #region id="VfsRDugJH-wT" colab_type="text" -->
# Crazy staff
<!-- #endregion -->

```python id="ynKZfdgk_Dcv" colab_type="code" colab={}
!pip install geopy
```

```python id="UIfqySKuIAf0" colab_type="code" colab={}
# spawdzamy długość i szerokość geograficzną jakiegoś adresu

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
adres = "Francuska 2/4, Warszawa"
print("Adres:", adres)
location = geolocator.geocode(adres)
print(f"Długość i szerokość geograficzna: {location.latitude, location.longitude}")
```

<!-- #region colab_type="text" id="v0ssEIjIfYDP" -->
### Ćwiczenia e270
Porównaj szerokość geograficzną Nowego Jorku i Warszawy
<!-- #endregion -->

```python colab_type="code" id="v7DZZ7E3_OxV" colab={}
# ćwiczenie

```

<!-- #region id="5aL9L6FhcgrR" colab_type="text" -->
# Własny strona AI z rozpoznawaniem wieku
<!-- #endregion -->

```python id="QkTkAjZacZJq" colab_type="code" colab={}
!pip install flask-ngrok
```

```python id="BkiUwbOoWKze" colab_type="code" colab={}
from flask_ngrok import run_with_ngrok
from flask import Flask
import random

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run

@app.route("/")
def home():
    return "<h1>API documentation</h1><p> <b>GET /age</b> przewiduje ile masz lat</p>"

@app.route('/age', methods=['GET'])
def age():
    return str(random.randint(1, 100))
  
app.run()
```

<!-- #region colab_type="text" id="Bkg-3MU6_cjO" -->
# Egzamin końcowy e280

 Randomly generate a 4-digit number.  
 Ask the user to guess a 4-digit number. 

> For every digit that the user guessed correctly in the correct place, they have a “cow”.  
 For every digit the user guessed correctly in the wrong place is a “bull”  
 Every time the user makes a guess, tell them how many “cows” and “bulls” they have.  
 Once the user guesses the correct number, the game is over.  

 Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
   
** Say the number generated by the computer is 1038. An example interaction could look like this:** 
```
   Welcome to the Cows and Bulls Game! 
   Enter a number: 
   >>> 1234
   2 cows, 0 bulls
   >>> 1256
   1 cow, 1 bull
   ...
```
<!-- #endregion -->

```python id="8vdMPnEDUFUd" colab_type="code" colab={}
import random
print('welcome to cows and bulls game!\n\n')

ilosc_prob = 0
cows = 0
bulls = 0

do_odgadniecia = '1234' #str(random.randint(1000, 9999))

while True:

  cows = 0
  bulls = 0
  zgadywanie = input('podaj czterocyfrowy numer:  ')
  
  if zgadywanie == 'q':
    print('dziękuję za grę')
    break
  
  for i in range(len(zgadywanie)):
    if zgadywanie[i] == do_odgadniecia[i]:
      bulls += 1
    elif zgadywanie[i] in do_odgadniecia:
        cows += 1

  print('bulls: ', bulls)
  print('cows: ', cows)
  ilosc_prob += 1

  if bulls == 4:
    print('proby', ilosc_prob)
    print('wygrales')
    break
```

<!-- #region id="ch0aTqKW9eHp" colab_type="text" -->
# Bonus


<!-- #endregion -->

```python id="YtkMoZhyEjbN" colab_type="code" colab={}
# online materials

https://snakify.org/en/lessons/print_input_numbers/


```
