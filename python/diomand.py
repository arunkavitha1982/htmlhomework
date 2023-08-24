def arunspace(n):
    for a in range (1,n+1):
        print(" ",end='')
        
def arunstarspace(n):
    for a in range (1,n+1):
        print("* ",end='')
        
x=int(input("enter your number : "))
for i in range(1,x+1,1):
    arunspace(x-i)
    arunstarspace(i)
    print()
for i in range(x-1,0,-1):
     arunspace(x-i)
     arunstarspace(i)
    
     print()
