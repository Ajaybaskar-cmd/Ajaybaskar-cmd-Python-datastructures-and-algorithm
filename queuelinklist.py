class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class queue():
    def __init__(self):
        self.first=None
        self.last=None
    def display(self):
        if self.first is None:
            print("Queue is empty")
        else:
            temp=self.first
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next
    def enqueue(self,newdata):
        newnode=node(newdata)
        temp=self.first
        if self.first is None:
            self.first=newnode
        else:
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
    def dequeue(self):
        if self.first is None:
            print("Queue is empty")
        else:
            temp=self.first
            while temp.next is not None:
                prev=temp
                temp=temp.next
            temp=None
            prev.next=None
        print("Dequeue successfully")
    
q=queue()
n=node(10)
q.first=n
q.first.next=node(20)
q.enqueue(30)
q.dequeue()
q.display()
        