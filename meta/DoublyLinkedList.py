
class DLListNode:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

# append, appendleft, pop, popleft, remove (from back)
class DLList:
  def __init__(self):
    self.front = None
    self.back = None
    self.size = 0

  def getBackNode(self):
    return self.back
  
  def getFrontNode(self):
    return self.front
  
  def append(self, val):
    newNode = DLListNode(val, prev=self.back)
    if (self.back):
      self.back.next = newNode
      self.back = newNode
    else: 
      self.back = newNode
      self.front = newNode
    
    self.size += 1
  
  def appendLeft(self, val):
    newNode = DLListNode(val, next=self.front)
    if (self.front):
      self.front.prev = newNode
      self.front = newNode
    else: 
      self.back = newNode
      self.front = newNode
    
    self.size += 1
  
  # gets value
  def pop(self):
    if (self.size == 0): raise RuntimeError("Error, pop when size is 0")

    node = self.back

    if (self.size == 1): 
      self.back = None
      self.front = None
    else:
      self.back.prev.next = None
      self.back = self.back.prev
      node.prev = None
      node.next = None
    
    self.size -= 1
    return node.val
  
  def popFront(self):
    if (self.size == 0): raise RuntimeError("Error, pop when size is 0")

    node = self.front

    if (self.size == 1): 
      self.back = None
      self.front = None
    else:
      self.front.next.prev = None
      self.front = self.front.next
      node.prev = None
      node.next = None
    
    self.size -= 1
    return node.val
  
  def remove(self, node):
    val = node.val
    if (node.next): node.next.prev = node.prev
    if (node.prev): node.prev.next = node.next

    # remove links
    node.next = None
    node.prev = None

    self.size -= 1

    return val
  

  

