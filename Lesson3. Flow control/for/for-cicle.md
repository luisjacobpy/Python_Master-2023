## while bucle vs for bucle
````python
"""
while bucle
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
indice = 0

while (indice < len(numbers)):
    print(numbers[indice])
    indice+=1
"""
for bucle
"""
for numero in numbers:
    print(numero)
````
## For in [list]
````python
"""
Multipliocation in valueas of list
"""
indice = 0
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    numbers[indice] *= 10 # Self value *10
    indice+=1
print(numbers)
````
### Output
````commandline
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
````


## Enumerate
````python
'''
enumerate
lectura secuencial con clave y valor
'''

numbers = [1,2,3,4,5,6,7,8,9,10]
for indice, number in enumerate(numbers):
    numbers[indice] *= 10
print(numbers)
"""
is not necessary use a indice in value 0 'indice = 0'
is not necessry add +1 in the cicle 'indice+=1'
"""
````
### Output
````commandline
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
````

## Strings
````python
'''
For in Strings
'''
string1 = 'hello my friend!'
for character in string1:
    print(character)

'''
I what add character * in the string
'''
string2 = ''
string3 = ''
for character in string1:
    print(character)
    string2 += "*"
    string3 += character * 2
print(string1)
print(string2)
print(string3)
````
### Output
```commandline
h
e
l
l
o
 
m
y
 
f
r
i
e
n
d
!
h
e
l
l
o
 
m
y
 
f
r
i
e
n
d
!
hello my friend!
****************
hheelllloo  mmyy  ffrriieenndd!!

Process finished with exit code 0
```
## for in range
````python
"""
range was interpreted in the execution, cause is not use the memory
"""
print(range)

for i in range(10):
    print(i)
'''
cast
save in a list
'''
print(list(range(10)))
````
### output
````commandline
<class 'range'>
0
1
2
3
4
5
6
7
8
9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

````
