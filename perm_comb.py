import math 


def permutation(n,r):
    perm = (math.factorial(n)/(math.factorial(n-r)))
    return perm

def combinatoric(n,r):
    comb = (math.factorial(n)/(math.factorial(n-r))*(math.factorial(r)))
    return comb

ans = input("Would you like to try a combinatoric (c) or permutation (p) ?")

if ans == "P" or "p": 
    n = input("what is your n? ")
    r = input("What is your r? ")
    print("Your permutation is: " + str(permutation(int(n), int(r))))

else: 
    n = input("what is your n? ")
    r = input("What is your r? ")
    print("Your combinatoric is: " + str(combinatoric(int(n), int(r))))
