# Prueba RealLabs

## Implementación
1. console.py controla el input de usuario y arroja mensajes informativos
2. sequences_calculator
    """
    sequence_to_one() 
    Parameters
    ----------
    number : int
        numero entero positivo 'n'

    Returns
    -------
    int
    if n%2 != 0, n*3+1
    if n%2 = 0, n/2
    when return == 1, throw end msg
    """

    """
    find_sequences()   
         
    Parameters
    ----------
    int
        limit: enteros >0 & <= limit

    Returns
    -------
    int
    int: la longitud de las dos secuencias más largas arrojadas por sequence_to_one()
    """

# Ejercicio:

## Para cualquier numero entero positivo 'n' definimos dos reglas.
    - si es par: dividir en 2
    - si es impar: multiplicar por 3, después, sumar 1

Repetir este proceso hasta que se llegue al numero '1'

Esto va a generar una secuencia de números como los que se muestran a continuación, convergiendo a '1':

`3, 10, 5, 16, 8, 4, 2, 1`

`7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1`

Para cada numero 'n' nosotros debemos contar la cantidad de pasos requeridos para alcanzar '1'

Entonces la secuencia anterior empezando con '3', tiene una longitud de 8 (incluyendo el valor inicial y final).

La segunda secuencia comenzada en '7' tiene una longitud de 17.


# Reto:
## Encuentre, de las secuencias, la  mas larga y la segunda mas larga de todos los enteros menores o iguales a 10 Millones(10'000.000) y comparta el código.

## Pista/Ayuda/Valores de calibración:
La secuencia mas larga para los números menores a 1000 tiene una longitud de 179
La secuencia mas larga para los números menores a 10000 tiene una longitud de 262
