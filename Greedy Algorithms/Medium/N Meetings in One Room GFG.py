'''
You are given two arrays:

start[] - the starting times of meetings
end[] - the ending times of meetings
Your task is to find the maximum number of meetings that can be scheduled in a single room such that no two meetings overlap.

Example 1:
Input: 
start = [1, 3, 0, 5, 8, 5] 
end   = [2, 4, 6, 7, 9, 9]

Output: 4
Explanation:
One of the possible selections is meetings at:
(1,2), (3,4), (5,7), (8,9)
So, maximum 4 meetings can be held in the room.

Example 2:
Input:
start = [10, 12, 20]
end   = [20, 25, 30]

Output: 2
Explanation:
We can schedule meetings (10,20) and (20,30).
'''

class Meeting:
    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position


class Solution:
    def maximumMeetings(self, start, end):
        n = len(start)
        # Create Meeting objects with start, end, and position
        meets = [Meeting(start[i], end[i], i + 1) for i in range(n)]
        
        # Sort meetings by end time (then by start time if needed)
        meets.sort(key=lambda x: (x.end, x.start))
        
        lastTime = meets[0].end
        count = 1  # Select the first meeting by default
        
        # Iterate through the rest of the meetings
        for i in range(1, n):
            if meets[i].start > lastTime:
                count += 1
                lastTime = meets[i].end
                
        return count
sol = Solution()
print(sol.maximumMeetings(start=[1, 3, 0, 5, 8, 5], end=[2, 4, 6, 7, 9, 9]))