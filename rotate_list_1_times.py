list1 = [1,2,3,4]
rotation = 1
rotated = list1[rotation:] + list1[:rotation]
joined_str = " ".join(str(x) for x in rotated)
print(joined_str)