# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:18:53 2021

@author: Odette
"""

#USO DE LA DECLARACIÓN CONTINUE

#evitar que aparezca el 5, que desaparezca el 5
    
x=1
while x<=10:
    if x==5:
        x+=1
        continue
    print(x)
    x+=1

    