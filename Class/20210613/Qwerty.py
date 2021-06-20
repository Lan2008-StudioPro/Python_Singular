alls = []
while True:
    name = input()
    subject = input()
    try:
        score = int(input())
    except ValueError:
        print('Try again.')
    else:
        for i in alls:
            if name in i:
                i.append([subject, score])
                print(alls)
                break
        else:
            alls.append([name, [subject, score]])
            print(alls)