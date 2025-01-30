class SortingSort:
    def __init__(self):
        self.list = []
    
    def bubble_sort(self):
        n = len(self.list)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
                    swapped = True
            if not swapped:
                break
        return self.list
    
    def selection_sort(self):
        n = len(self.list)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.list[j] < self.list[min_idx]:
                    min_idx = j
            self.list[i], self.list[min_idx] = self.list[min_idx], self.list[i]
        return self.list
    
    def insertion_sort(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key
        return self.list
    
    def merge_sort(self):
        def merge(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                merge(L)
                merge(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        merge(self.list)
        return self.list
    
    def quick_sort(self):
        def quicksort(arr):
            if len(arr) < 2:
                return arr
            else:
                pivot = arr[0]
                less = [i for i in arr[1:] if i <= pivot]
                greater = [i for i in arr[1:] if i > pivot]
                return quicksort(less) + [pivot] + quicksort(greater)
        self.list = quicksort(self.list)
        return self.list
