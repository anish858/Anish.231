user_input = input("Enter the numbers separated by space : ")
list1 = list(map(int,user_input.split()))
list1.sort(reverse=True)
print(f"The secoend largest element is {list1[1]}")