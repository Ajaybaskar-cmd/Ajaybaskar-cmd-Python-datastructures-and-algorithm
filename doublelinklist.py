class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll():
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            print("\ndisplay:\n")
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
    def displayrev(self):
        temp=self.tail
        print("\nDisplay reverse:\n")
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.prev
    def insertbegin(self,newdata):
        newnode=node(newdata)
        temp=self.head
        temp.prev=newnode
        newnode.next=self.head
        self.head=newnode
    def insertlast(self,newdata):
        """newnode=node(newdata)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
        self.tail=newnode"""
        newnode=node(30)
        temp=self.tail
        temp.next=newnode
        newnode.prev=temp
        self.tail=newnode
    def insertpos(self,pos,newdata):
        newnode=node(newdata)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newnode.prev=temp
        newnode.next=temp.next
        temp.next.prev=newnode
        temp.next=newnode
    def deleteatbegin(self):
        temp=self.head
        temp.next.prev=None
        self.head=temp.next
        temp.next=None
    def deleteatlast(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None
        self.tail=temp.prev
    def deletepos(self,pos):
        temp=self.head
        for i in range(pos):
            temp=temp.next
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None

    
d=dll()
n1=node(10)
d.head=n1
n2=node(20)
n1.next=n2
n2.prev=n1
d.tail=n2
d.insertbegin(5)
d.insertlast(30)
d.insertpos(2,15)
d.deleteatbegin()
d.deleteatlast()
d.deletepos(1)
d.display()
d.displayrev()