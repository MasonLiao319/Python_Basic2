#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     w0424837
#Student Name:  Mason Liao

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Start of Program
    # Get the user info(Gender, Age, Price of vehicle)
    checkGender = input("Are you 'male' or 'female': ").lower()       
    userAge = int(input("Enter your age: "))
    priceOfVec = float(input("Enter the price of your vehicle: "))

    # Define isMale and isFemale variables and Rate variables. Use Nested if: else:(Gender value should be valid)
    isMale = checkGender == "male"
    isFemale = checkGender == "female"

    if isMale or isFemale:

        # Assigh different rate to variables(M, F)
        m15To25Rate = 0.25
        m25To40Rate = 0.17
        m40To70Rate = 0.1
        f15To25Rate = 0.2
        f25To40Rate = 0.15
        f40To70Rate = 0.1
        # Male monthly pay
        m15To25MonthlyPay = priceOfVec * ( m15To25Rate/ 12)
        m25To40MonthlyPay = priceOfVec * ( m25To40Rate / 12)
        m40To70MonthlyPay = priceOfVec * ( m40To70Rate/ 12)

        # Female monthly pay
        f15To25MonthlyPay = priceOfVec * ( f15To25Rate / 12)
        f25To40MonthlyPay = priceOfVec * ( f25To40Rate / 12)
        f40To70MonthlyPay = priceOfVec * ( f40To70Rate / 12)

        # User age range
        between15To25 = 25 > userAge >= 15
        between25To40 = 40 > userAge >= 25
        between40To70 = 70 > userAge >= 40

        # Check if you are male or female and falls into which range
        # Male rate range
        if  isMale and between15To25:
            monthlyPay = m15To25MonthlyPay
        elif isMale and between25To40:
            monthlyPay = m25To40MonthlyPay
        elif isMale and between40To70:
            monthlyPay = m40To70MonthlyPay

        # Female rate range
        elif  isFemale and between15To25:
            monthlyPay = f15To25MonthlyPay
        elif isFemale and between25To40:
            monthlyPay = f25To40MonthlyPay
        elif isFemale and between40To70:
            monthlyPay = f40To70MonthlyPay

        # Users enter ages beyond our age range. print alert   
        else:
            print("Age is not applicable, Please contact our agent for advice.")
            return
        
        # Give the output
        print("Your monthly insurance will be ${0:.2f}".format(monthlyPay))
       

        # Else print"Invalid value, please enter 'male' or 'female'"
    else:
        print("Invalid value, please enter 'male' or 'female'")

    # End of Program

    # Ready for Marking


    # YOUR CODE ENDS HERE

main()