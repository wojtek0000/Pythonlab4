class PiContainer:
    def __init__(self):
        self.a = []

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def foo(x):
    b = 0
    c = 1
    for i in range(x):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def my_enumerate(pi: PiContainer):
    for element in pi.a:
        print(element)


#print('All functions are defined')

#1. Usunięcie wejściowego argumentu a, z metody inicjalizującej __init__, oraz dodanie pustej listy
#2. Niepotrzebna deklaracja zmiennych b i c na początku pliku, oraz deklaracja jako global w foo()
#3. Deklaracja zapisana na 2 różne sposoby (spacje, oraz bez)
#4. W pętlach for używamy nazw niepasujących do wykonywanej funkcji (hello)
#5. Zbyt długi komentarz
#6. Usunięcie yield 'finished'
#7. Niepotrzebny komunikat All functions are defined
#8. Zmiana nazwy hello na element
#9. Zmiana nazwy funkcji enumerate, na my_enumerate, aby nie było kolizji nazw z funkcją wbudowaną enumerate()
#10. Zmiana nazwy klasy na zaczynającą się z wielkiej litery i bez znaków specjalnych
#11. Między definicjami funckji powinny być 2 linie odstępu, a nie 1