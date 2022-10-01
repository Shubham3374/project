import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date
from tokenize import Name

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    '''Create an Event with the details entered by organizer'''
   
    if type.lower()=='Create Event':
        f=open(events_json_file,'a+')
        d={
            "ID" : Event_ID,
            "Event Name": Event_Name,
            "Start_Date":Start_Date,
            "Start_Time":Start_Time,
            "End_Date":End_Date,
            "End_Time":End_Time,
            "Capacity":Capacity,
            "Seats Available":Availability,
            "Event details":[]

        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open("members.json",'r+')
        d={
           "ID" : Event_ID,
            "Full Name":Name,
            "Start_Date":Start_Date,
            "Start_Time":Start_Time,
            "End_Date":End_Date,
            "End_Time":End_Time,
            "Total_Seats":Capacity
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    if type.lower()=='2':
        
        try:
            f=open(events_json_file,'r+')
            content = json.load(f)
            print("-------------Event Details------------")
        
            for i in content:
                print(f'Event ID : {i}')
                print(f" Name : {content[i]['Name']}")
                print(f"Organizer : {content[i]['Organizer']}")
                print(f"Start_Date : {content[i]['Start_Date']}")
                print(f"End_Date : {content[i]['End_Date']}")
                print(f"Total_Seats : {content[i]['Capacity']}")
                print('----------------------------------------')
            
            return True
        except json.JSONDecodeError:
            content = {}
            return 'No Seats available'
        
    


def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    if type.lower()=='3':
        try:

            n = input("Enter the Id of that event :")
            f=open(events_json_file,'r+')
            content = json.load(f)
            for i in content:
                if i["ID"] == n:
                    print(f"The Details of that event ID is : {i}")

                else:
                    print("No events available .")

        except Exception:
             print("Kindly put the valid event Id.")

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    if type.lower()=='4':
        file = open(events_json_file, 'r+')
        content = json.load(file)
    
        for i in content:
            eventId = input("Enter the Id where you want to update: ")
            if eventId == i["ID"]:
                print('What you want to update??')
                print("1) Update Name")
                print("2) Update Start date")
                print("3) Update Start Time")
                print("4) Update End Date")
                print("5) Update End Time ")
                val = input('Enter your choice : ')
        
                if val == "1":
                    i["Name"] = input('Enter updated name : ')
                    print("Updated successfully")
                elif val == "2":
                    i["Start Date"] = input("Enter updated Date in (DD/MM/YYYY) : ")
                elif val == "3":
                    i["Start Time"] = input("Enter new Updated Time (HH:MM:SS) : ")
                elif val == "4":
                    i["End Date"] = input("Enter updated Date in (DD/MM/YYYY) : ")
                elif val == "5":
                    i["End Time"] = input("Enter updated Date in (HH:MM:SS) : ")
                else:
                    break
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()
        return True

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    if type.lower()=='5':

        file = open(events_json_file, 'r+')
        data = json.load(file)
        
        for i in data:
            if i == input('Enter Event ID : '):
                del data[i]
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                file.close()
                return 'Success'
            return 'Please enter valid Event ID'

def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
       

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    
    file = open(members_json_file, 'r+')
    content = json.load(file)
    
    for i in content:
        name = input(" enter the name : ")
        if name == i["Name"]:
            i["Password"] = input("Enter the new updated password : ")
            return True
        return False
            


def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
