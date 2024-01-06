course = {'DBDA':(100,60),'DAI':(200,60)}

def addnewcourse():
    cname = input("Enter Course Name : ")
    duration = int(input("Enter Duration : "))
    capacity = int(input("Enter Capacity : "))
    #v = course.setdefault(cname,(duration,capacity)):
    value = course.get(cname,-1)
    if value == -1:
        course[cname] = (duration,capacity)
        return True
    else:
        return False
             
         
def deletecourse():
    x = input("Enter The Course You Want to Delete : ")
    v = course.pop(x,-1)
    if v != -1:
        return True
    else:
        return False
    
    pass
    
def coursecapacity():
    cname = input('Enter The Course Name You Want to modify :')
    cap = int(input('Enter The New Capacity : '))
    v = course.get(cname,-1)
    if v != -1:
        durarion = course[cname][0]
        course.pop(cname)
        course[cname] = (durarion,cap)
        return True
    else:
        return False

    
    
def modifybycourseName():
    cname = input('Enter the old course name :')
    n_cname = input("Enter the new course name : ")
    v = course.get(cname,-1)
    if v != -1:
        value = course[cname]
        course.pop(cname)
        course[n_cname] = value
        return True
    else:
        return False

    
def displayall(d=course):
    for k,v in d.items():
        print(f"{k}-->{v}")
        
def displaybycapacity(capacity):
    d = {}
    for k,v in course.items():
        if v[1] > capacity:
            d[k]=v
    if len(d)!=0:
        return d
    else:
        return None

case=0
while True:   
    case = int(input("""
    1. add new course
    2. delete the course
    3. modify course capacity
    4. modify course name
    5. display all
    6. display only courses with capacity > given capacity
    7. exit
    choice:"""))
    match case:
        case 1:
            status=addnewcourse()
            if status:
                print("new course added successfully")
        case 2:
            status=deletecourse()
            if status:
                print("Course Deleted Sucessfully...")
            else:
                print("Course Not Found ")
        case 3:
            status=coursecapacity()
            if status:
                print("Course Capcity is Modified")
                pass
            else:
                print("Course Capcity is Not Modified")
                pass
        case 4:
            status=modifybycourseName()
            if status:
                print("Course Name is Modified")
                pass
            else:
                print("Course Name is Not Modified")
                pass
        case 5:
            displayall()
        case 6:
            x = int(input("Enter Capacity : "))
            data = displaybycapacity(x)
            print(data)
        case 7:
            print("Thank you for visiting....")
            break
        