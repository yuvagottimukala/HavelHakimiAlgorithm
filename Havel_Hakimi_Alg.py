#########YUVA GOTTIMUKALA#########
## WORKS HAVEL-HAKIMI ALGORITHM ##
'''
purpose of the algorithm is to take in a potential degree
sequence from user and be able to determine if its a graphical
degree sequence or not using the mathematically proven
Havel-Hakimi algorithm. 

'''
def havel_hakimi_graph(deg_sequence):
    mDegSeq = deg_sequence 
    mDegSeq.sort(reverse=True)
    #print("Your degree sequence is: ", end='' )
    print(*mDegSeq, sep = ", ")


    WORKS_OR_NOT = False
    index = 0
    iteratingIndex = index + 1
    numAtIndex = mDegSeq[index]
    length = len(mDegSeq)

  
    while(mDegSeq[index] < length ):
        if(mDegSeq[index] > length -index):
            return WORKS_OR_NOT 
    
        while(index < length):
            
            index = 0
            iteratingIndex = index + 1
            if(len(mDegSeq) == 0):
                break
            numAtIndex = mDegSeq[index]
            length = len(mDegSeq)
            try:
                while(iteratingIndex <= numAtIndex):
                    mDegSeq[iteratingIndex] -= 1
                    iteratingIndex += 1
            except:
                return(WORKS_OR_NOT)  
            if(len(mDegSeq) == 0):
                break
            mDegSeq[index] = 0
            mDegSeq.sort(reverse=True)
            mDegSeq = [i for i in mDegSeq if i != 0]
            print(*mDegSeq, sep = ", ")
        
    print(*mDegSeq, sep = ", ")
    if (len(mDegSeq) == 0):
        WORKS_OR_NOT = True

    return(WORKS_OR_NOT)


