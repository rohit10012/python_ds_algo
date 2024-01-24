#This program will merge two array inm ascending order

def mergeArrays(ArrayA, ArrayB):

    return sorted(set(ArrayA + ArrayB))


a = [2,4,8,0,1,2,6,7]
b = [3,1,2,7,8,0,5,4,1]
c = mergeArrays(a,b)
print(c)
