"""
Greates Common Divisor

- Largest number k that divides both m and n
- Example : 
    - gcd(8,12) = 4
    - gcd(18,25) = 1

- Note : 1 divides every number and there's at least one number that divides both m and n

Algorithm

    - List out the factors of m
        - Factors of m must be between 1 and m
        - Test each number in its range, whether it divdes m without a remainder
        - Add it to the list of factors 
    - List out the factors of n
        - Factors of n must be between 1 and n
        - Test each number in its range, whether it divdes n without a remainder
        - Add it to the list of factors 
    - Report the largest number that appears on both the lists

Example : gcd(14, 63)

    - Factors of 14 : 1,2,7,14
    - Factors of 63 : 1,3,7,9,21,63
    - Common Factors of 14 and 63
        - 1 and 7
    - Largest common factor : 7

Code Algorithm -- gcd(m,n)
    - fm and fn list of factors for m and n respectively
    - for each i, from 1 to m, add i to fm if i divides m
    - for each j, from 1 to m, add j to fn if i divides n
    - Use cf for list of common factors
        - For each f in fm, add f to cf if f also appears in fn
        - Return the rightmost value of cf
""" 

def gcd(m,n):
    """
    The function will get the greatest common divisor

    Input Parameters : 
        - m & n : Two input parameters, both integers preferably

    Returns : 
        - Returns an integer value
    """
    fm = list()
    fn = list()
    cf = list()
  
    # Getting the list of factors for m
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)
            i=i+1
        else:
            i=i+1
    
    # Getting the list of factors for n
    for j in range(1,n+1):
        if n%j==0:
            fn.append(j)
            j=j+1
        else:
            j=j+1

    # Getting the list of common factors
    for f in fm:
        if f in fn:
            cf.append(f)

    # Returning the last element of common factors
    return cf[-1]

print("The Greatet Common Divisor for {} and {} is {}". format(23,526,int(gcd(23,523))))
