def print_number(n):
    if n == 0:
        return 0
    
    print(n)
    print_number(n - 1)


def print_number_v2(n):
    if n == 0:
        return 0
    
    print_number(n - 1)
    print(n)

if __name__ == "__main__":
    # print_number(5)
    print_number_v2(5)