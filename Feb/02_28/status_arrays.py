"""The status of each element of an array of integers can 
be determined by its position in the array and the value 
of the other elements in the array. The status of an element 
E in an array of size N is determined by adding the 
position P, 0 <= P < N, of the element in the array to the 
number of array elements in the array that are less than E.

For example, consider the array containing the integers: 
6 9 3 8 2 3 1. 
The status of the element 8 is 8 because its position 
is 3 and there are 5 elements in the array that are less than 8.

You will return the elements of the original array from low to 
high status order. In the event there is a tie for status of 
two or more elements, you will output them in order of appearance 
in the array.

"""

def status(nums):
    # empty dictionary that contains status, array element
    status_dict = {}
    # address outliers:
    if len(nums) == 0:
        return "No items found"
    else:
        for n in nums:
            # 1. Find the position of num in the array 
            position = nums.index(n)

            # 2. Find the elements that are less than n
            count = 0
            x  = n
            for i in range(len(nums)):
                if x > nums[i]:
                    count += 1
            
            # adding n, count to dictionary
            status_dict[n] = count
    
    # 4. Get list ordered by status
    result = []
    lst = []
    for k,v in status_dict.items():
        lst.append(status_dict[k])
    
    for x in sorted(lst):
        for k,v in status_dict.items():
            if x == v:
                result.append(k)
    return result
        

print(status([0, 10, 4, 5, 2]))
# print(status([]))

