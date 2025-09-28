import re
import random

# Ejercicio 1: Decodificador de Mensajes Secretos
def decodificar_mensaje(mensaje_cifrado):
    """
    Decodifica un mensaje invertido eliminando caracteres especiales
    """
    # Voltear la cadena
    mensaje_volteado = mensaje_cifrado[::-1]
    
    # Eliminar caracteres no alfabéticos usando expresión regular
    mensaje_limpio = re.sub(r'[^a-zA-Z\s]', '', mensaje_volteado)
    
    return mensaje_limpio.strip()

# Ejercicio 2: Simulador de Ahorro Mensual
def simulador_ahorro(cantidad_inicial, cantidad_mensual, num_meses):
    """
    Simula el ahorro mensual y calcula el total final
    """
    total_ahorrado = cantidad_inicial + (cantidad_mensual * num_meses)
    
    print(f"Total ahorrado después de {num_meses} meses: {total_ahorrado}€")
    
    if total_ahorrado > 5000:
        print("¡Felicitaciones! Has superado los 5000€ de ahorro.")
    
    return total_ahorrado

