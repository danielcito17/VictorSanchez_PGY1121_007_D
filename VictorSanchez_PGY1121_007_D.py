import Funciones as fn

while True:
    fn.mostrar_menu()
    opcion =  fn.validar_opcion()
    if opcion == 1:
        fn.comprar_entradas()
    elif opcion == 2:
        fn.ver_escenario()
    elif opcion == 3:
        fn.buscar()
    elif opcion == 4:
        fn.ganancias()
    else:
        print("Victor sanchez, 06/07/2023")