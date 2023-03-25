class GFG:
    def max_neighbors(self, arr, n):
        # arr = [1, 3, 20, 4, 1, 0]
        deepak = []
        for i in range(1,n):
            if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
                deepak.append(arr[i])
        return deepak

    def rearrange_3_var(self, arr, n):
        # arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
        start = i = 0
        end = n-1
        while(i<=end):
            if(arr[i]==0):
                arr[start], arr[i] = arr[i], arr[start]
                i+=1
                start+=1
            elif(arr[i]==1):
                i+=1
            else:
                arr[end], arr[i] = arr[i], arr[end]
                end -= 1
    
    def subarray_sum(self, arr, n, sum):
        # arr = [1, 4, 20, 3, 10, 5] sum = 33
        temp_sum = arr[0]
        start = 0
        i = 0
        while(i<n):
            if(temp_sum == sum):  return start,i
            elif(temp_sum>sum and start<i):
                temp_sum -= arr[start]
                start += 1
            else:
                i += 1
                if(i==n):   return -1
                else:
                    temp_sum += arr[i]
    
    def first_negative_postive(self, arr, n):
        # arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
        # OUTPUT =  -12 -13 -5 -7 -3 -6 5 6 11
        start = 0
        for i in range(n):
            if(arr[i]<0):
                arr[start], arr[i] = arr[i],arr[start]
                start +=1 
    
    def cyclically_rotate_right_1(self, arr, n):
        # arr = [1, 2, 3, 4, 5]
        for i in range(n):
            index = (i+1)%n
            print(arr[index], end=" ")
    
    def count_pairs_given_sum(self, arr, sum):
        # arr = [1, 5, 7, -1] ans sum=6
        count = 0
        check_dict = {}
        for ele in arr:
            if sum-ele in check_dict:
                count += check_dict[sum-ele]
            if ele in check_dict:
                check_dict[ele] += 1
            else:
                check_dict[ele] = 1
        return count

    def find_duplicate(self, arr, n):
        # arr = [1, 2, 3, 6, 3, 6, 1]
        res = []
        duplicates_array = []
        for ele in arr:
            if ele in res:
                duplicates_array.append(ele)
            else:
                res.append(ele)
        return duplicates_array
    
    def make_pivot(self, arr, low, high):
        pivot = arr[high-1]
        start = low
        for i in range(low, high):
            if(arr[i]<pivot):
                arr[start], arr[i] = arr[i], arr[start]
                start += 1
        arr[start], arr[high-1] = arr[high-1], arr[start]
        return start
    
    def quick_sort(self, arr, low, high):
        # array = [10, 7, 8, 9, 1, 5]
        if(low<high):
            pi = self.make_pivot(arr, low, high)
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)
    
    def mergeSort(self, arr, n):
        if n>1:
            mid = n//2
            leftSide = arr[:mid]
            rightSide = arr[mid:]
            self.mergeSort(leftSide, mid)
            self.mergeSort(rightSide, n-mid)
            
            n1 = 0
            n2 = 0
            k = 0
            
            while(n1<len(leftSide) and n2<len(rightSide)):
                if(leftSide[n1]<rightSide[n2]):
                    arr[k] = leftSide[n1]
                    n1+=1
                else:
                    arr[k] = rightSide[n2]
                    n2+=1
                k += 1
            
            while(n2 < len(rightSide)):
                arr[k] = rightSide[n2]
                k+=1
                n2+=1
            while(n1<len(leftSide)):
                arr[k] = leftSide[n1]
                n1+=1
                k+=1
    
    def missing_smallest_number(self, arr):
        # arr = [2, 3, 7, 6, 8, -1, -10, 15]
        for i in range(1, max(arr)):
            if i not in arr:
                print(i)
                break
    
    def majority_element(self, arr, n):
        # arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
        deepak = {}
        for ele in arr:
            if ele in deepak:
                deepak[ele] += 1
            else:
                deepak[ele] = 1
        
        key, val = max(deepak.items())
        return key, val




if __name__ == '__main__':
    n=int(input())
    arr = list(map(int, input().split()))
    obj = GFG()

    # question-1
    # res = obj.max_neighbors(arr,n)            
    # print("elements are grater than neighbors are: ", *res)

    # question-2
    # obj.rearrange_3_var(arr, n)               
    # print("rearraranging 0,1 and 2 in the array are ", *arr)

    # question-3
    # sum = int(input())                          
    # print("index starting and ending are: ", obj.subarray_sum(arr, n, sum))

    # question-4
    # obj.first_negative_postive(arr, n)
    # print("First negative elements then positive elements are: ", *arr)

    # Question-5 level-2
    # obj.cyclically_rotate_right_1(arr, n)

    # Question-6: count pairs for given sum 
    # sum = int(input())
    # print("Number of pairs for given sum is: ", obj.count_pairs_given_sum(arr, sum))

    # Question-7: find duplicates of an element in the array
    # res = obj.find_duplicate(arr, n)
    # print("Duplicate elements are ", *res)

    # Question-8: sorting the elements through Quick Sort
    # obj.quick_sort(arr, 0, n)
    # print("Array after doing Quick SOrt Operation are: ", *arr)

    # Question-9: sorting the elements through Merge sorted
    # obj.mergeSort(arr, n)
    # print("Array after doing Merge SOrt Operation are: ", *arr)

    # Question-10: find misisng smallest positive number
    # obj.missing_smallest_number(arr)

    # Question-11: get majority elements in the array
    ele, value = obj.majority_element(arr, n)
    print("majority element is {} with frequesncy {}" .format(ele,value))
