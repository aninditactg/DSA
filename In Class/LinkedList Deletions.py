# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 12:57:26 2023

@author: User
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def traverse(self,head):
        while head != None:
            print(head.data)
            head = head.next
        
        
first = Node(10)
second = Node(20)
third = Node(30)
newNode = Node(40)
endNode = Node(50)
midNode = Node(60)

L = LinkedList()
L.head = first
first.next = second
second.next = third
newNode.next = L.head
L.head = newNode
#End node
third.next = endNode

temp= L.head
flag = 0
   while temp! = None:
    if temp.data ==20:
        flag=1
        break
    else:
        temp= temp.next
        if flag == 1:
            midNode.next= temp.next
            temp.next= midNode
            
#delete in beginning

L.head= L.head.mext

L.traverse(L.head)

midNode.next = temp.mext
   
#Deletion
L.head = L.head.next

#Deletion from end
t = L.head
while t.next.next ! = None:
    t= t.next
    
    t.next = None
    L.traverse(L.head)
   
   t.next =None
   
 #delete by value
 prev = L.head
 while prev.next.next! = Nome:
     if prev.data == 60:
         break
     else:
         prev = prev.next
cur = prev.next
prev.next = cur.next

#seletion by location
prev = L.head
p=2
c=1
while prev.next! = None:
    if c == (p-1):
        break
    else:
        prev = prev.next
        c=c+1
cur = prev.next
prev.next = cur.next
                         

   
   
   
   
   
   
   
   
   


