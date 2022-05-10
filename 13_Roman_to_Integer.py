class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum_ = 0

        # Checked each letter in word
        for i in range(len(s)):
            # first condition was created to provent IndexError of second condition in last time for checking
            # secode condition was created to investigate writing criteria of roman number
            # if front letter has less valuable than back number that mean back - front number
            if i + 1 < len(s) and symbols[s[i]] < symbols[s[i + 1]]:                
                sum_ -= symbols[s[i]]
            # if not let added the letter 
            else:
                sum_ += symbols[s[i]]
        return sum_

print(Solution().romanToInt("MCMXCIV"))