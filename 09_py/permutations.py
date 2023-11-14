def permutations(array: list):
    perm = []
    if len(array) <= 1:
        perm.append(array)
    elif len(array) == 2:
        for i in range(0, 2):
            perm.append([i for i in array])
            a = array.pop(0)
            array.append(a)
    elif len(array) >= 3:
        for i in range(0, len(array)):
            a = [array.pop(i)]
            b = permutations(array)
            array.insert(i, a[0])
            for i in range(0, len(b)):
                b[i] = a + b[i]
            perm += b
    return perm

# list = [1, 2, 3, 4, 5]
# sec_list = [3, 4]
# for i in sec_list:
#     list.append(i)
# print(permutations(list))
# a = list.pop(0)
# print(list)
# list.append(a)
# print(list)
