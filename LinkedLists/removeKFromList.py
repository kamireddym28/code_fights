# Definition for singly-linked list:
#class ListNode(object):
#   def __init__(self, x):
#       self.value = x
#       self.next = None

def removeKFromList(l,key):
    temp = l
    
    while l!=None and l.value == key:
        l = l.next
    
    while temp: 
        prev = temp
        temp = temp.next
        while temp and (temp.value == key):
            temp = temp.next
        prev.next = temp
    
    return l
