# my prime number generator

num = int(input("find prime numbers in which range:"))
list_of_primes = []
for x in range(2, num+1):
    prime_no = True

    for y in range(2,x):
        if x % y == 0:
            prime_no = False

    if prime_no:
        list_of_primes.append(x)
print(list_of_primes)
