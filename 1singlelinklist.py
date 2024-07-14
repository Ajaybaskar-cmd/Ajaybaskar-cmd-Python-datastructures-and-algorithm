class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinklist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
                
    def insertbegin(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
    def insertatlast(self,newdata):
        newnode=node(newdata)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        
    def insertatpos(self,newdata,pos):
        newnode=node(newdata)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def deletebegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

        
l=singlelinklist()
e=node(10)
l.head=e
e1=node(20)
l.head.next=e1
e2=node(30)
e1.next=e2
l.insertbegin(5)
l.insertatlast(40)
l.insertatpos(15,2)
#l.deletebegin()
l.display()