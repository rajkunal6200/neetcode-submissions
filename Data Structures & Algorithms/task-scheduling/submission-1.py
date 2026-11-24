from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq =max(count.values())

        maxcount = 0
        for Freq in count.values():
            if Freq == maxFreq:
                maxcount+=1
        return max(len(tasks),(maxFreq-1)*(n+1)+maxcount)        

