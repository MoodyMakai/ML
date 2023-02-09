def hola():
    print('hello world')

def prolem():
    x = input()
    y = input()
    z= x+y
    print(z)
    

def fibb():
    fib = [0, 1, 1]
    for n in range(3,2000):
        x = n-1
        y = n-2
        I = fib[x] + fib[y]
        fib.append(I)
    print(fib)
    
def vowel():
    phrase = input()
    lib = ['a','e','i','o','u']
    for i in range(0,len(phrase)):
        for x in phrase:
            if x == lib[i]:
                print(x)
                
def num():
    input_int_array = [int(x) for x in input().split()]
    x=0
    for I in input_int_array:
        if x < I:
            x = I
    print(x)
            
def temp():
    n = int(input())
    print(n*1.8 +32)
    
def prime():
    n = int(input())
    n/2
    if (n %2) ==0:
        print('is even')
    else:
        n/3
        if (n%2) ==0:
            print('is even')
        else:
            n/5
            if (n%2) ==0:
                print('is even')
            else:
                print('prime')

def fax():
    import math
    n = int(input())
    blagh = [n]
    for e in range(1, n):
       x = n-e
       blagh.append(x)
    print(math.prod(blagh))
    
def alph():
    phrase = input()
    bet={}
    for x in phrase:
        bet[x]=bet.get(x,0)+1
    print(bet)
    
def st():
    phrase = input()
    x = phrase.split()
    z=''
    print(x)
    for i in range(0,len(x)):
        z += x[i]
        z += " "
    print(z)

def yed(n):
    for x in n:
        while (x%2) == 0:
            yield(x)

def lic(n):
    posList = [x>=0 for x in n]
    print(posList)

def sq(n):
    nums = [i*i for i in n]
    print(nums)
    
def strang(n):
        newList = [x for x in n if "@" in x]
        print(newList)

def cDic(n):
    newDic = {x:x**2 for x in n}
    print(newDic)

def div(n):
    for x in range(1, int(n/2)+1):
        if n % x==0:
            yield(x)

def let(n):
    newList = [x for x in n if 'a' in x[0]]
    print(newList)
    
def dot():
    import numpy 
    a = int(input())
    b = int(input())
    print(numpy.dot(a,b))
    
def pali(n):
    newList = [x for x in n if x[::-1] in n]
    print(newList)

def tDic(n):
    dic = {x:True for x in n if (x%2)==0}
    print(dic)


    

            


          
                
        
    

    


    


