if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2=list(arr)
    if n>1:
        max_element=max(arr2)
        arr2=[x for x in arr2 if x!=max_element]
        print(max(arr2))
    else:
        print("No runner up!")
