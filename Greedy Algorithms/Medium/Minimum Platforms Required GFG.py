'''
Given two arrays:
arr containing arrival times
dep containing departure times
Find the minimum number of platforms required so that no train waits. A platform occupied by a train from its arrival time until its departure time cannot be used by another train in that interval.

Example 1
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
Explanation:
At time around 950 to 1100 multiple trains overlap in the station, so three platforms are needed at peak.

Example 2
arr = [100, 200, 300]
dep = [110, 210, 320]
Output: 1
Explanation:
No overlaps beyond one at any time. One platform is sufficient.
'''

class Solution:
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()

        ans = 1
        count = 1
        i = 1
        j = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:  # one more platform needed
                count += 1
                i += 1
            else:  # one platform can be reduced
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans
sol = Solution()
print(sol.minimumPlatform(arr = [100, 200, 300] , dep = [110, 210, 320]))