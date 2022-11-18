import json, random, os
from termcolor import colored, cprint

def write_statistics():
    with open("statistics.json", "w") as filehandle:
        filehandle.write(json.dumps(statistics))

def learn_all():
    log = list()
    while True:
        vehicle_list = list()
        for key in vehicles:
            vehicle_list.append(key)


        vehicle = vehicle_list[random.randint(0, len(vehicle_list))]
        while vehicle in log:
            vehicle = vehicle_list[random.randint(0, len(vehicle_list))]

        log.insert(0, vehicle)

        try: 
            log.pop(14)
        except IndexError:
            pass
    
        print(f"\nWhat is: {vehicle}")

        evaluate_answer(vehicle, input(">"))
    

def learn_wrongs():
    while True:
        statistics_list = list()
        
        for key in statistics:
            if statistics[key] < 0:
                statistics_list.append(key)

        if len(statistics_list) == 0:
            break        

        vehicle = statistics_list[random.randint(0, len(statistics_list) - 1)]

        print(f"\nWhat number is: {vehicle}")

        evaluate_answer(vehicle, input(">"))


def evaluate_answer(vehicle: str, answer: str):
    os.system("clear")
    
    if answer == "x":
        print("Goodbye!")
        exit()
    
    if answer == vehicles[vehicle]:
        print(f"{colored('Correct!', 'green')} '{vehicle}' is {vehicles[vehicle]}")
        statistics[vehicle] += 1
    else:
        print(f"{colored('Incorrect!', 'red')} '{vehicle}' is: {vehicles[vehicle]}")
        statistics[vehicle] -= 1
    write_statistics()




with open("vehicles.json", "r") as filehandle:
    vehicles = json.loads(filehandle.read())

with open("statistics.json", "r") as filehandle:
    statistics = json.loads(filehandle.read())

while True:
    print("""
    What do you wanna do?
    1: learn numbers by vehicles
    2: learn frequently wrong ones
    """)

    user_in = input("choose >")

    match user_in:
        case "1":
            learn_all()
        case "2":
            learn_wrongs()
        case "x":
            print("Goodbye!")
            exit()