n = int(input())

def fibonachi(num):
    if num <= 1:
        return num
    

    return fibonachi(num-1) + fibonachi(num-2)
        
    
print(fibonachi(n))

   