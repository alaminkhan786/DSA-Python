#Algorithms:

# 1.	Set a list named 'list' with values.
# 2.	Get user input for the search value and store it in the variable 'search'.
# 3.	Set a variable 'found' to False. (Because, Program hasn’t started yet.)
# 4.	Initialize a variable 'i' to 0 for indexing.
# 5.	[Use FOR loop] For each 'item' in 'my_list':
# a.	Check if 'search' == 'item'.
# b.	If equal, set 'found' to True, break out of the loop.
# c.	Set i:= i+1.
# [End the loop]
# 6.	Check if  'found' is True:
# a.	Print the search value, ‘position’, and a message indicating it is found.
# 7.	If 'found' is False:
# a.	Print a message indicating the search value is not found.
# 8.	Exit.




#----------------------------------

#Python_Code

list_len = int(input("Enter the list lenght: "))
list = []

print("Enter the", list_len, "element of list...")

for i in range(list_len):
    list.append(input(f"Enter no. {i+1} element: "))
    i = i + 1

print("Original list:", list)


search = input("Enter your Search value: ")
found = False
i = 0
for item in list:
    if search == item:
        found = True
        break
    i += 1

if found == True:
    print(search, "is found and ", search, "position", i + 1)
else:
    print(search, "is not found")