#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Write a Python function to find prime factorization of a given number.
# Input: Integer / Output: List of prime factors
# E.x get_prime_factors(630) -> [2, 3, 3, 5, 7]

def get_whole_number_scope(number):
    
    if((not isinstance(number,int)) | number==1):
       raise TypeError
   
    whole_numbers = []
    x_number=1

    while x_number<number:
        x_number+=1
        whole_numbers.append(x_number)
        
    return whole_numbers

def get_prime_numbers(number):
  
   prime_numbers = get_whole_number_scope(number)
   
   for x in prime_numbers:
    flag = 0
    y=2
    while(y<=x):
        
        if(x%y==0):
            flag+=1
        y+=1
        
    if(flag!=1):
     prime_numbers.remove(x)
   
   return prime_numbers

def get_prime_factors(number):
   multiply_number = []
   prime_numbers = get_prime_numbers(number)
   
   if(number in prime_numbers):
      multiply_number.append(number)
      return multiply_number
   
   else:
      prime_numbers_iteration = iter(prime_numbers)
      prime_number = next(prime_numbers_iteration)
      while (number!=1):
   
         if(number%prime_number==0):
               number = number/prime_number
               multiply_number.append(prime_number)
         else:
            prime_number = next(prime_numbers_iteration)
               
      return multiply_number
     
    
# Choose big number
num = 424

# Get prime factors of specified number
prime_factors_of_num = get_prime_factors(num)

print(*prime_factors_of_num, sep = " x ", end =" ")    
print(f'= {num} ' )    

