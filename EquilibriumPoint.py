
def equibrilimpoint(arr, al) :

    leftside = 0
    rightside = 0 

    for i in range(al) :

        leftside = 0 
        rightside = 0

        for j in range(i) :
            leftside += arr[j] 

        for j in range(i+1 , al) :

            rightside += arr[j] 

        if leftside == rightside :
            return arr[i]
        
    return -1

a = [1,1,4,1,1]
print(equibrilimpoint(a , len(a)))