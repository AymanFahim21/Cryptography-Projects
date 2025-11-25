import random

# --- 1. MRT: Miller-Rabin Primality Test [cite: 3, 4, 5] ---
def powmod_sm(base, exponent, modulus):
    #  Square and multiply algorithm
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def is_prime_mrt(n, k=40):
    # [cite: 4] Check primality using Miller-Rabin
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = powmod_sm(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = powmod_sm(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# --- 2. EA: Euclidean Algorithm  ---
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# --- 3. EEA: Extended Euclidean Algorithm  ---
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def get_mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi



