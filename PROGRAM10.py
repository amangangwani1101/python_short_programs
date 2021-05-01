def rec(num):
    if(num==0):
        return 0
    return num+rec(num-1)
ans=rec(100)
print(f"Sum of number ranging from 0-100 is:-{ans}")
    
