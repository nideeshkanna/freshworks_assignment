import main as app
import json
print("Options :")
print("1 for Creating a key value pair without Time-To-Live,")
print("2 for Creating a key value pair with Time-To-Live,")
print("3 for Knowing the value of a given key,")
print("4 for Deleting a key.")
print("5 to save the datastore locally")
print("Enter your option")
option = int(input())
while(option in [1,2,3,4]):
    if(option == 1):
        print("Enter the key:")
        key = input()
        print("Enter its value:")
        value = input()
        res = app.create(key,value)
        if(res):
            print("Key Value pair has been added successfully")
    elif(option == 2):
        print("Enter the key:")
        key = input()
        print("Enter its value:")
        value = input()
        print("Enter the time-to-live")
        ttl = int(input())
        res = app.create(key,value,ttl)
        if(res):
            print("Key Value pair has been added successfully")
    elif(option == 3):
        print("Enter the key:")
        key = input()
        app.read(key)
    elif(option == 4):
        print("Enter the key:")
        key = input()
        app.delete(key)
    print("Enter your option")
    option = int(input())
if(option == 5):
    datastore = app.save()
    with open("library.json",'w') as file:
        datastore = json.dumps(datastore)
        file.write(datastore)
    
    
