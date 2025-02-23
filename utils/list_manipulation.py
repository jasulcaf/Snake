def print_list(arr):
    curr = "".join(arr)
    print(curr)

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    res = []
    for i in range(0, len(arr1)):
        res.append(arr1[i] + arr2[i])
    return res