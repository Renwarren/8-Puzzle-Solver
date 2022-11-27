#count the number of inversions       
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def isSolvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==1):
        return True
    return False


#1,8,2,0,4,3,7,6,5 is solvable
#2,1,3,4,5,6,7,8,0 is not solvable
