def tuplesOfOne(lst):
    """
    return a list of tuples identifying start and end of 1's
    in a list of 0 and 1. 
    
    
    aList = [0, 1, 1, 1, 0, 1, 1, 0]
    tuplesOfOne(aList) --> [(1, 3), (5, 6)]
    
    """
    # list to store tuples
    tupList = []
    
    # indices to keep track of start and end of 1
    firstIndex = 0
    lastIndex = 0
    idx = 0
    while(idx < len(lst)):
        print "Index now:" , idx
        if lst[idx] == 1:
            # set firstIndex to first occurence of 1 since last iteration
            firstIndex = idx 
            lastIndex = idx 
            
            print "first index:", firstIndex
            
            while(lst[lastIndex + 1] == 1):
                lastIndex += 1


            print "last index:", lastIndex
                
            # we have found a 0 so stop
            if(lst[firstIndex] == 1 and lst[lastIndex] == 1):
                tempTup = (firstIndex, lastIndex)
                print "adding:" , tempTup
                tupList.append(tempTup)
                idx = lastIndex

        idx += 1                
        print "------------"

    return tupList

aList = [0, 1, 1, 1, 0, 1, 1, 0]
print tuplesOfOne(aList)
            
                