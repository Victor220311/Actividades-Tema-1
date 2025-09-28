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

# Ejercicio 3: Clasificador de Números
def clasificar_numeros(lista_numeros):
    """
    Clasifica números en pares, impares y negativos
    """
    pares = []
    impares = []
    negativos = []
    
    for numero in lista_numeros:
        if numero < 0:
            negativos.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares, negativos

# Ejercicio 4: Calculadora de Notas
def calculadora_notas(notas):
    """
    Calcula estadísticas de una lista de notas
    """
    if not notas:
        return None
    
    media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    # Verificar notas suspensas
    suspensas = [nota for nota in notas if nota < 5]
    
    print(f"Media: {media:.2f}")
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")
    
    if suspensas:
        print(f"¡Atención! Hay {len(suspensas)} nota(s) suspensa(s): {suspensas}")
    
    return media, nota_maxima, nota_minima

# Ejercicio 5: Generador de ADN
def generar_adn(longitud):
    """
    Genera una cadena de ADN aleatoria y cuenta las bases
    """
    bases = ['A', 'T', 'C', 'G']
    adn = ''.join(random.choice(bases) for _ in range(longitud))
    
    # Contar cada base
    contador = {base: adn.count(base) for base in bases}
    
    print(f"Cadena de ADN generada: {adn}")
    print("Conteo de bases:")
    for base, cantidad in contador.items():
        print(f"{base}: {cantidad}")
    
    return adn, contador


