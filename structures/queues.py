class ListNode:
    def __init__(self, val, next = None, tail = None):
        self.val = val
        self.next = next
        self.tail = tail

def enqueue(self, val):
    newNode = ListNode(val)
    if self.next:
        self.next.next = newNode
        self.next = self.next.next
    else:
        self.left = self.right = newNode

def dequeue(self):
    if not self.left:
        return None
    
    val = self.left.val
    self.left = self.left.next

    if not self.left:
        return None

    return val
