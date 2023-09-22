from Road import Road
from Tool import Tool
from Suggestion import Suggestion

def welcome():
    print('Welcome to \"Thi Ly Ta\" adventure!')
    print('Here is a big challenge for your brave!')
    print()
    print('You are on the way to seek tresure, there is an intersection here to choose where do you want to go!')

def showRoadList(roads):
    print('Here is the list of the way you should choose: ')
    for number, road in enumerate(roads,0):
        print(number, ": ", road.name)
def setInput():
    numbers = [0,1,2,3]
    run = True
    while run:
        choise = input("Enter your choise by entering the number you choose: " )
        if not choise.isdigit() or int(choise) not in numbers :
            print("Sorry, We didn\'t understand you, Pls enter a digit from 0 to 3")
            continue
        elif int(choise) == 0:
            print("Quit Game!")
            break
        elif int(choise) ==1:
            print("You choosed to go into a Cave!")
            run = False
        elif int(choise) == 2:
            print("You choosed to go into a Island!")
            run = False
        else:
            print("You choosed to go into a Forest!")
            run = False
    return int(choise)
def toolChoise(choise):
    print("Pls choose one tool that will help your journey!")
    for tool in listRoad[int(choise)].getTools():
        print(tool.capitalize())
    run = True
    while run:
        toolChoise = input("Pls enter the tool that you want to choose: ")
        if toolChoise.lower() not in listRoad[int(choise)].getTools():
            print("Pls check again the tool name you have choised!")
            continue
        else:
            print("You have choosed: ", toolChoise.capitalize())
            run = False
def suggestionChoise(listSuggestion):
    run = True
    while run:
        sugChoise = input("We have 3 suggestions, pls randomly enter a number from 1 to 3  :")
        if not sugChoise.isdigit() or int(sugChoise) not in range(1,4):
            print("You should enter a number from 1 to 3")
            continue
        else:
            print("Pls get the suggestion: ", "\n", listSuggestion[int(sugChoise)-1])
            run = False

shovel = Tool("Shovel")
poleax = Tool("Poleax")
surf = Tool("Surf")
sword = Tool("Sword")
mapp = Tool("Map")
boot = Tool("Boot")
sg1 = (1, "The treasure is near a big old tree, next to a lake")
sg2 = (2, "Be careful with traps on the main road")
sg3 = (3, "You can use a support item to go faster")

listSuggestion= [sg1, sg2, sg3]

forest = Road("Forest")
forest.addTools(shovel.name.lower())
forest.addTools(poleax.name.lower())
forest.addTools(sword.name.lower())
forest.addTools(mapp.name.lower())

quitGame = Road("Quit Game")

island = Road("Island")
island.addTools(shovel.name.lower())
island.addTools(boot.name.lower())
island.addTools(surf.name.lower())
island.addTools(mapp.name.lower())

cave = Road("Cave")
cave.addTools(boot.name.lower())
cave.addTools(surf.name.lower())
cave.addTools(poleax.name.lower())
cave.addTools(sword.name.lower())

listRoad = [quitGame, cave, island, forest]

#Start Adventure:
welcome()
showRoadList(listRoad)
choise = setInput()
toolChoise(choise)
suggestionChoise(listSuggestion)




        
    
    