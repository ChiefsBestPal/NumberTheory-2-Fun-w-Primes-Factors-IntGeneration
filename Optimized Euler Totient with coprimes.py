from collections import Counter
import math


def primeFactorization(num):
    res = {'2' : 0}
    test = []
    while num % 2 == 0:
        res['2'] += 1
        num /= 2
    #num is now odd. the range of possible odd prime factors is 3 to int(sqrt(num)) to test which can do proper // with num
    for odd_factor in range(3,int(math.sqrt(num))+1,2):
        while num % odd_factor == 0:
            res.setdefault(str(odd_factor),0)
            res[str(odd_factor)] += 1
            num /= odd_factor
    #in case of remainder: it is a prime, so update dict
    if num > 2:
        res.update({str(int(num)): 1})


    #\u207 for before each digit of exponent that are betweem 4 and 9, 
    #\u00B for before each digit of exponent that are 2 or 3 
    # if exponent is one, only number .... if exponent is zero, omit number

    print(display_unicode_factor_decomposition(res))
    print(res)
    return res

def euler_totient(num):
    factorizationResult = primeFactorization(num)
    num_of_coprimes = 1
    for k,v in factorizationResult.items():
        prime,exp = int(k),v
        num_of_coprimes *= (prime**(exp-1))*(prime-1) #Euler totient product formula (phi)

    return int(num_of_coprimes * 2) #x2 is deduction from alg #!ERROR CHECK CODEWARS: 3/4 PASSED, 1\4 FAILED BUT OUTPUT THE ANSWER MULT BY TWO !

def euler_totient_dev(num):
    factorizationResult = primeFactorization(num)
    num_of_coprimes = num #default
    for k,v in factorizationResult.items():
        if v != 0:
            prime = int(k)
            num_of_coprimes *= (1-(1/prime))  #Euler totient product formula DEVELOPPED WITH DEFINITION OF N (phi) (SEE .IPythonNoteBook)
    
    return num_of_coprimes


def display_unicode_factor_decomposition(factorizationResult):
    unicode_hex_encode = lambda string: chr(int(string.replace(r'\u','0x'),16))
    final_string = ""
    for k,v in factorizationResult.items():
        exponent = str(v)
        exp_arr = list(map(int,[digit for digit in exponent]))
        for c,digit in enumerate(exp_arr):
            if digit == 1:
                exp_arr[c] = unicode_hex_encode(r"\u00B9") 
            elif digit in range(4,10) or digit == 0:
                exp_arr[c] = unicode_hex_encode(r"\u207" + str(digit))
            elif digit in [2,3]:
                exp_arr[c] = unicode_hex_encode(r"\u00B"+ str(digit))
            else:
                pass
        exp_arr = map(str,exp_arr)
        exponent = "".join(exp_arr)
        final_string += k + exponent + " \u00D7 "
    final_string = final_string[:-3]
    return final_string


# Python3 program to calculate  
# Euler's Totient Function 
def phi(n): 
    """This interpretation aims at finding directly the number of non prime factors (we know comprimes have a gcd == 1)
    param - number of prime factors and their related multiples = res"""  
     
    result = n  

    p = 2  
    while(p**2 <= n): 
          
        # Check if p is a prime factor. 
        if (n % p == 0):  
               
            # update n and result 
            while (n % p == 0): 
                n = n // p 
            result -= result // p 
        p += 1
    
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most  
    # one such prime factor) 
    if (n > 1): 
        result -= result // n 
    return result
"""
1) Initialize result as n
2) Consider every number 'p' (where 'p' varies from 2 to Φn). 
   If p divides n, then do following
   a) Subtract all multiples of p from 1 to n [all multiples of p
      will have gcd more than 1 (at least p) with n]
   b) Update n by repeatedly dividing it by p.
3) If the reduced n is more than 1, then remove all multiples
   of n from result.
"""


denominator = 12
print(primeFactorization(denominator))
exit()
print("GOOD ONE    " + str(phi(denominator))) #The right one ???
print(euler_totient_dev(denominator)) #sometimes wrong by factor of 2 #! 1/prime
print(euler_totient(denominator)) #also sometimes wrong by factor of 2 #! prime **


from fractions import Fraction
d = 7
range_n = (n for n in range(1,d+1))
range_n = iter(range_n)
c = int()

while True:
    try:
        n = next(range_n)
    except StopIteration as err:
        print("End")
        break
    else:
        if gcd(n,d) == 1:
            c += 1
        
print(c)
"""
def ERROR_FORMAL_TOTIENT(num):
    phi = 1
    m = num
    for p in list(filter(is_prime,range(1,int(math.sqrt(num))+1))):
        print(p)
        if p % m == 0:
            phi *= (p-1)
            m /= (p-1)
        while p % m == 0:
            phi *= p
            m /= p
    if m > 1: # m is prime factor greater than sqrt(num) for sure
        phi *= (m-1)
    return phi
"""