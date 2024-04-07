# List

unsorted = [3, 1, 2]
list = list()
def hi(unsorted):
    while len(unsorted) > 0: # while loop so it knows when to stop when empty.
        out = min(unsorted)
        unsorted.remove(out)
        list.append(out) # lists are actually objects. Hence why they have methods.
    print(list)

# hi(unsorted)

# goodness. I could not even solve this problem. I was thinking about if conditionals, but then
# I didn't know how it would get the next list values. But yeah this list algorithm works better.
# I don't think I would have thought of this solution, but I understand how it works. I also added a twist: using a function


print(sorted(unsorted)) # what the hell. There was already a built-in sorted function in Python

# Also I tried printing both my own function and sorted. But since the hi finished, unsorted was empty

# Failed attempt
n = 11
primes = list()
for i in range(2, n):
    if n <= i/2:
        primes.append(i)

    else:

# Analyzing Code:

n = 12
count = 0

for i in range(2, n+1): # n + 1 because it stops at 11 if not for + 1.
    no_factors_found = True # AAssume prime until disproven
    f = 2
    while no_factors_found and f < i:
        if i % f == 0: # 2 / 2 = 0
            no_factors_found = False
        f += 1

    if no_factors_found:
        count += 1
# basically finds how many prime numbers between 2 and n. If 11, there is 5. It wouldn't print the value
# the while loop keeps going. There is some math formulas with f = 2 and slowly goes up and stuff. Some pattern.

# Uses the  Sieve of Eratosthenes


