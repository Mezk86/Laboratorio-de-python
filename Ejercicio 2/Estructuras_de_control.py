# MÓDULO 2: Bucle principal y lógica de toma de decisiones
while True:
    print("\n1. Vender | 2. Estadísticas | 3. Salir")
    opcion = input("Seleccione opción: ")
    
    if opcion == '1':
        # Ejemplo de condicional para validar entrada de usuario
        sector = input("Sector: ").upper()
        if sector in sectores:
            # Lógica de negocio (descuentos)
            cantidad = int(input("Cantidad: "))
            if cantidad >= 4:
                print("Descuento del 10% aplicado.")
        else:
            print("Sector no encontrado.")
    elif opcion == '3':
        break # Salida del bucle