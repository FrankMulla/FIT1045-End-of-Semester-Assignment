# Code by Takudzwa Frank Mukarakate, Monash Id: 27754251
# This piece of code accepts a file of comma separated values, containing database of music
# It can sort, find and print elements of file in a nice format

# Functions
# print list () prints the list in a nice format
# In the case that a another type is passed it just prints it normally
def PrintList(Output):
    if type(Output) == list:
        for line in Output:
            print("Title: " + str(line[0]) + "  |Artist: " + str(line[1]) + "  |Genre: " + str(line[2]) + " |Price : $" + str(line[3]))
    else:
        print(Output)

# Create database() takes the values from the file and puts them into list of lists containing song details
def CreateDatabase():
    CdFile = open("CD_Store.txt")
    for line in CdFile:
        CdDB.append(line.split(","))
        BaseDB.append(line.split(","))
    for count in range(0, len(CdDB)):
        CdDB[count][3] = float(CdDB[count][3].strip("\n"))
        BaseDB[count][3] = float(BaseDB[count][3].strip("\n"))
    CdFile.close()

# Display menu() Prints the main menu for easy interaction
def DisplayMenu():
    print('''
1. Print List of CDs
2. Sort CDs by Title
3. Sort CDs by Artist
4. Sort CDs by Genre
5. Sort CDs by Price
6. Find All CDs by Title
7. Find All CDs by Artist
8. Find All CDs by Genre
9. Find All CDs with Price at Most X.
10. Quit''')


# Considering possible duplicates the Binary search was not suitable for finding duplicates for solutions
# Therefore Only used for title
# BinarySearch() is a recursive function that takes an array a target and a respective index
# It return the record that matches the target or a string error message if its not found
def BinarySearch(searchArray, Target, searchIndex):
    midInd = len(searchArray)//2
    if searchArray[midInd][searchIndex] == Target:  # Base cases if the target is found or array has one element
        Record = searchArray[midInd]
    elif len(searchArray) == 1:
        Record = "\n Error!!!! - This item doesn't exist in the list (Check spelling and try again) \n"
    else:
        if Target < searchArray[midInd][ searchIndex]:
            Record = BinarySearch(searchArray[:midInd], Target, searchIndex)
        else:
            Record = BinarySearch(searchArray[midInd:], Target, searchIndex)
    return Record

# SequentialSearch() searches through sorted list of elements and returns all instances of the target if any or error
# The function takes the database array, search target and an index for element searching
def SequencialSearch(searchArray, Target, searchIndex):
    soln = []
    Found = False
    for i in range(len(searchArray)):
        if Target == searchArray[i][searchIndex]:
            Found = True
            soln.append(searchArray[i])
        else:
            if Found == True:   # All entries matching the target have been found so we can  escape
                break
            else:
                Found = False
    if Found:
        return soln
    else:
        return "\n Error!!!! - This item doesn't exist in the list (Check spelling and try again) \n"

# PriceList() takes an array and a target and returns all the items below the target price
#  or an error message if there are non
def PriceList(searchArray, targetPrice):
    priceList = []
    if targetPrice < searchArray[0][3]:     # Check if target is less than lowest price
        return "\n Error!!!! - This are no items below this price\n"
    elif targetPrice > searchArray[-1][3]:  # Check if target is greater than highst price
        return searchArray
    else:
        for i in range(1,len(searchArray)):
            if targetPrice < searchArray[i][3]:
                break
        if i > 0:   #   Adds all elements before i (taking advantage of the sort)
            priceList.extend(searchArray[:i])
            return priceList

# merge() takes two sorted lists of one or more elements and returns a combined sorted list (merged)
def merge(leftList, rightList, sortIndex):
    merged = []
    L = 0
    R = 0
    for i in range((len(leftList)+len(rightList))):
        if leftList[L][sortIndex] <= rightList[R][sortIndex]:
            merged.append(leftList[L])
            L+=1
        else:
            merged.append(rightList[R])
            R+=1
        #   Checks to see if any of the lists are finished to then just append1(extend) the other list elements
        if L == len(leftList):
            merged.extend(rightList[R:])
            break
        elif R == len(rightList):
            merged.extend(leftList[L:])
            break
    return merged

# mergeSort() is a secondary "interactive" recursive function for merge sorting it splits the list into two every iteration
# then merges them and returns the sorted list
def mergeSort(List, sortIndex):
    if len(List) != 1:  # Base case checks length of the lisy
        midInd = len(List)//2
        L = mergeSort(List[0:midInd], sortIndex)
        R = mergeSort(List[midInd:len(List)], sortIndex)
        return merge(L,R, sortIndex)
    else:
        return List

# DB Sort () is the main "interaction" function linked to the merge sort
# It Takes parameter determining what element sort was selected by user
# sets up parameters and returns sorted list by "Specified Field"
def DBSort(Type):
    if Type == 2:
        print("Sorting Completed :By Title")
        return mergeSort(CdDB, 0)
    elif Type == 3:
        print("Sorting Completed :By Artist")
        return mergeSort(CdDB, 1)
    elif Type == 4:
        print("Sorting Completed :By Genre")
        return mergeSort(CdDB, 2)
    else:
        print("Sorting Completed :By Price")
        return mergeSort(CdDB, 3)

# DB Find () is the main "interactive" function for searching the database
# Uses to the type parameter to determine target search fields and target to set parameters
# Returns the found record or error message if not found
def DBFind(Type):
    if Type == 6:
        print("Find by Title")
        SearchTarget = input("Please enter the title of the song you're looking for : ")
        print()
        ##return BinarySearch(mergeSort(CdDB, 0),SearchTarget, 0)     # Assumes all titles are distinct
        return SequencialSearch(mergeSort(CdDB, 0),SearchTarget, 0)
    elif Type == 7:
        print("Find by Artist")
        SearchTarget = input("Please enter the artist of the song(s) you're looking for : ")
        print()
        return SequencialSearch(mergeSort(CdDB, 1),SearchTarget, 1)
    elif Type == 8:
        print("Find by Genre")
        SearchTarget = input("Please enter the genre of the song(s) you're looking for : ")
        print()
        return SequencialSearch(mergeSort(CdDB, 2),SearchTarget, 2)
    else:
        print("Find by Max Price")
        SearchTarget = float(input("Please enter the max price of the song(s) you're looking for : "))
        print()
        return (PriceList(mergeSort(CdDB, 3), SearchTarget))

# Variables
CdDB = []          # keeps the CD list of List
BaseDB = []        # Holds the original loaded file unedited
StopOpt = False    # Keeps track of users decision to quit

# Actual program
CreateDatabase()
while not StopOpt:  # program runs while user doesnt want to quit
    DisplayMenu()
    print()
    MenuOpt = int(input("Please Enter Number Option: "))
    if MenuOpt == 1:
        PrintList(CdDB)
    elif MenuOpt < 6:
        CdDB = DBSort(MenuOpt)
    elif MenuOpt < 10:
        PrintList(DBFind(MenuOpt))
    elif MenuOpt == 10:
        print("Thank You :)")
        StopOpt = True
        quit()
    else:
        print("Sorry invalid input!! Please try again(1 - 10)")
        print()
