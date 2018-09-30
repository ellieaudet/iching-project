3half1 = [0, 0, 0]
half2 = [0, 0, 0]
remainder = [0, 0, 0]
points = [0, 0, 0]

half1[0] = int(input("first half? "))
half2[0] = 49 - half1[0]
remainder[0] = (half1[0]-1) % 4 + half2[0] % 4 + 1
print("remainder one is ", remainder[0])

half1[1] = int(input("second half? "))
half2[1] = (49-remainder[0]) - half1[1]
remainder[1] = (half1[1]-1) % 4 + half2[1] % 4 + 1
print("remainder two is ", remainder[1])

half1[2] = int(input("third half? "))
half2[2] = (49-remainder[0]-remainder[1]) - half1[2]
remainder[2] = (half1[2]-1) % 4 + half2[2] % 4 + 1
print("remainder three is ", remainder[2])

for x in range(0,3):
    if remainder[x] == 9 or 8:
        points[x] = 2
    if remainder[x] == 5 or 4:
        points[x] = 3

total = points[0]+points[1]+points[2]
print("total points ", total)