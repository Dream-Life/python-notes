arr = [5,2,1,8,4,7,3,6]

def select_sort(items, comp=lambda x,y: x<y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]
    return items

# def bubble_sort(items, comp=lambda x,y:x<y):
#     items = items[:]
#     for i in range(len(items)-1):
#         for j in range(len(items)-1):
#             if comp(items[j],items[j+1]):
#                 items[j],items[j+1] = items[j+1],items[j]
#     return items

# def bubble_sort(items, comp=lambda x, y: x > y):
#     """冒泡排序"""
#     items = items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range( len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 print(items)
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if not swapped:
#             break
#     return items

def bubble_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

if __name__ == "__main__":
    print('select sort: %s' % select_sort(arr))
    print('bubble sort: %s' % bubble_sort(arr))
