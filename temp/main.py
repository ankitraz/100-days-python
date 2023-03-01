def binarysearch(l, target):
    start = l[0]
    end =   l[len(l)-1]

    while start <= end:
        mid = (start+end)//2

        if target > l[mid]:
            start = mid + 1

        elif target < l[mid]:
            end = mid - 1

        else:
            return mid


def linear_search(l,target):
    '''This function is used to find element.'''
    for index,i in enumerate(l):
        if i == target:
            return index




ls = [2,4,6,7,8,9]
ans = binarysearch(ls,7)
ans2 = linear_search(ls,7)
print (ans2)