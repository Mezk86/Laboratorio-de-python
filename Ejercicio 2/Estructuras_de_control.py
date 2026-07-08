# MÓDULO 2: Bucle principal y lógica de toma de decisiones

sectores = {
    "VIP": {"precio": 50000, "capacidad": 50, "vendidas": 0},
    "PLATEA": {"precio": 30000, "capacidad": 100, "vendidas": 0},
    "GENERAL": {"precio": 15000, "capacidad": 200, "vendidas": 0}
}

recaudacion_total = 0.0


def mostrar_menu():
    print("\n1. Vender | 2. Estadísticas | 3. Salir")


def mostrar_sectores():
    print("\nSectores disponibles:")
    for nombre, datos in sectores.items():
        print(f"- {nombre}: ${datos['precio']} | Disponibles: {datos['capacidad']}")


def aplicar_descuento(total, cantidad):
    if cantidad >= 4:
        descuento = total * 0.10
        print("Descuento del 10% aplicado.")
        return total - descuento
    print("Sin descuento aplicado.")
    return total


def registrar_venta_archivo(sector, cantidad, total):
    with open("historial_ventas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{sector},{cantidad},{total}\n")


while True:
    mostrar_menu()
    opcion = input("Seleccione opción: ").strip()

    if opcion == '1':
        mostrar_sectores()
        sector = input("Sector: ").strip().upper()

        if sector not in sectores:
            print("Sector no encontrado.")
            continue

        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            continue

        if cantidad > sectores[sector]["capacidad"]:
            print(f"Capacidad insuficiente. Solo quedan {sectores[sector]['capacidad']} entradas.")
            continue

        subtotal = sectores[sector]["precio"] * cantidad
        total_pagar = aplicar_descuento(subtotal, cantidad)

        sectores[sector]["capacidad"] -= cantidad
        sectores[sector]["vendidas"] += cantidad
        recaudacion_total += total_pagar
        registrar_venta_archivo(sector, cantidad, total_pagar)

        print(f"Venta exitosa. Total a pagar: ${total_pagar:,.2f}")

    elif opcion == '2':
        print("\nEstadísticas")
        print(f"Recaudación total: ${recaudacion_total:,.2f}")
        for nombre, datos in sectores.items():
            print(f"- {nombre}: {datos['vendidas']} entradas vendidas")

    elif opcion == '3':
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")