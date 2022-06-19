
def calc(a=2,b=2):
    sum=a+b
    return sum

def call(*a):
    print("1st value is :"+str(a[0])+" 2nd value is :"+str(a[1]))

def linear_search_seq():
    n = int(input("Enter the limit of list "))
    ls = []
    for i in range(n):
        item = int(input("Enter element " + str(i + 1)) + " ")
        ls.append(item)

    display_list(ls,n)

    key = int(input("Enter the key"))

    linear_search(key,ls)

def linear_search(key,ls):

    flag = 0
    for i in range(0,len(ls)):
        if (key==ls[i]):
            flag = 1
            break;

    if (flag==1):
        print("Element " + str(key) + "found at position " + str(i))
    else:
        print("Element not found")

def bubble_sort(ls,n):
    for i in range(n):
        for j in range(n-1-i):
            if(ls[j]>ls[j+1]):
                temp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = temp

    return ls;

def display_list(ls,n):
    print("[", end=" ")
    for i in ls:
        print(i, end=" ")
    print("]")

def binary_search(ls, key):
    low = 0
    high = len(ls) - 1
    mid = 0
    flag=0
    while low <= high:

        mid = low+high/2

        if(key<ls[mid]):
            high=mid-1
        elif(key>ls[mid]):
            low=mid+1
        else:
            flag=1
            break

    if(flag==1):
        print("Element found")
    else:
        print("Elemment not found")

def binary_search_seq():
    n=int(input("Enter the limit of the list "))

    ls=[]
    for i in range(n):
        item=int(input("Enter element "+str(i+1))+" ")
        ls.append(item)

    print("The List before sorting is")
    display_list(ls,n)

    #Performing BUBBLE SORT
    ls=bubble_sort(ls,n)

    print("The List after Sorting is")
    display_list(ls,n)

    key=int(input("Enter the key"))

    binary_search(ls,key)

marksheet=[]
grade=[]

n=int(input("Enter the number of students - "))
for i in range(n):
    name=input("Enter the name - ")
    mark=float(input("Enter the mark - "))
    marksheet.append([name,mark])
    grade.append(mark)

grade=sorted(set(grade))
second_lowest=grade[1]
names=[]
for val in marksheet:
    if second_lowest==val[1]:
        names.append(val[0])

names.sort()
for nm in names:
    print(nm)

