import sys
import json
import threading
import time
from threading import *

lib = {}

def create(k,v,ttl = 0):
    f = 0
    if(len(lib) < (1024 * 1024 * 1024)):
        if k in lib:
            print("Error : This Key already exists in the datastore")
        else:
            if(k.isalpha()):
                if(int(v) < (16 * 1024)):
                    if(ttl == 0):
                        value_list = [v,ttl]
                    else:
                        value_list = [v,time.time() + ttl]
                    if(len(k) <= 32):
                        lib[k] = json.dumps(value_list)
                        f = 1
                    else:
                        print("Error : Length of the Key must not exceed 32chars")
                else:
                    print("Error : Size of value ")        
            else:
                print("Error : Key must always be a string")
    else:
        print("Error : Memory Limit of Datastore Exceeded")
    return f


def read(k):
    if k not in lib:
        print("Error : This Key doesn't exist in the dataset")
    else:
        value_list = lib[k]
        ttl = value_list[1]
        if(ttl):
            if(time.time() > value_list[1]):
                print("Error : Time-To-Live for ",k," has expired")
            else:
                print("The value for " + str(k) + " is " + str(lib[0]))
        else:
            print("The value for " + str(k) + " is " + str(lib[0]))

def delete(k):
    if k not in lib:
        print("Error : This Key doesn't exist in the dataset")
    else:
        value_list = lib[k]
        ttl = value_list[1]
        if(ttl):
            if(time.time() > value_list[1]):
                print("Error : Time-To-Live for ",k," has expired")
            else:
                del lib[k]
                print("The key has been deleted successfully")
        else:
            del lib[k]
            print("The key has been deleted successfully")
            
def save():
    return lib
