
from collections import Counter
def anagram(s:str,t:str):
    Scount = Counter(s)
    Tcount = Counter(t)
    if Scount == Tcount:
       return True
    else:
        return False
print(anagram("Hello","ello"))    