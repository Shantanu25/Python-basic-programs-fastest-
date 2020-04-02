def isPrime(num) :

  #corner cases
  if num <= 1:
    return False
  #smallest primes
  if num <= 3:
    return True
  
  #Anything divisible by smallest primes is ruled out
  if (num%2 == 0 or num%3 == 0):
    return False

#Now the number can be a multiple of a prime number
#6k+-1 are all primes  
#check only until 6k-1 <= sqrt(num)
  i = 6
  while ( (i-1) * (i-1) <= num):
    if(num % (i-1) == 0 or num % (i+1) == 0):
      return False
    i+=6

  return True

  # Driver Program  
user_num = input("Enter number: ")
if (isPrime(int(user_num))) : 
    print("" + str(user_num) + " is a prime number") 
else : 
    print("" + str(user_num) + " is NOT a prime number")  
