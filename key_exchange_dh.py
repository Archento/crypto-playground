""" Diffie-Hellman Key Exchange
(perfect forward secrecy)

1. Establish common variables
- Alice and Bob agree on a Prime number: P, and a Base: G.
- These numbers are NOT secret, they can be known by an evesdropper.
- P must be a prime number, and G is a Primitive root modulo.

2. Choose private variables
- Alice and Bob each randomly select their own private integer.
- Those variables are never shared or made public

3. Calculate and send individual public keys
- Alice calculates 'A = g^a mod p' and sends it to Bob publicly.
- Bob calculates 'B = g^b mod p' and sends it to Alice also publicly.

4. Calculate common/shared secret
- Alice computes shared secret, 's = B^a mod p'.
- Bob computes shared secret, 's = A^b mod p'.

-> Result
Alice and Bob now have a shared secret key, s
An evesdropper can not know the secret although he knows p, b, A, and B.
"""
from lib.prime_primitive_root import is_prime, find_primitive

sharedPrime = 0 # p
aliceSecret = 648225  # a
bobSecret = 158368    # b

while True:
    sharedPrime = int(input("Please input a prime number (e.g. 23 or 761): "))
    if is_prime(sharedPrime):
        break
    print(f"{sharedPrime} is no prime number. Please try again.\n")

sharedBase = find_primitive(sharedPrime) # g

# Begin
print("Publicly shared variables:")
print(f"\tPrime: {sharedPrime}")
print(f"\tBase:  {sharedBase}")

# Generate public parts
print("\nCalculate and send base^private_part % prime to the other person:")
ALICE_PRIV = (sharedBase**aliceSecret) % sharedPrime
print(f"\tAlice sends publicly: {ALICE_PRIV}")
BOB_PRIV = (sharedBase**bobSecret) % sharedPrime
print(f"\t  Bob sends publicly: {BOB_PRIV}")

# Generate private parts
print("\nPrivately calculate public_counterpart^private_secret % prime:")
alicesSharedSecret = (BOB_PRIV**aliceSecret) % sharedPrime
print(f"\tAlices shared Secret: {alicesSharedSecret}")
bobsSharedSecret = (ALICE_PRIV**bobSecret) % sharedPrime
print(f"\t  Bobs shared Secret: {bobsSharedSecret}")
