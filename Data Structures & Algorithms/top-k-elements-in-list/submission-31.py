class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else: freq[num] = 1
            
        for num, count in freq.items():
            buckets[count].append(num)
        print(buckets)

        result = []
        for i in range(len(buckets)-1, -1, -1):
            print(buckets[i])

            if len(buckets[i]) > 0 and len(result) < k:
                print(len(result))
                for value in buckets[i]:
                    result.append(value)
            
        return result
