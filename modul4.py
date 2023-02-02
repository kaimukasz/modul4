# ZADANIE: PALINDROMY

print("Program sprawdzajacy czy slowo jest palindromem")
def czyPalindrom(x):
    x = x.lower().replace(" ", "")
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
    return True
print("Podaj słowo : ")
word = input()
print("Podane slowo " + ("jest " if(czyPalindrom(word)) else "nie jest ") + "palindromem")



# ZADANIE: KALKULATOR

import logging
logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
log = logging.getLogger(__name__)

kalk = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))

if kalk == "1":
    log.info('Komunikat informacyjny')
    c = float(input("Podaj składnik 3: "))
    log.info(f"Dodaję {a}, {b} i {c}")
    log.info("Wynik to", a + b + c)
elif kalk == "2":
    log.info(f"Odejmuję {a} i {b} ")
    log.info("Wynik to", a - b)
elif kalk == "3":
    c = float(input("Podaj składnik 3: "))
    log.info(f"Mnożę {a}, {b} i {c}")
    log.info("Wynik to", a * b * c)
elif kalk == "4":
    log.info("Dzielę {a} i {b} ")
    log.info("Wynik to", a / b)
else:
    log.info("koniec")