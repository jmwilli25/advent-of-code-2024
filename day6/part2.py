# Idea: Before the guard starts moving look at matrix and place an obstacle where there isn't one. Set the guard on her
# path and if we enter a loop then increment a counter, remove the obstacle, add a new one and start the guard from the
# beginning again. If the obstacle does not cause a loop, don't count it and move on to placing the next obstacle.
# Iterate through every position in the floorplan_matrix and count the number of times placing a single
# new obstacle causes the guard to enter a loop.

# Idea to test if the guard is in a loop. If the guard has visited the same position going
# the same direction twice, they are in a loop.

