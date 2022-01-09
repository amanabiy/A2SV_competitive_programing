class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """ Time: O(n) Space: O(n)"""
        bulls = 0
        cows = 0
        guesses = set(guess)
        count = Counter(guess)
        seen = set()
        for index, sec in enumerate(secret):
            if guess[index] == sec:
                bulls += 1
                count[guess[index]] -= 1
                seen.add(index)
        for index, sec in enumerate(secret):
            if index not in seen:
                if sec and count[sec] > 0 and sec in guesses:
                    cows += 1
                    count[sec] -= 1
        return f"{bulls}A{cows}B"