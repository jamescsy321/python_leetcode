from typing import List


# 735. Asteroid Collision
# stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                prev_asteroid = stack.pop()

                if prev_asteroid > abs(asteroid):
                    asteroid = prev_asteroid
                elif prev_asteroid == abs(asteroid):
                    asteroid = 0

            if asteroid != 0:
                stack.append(asteroid)

        return stack


if __name__ == '__main__':
    result = Solution()
    asteroids = [5, 10, -5]
    ans = result.asteroidCollision(asteroids)
    print(ans)
