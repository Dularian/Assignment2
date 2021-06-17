class Ratings:

    def rating(List, amount):
        """input rating is checked if it is below 5"""
        """adds to list and increments counter"""
        count = 0
        while (count <= amount):
            rating = int(input())
            while (int(rating) > 5):
                print("invalid. try again.")
                rating = int(input())
            List.append(rating)
            count += 1
            return List

    def frequency(rating, List, freq):
        """For each rating in the List it will check if its in freq dictionary."""
        """It will then add a frequency counter if it is/else it will assume its the first time and equal 1"""
        for rating in List:
            if (rating in freq):
                freq[rating] += 1
            else:
                freq[rating] = 1
        return freq

    freq = {}
    counter = 0
    List = []
    enter_ratings = 0

    """conditional statement to get additional ratings later on."""
    while(enter_ratings == 0):

        counter = 0
        """Asks how many ratings to enter and gathers those ratings through the rating method"""
        """afterwards the frequency is acquired"""
        amount = 0
        print("How many ratings do you want to enter?")
        amount = int(input())
        while(counter < amount):
            rating(List, amount)
            counter += 1
        frequency(rating, List, freq)

        """Prints out the rating followed by its frequency"""
        for key, value in freq.items():
            print("% d : % d" % (key, value))

        """asks if user wants to enter more ratings."""
        print("Would you like to enter more? ")
        print("Type 'y' to enter more.")
        if(str(input()) == 'y'):
            continue
            counter = 0
        else:
            enter_ratings = 1


