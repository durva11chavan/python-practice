def list_operations():
    nums = [1, 2, 3, 4]

    nums.append(5)
    nums.remove(2)

    print("List:", nums)

    # Reverse list
    print("Reversed:", nums[::-1])