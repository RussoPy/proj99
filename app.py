import pandas as pd
from enum import Enum
import json
class Actions(Enum):
    Exit = 1
    Read = 2
    Create =3
    Delete = 4
    Load =5 

people = []
char =""
user_answer =""
df = pd.read_json('people.json')
FILE_NAME = "people.json"

ids = list(df['id'].unique())
names = list(df['name'].unique)
ages = list(df['age'].unique)
statuses = list(df['status'].unique)


def delete():
        print("delete works")
    
def create():
    people.append({ "id" : input("id?"), "name" : input("name"), "age" : input("age?"), "status" : input("status?")})
    save_to_file()

def read():
    char = input("name/id/age/status ? ")
    if char == "name":
        for index, i in enumerate(names):
            index +=1
            print(f"{index} : name - {i}")


    elif char == "id": 
        for index, i in enumerate(ids):
            index +=1
            print(f"{index} : id - {i}")


    elif char == "age":
        load_people_from_file
        for index, i in enumerate(ages):
            index +=1
            print(f"{index} : age - {i}")
    
            

    elif char == "status": 
        for index, i in enumerate(statuses):
            index +=1
            print(f"{index} : status - {i}")

def save_to_file():
    with open(FILE_NAME, 'w+') as f:
        json.dump(people, f,indent=4)

def load_people_from_file():
    global people
    try:
        with open(FILE_NAME, 'r') as f:
            people = json.load(f)
    except json.JSONDecodeError:
        print("The file does not exist")


def menu():
    for act in Actions: print(f"{act.value} - {act.name}")
    return input("what is your selection?")

if __name__ == "__main__":

    load_people_from_file()

    while True:
        user_answer = Actions(int(menu()))
        if user_answer == Actions.Exit : exit()
        elif user_answer == Actions.Read : read()
        elif user_answer == Actions.Create : create()
        elif user_answer == Actions.Delete : delete()
        elif user_answer == Actions.Load : load_people_from_file()

