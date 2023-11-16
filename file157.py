from file87 import *

try:
    my_pi = PiContainer()
    pi_gen = foo(5)
    my_pi.mth([i for i in list(pi_gen)])
    print('my first pi')
    my_enumerate(my_pi)
except:
    print('something went horribly wrong :(')

my_pi_2 = PiContainer()
pi_gen_2 = foo(2)
my_pi_2.mth([i for i in list(pi_gen_2)])
print('my second pi')
my_enumerate(my_pi_2)

my_pi_3 = PiContainer()
pi_gen_3 = foo(196)
my_pi_3.mth([i for i in list(pi_gen_3)])

new_file = open('some-file.txt', 'w')
new_file.write(f'my best pi: {my_pi_3.a[-1]}')
new_file.close()

#1. wywołanie funckji 7 razy w 7 liniach zamiast utworzenia pętli
#2. Zdefiniowanie my_pi_2 w try, który może się nie wykonać
#3. Za dużo wywołań metody mth (7), w porównaniu do argumentów wejściowych funkcji foo(5)
#4. Niewłaściwa nazwa "pIgEn3"
#5. Brak oddzieleń między linijkami, dla większej czytelności kodu
#6. Zbyt długa nazwa zmiennej "the_variable_that_contains_next_approximations_of_pi_from_generator"
#7. Użycie metody __next__, oraz next() i [i for i in list(pi_gen)], zamiast jednego
#8. Podwójna deklaracja funkcji enumerate, oraz nazwa tej funkcji taka sama jak funkcji wbudowanej enumerate()
#9. Aby wypisać najbardziej przybliżoną wartość pi w pliku, należy zmienić indeks na -2, bo -1 to "finished"
#10. Nazwa klasy powinna zaczynać się od wielkiej litery
