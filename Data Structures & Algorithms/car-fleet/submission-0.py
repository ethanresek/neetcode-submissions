"""
Can figure out how many turns it will take with equation:
    (target - position) / speed
So with target 10, position 1, and speed 3, you get there in 3 turns
Need to account for if the result is non-integral

We'll want some sort of monotonic stack where you add cars. 

Zip lists and sort in reverse order
Initialize list to act as stack
Create counter for fleets

Loop through the reversed list:
 - Keep track of the latest arriver of the current fleet (also would be the front of the fleet)
 - for every item compare it to the top of the stack
    - if it will reach the target at the same time or sooner than the latest arriver, add it to the stack
    - if it will reach the target later than the current target
        - remove all items of the stack. Each of these items is a part of the same fleet.
        - increment the fleet counter
        - add the new item to the stack
If there are any items in the stack still once the loop is done, increment the fleet counter once more
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position) == 0:
            return 0

        turns = []
        for i in range(len(position)):
            turns.append((target - position[i]) / speed[i])
        
        zipped = list(zip(position, speed, turns))
        zipped.sort(reverse=True)
        stack = [zipped[0]]
        num_fleets = 0

        for i in range(1, len(zipped)):
            if stack[0][2] >= zipped[i][2]:
                stack.append(zipped[i])
            else:
                while stack:
                    stack.pop()
                num_fleets += 1
                stack.append(zipped[i])

        if stack:
            num_fleets += 1

        return num_fleets