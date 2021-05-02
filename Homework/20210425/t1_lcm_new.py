def lcm(a, b):
    m = max(a, b)
    while True:
        if m % a == 0 and m % b == 0:
            print(m)
            break
        m += 1

lcm(int(input()), int(input()))