def mortal_fib_rabbits(n, m):
    ages = [0 for i in range(m)]
    ages[0] = 1 # Add one rabbit to the 0 year-olds
    for _ in range(1,n):
        babies = sum(ages[1:])
        ages[1:] = ages[:-1]
        ages[0] = babies

    return sum(ages)

        
if __name__ == "__main__":
    print(mortal_fib_rabbits(6, 3))
    print(mortal_fib_rabbits(91, 16))