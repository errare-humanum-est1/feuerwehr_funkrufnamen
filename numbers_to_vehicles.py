import json


with open("numbers.json", "r") as filehandle:
    numbers = json.loads(filehandle.read())

vehicles = dict()

for key in numbers:
    veh_list = numbers[key]
    for vehicle in veh_list:
        vehicles[vehicle] = key

with open("vehicles.json", "w") as filehandle:
    filehandle.write(json.dumps(vehicles))