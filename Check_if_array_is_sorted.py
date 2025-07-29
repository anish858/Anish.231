user_input = input("Enter the number of the list with space : ")
list1 = list(map(int,user_input.split()))
if list1 == sorted(list1):
    print(f"{list1} is a sorted list")
else:
    print(f"{list1} is not a sorted list.")