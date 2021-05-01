'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
def lcm(m, n):
    import sys
    try:
        int(m)
        int(n)
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    else:
        m = int(m)
        n = int(n)
        list_lcm_m = [m]
        list_lcm_n = [n]
        cfactors = []
        lcmnum = 1
        if m > 1 and type(m) == int:
            for x in range(2, m):
                if m % x == 0:
                    list_lcm_m.remove(m)
                    for a in range(2, m):
                        while m % a == 0:
                            list_lcm_m.append(a)
                            m /= a
        else:
            sys.exit('\nValueError - input should be a natural number')
        cfactors.extend(list_lcm_m)
        if n > 1 and type(n) == int:
            for y in range(2, n):
                if n % y == 0:
                    list_lcm_n.remove(n)
                    for a in range(2, n):
                        while n % a == 0:
                            list_lcm_n.append(a)
                            n /= a
        else:
            sys.exit('\nValueError - input sholud be a natural number')
        cfactors.extend(list_lcm_n)
        cfactors = set(cfactors)
        for fcheck in cfactors:
            if list_lcm_m.count(fcheck) > list_lcm_n.count(fcheck):
                lcmnum *= fcheck ** list_lcm_m.count(fcheck)
            else:
                lcmnum *= fcheck ** list_lcm_n.count(fcheck)
        print(int(lcmnum))

lcm(input(), input())