import random
import math
import os

def czysc_konsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def poziom_trudnosci():
    while True:
        try:
            poziom_trudnosci_wybor = int(input("Wybierz poziom trudności: \n1 - Łatwy \n2 - Normalny \n3 - Trudny\n"))
            if poziom_trudnosci_wybor == 1:
                return 3
            elif poziom_trudnosci_wybor == 2:
                return 1
            elif poziom_trudnosci_wybor == 3:
                return 0
            else:
                print("Błąd: Podaj liczbę 1, 2 lub 3.")
        except ValueError:
            print("Błąd: Upewnij się, że podałeś liczbę całkowitą.")

def setup():
    while True:
        try:
            dane = input("Podaj zakres (np: 1-100): ")
            liczba1, liczba2 = map(int, dane.split('-'))
            if liczba1 < liczba2:
                break
            else:
                print("Błąd: Pierwsza liczba musi być mniejsza od drugiej. Spróbuj ponownie.")
        except ValueError:
            print("Błąd: Upewnij się, że podałeś dwie liczby całkowite oddzielone znakiem '-'.")

    numer_to_guess = random.randint(liczba1, liczba2)  # Losowanie liczby w pełnym zakresie
    poziom_trudnosci_w = poziom_trudnosci()
    choices = int(math.log2(liczba2 - liczba1 + 1)) + poziom_trudnosci_w
    czysc_konsole()
    print(f"Zakres do zgadywania to {liczba1}-{liczba2}.\nMasz {choices} prób, żeby zgadnąć!")

    return numer_to_guess, choices

def game():

    while True:
        czysc_konsole()
        print('Witam w grze "Zgadnij liczbę"! Twoim zadaniem jest odgadnięcie liczby, którą wylosowałem.')

        numer_to_guess, choices = setup()
        gueses_counter = 0

        while gueses_counter < choices:
            gueses_counter += 1
            try:
                my_guess = int(input(f'Próba {gueses_counter}. Podaj liczbę: '))
            except ValueError:
                print("Błąd: Proszę podać liczbę całkowitą.")
                continue

            if my_guess == numer_to_guess:
                print(f'Zgadłeś! Moja liczba to {numer_to_guess}. Zajęło Ci to {gueses_counter} prób!')
                break
            elif my_guess > numer_to_guess:
                print('Liczba jest za duża')
            elif my_guess < numer_to_guess:
                print('Liczba jest za mała')

            if gueses_counter == choices:
                print(f'Przegrałeś! Moja liczba to {numer_to_guess}. Powodzenia następnym razem!')
        
        play_again = input('Chcesz zagrać ponownie? (y/n): ')
        if play_again.lower() != 'y':
            break

game()
