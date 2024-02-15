#Algorithms:

# The function "bubble_sort" takes a list 'my_list' as input and performs bubble sort on it. It returns the sorted list.
# 1.	Set variable 'n' to the length of my_list.
# 2.	[Outer Loop – 3 to 6 steps] Iterate over each element in the range from 0 to n:
# 3.	[Inner Loop – 4 and 5 steps] Iterate over each element in the range from 0 to n-1:
# 4.	Check if the current element at index j is greater than the next element at index j+1.
# 5.	If true, swap the elements at indices j and j+1 in my_list.
# [End of Inner loop]
# 6.	Return the sorted my_list.
# [End of Outer loop]
# 7.	Exit.




#----------------------------------

#Python_Code

def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n):
        for j in range(n - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list

Array_len = int(input("Enter the array lenght: "))
Array = []

print("Enter the", Array_len, "element of array: ")

for i in range(Array_len):
    Array.append(int(input(f"Enter no. {i+1} element: ")))
    i = i + 1


print("Original Array:", Array)

sorted_array = bubble_sort(Array)
print("Sorted Array:", sorted_array)