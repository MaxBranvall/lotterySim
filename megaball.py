import random
import time

winningSet = set()
winningMegaball = []
myNumbers = []
myMegaball = []
userWon = False

winningMegaball = 5
myMegaball = 5

startTime = time.time()

def generateWinningNumbers():
    def generateWinningMegaball():
        x = random.randint(1,25)

        return x

    winningMegaball = generateWinningMegaball()

    iterationNumber = 0
    while iterationNumber < 5:
        ran = random.randint(1,70)

        if ran not in winningSet:
            winningSet.add(ran)
            iterationNumber += 1

    return winningSet, winningMegaball

def generateUserNumbers():
    def generateUserMegaball():
        x = random.randint(1,15)

        return x

    myMegaball = generateUserMegaball()

    iterationNumber = 0
    while iterationNumber < 5:
        ran = random.randint(1,75)

        if ran not in myNumbers:
            myNumbers.append(ran)
            iterationNumber += 1

    return myNumbers, myMegaball

winningNumbers, winningMegaball = generateWinningNumbers()
print(f'{winningNumbers} + {winningMegaball}\n\n\n')

iterationNumber = 0
time.sleep(5)

while userWon == False:
    myNumbers.clear()

    userNumbers, userMegaball = generateUserNumbers()
    print(f'{iterationNumber}. {userNumbers} + {userMegaball}')

    iterationNumber += 1
    winningNumber = 0

    for num in userNumbers:
        if num in winningNumbers:
            winningNumber += 1

            if winningNumber == 5 and userMegaball == winningMegaball:
                userWon = True
                endTime = time.time()

                print('Winner!')
                print(f'Time Elapsed: {int(endTime - startTime) / 60}')
        else:
            pass
