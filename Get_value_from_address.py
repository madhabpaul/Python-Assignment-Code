#!/usr/bin/python3

import ctypes

a=50
address=id(a)
print(address)
print(ctypes.cast(address, ctypes.py_object).value)
