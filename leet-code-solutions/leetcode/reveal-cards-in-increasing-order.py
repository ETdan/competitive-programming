class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        queue = deque(range(len(deck)))

        result = [0] * len(deck)

        for card in deck:
            index = queue.popleft()
            result[index] = card
            if queue:
                queue.append(queue.popleft())

        return result