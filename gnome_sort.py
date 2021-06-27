# Задача 2. Написать тесты для домашних работ из курса «Python 1».
def gnome(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


