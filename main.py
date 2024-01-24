# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

#Deniss Žuravels

import random

a = 100
b = 1
c = 1

print("Welcome to circus")

i = 1
#tas skaita lai spēle bija maksimum 25 raundi
while i <= 25:
    print(i)
    i = i + 1
 
    #tas dara speletaja gālienu
    if a > b :
        print("You throw cube")
        user_throw = int(random.randint(1, 6))
        print("Your throw is:" + str(user_throw))
        b = b + user_throw
        print("You are on square:" + str(b))
        blue = [18, 80, 74]
        #tas parbauda vai speletajs trapeja uz ziles kapnes 
        for x in blue:
            if b == x:
                print("You are on blue ladder! You go to 11 cells ago!")
                b = b - 11
                print("You are on square:" + str(b))
        blues = [67]
        #tas parbauda vai speletajs trapeja uz ziles kapnes kas dara vairak ceļus atpakaļ
        for x in blue:
            if b == x:
                print("You are on blue ladder! You go to 21 cells ago!")
                b = b - 21
                print("You are on square:" + str(b))
        red = [15, 39, 87]
        #tas parbauda vai speletajs trapeja uz sarkanas kapnes 
        for y in red:
            if b == y:
                print("You are on red ladder! You go to 9 steps forward!")
                b = b + 9
                print("You are on square:" + str(b))
        reds = [33]
        #tas parbauda vai speletajs trapeja uz sarkanas kapnes kas dara vairak ceļus uz priekšu
        for y in red:
            if b == y:
                print("You are on red ladder! You go to 19 steps forward!")
                b = b + 19
                print("You are on square:" + str(b))
        #tas parbauda vai speletajs uzvareja
        if a <= b :
            print("You win!")
            break
    #tas dara kompjutera gālienu
    if a > c :
        print("Computer throw cube")
        computer_throw = int(random.randint(1, 6))
        print("Computer throw is:" + str(computer_throw))
        c = c + computer_throw
        print("Computer are on square:" + str(c))
        blue = [18, 80, 74]
        #tas parbauda vai speletajs trapeja uz ziles kapnes
        for x in blue:
            if c == x:
                print("Computer are on blue ladder! Computer go to 11 cells ago!")
                c = c - 11
                print("Computer are on square:" + str(c))
        blues = [67]
        #tas parbauda vai kompjuters trapeja uz ziles kapnes kas dara vairak ceļus atpakaļ
        for x in blue:
            if c == x:
                print("Computer are on blues ladder! Computer go to 21 cells ago!")
                c = c - 21
                print("Computer are on square:" + str(c))
        red = [15, 39, 87]
        #tas parbauda vai kompjuters trapeja uz sarkanas kapnes 
        for y in red:
            if c == y:
                print("Computer are on red ladder! Computer go to 9 steps forward!")
                c = c + 9
                print("Computer are on square:" + str(c))
        reds = [33]
        #tas parbauda vai kompjuters trapeja uz sarkanas kapnes kas dara vairak ceļus uz priekšu
        for y in red:
            if c == y:
                print("Computer are on reds ladder! Computer go to 19 steps forward!")
                c = c + 19
                print("Computer are on square:" + str(c))
        #tas parbauda vai kompjuters uzvareja
        if a <= c :
            print("Computer win!")
            break
#ja uzvaraja nav tad ir rakstits ka neizšķirts
else :
        print("Game over! It's a tie!")