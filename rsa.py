import numpy as np


"""
    Implement RSA Encryption, call your method names, details below:
    sieve(), gcd_ex(a, b), modulo_expo(base, exponent, modulus), 
"""


# zero-fill sieves it's generally faster than one-filling
#     value of zero in the array implies that the current index is a prime number
#     value of one in the array implies that the current index is a composite number
sieves = np.zeros(shape=2**17, dtype=np.uint32)
primes = []  # fill primes array with prime #s calculated by sieve

# init prime number list for unit tests


""" 
    using the Sieve of Eratosthenes, please calculate prime numbers < 2^17
    For this assignment only use prime numbers > 2^16, which is a little less than half the prime numbers)
"""
def sieve():
    global primes, sieves
    n = 2**17
    sieves[0] = 1
    sieves[1] = 1
    
    for i in range(2, int(np.sqrt(n)) + 1):
        if sieves[i] == 0:
            for j in range(i*i, n, i):
                sieves[j] = 1
    
    for i in range(2**16, n):
        if sieves[i] == 0:
            primes.append(i)
            
sieve()


"""
Please see Canvas | Files | Lecture Notes | 'CS3310Lect07-08a_Euclid, Fibonacci, Binet, and Lamé, The first recorded
complexity analysis of an algorithm.' Note: the ***basic*** Euclidean Algorithm only returns the gcd, but your code needs to use
the ***Extended*** Euclidian Algorithm's and return the tuple(gcd, s, and t)

Like the aforementioned document mentions, in section 5.g, the efficiency of the Extended Euclidian algorithm
is big-Theta of (lg n). Since lg n is very efficient, it's okay to calculate the Extended Euclidian Algorithm using D&C (recursively).
However, you can also calculate it iteratively, which has the same time complexity as the D&C does, 
but will be an order of magnitude faster than D&C.

The zybook (see see https://learn.zybooks.com/zybook/UVUCS3310Spring2023/chapter/9/section/5) 
doesn't do a very good job of clearly defining how to calculate the extended GCD. 
Therefore, please see https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm 
for the pseudo-code of the Extended Euclidian Algorithm.
"""
def gcd_ex(a, b):
    s = 0 
    old_s = 1
    t = 1 
    old_t = 0
    r = b
    old_r = a
     
    while r != 0:
        quotient = old_r // r
        temp = old_r
        old_r = r
        r = temp - quotient * r
        temp = old_s
        old_s = s
        s = temp - quotient * s
        temp = old_t
        old_t = t
        t = temp - quotient * t

    gcd = old_r
    s = old_s
    t = old_t
    
    my_tuple = (gcd, s, t)
    return my_tuple

""" 
implement modular exponentiation
https://learn.zybooks.com/zybook/UVUCS3310Spring2023/chapter/9/section/7
See Figure 9.7.4: An iterative algorithm for fast modular exponentiation.
"""
def modulo_expo(base, exponent, modulus):
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
            
        exponent = exponent // 2
        base = (base * base) % modulus
        
    return result


"""
modulo_number used to calculate d and e will be (p-1)*(q-1)
function should return d, e; function should use extended euclidian algorithm
"""
def get_keys(p, q):
    n = p * q
    phi_n = (p-1) * (q-1)
    e = 3
    while True:
        gcd, s, t = gcd_ex(e, phi_n)
        if gcd == 1:
            break
        e += 2
    d = modulo_expo(e, s, phi_n)
    return (d, e)


"""
c = (m ** e) % n (return c)
where c is the encrypted message (m allowable up to max of a 32 bit unsigned integer, 2^32-1)
"""
def encrypt(m, e, n):
    c = (m**e ) % n
    #print(c)
    return c


"""
m = (c ** d) % n (return m)
where m is the decrypted plain text message (up to 32 bit unsigned integer)
"""
def decrypt(c, d, n):
    #m = (c**d) % n
    #print(m)
    m = modulo_expo(c, d, n)
    return m

def main():
    # Generate primes
    sieve()

    # Generate public and private keys
    p = 74567
    q = 87721
    while p == q:
        q = primes[np.random.randint(0, len(primes))]
    d, e = get_keys(p, q)
    n = p * q

    # Generate random message
    m = np.random.randint(0, 2**32 - 1)

    # Encrypt message
    c = encrypt(m, e, n)

    # Decrypt message
    m_after = decrypt(c, d, n)
    print("decrypt not the problem")

    # Print results
    print("Original message:", m)
    print("Encrypted message:", c)
    print("Decrypted message:", m_after)
    print("Are the messages the same?", m == m_after)


    # Verify that the decrypted message matches the original plaintext message


if __name__ == '__main__': 
    main()