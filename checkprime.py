# Function to check if a number is prime
def is_prime(num):
   if num <= 1:
       return False # Numbers less than or equal to 1 are not prime
   for i in range(2, int(num**0.5) + 1): # Check divisors up to the square root of num
       if num % i == 0:
           return "is not prime" # Found a divisor, not prime
   return "is prime" # No divisors found, it's prime
