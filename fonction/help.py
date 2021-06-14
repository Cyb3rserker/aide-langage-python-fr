"""
La fonction help permet d'accéder à la documentation d'un élément 
comme une classe, une fonction ou autre :
"""

#coding:utf-8

help(print)

"""
sortie au terminal :

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)     
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.        
    flush: whether to forcibly flush the stream.
"""

"""
On peut aussi faire la documentation de nos propre fonctions :
"""

def bonjour() :
# Il faut faire attention à l'indentation et à mettre la documentation 
# dans des commentaire avec """ car les commentaires comme celui-ci ne 
# sont pas pris en compte.
    """
    Documentation de bonjour :
    permet de dire bonjour.
    """
    print("Boujour !")

help(bonjour)

"""
sortie au terminal :

Help on function bonjour in module __main__:

bonjour()
    Documentation de bonjour :
    permet de dire bonjour.
"""