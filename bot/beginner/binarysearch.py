#Hunter Esler 8/27/2020
#Simple binary search for sorted array, very fast

#utilizes 
#   binary searching arrays

#basic python learning

#Idea from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners

#Usage: py binarysearch.py num.. assumes correct input
#maxrange: must be greater than 0
 
import sys, os, time

num = int(sys.argv[1])

a = [x for x in range(1000000)] # big array to search through


#searches through array by keeping track of a few variables. only works with an array
arrlen = len(a)
searchlen = arrlen#our search space length
mid = int(max((arrlen/2) - 1,0))#our current position in the search
found = -1#index we found it at
lsize = mid#the size of space on our left
rsize = searchlen - lsize#right

iterations = 0

starttime = time.perf_counter()

for i in range(arrlen): # arrlen being reached means something funky
    iterations = iterations + 1
    if mid > arrlen or mid < 0:#out of bounds
        break
    val = a[mid]
    if (val==num):#found our number
        found = mid
        break
    if (num < val):
        searchlen = lsize
        lsize = int(lsize / 2)
        mid = mid - lsize

        #if even... need to have different sizes
        if searchlen%2==1:
            rsize = lsize
        else:
            rsize = lsize+1
            mid = mid - 1
    else:
        searchlen = rsize
        rsize = int(searchlen / 2)
        lsize = int(searchlen / 2)
        mid = mid + rsize
        #same here
        if searchlen%2==0:
            mid = mid + 1          

endtime = time.perf_counter()
if found > -1:
    print(f"Found our number after {iterations} iterations in {endtime - starttime} seconds!")
else:
    print("Number not found.")

