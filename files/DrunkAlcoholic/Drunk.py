numberOfTimes = int(input())
global steps
for i in range(0, numberOfTimes):
    seconds = int(input())
    steps = 0
    for j in range(1, seconds+1):
        if j % 2 != 0:
            steps += 3
        else:
            steps -= 1
    print(steps)

