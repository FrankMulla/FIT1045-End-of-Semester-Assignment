# Code by Takudzwa Frank Mukarakate, Monash Id: 27754251
# This piece of code accepts a positive integer(N)
# It then generates and prints n+1 rows of pascals triangle
pascalList = []
print("The following program accepts a number 'N' and prints 'N+1' rows of Pascals triangle")
print()

# Populate list() creates a list with n+1 elements of zero
# It then puts the invariant (1 at the start of every triangle)
# Returns the list
def populateList(N):
    zeroList = []
    for count in range(N):
        zeroList.append(0)
    zeroList[0] = 1
    return zeroList

# print pascal is a recursive function it accepts a list L containing 0 or more rows of pascals triangle
# Then generates the next N rows and prints the generated rows every time
# Output are a list of list of pascals triangle with n+1 elements and n+1 Lists(Rows)
def printPascal(passList, N):
    # Base Case checks that no more rows need to be generated
    if N != 0:
        if len(passList) == 0:
            passList.append(populateList(numN+1))
            # print list handles the layout of the final print
            printList(passList[0])
        else:
            currentRow = populateList(numN+1)
            for count in range(1,(len(currentRow))):
                currentRow[count] = passList[-1][count] + passList[-1][count-1]
            printList(currentRow)
            passList.append(currentRow)
        printPascal(passList, N-1)

# printList accepts a List as input and prints it in an acceptable format for Pascals triangle as a string
def printList(List):
    OutputString = ""
    for rowCount in range(len(List)):
        if List[rowCount] != 0:
            OutputString += str(List[rowCount]) + " "
    print(OutputString)
# Setting numN to an incorrect number to improve validation check
numN = -1
# Simple while loop Validating positive input for (N)
while numN < 0:
    numN = int(input("Please enter a number: "))
    if numN < 0:
        print("Error Please enter a positive integer")

printPascal(pascalList, numN+1)



