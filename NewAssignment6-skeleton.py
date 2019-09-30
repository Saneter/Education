from functools import reduce

scores = [25, 56, 79, 94, 99]
print("Initial scores are: " + str(scores))

# figure total scores using the reduce function from book
# fill in the () of the reduce function to summarize all the scores in the scores list
# Note:  25+56+79+94+99 = 353.  
total_scores = reduce( ) # fix this line of code

average = total_scores/len(scores)
print("Sum of all scores: " + str(total_scores))
print("Average: " + str(average))

# use filter to figure scores that are above average
#above_avg = filter( ) # fix this line of code so the filter method works and filters the scores list
print("Scores above average: " + str(list(above_avg)))

# use map to curve scores by 5 points
# add 5 points to each score
curved_scores = map()  #map the scores list by adding 5 to each item in the list
print("Curved scores are: " + str(list(curved_scores)))