import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    with open(fileName, "w") as file:
        for n in inputList:
            file.write(f"{n}\n")
    return fileName


def sortNames(sourceName, targetName):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    randomList =[]

    with open(sourceName, "r") as sourceFile:
        with open(targetName, "w") as targetFile:
            for line in sourceFile:
                randomList.append(line)
            randomList.sort()
            for n in randomList:
                targetFile.write(n)

def get_average(numbers):
    return sum(numbers)/ len(numbers) if numbers else 0




def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    scoreList = []
    with open("scores.txt", "a") as file:
        file.write(f"{newScore}\n")
    with open("scores.txt", "r") as file:
        for line in file:
            print(line)
            scoreList.append(int(line))
    avg = get_average(scoreList)
    return(avg)

print(highScore(30))

