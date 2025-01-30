class Sortingsort():
    def __init__(self):
        self.list = []
        
    def bubble_sort(self):
        for i in range(len(self.list)-1):
            print(self.list)
            for j in range(len(self.list)):
                if j == (len(self.list)-1):
                    continue
                elif self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
                j+=1
        return self.list
    