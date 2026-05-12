

# * Notes: 2 solutioons first was the on u made urself. Basically set the values in a hash map to there pair. Check whether a bracket is opening if not compare it to its mappingi n the hashset. Other solution simpler in terms of code logic but better efficency

# ! SELF MADE SOLUTION
class Solution:
    def isValid(self, s: str) -> bool:
        
        hashset = { '[' : ']', '{' : '}', '(' : ')'}
        stack = []

        for c in s:
            if c in hashset:
                stack.append(c)
            else:
                if not stack or hashset[stack.pop()] != c:
                    return False
                    
        return not stack

# ! More efficent
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if ch == ')' and top!='(':
                    return False
                if ch == '}' and top!='{':
                    return False
                if ch == ']' and top!='[':
                    return False
        if len(stack)==0:
            return True
        return False
