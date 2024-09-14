list = [1, 2, 3, 9, 4, 5]

# Initialize with the smallest possible values
large_num = float('-inf')
second_large = float('-inf')

for num in list:
    if num > large_num:
        second_large = large_num
        large_num = num
    elif num > second_large and num != large_num:
        second_large = num

print("Largest number:", large_num)
print("Second largest number:", second_large)
