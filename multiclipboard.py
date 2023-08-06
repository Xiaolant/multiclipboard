import sys
import json
import clipboard

SAVED_DATA="clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    
    try:
        with open(filepath, "r") as f:
            data=json.load(f)
            return data
    
    except:
        return {}

if len(sys.argv)==2:
    command=sys.argv[1]
    data=load_items(SAVED_DATA)

    if command=="save":
        key = input("Enter a key:")
        data[key]=clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data saved")
    
    elif command=="load":
        key = input("Enter a key asscoiated with the data:")
        if key in data:
            clipboard.copy(data[key])
            print("Data loaded")
        else:
            print("Key does not exist")

    elif command=="list":
        print(data)

    elif command=="delete":
        key = input("Enter the key of item to delete:")
        del data[key]
        save_items(SAVED_DATA, data)
        print("Item deleted.")

    else:
        print("Unknown command")

else:
    print("Please pass exactly one command")