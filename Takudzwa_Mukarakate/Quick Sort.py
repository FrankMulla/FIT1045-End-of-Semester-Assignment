Array = []
def quickSort(List):
    end = len(List)
    

def quickSplit(List, start, end):
    pivot = List[start]
    boundary = start
    for sortIndex in range(end):
        if boundary < List[sortIndex]:
            boundary += 1
            List[boundary], list[sortIndex] = list[sortIndex], list[boundary]
    return List

