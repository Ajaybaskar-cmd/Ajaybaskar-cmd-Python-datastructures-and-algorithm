class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinklist():
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,"-->",end="")
                temp=temp.next
    def insertbegin(self,newdata):
        newnode=node(newdata)
        if self.head is None:
            newnode.next=None
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertlast(self,newdata):
        newnode=node(newdata)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
    def insertpos(self,pos,newdata):
        newnode=node(newdata)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def deletebegin(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            self.head=temp.next
            #temp.next=None
    def deletelast(self):
        temp=self.head
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
    def deletepos(self,pos):
        temp=self.head
        for i in range(pos):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp.next=None
l=singlelinklist()
l.head=node(20)
n=node(30)
l.head.next=n
n2=node(40)
n.next=n2
l.insertbegin(10)
l.insertlast(50)
l.insertpos(1,15)
l.deletebegin()
l.deletelast()
l.deletepos(1)
l.display()
            