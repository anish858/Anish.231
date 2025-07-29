user_input = input("Enter the element of the list with space : ")
list1 = list(map(int,user_input.split()))
unique_element = set(list1)
for item in unique_element:
    print(f"{item} is {list1.count(item)} items in the list.")