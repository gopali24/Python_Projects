import sys
import clipboard
import json

SAVED_FILE = 'clipboard.json'

# working with clipboard module(basics)
# data = clipboard.paste()
# print(data)
# clipboard.copy("helooooo")
# print(clipboard.paste())

# taking arguments
# print(' '.join(sys.argv[1:]))

def save_data(filepath,data):
    with open(filepath,'w') as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv[1:]) == 1:
    command = sys.argv[1]
    data = load_data(SAVED_FILE)

    if command == 'load':
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
        else:
            print("Key does not exist.")
        print("Data copied into clipboard!")
    
    elif command == 'save':
        key=input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_FILE,data)
        print("Data Saved!")
    
    elif command == 'list':
        print("The keys present are :", " ".join(data.keys()))
    
    else:
        print("Unknown command!!")

else:
    print("Please pass exactly one command.")
