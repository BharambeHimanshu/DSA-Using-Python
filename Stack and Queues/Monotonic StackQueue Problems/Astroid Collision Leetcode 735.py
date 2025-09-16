# Astroid Collision
# Leetcode 735
'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
'''

class Solution:
    def asteroidCollision(self, asteroids):

        # Size of the array
        n = len(asteroids)

        # List implementation of stack
        st = []

        # Traverse all the asteroids
        for i in range(n):

            # Push the asteroid in stack if a
            # right moving asteroid is seen
            if asteroids[i] > 0:
                st.append(asteroids[i])

            # Else if the asteroid is moving
            # left, perform the collisions
            else:

                # Until the right moving asteroids are
                # smaller in size, keep on destroying them
                while st and st[-1] > 0 and st[-1] < abs(asteroids[i]):

                    # Destroy the asteroid
                    st.pop()

                # If there is right moving asteroid
                # which is of same size
                if st and st[-1] == abs(asteroids[i]):

                    # Destroy both the asteroids
                    st.pop()

                # Otherwise, if there is no left
                # moving asteroid, the right moving
                # asteroid will not be destroyed
                elif not st or st[-1] < 0:

                    # Storing the array in final state
                    st.append(asteroids[i])

        # Return the final state of asteroids
        return st
sol = Solution()
print(sol.asteroidCollision([5,10,-5]))