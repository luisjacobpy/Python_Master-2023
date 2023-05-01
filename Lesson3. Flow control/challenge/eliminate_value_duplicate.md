Dadas dos listas, debes generar una tercera con tosos los elementos que se repiten en ellas,
pero no debe repetirse ningun elemento en la nueva lista

```python
list_1 = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
list_2 = ['h', 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']

list_3 = []
for letra in list_1:
    if letra in list_2 and letra not in list_3:
        list_3.append(letra)
print(list_3) # ['h', 'o', 'l', 'a', ' ', 'u', 'n']
```

### Output
```Bash
['h', 'o', 'l', 'a', ' ', 'u', 'n']
```
