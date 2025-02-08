#Insert n in the last position in the array:
def pushback(self, n):
    if self.length == self.capacity:
        resize()
    self.arr[self.length] = n
    self.length += 1 

#resize the given array:
def resize(self):
    self.capacity = 2 * self.length
    newArr = [0] * self.capacity

    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr