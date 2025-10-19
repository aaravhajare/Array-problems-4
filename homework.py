
def fliper(arr) :

    al = len(arr)
    no_of_zero = 0
    no_of_one = 0

    for i in range(0,al) :

        if arr[i] == 0 :
            no_of_zero += 1

        elif arr[i] == 1 :
            no_of_one += 1

    print(f"n.o of 1s required to switch zeros are {no_of_zero}")
    print(f"n.o of 0s required to switch ones are {no_of_one}")

a = [0,0,0,1,0,1,1,0,1,0,1,0]
print(fliper(a))