# -*- coding: utf-8 -*-
"""Actividad 1 - Ames - CDR

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155kzcdXmexsPEaVhKk_UnSRW_YmbDeK9

¿Qué crees que significa cada columna? ¿Qué crees que significa cada fila?
"""

!head data.tsv

"""¿Cuántos pedidos parece haber?"""

!tail data.tsv

"""¿Cuántas líneas hay en este archivo?"""

!wc -l data.tsv

"""¿Qué burrito es más popular, steak o chicken?"""

!grep -i "chicken burrito" data.tsv | wc -l ; grep -o -i "steak burrito" data.tsv | wc -l

"""
¿Los burritos de pollo suelen tener frijoles negros o frijoles pintos? """

!grep -ic "chicken burrito.*black beans" data.tsv

!grep -ic "chicken burrito.*pinto beans" data.tsv