
def area(a):
    '''Вычисляет площадь квадрата по стороне'''
    return a * a


def perimeter(a):
    '''Вычисляет периметр квадрата по стороне'''
    return 4 * a


def sift_down(data, size, i):
    while 2 * i + 1 < size:
        l = 2 * i + 1
        r = l + 1
        largest = l
        if r < size and data[r] > data[l]:
            largest = r
        if data[i] >= data[largest]:
            break
        data[i], data[largest] = data[largest], data[i]
        i = largest


def build_heap(data):
    size = len(data)
    for i in range(size // 2, -1, -1):
        sift_down(data, size, i)


def heap_sort(data):
    size = len(data)
    build_heap(data)
    # print(data)
    for i in range(size - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        size -= 1
        sift_down(data, size, 0)
    return data


n = int(input())
a = list(map(int, input().split()))

heap_sort(a)
print(*a)
