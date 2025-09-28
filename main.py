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

