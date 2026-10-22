from math import sqrt
from collections import Counter


def get_number(str) -> int:
    while True:
        try:
            num = int(input(str))
            if num > 1:
                return num
        except ValueError:
            print("The number has to be integer")


def find_subdiv_array(num,primes):
    result = []
    i = 0
    while num > 1:
        if num % primes[i] == 0:
            num //= primes[i]
            result.append(primes[i])
        else:
            i += 1
    return result


def lcm_using_factorization(num1, num2):

    max_num = max(num1, num2)
    primes = find_primes(max_num)
    subdiv_factors1 = Counter(find_subdiv_array(num1,primes))
    subdiv_factors2 = Counter(find_subdiv_array(num2,primes))

    lcm_factors = subdiv_factors1 | subdiv_factors2

    
    result = 1
    for factor, count in lcm_factors.items():
        result*=factor**count
    return result

def find_primes(number):

    is_prime:list[bool] = [True] * (number+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(sqrt(number)) + 1):
        if is_prime[i]: # type: ignore
            for j in range(i * i, number + 1, i):
                is_prime[j] = False

    return [i for i,prime in enumerate(is_prime) if prime]
    



if __name__=="__main__":
   num1 = get_number("Input first number: ")
   num2 = get_number("Input second number: ")
   print(lcm_using_factorization(num1,num2))
