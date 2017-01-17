def prime_no_test():
    n = 7
    prime_in_range = []
    for x in range(1,n):
        if n%x == 0:
            prime_in_range.append(n)
        print(prime_in_range)
