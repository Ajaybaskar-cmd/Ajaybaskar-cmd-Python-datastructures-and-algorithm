class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        print(temp.data,"-->",end=" ")
        while(temp.next!=self.head):
            temp=temp.next
            print(temp.data,"-->",end=" ")
    def insertbegin(self,newdata):
        newnode=node(newdata)
        newnode.next=self.tail.next
        self.tail.next=newnode
        self.head=newnode
    def insertlast(self,newdata):
        newnode=node(newdata)
        newnode.next=self.tail.next
        self.tail.next=newnode
        self.tail=newnode
    def insertpos(self,newdata,pos):
        newnode=node(newdata)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def deletebegin(self):
        if(self.head.next==self.head):
            self.head=None
            self.tail=None
        else:
            self.tail.next=self.head.next
            self.head=None
            self.head=self.tail.next
    def deletepos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(pos-1):
            prev=prev.next
            temp=temp.next
        prev.next=temp.next
        temp.next=None
    def deletelast(self):
        temp=self.head
        while temp.next!=self.tail:
            temp=temp.next
        self.tail=None
        self.tail=temp
        temp.next=self.head

c=cll()
n=node(10)
c.head=n
c.tail=n
c.tail.next=c.head
n1=node(20)
c.tail.next=n1
c.tail=n1
c.tail.next=c.head
c.insertbegin(5)
c.insertlast(25)
c.insertpos(15,2)
c.deletebegin()
c.deletepos(1)
c.deletelast()
c.display()    
    