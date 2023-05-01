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
