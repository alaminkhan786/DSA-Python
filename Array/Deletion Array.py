#Algorithms:

# The function "delete index" takes a list 'my_list', and the position at which the value should be inserted 'delete_position'. It returns # a new list with removes the element at the specified position in the input list and returns a new list without that element.
# 1. Set an empty list new_list.
# 2. Set variables 'i' for index and 'j' the length of my_list.
# 3. [Repeat Steps 4 and 5] While i < j
# 4. Check If i != delete_position, add the value’s to new_list one by one.
# 5. [Increase Counter] Set i:= i-1.
# [End the loop]
# 7. Return new_list.
# 8. Exit



#----------------------------------

#Python_Code

def delete_index(my_list, delete_position):
    new_list = []
    i = 0
    j = len(my_list)
    delete_position = delete_position - 1

    while i < j:
        if i != delete_position:
            new_list = new_list + [my_list[i]]
        i += 1

    return new_list


Array_len = int(input("Enter the array lenght: "))
Array = []

print("Enter the", Array_len, "element of array: ")

for i in range(Array_len):
    Array.append(int(input(f"Enter no. {i+1} element: ")))
    i = i + 1


k = int(input("Position: "))

if 1 <= k < (len(Array) + 1):
    print("Original Array:", Array)

    Output = delete_index(Array, k)
    print("Modified Array:", Output)
else:
    print("Array:", Array)
    print("Delete position Error!")