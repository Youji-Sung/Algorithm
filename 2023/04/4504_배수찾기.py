n = int(input())
while True:
    num = int(input())
    if num == 0:
        break
    if num%n == 0:
        print(f'{num} is a multiple of {n}.')
    if num%n != 0:
        print(f'{num} is NOT a multiple of {n}.')
