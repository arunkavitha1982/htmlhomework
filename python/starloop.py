def arunspace(n):
    for a in range (1,n+1):
        print(" ",end='')
def arunstar(n):
    for a in range (1,n+1):
        print("*",end='')



start=int(input("enter your number : "))

for i in range (1,start+1):
    arunspace(start-i)
    arunstar(i)
    print()

for j in range (start-1,0,-1):
    arunspace(start-j)
    arunstar(j)
    print()
    


