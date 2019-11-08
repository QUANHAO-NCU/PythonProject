def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            print(num,'这不是素数',i)
            return False
    print(num,'这是素数')
    return True


def len_prime(ls):
    return len(list(filter(is_prime, ls)))


ls = [23, 45, 78, 87, 11, 67, 89, 13, 243, 56, 67, 311, 431, 111, 141]

print(len_prime(ls.copy()))