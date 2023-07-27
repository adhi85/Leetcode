class Solution:
    def carFleet(self, target: int, position, speed):

        pair = [[p, s] for p, s in zip(position, speed)]

        fleet = curtime = 0

        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s

            if curtime < time:
                curtime = time
                fleet += 1

        return fleet
