def arunspace(n):
    for a in range (1,n+1):
        print(" ",end='')
        
def arunstar(n):
    for a in range (1,n+1):
        print("*",end='')
        
x=int(input("enter your number : "))

for i in range (x-2,0,-2):
    arunstar((x-i)//2)
    arunspace(i)
    arunstar((x-i)//2)
    print()
print("*"*x)
for i in range(1,x,2):
    arunstar((x-i)//2)
    arunspace(i)
    arunstar((x-i)//2)
    print()
