
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" align="center" width='500'>

# Python
to jeden z najpopularniejszych i najlatwiejszych do nauczenia się języków programowania.  
Kod w języku Python jest krótki i czytelny, nie pozostawia wątpliwości co do sposobu działania.  
Dodatkowy bonus - jest to język nauki i sztucznej inteligencji :-)


```python
!git clone https://github.com/ajankowski/python_tiny_workshop.git
```


```python
mv /content/python_tiny_workshop/solutions.yaml /content
```


```python
%run /content/python_tiny_workshop/solutions.py
```


```python
hint('e220', 1)
```

## Syntax (struktura, uporządkowanie słów w zdaniu - gramatyka Pythona)
- Bloki kodu oddzielone są wcięciami (stosuje się 4 spacje, nie jest to konieczne, ale musimy być konsekwentni, tzn. kolejne wcięcia muszą być takie same, linia bez wcięcia znajdować się będzie poza blokiem).
- Wyrażenia które wymagają wcięć zakończone są dwukropkiem **:**
- Ważna jest wielkość liter.
- Komentarze w kodzie zaczynamy od znaku #


```python
print('hello world')
```


```python
!wget 
```

# Zmienne
Zmienna = miejsce, gdzie komputer przechowuje dane  
Zmienne przypisujemy do nazw znakiem rowności '='  , a testujemy czy dane są równe znakiem '=='  


```python
kot = 3
pies = 7

```


```python
kot + pies
```


```python
kot == 3
# kot == pies
```


```python
# wszystko od '#' do końca wiersza to komentarz (Python go pomija)
napis_1 = 'hallo'
napis_2 = "world!"

napis_3 = napis_1 + napis_2 # komentarz może zacząć się nie-na-początku wiersza
```


```python
print(napis_3)
```


```python
#  możemy też wyświetlać dłuższy tekst
print('''dłuższy tekst
w kilku 
linijkach''')
```


```python
print('lecimy dalej)
```


```python
# czasem program odmówi działania i pokaże nam błąd :-)
```

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


```python
# mozemy sprawdzić czy jakaś liczba dzieli sie przez inną 
8%3
```


```python
print('reszta z dzielenia 8/3 -> ' + str(8%3))
```


```python
imie = input('jak masz na imie? ')
print('hej '+ imie)
```

### Ćwiczenia e110

Poproś uzytkownika o wprowadzenie jakiejś cyfry i wydrukuj wynik mnożenia jej przez 3


```python
# ćwiczenie

```

### Ćwiczenia e120

Poproś uzytkownika o wprowadzenie imienia i wieku, odpowiedz mu w którym roku będzie miał 100 lat.  

Oczekiwany wynik dla Bartka, 33 lata:  
'Bartek będziesz miał sto lat w 2053 roku'


```python
# ćwiczenie
```

# Typy danych

W pythonie mamy dostępne kilka typów danych, podstawowe z nich to:   
- *int* - (integer) -liczby całkowite:  -99, -98,..., -2, -1, 0, 1, 2, ..., 98  
- *float* - floating point -liczby rzeczywiste (zmiennoprzecinkowe):  0.2, 3.14, -0.8897  
- *str* - tekst (string), tekstem jest dowolne wyrażenie w cudzysłowie pojedynczym lub podwójnym: 'python' lub "python"


```python
liczba_calkowita = 6
liczba_rzeczywista = 0.56
```


```python
type(liczba_calkowita)
type(liczba_rzeczywista)
```


```python
napis = 'kuble'
```


```python
type(napis)
```


```python
napis[1:4]
```


```python
n = 'ala ma kota'
len(n) # liczba znaków w tekście
```


```python
n.split()
```

### Ćwiczenia e130
Sprawdź co się stanie jeśli dodasz do siebie dwa słowa


```python
# ćwiczenie

```

### Ćwiczenia e140
Oddziel typ pliku od jego nazwy np.  
obrazek.jpg > jpg
dane.xlsx > xlsx


```python
# ćwiczenie

```

# Struktury danych w Pythonie
- listy - grupują wartości dowolnego typu (tekst, liczby, inne listy, ....)
    - tworzymy je uzywając kwadratowych nawiasow []
- tuples (krotki) - działają tak jak listy, ale sa niezmienialne (immutable)
    - tworzymy je uzywając nawiasów okrąglych () 


- slowniki - grupują wartości typu klucz-wartość
    - tworzymy je używając nawiasów {}
- sety
    - tworzone przy uzyciu słowa kluczowego **set**
    - używamy nawiasów **{}**

Metody dostepne w przypadku struktur danych sa w wiekszosci wypadkow podobne.
Na przydlad len() pokaże nam dlugość zarówno listy, tupli jak i setu.

## Listy i tuple


```python
lista = [] #pusta lista
lista_2 = [3, ["inna", "lista"],"a", lista]
```


```python
lista.append(15)
lista.append('slowo')
lista
```


```python
# możemy wybrać jeden lub więcej elementów z listy
lista_2[0] 
```


```python
# usuwanie elementu z listy 
print(lista)
del lista[1]
```


```python
print(lista)
```


```python
tupla = (3, 7, 9)
```


```python
#roznice miedzyy listą i tuplą - tupli nie można zmienic
tupla.append(10)
```


```python
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


```python
# po liście można też iterować for -- dostajemy wtedy jej elementy
for element in lista_3:
    print(element)
```


```python
# lista list
koszyk = [['mleko', 'ser'], ['chleb', 'bulki','rogaliki'], [3, 7, 6]]
```


```python
koszyk[1][0]
```

### Ćwiczenia e150
stwórz listę zadań do wykonania i wydrukuj jej trzeci element


```python
# ćwiczenie

```

### Ćwiczenia e160

Napisz listę zakupow z cenami produktów, a nastepnie policz i wyswietl całkowity koszt.  
burak 2  
kaczka 4.5  
total 6.5


```python
# ćwiczenie

```

## Słowniki

Słownik to kolekcja różnych elementów w którek każdy element ma klucz i odpowiadającą mu wartość.
To tak mini baza danych.


```python
slownik= {}  #pusty slownik
slownik = dict()  #pusty slownik

slownik = {"klucz": "zmienna", 2: 3, "pi": 3.14}
slownik['klucz']
```


```python
slownik["pi"] = 3.15 #tak zmieniamy wartosc zmiennych w slowniku
slownik['pi']
```


```python
import requests
response = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/chf/')
response.json()
```

### Ćwiczenia e170
wydrukuj symbol waluty, datę i  jej kurs:

USD, 2020-04-02, 3.85



```python
# ćwiczenie

```

# Instrukcje sterujące

W życiu często podejmujemy decyzje w zależności od sytuacji.  
W programowaniu też mamy taką możliwość i służą do tego instrukcje sterujące.
- if
- for 
- while 


```python
jestem_glodny = input('jestes glodny?\n')

if jestem_glodny == 'tak':
    print('pizza')
```


```python
jestem_glodny = input('jestes glodny?\n')

if jestem_glodny == 'tak':
    print('pizza')
    
elif jestem_glodny == 'nie':
    print('to popij')
```


```python
jestem_glodny = input('jestes glodny?\n')

if jestem_glodny == 'tak':
    print('pizza')
    
elif jestem_glodny == 'nie':
    print('to popij')
    
else:
    print('nie odpowiadasz? nie wiem co robić')
```


```python
lista_4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in lista_4:             # pętla for powtarza wielokrotnie tę samą operację
    if element in (3, 4, 7, 9):   #if sprawdza czy jakas zaleznosc jest prawdziwa
        print(element)
    else:
        print('co to jest??')
```


```python
# możemy użyć funkcji range(n), żeby wygenerować ciąg kolejnych liczb
for liczba in range(5):
    print(liczba)
```


```python
i = 0
while i < 6:
    print('dawaj jeszcze')
    i +=1
```

###  Ćwiczenia e180
zapytaj użytkownika o coś i wydrukuj różne komunikaty w zależności od odpowiedzi


```python
# ćwiczenie

```

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




```python
#definicja funkcji (tworzy funkcje, ale jej nie wywołuje)
def wielkie_litery(napis):
    wielki_napis = napis.upper()
    return wielki_napis

#wywołanie funkcji
wielkie_litery('kot')
```


```python
def kwadrat(x):
    return x*x

print(kwadrat(5))
```

### Ćwiczenia e190
Napisz funkcję która zwróci żart z podanym jej słowem ze strony https://api.chucknorris.io/ lub napisze, że żart z tym słowem nie istnieje.


```python
# ćwiczenie
```

### Ćwiczenia e200

stwórz funkcję która pyta o miasto zamieszkania i podaje fikcyjną pogodę


```python
# ćwiczenie

```

# Moduły

Moduły (biblioteki) to programy pythona które zawierają kodu (funkcje, klasy itp), który możemy wykorzystać.
Najpierw jednak musimy je zaimportować po prostu używająć slowa 'import'.  
Aby wykorzystać jakąś funkcję zdefiniowaną w zaimportowanym module,   musimy
przed nazwą funkcji dołączyć nazwę modułu. 


```python
import random #modul z funkcjami związanymi z losowością (liczby losowe, losowy wybór elementów z listy itp.)

losowa_liczba = random.randint(1, 100)
print(losowa_liczba)
```

### Ćwiczenia e210
Swórz wirtualną kostkę do gry i zasymuluj dwa rzuty.



```python
# ćwiczenie

```


```python
# ćwiczenie

```

### Ćwiczenia e220
Stwórz funkcję liczącą powierzchnie koła o danej średnicy



```python
# ćwiczenie

```

# Błędy 

### Ćwiczenia e230
Co tu jest nie tak?


```python
print('blad)
```


```python
pizza(salami)
```


```python
def pizza(skladnik):
  return f'dzisiaj pizza z {skladnik}'

```


```python
pizza()
```


```python
def szczekaj()
  return 'hau, hau'


```


```python
def dzielenie(a, b):
  return a/b
```


```python
dzielenie(4, 0)
```

# Zajęcia praktyczne

## Praca z plikami tekstowymi

Praca z plikami w Pythonie jest bardzo prosta.  
**open(name, mode)** zwraca obiekt z plikiem:
- name - ścieżka do pliku
- mode:  
    'r' (read): otwieramy tylko do odczytu   
    'w' (write): otwieramy tylko do pisania  
    'a' (append): otwieramy do dopisywania (następne linijki)  


```python
!wget -O plik.txt https://www.w3.org/TR/PNG/iso_8859-1.txt 
```


```python
with open('plik.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
```


```python
with open('plik.txt', 'r') as f:
    for linia in f:
        print(linia)
        break
```


```python
with open('plik.txt', 'w') as f:
  f.write('dziala to nasze pisanie, czy nie?')
```


```python
with open('plik.txt','r') as f:
    print(f.read())
```

### Ćwiczenia e240

Dodaj jeszcze jakiś tekst do naszego pliku.


```python
# ćwiczenie

```

## Praca z plikami


```python
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


```python
# ćwiczenie

```

## API


```python
import requests

r = requests.get("https://api.adviceslip.com/advice")
content = r.json()
print(content)
```

### Ćwiczenia e250
Wydrukuj porade dotyczącą X


```python
# ćwiczenie

```

# Klasy
Python jest całkowicie zorientowany obiektowo: możemy zarówno korzystać z wbudowanych klas jak i tworzyć własne klasy.

Tworzenie klas w Pythonie jest proste. Po prostu definiujemy klasę i zaczynamy ją stosować.  
Klasa w Pythonie rozpoczyna się słowem kluczowym **class**, po którym następuje nazwa klasy , która zwyczajowo pisana jest z dużej litery.


```python
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


```python
rudy = Pies('wilczur')
rudy.rasa
```


```python
rudy.zaszczekaj()
```

### Ćwiczenia e260
Stwórz własnego psa i spraw, żeby pomachał ogonem



```python
# ćwiczenie

```

# Crazy staff


```python
!pip install geopy
```


```python
# spawdzamy długość i szerokość geograficzną jakiegoś adresu

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
adres = "Francuska 2/4, Warszawa"
print("Adres:", adres)
location = geolocator.geocode(adres)
print(f"Długość i szerokość geograficzna: {location.latitude, location.longitude}")
```

### Ćwiczenia e270
Porównaj szerokość geograficzną Nowego Jorku i Warszawy


```python
# ćwiczenie

```

# Własny strona AI z rozpoznawaniem wieku


```python
!pip install flask-ngrok
```


```python
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

# Bonus



# online materials

https://snakify.org/en/lessons/print_input_numbers/


