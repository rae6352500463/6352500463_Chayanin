# -*- coding: utf-8 -*-
"""sort_object

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Khrjz15JcK2tUzsf-Zow59oLj66HYptO
"""

obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'dice': [155, 38], 'mouse':
[200, 45], 'keyboard': [298, 65], 'fan': [300, 36]}

obj_detected

dict(sorted(obj_detected.items(), key=lambda item: item[1]))