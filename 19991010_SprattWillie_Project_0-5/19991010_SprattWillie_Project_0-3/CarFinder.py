import os

FILENAME = 'allowed_vehicles.txt'

# Function to read vehicles from the file
def read_vehicles_from_file():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            vehicles = [line.strip() for line in file]
    else:
        vehicles = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]
        write_vehicles_to_file(vehicles)
    return vehicles

# Function to write vehicles to the file
def write_vehicles_to_file(vehicles):
    with open(FILENAME, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

def onLoad():
    AllowedVehiclesList = read_vehicles_from_file()

    execution = int(input(""" 
********************************
AutoCountry Vehicle Finder v0.5
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit                         
"""))

    if execution == 1:
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for make in AllowedVehiclesList:
            print(make)
        onLoad()
        
    elif execution == 2:
        search = input("""
********************************
Please Enter the full Vehicle name: """)
        if search in AllowedVehiclesList:
            print(search, "is an authorized vehicle\n\n")
            onLoad()
        else:
            print(search, "is not an authorized vehicle, if you received this in error please check the spelling and try again\n\n")
            onLoad()

    elif execution == 3:
        new_add = input("What Model Would you like to add: ")
        AllowedVehiclesList.append(new_add)
        write_vehicles_to_file(AllowedVehiclesList)
        print(f"""You have added "{new_add}" as an authorized vehicle""")
        onLoad()

    elif execution == 4:
        new_delete = input("Please Enter the full Vehicle name you would like to REMOVE: ")

        assurance = input(f"""Are you sure you want to remove "{new_delete}" from the Authorized Vehicles List (yes/no): """)
        
        if assurance.lower() == "no":
            onLoad()
        
        elif assurance.lower() == "yes":
            if new_delete in AllowedVehiclesList:
                AllowedVehiclesList.remove(new_delete)
                write_vehicles_to_file(AllowedVehiclesList)
                print(f"""You have removed "{new_delete}" as an authorized vehicle""")
            else:
                print(f"""Vehicle "{new_delete}" not found in the list""")
            onLoad()
    
    elif execution == 5:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    
    else:
        print("Sorry, Try Again with the available options")
        onLoad()

onLoad()
