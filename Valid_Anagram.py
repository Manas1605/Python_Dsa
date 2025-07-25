# Counter gives ouput 
# Get the most common element and its frequency as a list of one tuple
        # Example: [(2, 5)] → number 2 appears 5 times
from collections import Counter
def anagram(s:str,t:str):
    Scount = Counter(s)
    Tcount = Counter(t)
    if Scount == Tcount:
       return True
    else:
        return False
print(anagram("Hello","ello"))    