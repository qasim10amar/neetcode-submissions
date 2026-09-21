class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse = True)
 

        for car in cars:
            time = (target - car[0]) / car[1]
            
            stack.append(time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        



        # 4, 6, 8, 10
        # 1, 3, 5, 7, 9, 11
        # 0, 2, 4, 6 , 8, 10
        # 7, 8, 9, 10