ins=int(input("Enter digit n for printing fibonacci series:-\n"))
a=0
b=1
for i in range(ins-1):
    if(i==0):
        print(f"THE FIBBONACI SERIES FOR {ins} is:-{a},{b},",end="")
    else:
        c=a+b
        a=b
        b=c
        print(f"{c},",end="")
        
    
