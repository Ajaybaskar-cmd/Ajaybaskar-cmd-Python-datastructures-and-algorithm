class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class stack():
    def __init__(self):
        self.top=None
    def push(self,newdata):
        newnode=node(newdata)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
        print("push successfully",newdata)
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp=self.top
            print("Stack values:")
            while temp is not None:
                print(temp.data," ")
                temp=temp.next
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.next is None:
                self.top=None
            else:
                temp=self.top
                self.top=temp.next
                temp.next=None
        print("Pop successfully")
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top value:",self.top.data)
                
        
n=node(10)
n1=node(20)
s=stack()
s.top=n
s.top.next=n1
#s.push(20)
s.display()
s.pop()
s.display()
s.peek()