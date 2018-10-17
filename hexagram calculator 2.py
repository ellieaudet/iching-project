import inflect
p = inflect.engine()


total = [0 for i in range(7)]
a = 0


def printsticks(count):
    stickstring = ""
    for x in range(0, count):
        stickstring += "|"
        x += 1
    return stickstring


def linedetermine(i):
    if total[i] == 6:
        return "--x--"
    if total[i] == 8:
        return "-- --"
    if total[i] == 9:
        return "--o--"
    if total[i] == 7:
        return "-----"


while a < 6:
    emptyarray = [[0 for i in range(3)] for i in range(4)]
    half1, half2, remainder, points = list(emptyarray)
    remainder = [0, 0, 0]

    for x in range(0, 3):

        half1[x] = int(len(input("\n"+"half number "+p.number_to_words(x + 1)+"\n"+printsticks(49-remainder[0]-remainder[1])+"\n")))
        y, z = x, 49
        while y > 0:
            z -= remainder[y-1]
            y -= 1
        half2[x] = z - half1[x]
        r1 = (half1[x] - 1) % 4
        if r1 == 0:
            r1 = 4
        r2 = half2[x] % 4
        if r2 == 0:
            r2 = 4
        remainder[x] = r1 + r2 + 1
        print("remainder "+p.number_to_words(x + 1)+" is ", remainder[x])

    print("\n")
    print(remainder[0], remainder[1], remainder[2])

    for x in range(3):
        if remainder[x] == 9:
            points[x] = 2
        if remainder[x] == 8:
            points[x] = 2
        if remainder[x] == 5:
            points[x] = 3
        if remainder[x] == 4:
            points[x] = 3

    total[a] = points[0]+points[1]+points[2]
    print("point count:" + str(total[a]))
    print(linedetermine(a))
    print("\n")
    a += 1


i = 5
while i >= 0:
    print(linedetermine(i))
    i -= 1
