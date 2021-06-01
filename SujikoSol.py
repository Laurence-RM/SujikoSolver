import curses
import random, time
import ConGUI as gui

def main():
    gui.main()
    n = generate()
    gui.interact(n)
    exit()


def solve(sums, nums):
    # sums and nums go left to right, top to bottom

    # Solving strategy 1:
    #   Find possible nums for each square, within each quadrant , then try possibilities
    quads = []
    quads.append([sums[0], [0,1,3,4]])
    quads.append([sums[1], [1,2,4,5]])
    quads.append([sums[2], [3,4,6,7]])
    quads.append([sums[3], [4,5,6,8]])

    solution = None

    # Which nums 1-9 are not used
    available = []
    # list of possible nums for each num 1-9
    possible = []
    for n in nums:
        available.append(True if not n else False)
        possible.append(set([]))

    # Count # of free spaces
    for qu in quads:
        qu.append(qu[1].count(None))

    while not solution:
        for q in quads:
            # try strategies
            diff = q[0] - sum(nums[x] for x in q[1] if nums[x] is not None)
            # four empty squares
            if q[2] == 4:
                if diff == 30:
                    for x in q[1]:
                        possible[x] = {6,7,8,9}
                elif diff == 10:
                    for x in q[1]:
                        possible[x] = {1,2,3,4}
            elif q[2] == 3:
                if diff == 6:
                    for x in q[1]:
                        possible[x] = {1,2,3}
                elif diff == 24:
                    for x in q[1]:
                        possible[x] = {7,8,9}


            # three

            # two

            # one
    return




def generate():
    # generate nums 1-9
    nums = list(range(1, 10))
    random.shuffle(nums)

    # find circle vals
    sumVals = []
    sumVals.append(sum(nums[0:2] + nums[3:5]))
    sumVals.append(sum(nums[1:3] + nums[4:6]))
    sumVals.append(sum(nums[3:5] + nums[6:8]))
    sumVals.append(sum(nums[4:6] + nums[7:]))

    ind = random.randint(0,8)
    gui.addSums(*sumVals, ind, nums[ind])
    return nums

if __name__ == "__main__":
    main()