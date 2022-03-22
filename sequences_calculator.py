# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:46:01 2022

@author: aleja
"""


def sequence_to_one(number: int) -> int:
    """
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
    sequence = []
    res = number
    count = 1
    while not (res == 1):
        if res % 2 == 0:
            res = res / 2
        else:
            res = (res * 3) + 1
        count = count + 1
        sequence.append(res)
    return (count, (sequence))


def find_sequences(limit: int) -> int:
    """
    Parameters
    ----------
    int
        limit: enteros >0 & <= limit

    Returns
    -------
    int
       int: la longitud de las dos secuencias más largas arrojadas por sequence_to_one()
    """
    current, second = 0, 0
    index = 1

    while index <= int(limit):
        res_count, res_seq = sequence_to_one(index)
        if res_count > current:
            second = current
            current = res_count
            print(
                "Trabajando. Secuencias más largas {} y {}. Número actual {}".format(
                    current, second, index
                )
            )
        index += 1

    print("La secuencia más larga es de: {}.".format(current))
    print("La segunda secuencia es de: {}.".format(second))

    return current
