import json
with open("vehicles.json", "r") as filehandle:
    vehicles = json.loads(filehandle.read())
    
for key in vehicles:
    vehicles[key] = 0
    
with open("statistics.json", "w") as filehandle:
    filehandle.write(json.dumps(vehicles))