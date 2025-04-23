find = True
num = 9999999

while not find and num >= 1000000:
    
    is_prime = True
    i = 2
    
    while is_prime and i * i <= num:
        if num % i == 0:
            is_prime = False
            
        i = i + 1
             
    if is_prime:
        print(num, end =" ")
        find = True
        
    num = num - 2