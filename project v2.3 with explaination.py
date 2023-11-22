#First you need to install keyboard library before running the programme
#To install keyboard libary, press "windows key + R" and type "cmd" in the pop up window. Once the command prompt is opened, type "pip install keyboard" and enter, done.

#Update the "game_status" list, move things from top to bottom, remove the gates when they get close to player
def copy(list):
    temp = 0
    for i in range(0,10):
        if list[i][1] == "+" or list[i][1] == "-" or list[i][1] == "x" or list[i][1] == "÷" or list[i][1] == "(":
            temp = i
            break
    if temp < 8:
        for i in range(8):
            list[temp+1][i], list[temp][i] = list[temp][i], list[temp+1][i]
    elif temp == 8:
        for i in range(8):
            list[temp][i] = list[temp-1][i]

#Display the "game_status" list
def display(list):
    for i in range(len(list)):
        for j in list[i]:
            if j == " ":
                print(j,end="")
            elif j == "ඞ":
                print(j,end="")
            else:
                print(j,end="")
        if i == 0:
            print("     Player "+player_name,end="")
        if i == 2:
            print("     Current power: ",power,end="")
        elif i == 3 and gate_count < 110:
            print("     Current stage: ",gate_count,end="")
        elif i == 4 and gate_count >= 110:
            print("     Boss Power: ",boss_power,end="")
        print()

#Generate two gate at the same line randomly and indiviually with weight (+:30% ; -:20% ; x:30% ; ÷:20%)   
def gate():
    temp = random.randint(1,20)
    temp2 = ""
    if 0 < temp < 7:
        temp2 += "+"
    elif 6 < temp < 11:
        temp2 += "-"
    elif 10 < temp < 17:
        temp2 += "x"
    elif 16 < temp < 21:
        temp2 += "÷"
    game_status[0][1], game_status[0][2], game_status[0][3] = temp2, str(random.randint(1,9)), "|"

    temp = random.randint(1,20)
    temp2 = ""
    if 0 < temp < 7:
        temp2 += "+"
    elif 6 < temp < 11:
        temp2 += "-"
    elif 10 < temp < 17:
        temp2 += "x"
    elif 16 < temp < 21:
        temp2 += "÷"
    game_status[0][4], game_status[0][5], game_status[0][6] = "|", temp2, str(random.randint(1,9))

#Check if it is ready to calculate the power (when player get close to the gate)
def ready_to_power_cal():
    if game_status[8][1] == "+" or game_status[8][1] == "-" or game_status[8][1] == "x" or game_status[8][1] == "÷":
        return True
    return False

#Check if it is ready to fight the boss (when player get close to the boss)
def ready_to_fight():
    for i in range(8):
        if game_status[1][i] == "ඞ":
            return True
    return False 

#Power calculation algorithm
def power_cal(num):
    current_pos = -1
    for i in range(8):
        if game_status[9][i] == "ඞ":
            current_pos = i
            break
    if 4 > current_pos > 0:
        if game_status[8][1] == "+":
            num += int(game_status[8][2])
        elif game_status[8][1] == "-":
            num -= int(game_status[8][2])
        elif game_status[8][1] == "x":
            num *= int(game_status[8][2])
        elif game_status[8][1] == "÷":
            num /= int(game_status[8][2])
    elif 8 > current_pos > 3:
        if game_status[8][5] == "+":
            num += int(game_status[8][6])
        elif game_status[8][5] == "-":
            num -= int(game_status[8][6])
        elif game_status[8][5] == "x":
            num *= int(game_status[8][6])
        elif game_status[8][5] == "÷":
            num /= int(game_status[8][6])
    return round(num)

#Generate boss
def boss():
    game_status[0][1], game_status[0][2], game_status[0][3] = "("," ","･ิ"
    game_status[0][4], game_status[0][5], game_status[0][6] = "ω","･ิ",")"

#Update the "game_status" list, move the player from bottom to top, until the player get in front of the boss
def boss_copy(list):
    temp = 0
    for i in range(0,10):
        for j in range(8):
            if list[i][j] == "ඞ":
                temp = i
                break
    if temp > 1:
        for i in range(8):
            list[temp-1][i], list[temp][i] = list[temp][i], list[temp-1][i]

#Player move algorithm (left)
def move_left(x):
    for i in range(8):
        if game_status[9][i] == "ඞ":
            if game_status[9][i-1] == "|":
                break
            else:
                game_status[9][i] = " "
                game_status[9][i-1] = "ඞ"
                break

#Player move algorithm (left)
def move_right(x):
    for i in range(8):
        if game_status[9][i] == "ඞ":
            if game_status[9][i+1] == "|":
                break
            else:
                game_status[9][i] = " "
                game_status[9][i+1] = "ඞ"
                break

#Generate monster randomly
def monster():
    game_status[0][random.randint(1,6)] = "☠"

#Power calculation algorithm (when encounter with the monster)
def fight_monster(num):
    num -= 100
    if num < 0:
    	num = 0
    return num

#Update the "game_status" list, move the monster from top to bottom
def monster_copy():
    x = 0
    y = 0
    for i in range(8):
        for j in range(1,7):
            if game_status[i][j] == "☠":
                x = i
                y = j
                break
    game_status[x+1][y], game_status[x][y] = game_status[x][y], game_status[x+1][y]
                
#Generate bonus
def bonus():
    game_status[0][random.randint(1,6)] = "★"

#Update the "game_status" list, move the monster from top to bottom
def bonus_copy():
    x = 0
    y = 0
    for i in range(8):
        for j in range(1,7):
            if game_status[i][j] == "★":
                x = i
                y = j
                break
    game_status[x+1][y], game_status[x][y] = game_status[x][y], game_status[x+1][y]

def bonus_cal(num):
    temp = random.randint(1,2)
    if temp == 1:
        num += 1000
    elif temp == 2:
        num *= 10
    return num

#The libraries used in this game
from os import system
import random
import keyboard
import time

#Execute the function when press the corresponding key
keyboard.on_press_key("left arrow", move_left)
keyboard.on_press_key("right arrow", move_right)

#Define the variables
turn = [10,20,30,40,50,60,70,80,90,100]
monster_turn = [25,35,45,55,65,75,85,95]
math_sym = ["+","-","x","÷"]

game_status = [["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," "," "," "," "," ","|"],
               ["|"," "," ","ඞ"," "," "," ","|"]]
gate_count = 0
power = 1
stage = 0


#Real game execution
print("Welcome to \"Run with Number\"\n\nYou need to gain power by Addition and Multiplication\nHowever, you will lose power when you encounter Subtraction, Division and Obstacles☠ (-100 power)\nDuring gameplay, there will be a bonus★ (+1000 or x10 power)\nGain power as many as possible in 10 stages to defeat the boss\n")
player_name = input("Please enter your player name: ")
diff = int(input("Choose a difficulty (1 : Normal | 2 : Hard | 3 : Impossible): "))
system("cls") #Clear all the output in the terminal

#Change the speed and boss power according to the difficulty
if diff == 1:
    speed = 0.25
    boss_power = 500
elif diff == 2:
    speed = 0.2
    boss_power = 1000
elif diff == 3:
    speed = 0.1
    boss_power = 2000

#Count down before start
for i in range(3):
    print(3-i)
    time.sleep(1)
    system("cls")

#Generate the bonus appear time, not in "turn" list and not in "monster_turn" list
while True:
    exception_list = [29,31,39,41,49,51,59,61,69,71,79,81,89,91]
    bonus_turn = random.randint(22,98)
    if bonus_turn not in turn and bonus_turn not in monster_turn and bonus_turn not in exception_list:
        break

#Game started
while True:
    display(game_status)
    time.sleep(speed) #The speed of the game, how often does it reflash
    
    #General gameplay before the boss appear
    if gate_count < 110:
        copy(game_status)
        
        #Clear the monster at row 8 & Check if the player encounter the monster. If yes, run "fight_monster" function
        for i in range(8):
            if game_status[8][i] == "☠":
                game_status[8][i] = " "
                if game_status[9][i] == "ඞ":
                    power = fight_monster(power)
        
        monster_copy()

        gate_count += 1

        #Refer to the "turn" list. If true, run "gate" function
        if gate_count in turn:
            gate()
            stage += 1
        
        if ready_to_power_cal():
            power = power_cal(power)
        
        #I don't know why I put it in here instead of in "power_cal" function
        if power < 0:
            power = 0
        
        if gate_count > 20: #Useless if condition
                if gate_count in monster_turn:
                    monster()

        if gate_count == bonus_turn:
            bonus()

        bonus_copy()

        for i in range(8):
            if game_status[8][i] == "★":
                game_status[8][i] = " "
                if game_status[9][i] == "ඞ":
                    power = bonus_cal(power)
        

        system("cls")
        continue #Ignore the rest of the code and start from the beginning (While-loop)

    else:
        boss_copy(game_status)
               

    if gate_count == 110:
        boss()

    
    
    system("cls")

    if ready_to_fight():
        if power > boss_power:
            print(f"You win! Congratulation Player {player_name}!\n")
            time.sleep(2)
            break
        else:
            print(f"You lose! Better luck next time Player {player_name}\n")
            time.sleep(2)
            break

#Hall of Fame
HoF = open("Hall of Fame.txt","a+")

HoF.write(f"\n{player_name} {power}")
'''
#The idea is possible but cannot execute (sort when writing in the data)
if type(HoF.read()) == str:
    HoF.seek(0)
    count = len(HoF.readlines())
    HoF.seek(0)
    for i in range(count):
        record = HoF.readline().split()
        if power <= int(record[1]):
            HoF.write(f"\n{player_name} {power}")
            break
else:
    HoF.seek(0)
    HoF.write(f"\n{player_name} {power}")
'''
#Split the read content, change the number from string to integer
HoF.seek(0)
content = HoF.readlines()
content_split = []
content.remove("\n")

for item in content:
    temp = item.split()
    temp[1] = int(temp[1])
    content_split.append(temp)

#Sorting Algorithm***
for i in range(len(content_split)):
    for j in range(len(content_split)-1):
        if content_split[j][1] < content_split[j+1][1]:
            content_split[j], content_split[j+1] = content_split[j+1], content_split[j]

#Print the Hall of Fame
print("Hall of Fame (Top 10)\n")
print("Player\t\tPower")
count = 0
for item in content_split:
    count += 1
    if count == 11:
        break
    else:
        for i in range(2):
            if i == 0:
                print(f"{item[i]}\t\t",end="")
            else:
                print(item[i])

HoF.close()


#Overall, this code works but it is unorganised and messy