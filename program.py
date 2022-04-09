print("Candidate: Talha Mehmet KARAMUK")


def getInput(fileName):
    with open(fileName, 'r') as f:
        inputArray = []
        counter = 0
        for lines in f:
            counter += 1
            line = lines.strip().split(" ")
            arrRow = []
            for num in line:
                if isPrime(int(num)):
                    arrRow.append(float('-inf'))
                else:
                    arrRow.append(int(num))
            inputArray.append(arrRow)
        for r in range(counter):
            for c in range(counter - r - 1, 0, -1):
                inputArray[r].append(c)
        return inputArray


def isPrime(num):
    x = 0
    i = 2
    while i <= num / 2:
        if num % i == 0:
            x = 1
            break
        i += 1
    if x == 0:
        return True
    else:
        return False


def findMaxPathSum(arr):
    for row in range(len(arr) - 2, -1, -1):
        for col in range(0, row + 2 - 1):
            if arr[row + 1][col] == float('-inf') and arr[row + 1][
                    col + 1] == float('-inf'):
                continue
            elif not arr[row + 1][col] == float('-inf') and not arr[row + 1][
                    col + 1] == float('-inf'):
                arr[row][col] += max(arr[row + 1][col], arr[row + 1][col + 1])
            elif arr[row + 1][col] == float('-inf'):
                arr[row][col] += arr[row + 1][col + 1]
            else:
                arr[row][col] += arr[row + 1][col]
    return arr[0][0]


def main():
    arr = getInput("numbers.txt")
    result = findMaxPathSum(arr)
    if result == float('-inf'):
        print("No path found")
    else:
        print("Max path sum is: " + str(result))


main()
'''
numbers.txt file:

215
193 124
117 237 442
218 935 347 235
320 804 522 417 345
229 601 723 835 133 124
248 202 277 433 207 263 257
359 464 504 528 516 716 871 182
461 441 426 656 863 560 380 171 923
381 348 573 533 447 632 387 176 975 449
223 711 445 645 245 543 931 532 937 541 444
330 131 333 928 377 733 017 778 839 168 197 197
131 171 522 137 217 224 291 413 528 520 227 229 928
223 626 034 683 839 053 627 310 713 999 629 817 410 121
924 622 911 233 325 139 721 218 253 223 107 233 230 124 233

'''
