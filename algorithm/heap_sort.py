class HeapSort():

  def __init__(self):
    self.swips = 0

  def heap(self,array,size, index):
    largest = index
    left = 2*index + 1
    right = 2*index + 2

    if left < size and array[left] > array[largest]:
      largest = left
      self.swips += 1

      
    if right < size and array[right] > array[largest]:
      largest = right
      self.swips += 1

      
    if largest != index:
      
      array[index], array[largest] = array[largest] , array[index]

      self.heap(array,size,largest)
  
  
  def heapsort(self,array):
    size = len(array)

    for i in range(size//2-1,-1,-1):
      self.heap(array,size,i)

    for i in range(size-1,0,-1):

      array[i],array[0] = array[0],array[i] 
      self.heap(array,i,0)
    
    