class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        #use a stack that if a string is a oepning bracket add it to a stack
        # if its not a opening bracket check if that openingbracket has a closing bracket
        #in other words check if the closing bracket has a corresponding opening bracket at the top of the stack
        #if it does we return true if the clsoing bracket doensnt mwatch the opening bracket we return false
        #we will return true if the stack is empty because if the stack is empty that means each closing bracket had a corresponding opening bracket at the stop  of the stack
        # now we can use a hashmap that maps each clsoing bracket to a opening bracket. that way we can cehck if the opening bracket is the correspoing value to a closing bracket. if thats the case we pop the opening bracket from the stack.