class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelink():
    def __init__(self):
        self.head=None
        
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
            
    def AtBegining(self,newdata):
        newnode=Node(newdata)
        
        newnode.next=self.head
        self.head=newnode
    def insertallast(self,newdata):
        new=Node(newdata)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
            
l=singlelink()
l.head=Node(2)
e=Node(3)

l.head.next=e
e1=Node(4)
e.next=e1
l.AtBegining(1)
l.insertallast(5)
l.print()