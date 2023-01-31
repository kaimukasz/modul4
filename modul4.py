ZADANIE: PALINDROMY

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
