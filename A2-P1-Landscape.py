#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:  W0424837   
#Student Name:  Mason Liao

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Start of program

    # Get the info from user

    # Enter house number
    houseNum = int(input("Enter House Number: "))

    # Enter property depth(feet)
    propertylength = float(input("Enter property depth(feet): "))

    # Enter property width(feet)
    propertyWidth = float(input("Enter property width(feet): "))

    # Enter type of grass(fescue, bentgrass, campus)
    typeOfGrass = input("Enter type of grass(fescue, bentgrass, campus): " ).lower()

    # Enter the number of trees
    numberOfTrees = int(input("Enter the number of trees: "))

    # Define the variables and do the math
    baseLabChar = 1000
    addLabChar = 500
    fescueRate = 0.05
    bentgrassRate = 0.02 
    campusRate = 0.01
    surface = propertylength * propertyWidth
    costOfTrees = numberOfTrees * 100
    

    # Calculate the grass cost : 3 different input
    
    if typeOfGrass == "fescue" :
        costOfGrass = fescueRate * surface
      
    elif typeOfGrass == "bentgrass":
        costOfGrass = bentgrassRate * surface    

    elif typeOfGrass == "campus":
        costOfGrass = campusRate * surface

    else:
        print("Invalid value of grass type, please enter'fescue, bentgrass or campus' ")
        return
        
    # Define the isOver5000 is surface over 5000 square feet. 
    isOver5000 = surface > 5000

    # Make the decition
    if isOver5000:
        totalcost = baseLabChar + addLabChar + costOfTrees + costOfGrass
    else:
        totalcost = baseLabChar + costOfTrees + costOfGrass
        
    # Give the output
    print("Total cost for house {0} is: ${1:.2f}".format(houseNum,totalcost))
    
    # End of program

    # Ready for Marking



    # YOUR CODE ENDS HERE

main()