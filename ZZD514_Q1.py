import statistics

print("Please enter the customers ratings between 1-5")
counter = 0
List = []

"""gathers a rating from input."""
"""checks to make sure rating is less than 5 to append to the list."""
while(counter < 5):
    rating = int(input())
    while(int(rating) > 5):
        print("invalid. try again.")
        rating = int(input())
    List.append(rating)
    counter += 1

"""assigning variables from statistics lib"""
min = min(List)
max = max(List)
range = (max-min)
mean = statistics.mean(List)
median = statistics.median(List)
mode = statistics.mode(List)
variance = statistics.variance(List)
stdev = statistics.stdev(List)

print("The min is: ", min)
print("The max is: ", max)
print("The range is: ", range)
print("The mean is: ", mean)
print("The median is: ", median)
print("The mode is: ", mode)
print("The variance is: ", variance)
print("The standard deviation is: ", "{:.2f}".format(stdev))