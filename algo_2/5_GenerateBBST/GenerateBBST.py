def FindKeyIndex(tree, key):
    cur_idx = 0
    while cur_idx < len(tree):
        cur_value = tree[cur_idx]
        if cur_value is None:
            return cur_idx * -1
        if key == cur_value:
            return cur_idx
        if key < cur_value:
            cur_idx = 2 * cur_idx + 1
        elif key > cur_value:
            cur_idx = 2 * cur_idx + 2
        else:
            return None


def AddKey(tree, key):
    found_idx = FindKeyIndex(tree, key)
    if found_idx is not None and found_idx <= 0:
        found_idx = found_idx * -1
        tree[found_idx] = key
        return found_idx
    return -1


def GenerateTreeArray(tree, arr):
    if len(arr):
        i = (len(arr)-1)//2
        AddKey(tree, arr[i])
        GenerateTreeArray(tree, arr[:i])
        GenerateTreeArray(tree, arr[i+1:])
    return tree


def calculate_depth(l, d=0):
    depth = 2**(d+1)-1
    if l > depth:
        return calculate_depth(l, d+1)
    return depth


def GenerateBBSTArray(arr):
    arr = sorted(arr)
    tree = [None] * calculate_depth(len(arr))
    return GenerateTreeArray(tree, arr)
