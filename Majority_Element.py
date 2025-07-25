# most_common(1) → returns [(num, freq)]
# [0] → get the first (num, freq) tuple
# [0] again → get just the num
from collections import Counter
from typing import List
def majorityElement( nums: List[int]):
       return Counter(nums).most_common(1)[0][0]
print(majorityElement([1,2,2,2,2,1,1]))