import re

def clasificar_triangulo(*lados):
    """
    Esta función clasifica un triángulo según sus lados.
    Args:
    lado1: La longitud del primer lado.
    lado2: La longitud del segundo lado.
    lado3: La longitud del tercer lado.
    Returns:
    Un string que indica si el triángulo es escaleno,
    isósceles, equilátero o inválido.
    """
    
    try:
        validar_entrada(lados)
        lado1, lado2, lado3 = lados
        validar_lados(lado1, lado2, lado3)
        
        # Clasificar el triángulo
        if lado1 == lado2 == lado3:
            return "Triángulo equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"
    except ValueError as e:
        return str(e)

def validar_entrada(lados):
    if len(lados) == 0:
        raise ValueError("Debe ingresar los datos")
    elif len(lados) < 3:
        raise ValueError("Debe ingresar todos los datos")
    elif len(lados) != 3:
        raise ValueError("Debe ingresar solo tres lados del triángulo")

def validar_lados(lado1, lado2, lado3):
    for lado in [lado1, lado2, lado3]:
        if isinstance(lado, bool):
            raise ValueError("No se pueden ingresar valores booleanos")
        if lado == 0:
            raise ValueError("El lado del triángulo no puede contener un valor cero")
        if not re.search(r'\d', str(lado)):
            raise ValueError("Solo se pueden ingresar valores enteros")
        if isinstance(lado, float):
            raise ValueError("Sólo se pueden ingresar valores enteros")
        if not isinstance(lado, int):
            raise ValueError("Debe ingresar los valores sin ningun caracter")
        if lado < 0:
            raise ValueError("El lado del triángulo no puede contener un valor negativo")
    
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        raise ValueError("El triángulo es un triángulo inválido")

# Aquí debajo se colocan las pruebas una a una, descomentando una a la vez, para verificar el correcto funcionamiento

#######################################################################
# Empiezan las pruebas

# Caso prueba 1: Triángulo escaleno
# Entrada: 7 10 16 
# Resultado esperado: escaleno
clasificacion = clasificar_triangulo(7, 10, 16)
print(f"Caso prueba 1: Triángulo escaleno \n - Resultado: {clasificacion}")

# Caso prueba 2: Triángulo equilátero
# Entrada: 5 5 5     
# Resultado esperado: equilátero
clasificacion = clasificar_triangulo(5, 5, 5)
print(f"Caso prueba 2: Triángulo equilátero \n - Resultado: {clasificacion}")

# Caso prueba 3: Triángulo isósceles
# Entrada: 13 13 10     
# Resultado esperado: isósceles
clasificacion = clasificar_triangulo(13, 13, 10)
print(f"Caso prueba 3: Triángulo isósceles \n - Resultado: {clasificacion}")

# Caso prueba 4: Triángulo inválido, suma de dos de los números sea menor que el tercero
# Entrada: 2, 2, 7
# Resultado esperado: El triángulo es un triángulo inválido
clasificacion = clasificar_triangulo(2, 2, 7)
print(f"Caso prueba 4: Triángulo inválido, suma de dos de los números sea menor que el tercero \n - Resultado: {clasificacion}")

# Caso de prueba 5: Triángulo inválido, lado es igual a la suma de las longitudes de los otros dos lados
# Entrada: 1, 2, 3
# Resultado esperado: El triángulo es un triángulo inválido
clasificacion = clasificar_triangulo(1, 2, 3)
print(f"Caso prueba 5: Triángulo inválido, lado es igual a la suma de las longitudes de los otros dos lados \n - Resultado: {clasificacion}")

# Caso prueba 6: Carácter como entrada
# Entrada: a 3 4
# Resultado esperado: Sólo se pueden ingresar valores enteros
clasificacion = clasificar_triangulo("a", 3, 4)  # Cambiado para provocar el error de tipo
print(f"Caso prueba 6: Carácter como entrada \n - Resultado: {clasificacion}")

# Caso prueba 7: Valor negativo como entrada
# Entrada: -3, 4, 5
# Resultado esperado: El lado del triángulo no puede contener un valor negativo
clasificacion = clasificar_triangulo(-3, 4, 5)
print(f"Caso prueba 7: Valor negativo como entrada \n - Resultado: {clasificacion}")

# Caso prueba 8: Valores decimales como entrada
# Entrada: 3.5, 4.5, 5.5
# Resultado esperado: Sólo se pueden ingresar valores enteros
clasificacion = clasificar_triangulo(3.5, 4.5, 5.5)  # Cambiado para provocar el error de tipo
print(f"Caso prueba 8: Valores decimales como entrada \n - Resultado: {clasificacion}")

# Caso de Prueba 9: Valor de un lado igual a 0
# Entrada: 0, 3, 4
# Resultado Esperado: El lado del triángulo no puede contener un valor cero
clasificacion = clasificar_triangulo(0, 3, 4)
print(f"Caso Prueba 9: Valor de un lado igual a 0 \n - Resultado: {clasificacion}")

# Caso prueba 10: Cadena como entrada
# Entrada: 5 5 cinco
# Resultado esperado: Solo se pueden ingresar valores enteros
clasificacion = clasificar_triangulo(5, 5, "cinco")  # Cambiado para provocar el error de tipo
print(f"Caso prueba 10: Cadena como entrada \n - Resultado: {clasificacion}")

# Caso Prueba 11: Valores booleanos como entrada
# Entrada: True False True
# Resultado esperado: Solo se pueden ingresar valores enteros
clasificacion = clasificacion = clasificar_triangulo(True, False, True)
print(f"Caso Prueba 11: Triángulo con valores booleanos \n - Resultado: {clasificacion}")

# Caso Prueba 12: Falta de Entrada
# Entrada: 
# Resultado esperado: Debe ingresar los datos
clasificacion = clasificar_triangulo()  # Cambiado para provocar el error de cantidad de argumentos
print(f"Caso Prueba 12: Falta de Entrada \n - Resultado: {clasificacion}")

# Caso Prueba 13: Entrada incompleta
# Entrada: 4 5
# Resultado esperado: Debe ingresar todos los datos
clasificacion = clasificar_triangulo(4, 5)
print(f"Caso Prueba 13: Entrada incompleta \n - Resultado: {clasificacion}")

# Caso Prueba 14: Exceso de datos en la entrada
# Entrada: 4 5 4 4 
# Resultado esperado: Debe ingresar 3 valores
clasificacion = clasificar_triangulo(4, 5, 4, 4)  # Cambiado para provocar el error de cantidad de argumentos
print(f"Caso Prueba 14: Exceso de datos en la entrada \n - Resultado: {clasificacion}")

# Caso Prueba 15: Número con caracteres 
# Entrada: 4,000 5,100 4,300 
# Resultado esperado: Debe ingresar los valores sin ningun caracter
clasificacion = clasificar_triangulo("4,000", "5,100", "4,300")  
print(f"Caso Prueba 15: Número con caracteres \n - Resultado: {clasificacion}")