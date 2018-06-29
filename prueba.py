number_to_guess = 3

user_number = int(input('Adivina el numero: '))

if number_to_guess == user_number:
    print('Has ganado, ¡enhorabuena!')
else:
    otro_intento = int(input('Mala suerte, inténtalo otra vez: '))
    if otro_intento == number_to_guess:
        print('Has ganado, ¡enhorabuena!')
    else:
        otro_intento = int(input('Mala suerte, inténtalo otra vez: '))

        if otro_intento == number_to_guess:
            print('Has ganado, ¡enhorabuena!')
        else:
            otro_intento = int(input('Mala suerte, inténtalo otra vez: '))

            if otro_intento == number_to_guess:
                print('Has ganado, ¡enhorabuena!')
            else:
                otro_intento = int(input('Mala suerte, inténtalo otra vez: '))

                if otro_intento == number_to_guess:
                    print('Has ganado, ¡enhorabuena!')
                else:
                    print('Te has quedado sin intentos, has perdido')



