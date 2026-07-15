class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        opp = sorted(freq, key=freq.get)   # -> [100, 2, 1]
        ans=[]
        for i in range(len(opp)-1, len(opp)-1-k,-1):
            ans.append(opp[i])
        return ans


        