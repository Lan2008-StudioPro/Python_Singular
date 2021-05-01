'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
def lcm(m, n):
    try:
        m = int(m)
        n = int(n)
    except ValueError:
        print('ValueError')
    else:
        list_lcm_m = [m]
        list_lcm_n = [n]
        cfactors = []
        lcmnum = 1
        while m > 1:
            for x in range(2, m):
                if m % x == 0:
                    list_lcm_m.remove(m)
                    for a in range(2, m):
                        while m % a == 0:
                            list_lcm_m.append(a)
                            m /= a
        cfactors.extend(list_lcm_m)
        print(list_lcm_m)
        while n > 1:
            for y in range(2, n):
                if n % y == 0:
                    list_lcm_n.remove(n)
                    for a in range(2, n):
                        while n % a == 0:
                            list_lcm_n.append(a)
                            n /= a
        cfactors.extend(list_lcm_n)
        print(list_lcm_n)
        cfactors = set(cfactors)
        print(cfactors)
        for fcheck in cfactors:
            if list_lcm_m.count(fcheck) > list_lcm_n.count(fcheck):
                lcmnum *= fcheck ** list_lcm_m.count(fcheck)
            else:
                lcmnum *= fcheck ** list_lcm_n.count(fcheck)
            print(lcmnum)
        print(int(lcmnum))

lcm(18, 8)