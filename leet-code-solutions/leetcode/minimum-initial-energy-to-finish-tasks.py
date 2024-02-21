class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[0] - x[1], x[1]))

        min_initial_energy = 0
        curr = 0

        for index, value in enumerate(tasks):
            if curr < value[1]:
                min_initial_energy += value[1] - curr
                curr += value[1] - curr
                curr -= value[0]
            else:
                curr -= value[0]

        return min_initial_energy
