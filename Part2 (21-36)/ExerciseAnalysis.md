# Exercise Analysis (24-26)
In this document the presented exercises have explicit errors.   
They will be analysed and expland on why this errors ocurred.



## Exercise 24
The original line of code presented is:  
```python
lista_colores ["rojo", "azul", "verde", "amarillo"]
```

This line will present an error, because the "=" equal symbol is missing, being the lack of initialization, which is a Name Error.  
The correct line will be:

```python
lista_colores = ["rojo", "azul", "verde", "amarillo"]
```

You can check the exercise in the [Exercise 24 file](Exercise24.py).



## Exercise 25
The original code presented is:  
```python
lista_colores = ["rojo", "azul" "verde", "amarillo"]
print(lista_colores(0))
```

This code has 2 error:   
* The lack of a comma inside the list, between "azul" and "verde".
* Using parentheses () to search of a list index instead of using brackets [].

This results in a Type Error.

The correction will be:   
```python
lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[0])
```

You can check the exercise in the [Exercise 25 file](Exercise25.py).



## Exercise 26
The original code presented is: 

```python
lista_colores = ["rojo", "azul", "verde"]
print(lista_colores[-0])
print(lista_colores[-4])
```

Although in python is possible to use negative indexes, in this case the list is only long enough to use -3 index, so the error will be a out of range one.

The corrected code will be: 

```python
lista_colores = ["rojo", "azul", "verde"]
print(lista_colores[-0])
print(lista_colores[-3])
```

You can check the exercise in the [Exercise 26 file](Exercise26.py).

