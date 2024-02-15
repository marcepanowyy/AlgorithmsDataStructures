# Minimum Number of Refueling Stops

# A car travels from a starting position to a destination which is target miles east of
# the starting position.

# There are gas stations along the way. The gas stations are represented as an array stations where
# stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the
# starting position and has fueli liters of gas.

# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.
# It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop
# and refuel, transferring all the gas from the station into the car.

# Return the minimum number of refueling stops the car must make in order to reach its destination.
# If it cannot reach the destination, return -1.

# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
# If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

from queue import PriorityQueue

def refueling(target, start_fuel, stations):

    pq = PriorityQueue()
    stations.append([float("inf"), 0])
    pq.put(-start_fuel)

    position, ans, i = 0, -1, 0

    while not pq.empty():

        additional_fuel = pq.get()
        additional_fuel *= (-1)
        position += additional_fuel
        ans += 1

        if position >= target: return ans

        while stations[i][0] <= position:
            pq.put(-stations[i][1])
            i += 1

    return -1


target1 = 100
startFuel1 = 10
stations1 = [[10,60],[20,30],[30,30],[60,40]]
# Expected: 2

target2 = 100
startFuel2 = 50
stations2 = [[25,25],[50,50]]
# Expected: 1

# print(refueling(target1, startFuel1, stations1))
# print(refueling(target2, startFuel2, stations2))