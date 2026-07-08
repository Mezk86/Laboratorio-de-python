# MÓDULO 3: Modularización
def calcular_total(precio, cantidad):
    total = precio * cantidad
    if cantidad >= 4:
        total *= 0.90
    return total

def mostrar_estadisticas_resumidas(recaudacion):
    # Función que recibe parámetros y muestra resultados
    print(f"La recaudación actual es: ${recaudacion}")