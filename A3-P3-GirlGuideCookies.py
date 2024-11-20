#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     W0402993
#Student Name:  Andrew Beaver

def openingMessage():
    print("Girl Guide Cookie Sell-off")

def findHighestSeller(guideList):
    #find highest amount of cookies sold
    return max(salesMax[1] for salesMax in guideList)

def main():

    openingMessage()

    #prizes / variables
    winnerPrize = "Trip to Girl Guide Jamboree in Aruba!"
    aboveAvgPrize = "Super Seller Badge"
    leftOvers = "Left over cookies"
    
    leftOversLowerBoundary = 0

    guideList = []
    avgSold = 0

    #Get the numbers the guides
    numGuides = int((input("\nEnter the number of guides selling cookies: ")))

    #Handle if the user inputs a 0 or negative for the number of guides
    if numGuides > 0:
        #Use the number of guides to create a loop
        #Get names and cookies sold and add to lists
        for i in range(numGuides):
            guideName = input("\nEnter the name of guide #{0}: ".format(i + 1))
            cookiesSold = int(input("Enter the number of boxes sold by {0}: ".format(guideName)))
        #Error handle to let user know they can't have a negative
            if cookiesSold < 0:
                print("WARNING. You can't make negative sales")
            guideList.append([guideName, cookiesSold])

        #Calculate average cookies sold
        totalSales = sum(salesTotal[1] for salesTotal in guideList)
        avgSold = totalSales / numGuides


        highestSales = findHighestSeller(guideList)

        #Display average cookies sold
        print("\nThe average number of boxes sold by each guide was {0:.1f}".format(avgSold))

        print("\nGuide\t\tPrizes Won:\n")
        
        #Establish prize winners, best seller gets trip, above avg gets badge, others with sales get left overs
        for i in range (numGuides):
            guideName, cookiesSold = guideList[i]
            if cookiesSold == highestSales:
                prize = winnerPrize
            elif cookiesSold > avgSold:
                prize = aboveAvgPrize
            elif cookiesSold > leftOversLowerBoundary and cookiesSold <= avgSold:
                prize = leftOvers
            else:
                prize = ""
        
            print("{0}\t\t- {1}".format(guideName, prize))
    else:
        print("Invalid girl guide number added")

main()