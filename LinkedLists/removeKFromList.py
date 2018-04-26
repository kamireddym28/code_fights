'''
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

- For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];

- For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
'''


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
