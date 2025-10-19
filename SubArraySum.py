
def SubArraySum(sum , arr , al) :

    for i in range(al) :

        cur_sum = arr[i] 


        j = i + 1

        while j <= al :

            if cur_sum == sum :

                print("Sum found between")
                print(f"{i} - {j-1}")
                print(f"{arr[i]} - {arr[j-1]}")
                return 1

            if cur_sum > sum or j == al :
                break

            cur_sum += arr[j] 
            j += 1


    print("no sub array found")
    return 0 

a = [2,3,4,5,2,3,2,5]
s = 11
SubArraySum(s , a , len(a))
