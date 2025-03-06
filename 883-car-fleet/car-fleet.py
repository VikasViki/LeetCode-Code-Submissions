class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(key=lambda x:x[0], reverse=True)

        fleet = []
        for p, s in pairs:
            distance = target - p
            time = distance / s
            if not fleet:
                fleet.append(time)
            else:
                if time > fleet[-1]:
                    fleet.append(time)
        
        return len(fleet)