# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        unused_group = 1

        row_group = dict()
        col_group = dict()

        linked_groups = dict()

        def ultimate_group(g):
            if linked_groups[g] == g:
                return g
            ult_g = ultimate_group(linked_groups[g])
            linked_groups[g] = ult_g
            return ult_g

        def merge_group(g1, g2):
            ultg1 = ultimate_group(g1)
            ultg2 = ultimate_group(g2)
            linked_groups[ultg1] = ultg2

        for row, col in stones:
            grow = row_group.get(row)
            gcol = col_group.get(col)

            if grow and gcol and grow != gcol:
                merge_group(grow, gcol)
            else:
                g = grow or gcol
                if not g:
                    g = unused_group
                    unused_group += 1
                    linked_groups[g] = g
                else:
                    g = ultimate_group(g)
                row_group[row] = g
                col_group[col] = g
        
        return len(stones) - len({ultimate_group(g) for _, g in linked_groups.items()})