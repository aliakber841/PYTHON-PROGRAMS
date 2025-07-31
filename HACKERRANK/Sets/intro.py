def average(array):
     set_array=set(array) 
     sum_height=sum(set_array)
     len_height=len(set_array)  
     average=round(sum_height/len_height,3)  
     return average 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)