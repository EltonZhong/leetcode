def find(arr, num):
    x = 0
    y = 0
    return search(arr, x, y, num)


def search(arr, x, y, given):
    if x < 0 or y < 0:
        return None

    if arr[x][y] == given:
        return x, y

    if arr[x][y] < given:
        x += 1
        y += 1

        return search(arr, x, y, given)

    if arr[x][y] > given:

       return search(arr, x, y - 1, given) or search(arr, x - 1, y, given)

arr = [[1, 2, 3, ], [2, 4, 5], [3, 5, 6]]
print find(arr, 4)
