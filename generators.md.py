"""
def squares(N):
    for i in range(N + 1):
        yield i ** 2

for num in squares(5):
    print(num)
"""

"""
def even_numbers(N):
    for x in range(0,N + 1,2):
        yield x 
        
N = int(input())
print(", ".join(map(str,even_numbers(N))))
"""

"""
def num(N):
    for i in range(N + 1):
        if i % 3 == 0 & i % 4 == 0:
            yield i

N = int(input())

print(", ".join(map(str,num(N))))
"""

""" 
def num(A, B):
    for i in range(A, B):  
        yield i ** 2  

A = int(input())
B = int(input())
        
for aaa in num(A, B):
    print(aaa)  
""" 

def countdown(n):
    for i in range(n, -1, -1): 
        yield i  

n = int(input("Enter a number: "))

for num in countdown(n):
    print(num)
