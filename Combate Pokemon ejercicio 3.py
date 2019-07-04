

pokemon_elegido = input('¡Escoge un contrincante!   (Charmander / Squirtle / Bulbasaur): ')

vida_Pikachu = 100
vida_enemigo = 0


if pokemon_elegido == 'Squirtle':
    vida_enemigo = 90
    nombre_pokemon = 'Squirtle'
    ataque_enemigo = 12
elif pokemon_elegido == 'Charmander':
    vida_enemigo = 80
    nombre_pokemon = 'Charmander'
    ataque_enemigo = 14
elif pokemon_elegido == 'Bulbasaur':
    vida_enemigo = 100
    nombre_pokemon = 'Bulbasaur'
    ataque_enemigo = 10
else:
    print('Sin enemigo no hay combate')

while vida_Pikachu > 0 and vida_enemigo > 0:
    ataque_pikachu = input('¡Da una orden! (Chispazo/Vola Boltio): ')
    if ataque_pikachu == 'Chispazo':
        vida_enemigo -= 10
    if ataque_pikachu == 'Bola Voltio':
        vida_enemigo -= 12


    print('¡Pikachu ataca!'
          'La vida del {} enemigo es de {}'.format(nombre_pokemon, vida_enemigo))

    print('{} te hace {} puntos de daño'.format(nombre_pokemon, ataque_enemigo))
    vida_Pikachu -= ataque_enemigo

    print('La vida de Pikachu es de {}'.format(vida_Pikachu))


if vida_enemigo <= 0:
    print('¡Has ganado!')
if vida_Pikachu <= 0:
    print('Has perdido')



print('El combate ha terminado')