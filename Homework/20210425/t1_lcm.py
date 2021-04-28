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
        list_lcm_m = []
        list_lcm_n = []
        cfactors = []
        lcmnum = 1
        while m > 1:
            for a in range(2, m):
                while m % a == 0:
                    list_lcm_m.append(a)
                    m /= a
            else:
                list_lcm_m.append(m)
        cfactors.extend(list_lcm_m)
        while n > 1:
            for b in range(2, n):
                while n % b == 0:
                    list_lcm_n.append(b)
                    n /= b
            else:
                list_lcm_n.append(n)
        cfactors.extend(list_lcm_n)
        for factorcheck in cfactors:
            if list_lcm_m.count(factorcheck) > list_lcm_n.count(factorcheck):
                lcmnum = factorcheck ** list_lcm_m.count(factorcheck)
            else:
                lcmnum = factorcheck ** list_lcm_n.count(factorcheck)
        print(int(lcmnum))

lcm(45, 72)