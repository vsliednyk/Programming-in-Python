from math import sqrt


def get_number() -> int:
    while True:
        try:
            num = int(input("Give a number n: "))
            if num > 1:
                return num
        except ValueError:
            print("The number has to be integer")



def find_primes(number):

    is_prime:list[bool] = [True] * (number+1)
    is_prime[0] = is_prime[1] = True

    for i in range(2, int(sqrt(number)) + 1):
        if is_prime[i]: # type: ignore
            for j in range(i * i, number + 1, i):
                is_prime[j] = False

    return [i for i,prime in enumerate(is_prime) if prime]


if __name__=="__main__":
    primes = find_primes(get_number())
    print("Primes of given number are: ",primes)
