class Solution(object):
    def isValid(self, s):
        stack = []  #create a stack
        for char in s: 
            if char in '({[': # if its open paranthesis push onto the stack
                stack.append(char)
            else:
                if len(stack) == 0:  
                    return False
                if (char == ')' and stack[-1] != '(') or \  # return false if char and top of stack mismatches
                   (char == '}' and stack[-1] != '{') or \
                   (char == ']' and stack[-1] != '['):
                    return False  
                stack.pop() #pop only if it's a match
        return len(stack) == 0 
