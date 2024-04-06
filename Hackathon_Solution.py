import csv

# Creating a list to store what type of merch will be needed based on occupation.

# This will allow the program to read each element of the CSV file.
with open ('Hacktest.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # FOR will read only the first line of the CSV file(for testing purposes).
    for row in readCSV:
        location = row[0]
        occupation = row[1]
        event = row[2]
        break

# Function that will identify which location the user had chosen.
def process_location(loc):
    merch = []
    
    # MATCH CASES will determine which location was selected.
    match loc:
        # Each case will call on the occupation function and assign the results to the merch list.
        case 'California':
            print ('Chevron: California Supplies')
            merch = process_occupation(occupation)
            
        case 'Texas':
            print ('Chevron: Texas Supplies')
            merch = process_occupation(occupation)
            
        case 'Virgina(D.C.)':
            print ('Chevron: D.C. Supplies')
            merch = process_occupation(occupation)

        case 'North Carolina(Greensboro)':
            print ('Chevron: Greensboro Supplies')
            merch = process_occupation(occupation)

        case _:
            print ('N/A Location')

    supplyItem1, supplyItem2 = process_eventType(event)

    merchSupply = [f"{merch[i]}, {supplyItem1 if i == 0 else supplyItem2}" for i in range(len(merch))]
    return merchSupply

# Function that will identify which occupation the user had chosen and help decide what products will be brought.          
def process_occupation(occ):

    # IF and ELIF statement will decide occuptaion and return the list result to the function.
    if(occ == 'Student'):
        print('Event Focus: Students')
        return ['USB Drives','T-Shirts']
        
    elif(occ == 'Teacher'):
        print('Event Focus: Faculty')
        return ['Mugs','Lanyards']
        
    else:
        return 'Invalid'
        return []

# Function will identify which event type the user had chosen and assign the suggested amount of items need for the event.
def process_eventType(evt):

    # Declaring the varibales of the items.
    supplyItem1 = 0
    supplyItem2 = 0

    # MATCH CASE will determine based on event how much merchandise will be needed for the events.
    match evt:
        case 'Lobby Day':
            supplyItem1 = 10
            supplyItem2 = 15
            
        case 'Conference':
            supplyItem1 = 6
            supplyItem2 = 10
            
        case 'Career Fair':
            supplyItemt1 = 15
            supplyItem2 = 10
            
        case 'Hackathon':
            supplyItem1 = 20
            supplyItem2 = 20
            
        case _:
            print ('N/A Event')
            
    return supplyItem1, supplyItem2

# This will call everything within the program, assisgning it to mechandise for the merchant to decide on what to order.
merchandise = process_location(location)
print ("Suggested merch order for the event will be", merchandise)

