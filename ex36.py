import sys 

players = ["1. Auston", "2. McJesus", "3. Marner"]
assists = [45, 57, 58]
goals = [54, 41, 30]
shots = [280, 179, 162]

def start():
    
    selection = input("> ")
    try:
        print(f"Try Current value of variable 'selection' is {selection}")
        int(selection)
        print(selection)
        convert = int(selection)
        print(convert)
        playernum = convert - 1
        print("You selected: ", players[playernum])
    except:
        print("Enter a Number here")
        
        selection = None
        print(f"Except Current value of variable 'selection' is {selection}")
        #sys.exit()
        start()

def points():
<<<<<<< HEAD
    print("something else")
=======
    print("something something")
>>>>>>> ab4ee33eca49944fc8aa00e12c80fd36da5356f7
    
start()
