'''
https://leetcode.com/problems/verifying-an-alien-dictionary

Creating a main list and appending each word as list of numbers by using the alphabet dict
ex: 
[[0, 15, 15], [0, 15, 15, 11, 4]] --> this is main_list
([0, 15, 15], [0, 15, 15, 11, 4])--> this is used for comparision 

https://stackoverflow.com/questions/13052857/comparing-two-lists-using-the-greater-than-or-less-than-operator
**comparison uses lexicographical ordering:** 
first the first two items are compared, and if they differ this determines the 
outcome of the comparison; if they are equal, the next two items are compared, 
and so on, until either sequence is exhausted.
'''

class Solution(object):
    def isAlienSorted(self, words, order)
        alphabets = {}
        for i in range(len(order)):
            alphabets[order[i]] = i
            
        main_list = []
        for word in words:
            newl = []
            for letter in word:
                newl.append(alphabets[letter])
            main_list.append(newl)
        print main_list
        for i in range(len(main_list)-1):
            print (main_list[i], main_list[i+1])
            if(main_list[i]>main_list[i+1]):
                    return False
        return True

def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict={}
        flag=False
        
        for i in range(len(order)): #Build dict
            order_dict[order[i]]=i
        
        for i in range(len(words)-1):
            min_length=min(len(words[i]),len(words[i+1]))
            for j in range(min_length):
                if order_dict[words[i][j]]<order_dict[words[i+1][j]]:
                    break
                elif order_dict[words[i][j]]==order_dict[words[i+1][j]]:
                    flag=True
                    continue
                else:
                    return False
            if flag==True:
                if len(words[i])>len(words[i+1]):
                    return False
            flag=False
```
