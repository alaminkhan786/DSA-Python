#Algorithms:

# The function "insert_value" takes a list 'my_list', a value to be 'inserted value', and the position at which the value should be inserted 'insert_position'. It returns a new list with the value inserted at the specified position.

# 1. Set an empty list new_list.
# 2. Set variables 'i' for index and 'j' the length of my_list.
# 3. [Repeat Steps 4 to 6] While i <= j
# 4. Check If i = insert_position, add the value to new_list.
# 5. Check If i < j, add the current element of my_list to new_list.
# 6. [Increase Counter] Set i:= i-1.
# [End the loop]
# 7. Return new_list.
# 8. Exit




#----------------------------------

#Python_Code


def insert_value(my_list, value, insert_position):
    new_list = []
    i = 0
    j = len(my_list)
    insert_position = insert_position - 1

    while i <= j:
        if i == insert_position:
            new_list = new_list + [value]
        if i < j:
            new_list = new_list + [my_list[i]]
        i += 1
    return new_list


Array_len = int(input("Enter the array lenght: "))
Array = []

print("Enter the", Array_len, "element of array: ")

for i in range(Array_len):
    Array.append(int(input(f"Enter no. {i+1} element: ")))
    i = i + 1

print("Original Array:", Array)

item = int(input("Value: "))
k = int(input("Position: "))

if 1 <= k <= (len(Array) + 1):
    print("Original Array:", Array)

    Output = insert_value(Array, item, k)
    print("Modified Array:", Output)
else:
    print("Array:", Array)
    print("Inserted position Error!")