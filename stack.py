import os
def insert(ele):
    if len(stack)==0:
        stack.append(ele)
    else:
        stack.insert(0,ele)
    print("insert at successful for",ele)
    os.system('pause')
def display():
    print("Stack values:")
    for ele in stack:
        print(ele," ")
    os.system('pause')
def pop():
    p=stack.pop(0)
    print("popped value:",p)
    os.system('pause')
def peek():
    print(stack[0])
    os.system('pause')
stack=list()
print("Stack operation:")
while(True):
    os.system('cls')
    print("0.insert")
    print("1.deletion")
    print("2.display")
    print("3.get the top value")
    s=input("Enter your choice:")
    if s=='0':
        ele=int(input("Enter the stack insert values:"))
        insert(ele)
    elif (s=='1'):
        pop()
    elif (s=='2'):
        display()
    elif (s=='3'):
        peek()
    else:
        quit()
        