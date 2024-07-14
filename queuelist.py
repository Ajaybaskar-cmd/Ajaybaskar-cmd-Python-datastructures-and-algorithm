def insertion(value):
    queue.append(value)
    print("insert successfull",value)
def display():
    print("Queue values:")
    if len(queue)==0:
        print("Queue is empty")
    else:
        for ele in queue:
            print(ele," ")
def deletion():
    p=queue.pop(0)
    print("Deletion succesful",p)
queue=[20,30]
insertion(10)
display()
deletion()
display()