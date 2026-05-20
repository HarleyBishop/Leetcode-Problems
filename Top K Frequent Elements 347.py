

#! first attept wads first solution next 2 are better bucket sort is optimal

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        res = []
        for i in range(k):
            num = max(count, key=count.get)
            res.append(num)
            count.pop(num)
        return res
    

#! Better than first solution cimilar in conecpt
def topKFrequent(self, nums, k):
    count = Counter(nums)
    # Sort the counted array so most frequent will be at the end
    # Ensure they are sorted by frequency not index as key
    # Reverse so most frequent first
    # Slice K elements so only most frequent K elements remain. e.g. give me everything up to element k so K = 2 give me the first 2 elements
    return sorted(count, key=count.get, reverse=True)[:k]

#! Best solution using bucket sort STIDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY STUDY

def topKFrequent(self, nums, k):
    count = Counter(nums)
    # create a bucket for the number of numbers in nums + 1
    # This is so the number of buckets matches the max number of possible frequency + account for index 0 
    buckets = [[] for _ in range(len(nums) + 1)]

    # Find the bucket of the number frequency. Insert the number into its frequency buckets e.g. numbe 2 appears 3 times therefore 2 goes into bucket 3
    # Num is key freq is value in dict
    for num, freq in count.items():
        buckets[freq].append(num)


    res = []
    # Start at the last index traversei n reverse. E.g. len: start, stop step therefore start at final bucket. -1 cause lists start at 0. then go to index 0 and for every step traverse -1 so go in revrser by 1 bucket ewach time
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            # add k numbers to the response list
            res.append(num)
            if len(res) == k:
                return res