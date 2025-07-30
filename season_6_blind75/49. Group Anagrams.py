"""

49. Group Anagrams

make fingerprint with dict
dict compare equality
group!


"""

def solve(strs):

    def compare(f1, f2):
        if len(f1) != len(f2):
            return False
        
        for k in f1:
            if k not in f2 or f1[k] != f2[k]:
                return False
        return True
    
    
            

