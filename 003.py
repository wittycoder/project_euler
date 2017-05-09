factor_this = 600851475143

def factors(num):
    z = 2
    while z * z <= num:
        if num % z == 0:
            print z
            num /= z
        else:
            z += 1
    if num > 1:
        print num
        
factors(factor_this)