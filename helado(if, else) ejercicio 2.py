apetece_helado_input = input('Te apetece un helado?  SI/NO = ').upper()
tiene_dinero_input = input('¿Tienes dinero para un helado?  SI/NO = ').upper()
esta_el_senor_helados_input = input('¿Esta el señor de los helados? SI/NO = ').upper()
esta_tu_tia_input = input('Estás con tu tía? SI/NO = ').upper()

apetece_helado = apetece_helado_input == 'SI'
tiene_dinero = tiene_dinero_input == 'SI'
esta_tu_tia = esta_tu_tia_input == 'SI'
esta_el_senor_helados = esta_el_senor_helados_input == 'SI'
puede_permitirselo = tiene_dinero or esta_tu_tia

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print('Pues comete un helado')
else:
    print('Pues nada')
