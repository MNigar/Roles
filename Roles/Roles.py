def managertask():
    print("task for manager")
    return managertask.__name__
def developertast():
        print("task for developer")

def testettask():
        print("task for tester")

def marketingtask():
        print("task for marketing")
#def assignpasstorole(_user,role):

roleandtask={
    'manager':"managertask",
    'developer':"developertast",
    'tester':"testettask",
    'marketing':"marketingtask"    
    }   
users=[]
roles=["Manager","developer","tester","marketingmanager"]
class User:
    def __init__(self, _name_, _surname_,_username_,_password_,_role_):
     self.name=_name_
     self.surname=_surname_
     self.username=_username_
     self.password=_password_
     self.role=_role_
users.append(User("Shovket","Hasanzade","Shovket","shovket@",roles[1]))
users.append(User("Nigar","Mammadova","nig","nigar@",roles[2]))
users.append(User("Eldar","Mahmudov","eldar","eldar@",roles[2]))
users.append(User("Ruslan","Babanli","Ruslan","ruslan@",roles[3]))
def getdata():
    username=input("username:")
    password=input("password:")
    return [username,password]
def logcheck():
    logindetail=getdata()
    for user in users:
      
     if( user.username==logindetail[0] and user.password==logindetail[1]):
         for _role,_task in roleandtask.items():
             if (_role==user.role):
                 globals() [_task]()
                 break
     
        
logcheck()