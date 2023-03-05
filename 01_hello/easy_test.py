
import random

number = random.randint(1, 100)
guesses_left = 5

print("Zgadnij liczbę od 1 do 100. Masz 5 prób.")

while guesses_left > 0:
    guess = int(input("Podaj swoją próbę: "))
    guesses_left -= 1
    
    if guess == number:
        print("Brawo! Zgadłeś liczbę.")
        break
    elif guess < number:
        print("Za mało. Spróbuj ponownie.")
    else:
        print("Za dużo. Spróbuj ponownie.")

if guesses_left == 0:
    print("Nie udało Ci się zgadnąć liczby. Była to liczba", number)
