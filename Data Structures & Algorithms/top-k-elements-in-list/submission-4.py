class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        top_k = {}
        all_freq = {}

        for num in nums:
            if num not in all_freq:
                all_freq[num] = 1
            else:
                all_freq[num] += 1
        
        sorted_items = sorted(all_freq.items(), key=lambda item: item[1], reverse=True)[:k]
        
        out = [item[0] for item in sorted_items]
        return out