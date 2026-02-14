class Solution:
    """
    Problem: Valid Parentheses
    
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    
    Time Complexity: O(n)
    - We traverse the string once.
    
    Space Complexity: O(n)
    - Stack can grow up to n/2 in size.
    """
    def isValid(self, s: str) -> bool:
        stack = []
        # Map close bracket to open bracket
        closeToOpen = { ")":"(", "]":"[", "}":"{" }
        
        for c in s:
            # If it's a closing bracket
            if c in closeToOpen:
                # Check if stack is not empty and top matches
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # If it's an opening bracket, push to stack
            else:
                stack.append(c)
                
        # Valid only if stack is empty
        return True if not stack else False
