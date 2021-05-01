def func(a):
    if(a==1):
        return 1
    return a*func(a-1)    
num=int(input("Enter any number:-\n"))
ans=func(num)
print(f"The factorial of {num}:-{ans}")
