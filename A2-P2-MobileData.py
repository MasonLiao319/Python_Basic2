#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:   w0424837  
#Student Name:  Mason Liao

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Start of program

    # Get users info
    # Enter the data usage
    dataUsage = float(input("Enter data usage (Mb): "))

    # Assign the different rate belong to different range  to variable
    upAndTo200FlateRate = 20
    over200To500Rate = 0.105
    over500To1GBRate = 0.110
    over1GBFlateRate = 118

    # Check the datausage fall into with range(if, else, elif)
    if 200 >= dataUsage > 0:
        totalCost = upAndTo200FlateRate
    elif 500 >= dataUsage > 200:
        totalCost = dataUsage * over200To500Rate
    elif 1000 >= dataUsage > 500:
        totalCost = dataUsage *over500To1GBRate
    else:
        totalCost = over1GBFlateRate

    # Give the output
    print("Total charge is ${0:.2f}".format(totalCost))

    # End of Program

    # Ready for Marking



    # YOUR CODE ENDS HERE

main()