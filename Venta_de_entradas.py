import os

# ==========================================
# 1. ESTRUCTURAS DE DATOS (Variables Globales)
# ==========================================
# Diccionario para administrar los sectores, precios, capacidad y contadores de ventas.
sectores = {
    "VIP": {"precio": 50000, "capacidad": 50, "vendidas": 0},
    "PLATEA": {"precio": 30000, "capacidad": 100, "vendidas": 0},
    "GENERAL": {"precio": 15000, "capacidad": 200, "vendidas": 0}
}

# Acumulador global para la recaudación total
recaudacion_total = 0.0

# ==========================================
# 2. FUNCIONES Y MODULARIZACIÓN
# ==========================================

def mostrar_menu():
    """Imprime el menú principal del sistema."""
    print("\n" + "="*40)
    print("🎫 SISTEMA DE VENTA DE ENTRADAS 🎫")
    print("="*40)
    print("1. Vender entradas")
    print("2. Ver estadísticas de ventas")
    print("3. Salir del sistema")
    print("="*40)

def mostrar_sectores():
    """Muestra los sectores, sus precios y la capacidad disponible."""
    print("\n--- Sectores Disponibles ---")
    for nombre, datos in sectores.items():
        print(f"- {nombre}: ${datos['precio']} (Disponibles: {datos['capacidad']})")
    print("-" * 28)

def aplicar_promocion(total, cantidad):
    """
    Aplica un 10% de descuento si se compran 4 o más entradas.
    Retorna el total con o sin descuento.
    """
    if cantidad >= 4:
        descuento = total * 0.10
        total -= descuento
        print(f"✅ ¡Promoción aplicada! Descuento por grupo: ${descuento:.2f}")
    return total

def registrar_venta_archivo(sector, cantidad, total):
    """Guarda el registro de la venta en un archivo de texto."""
    try:
        with open("historial_ventas.txt", "a") as archivo:
            archivo.write(f"{sector},{cantidad},{total}\n")
    except Exception as e:
        print(f"⚠️ Error al guardar en el archivo: {e}")

def procesar_venta():
    """Maneja la lógica completa de venta y validación de datos."""
    global recaudacion_total # Permite modificar el acumulador global
    
    mostrar_sectores()
    sector_elegido = input("Ingrese el nombre del sector deseado (VIP, PLATEA, GENERAL): ").upper()
    
    # Validación 1: Existencia del sector
    if sector_elegido not in sectores:
        print("❌ Error: El sector ingresado no existe. Intente nuevamente.")
        return

    # Validación 2: Manejo de errores con try-except para el ingreso numérico
    try:
        cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))
    except ValueError:
        print("❌ Error: Debe ingresar un número entero.")
        return

    # Validación 3: Cantidad positiva
    if cantidad <= 0:
        print("❌ Error: La cantidad debe ser mayor a cero.")
        return

    # Validación 4: Control de capacidad
    if cantidad > sectores[sector_elegido]["capacidad"]:
        print(f"❌ Error: Capacidad insuficiente. Solo quedan {sectores[sector_elegido]['capacidad']} lugares en {sector_elegido}.")
        return

    # Cálculos e importes
    precio_unitario = sectores[sector_elegido]["precio"]
    subtotal = precio_unitario * cantidad
    total_pagar = aplicar_promocion(subtotal, cantidad)

    # Actualización de contadores y acumuladores
    sectores[sector_elegido]["capacidad"] -= cantidad
    sectores[sector_elegido]["vendidas"] += cantidad
    recaudacion_total += total_pagar

    # Guardar en archivo
    registrar_venta_archivo(sector_elegido, cantidad, total_pagar)

    print(f"\n🎟️ ¡Venta exitosa! Total a cobrar: ${total_pagar:.2f}")

def mostrar_estadisticas():
    """Muestra los datos acumulados y el sector más demandado."""
    print("\n📊 --- ESTADÍSTICAS DEL EVENTO --- 📊")
    print(f"💰 Recaudación total acumulada: ${recaudacion_total:.2f}")
    
    print("\n📈 Ventas por sector:")
    sector_mas_vendido = ""
    max_ventas = -1
    
    # Estructura repetitiva para buscar el máximo (Sector más demandado)
    for nombre, datos in sectores.items():
        vendidas = datos["vendidas"]
        print(f" - {nombre}: {vendidas} entradas vendidas.")
        
        if vendidas > max_ventas:
            max_ventas = vendidas
            sector_mas_vendido = nombre
            
    if max_ventas > 0:
        print(f"\n🔥 El sector más demandado es: {sector_mas_vendido} ({max_ventas} entradas)")
    else:
        print("\nAún no se han registrado ventas.")

# ==========================================
# 3. BLOQUE PRINCIPAL (Estructura Repetitiva)
# ==========================================
def iniciar_sistema():
    """Bucle principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("👉 Seleccione una opción (1-3): ")
        
        # Estructuras condicionales para derivar la acción
        if opcion == '1':
            procesar_venta()
        elif opcion == '2':
            mostrar_estadisticas()
        elif opcion == '3':
            print("\n👋 Cerrando el sistema... ¡Gracias por utilizar nuestro software!")
            break
        else:
            print("❌ Opción no válida. Por favor, ingrese 1, 2 o 3.")

# Punto de entrada
if __name__ == "__main__":
    iniciar_sistema()