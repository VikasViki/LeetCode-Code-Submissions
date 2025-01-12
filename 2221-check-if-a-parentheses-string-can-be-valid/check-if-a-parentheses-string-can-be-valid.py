class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        s_len = len(s)
        if s_len % 2 != 0:
            return False

        lock_stack = []
        unlock_stack = []

        for index in range(s_len):
            if locked[index] == '0':
                unlock_stack.append(index)
            
            else:
                if s[index] == '(':
                    lock_stack.append(index)
                else:
                    # Check '(' in lock_stack
                    if lock_stack:
                        lock_stack.pop()
                    else: # Change unlocked char to '('
                        if unlock_stack:
                            unlock_stack.pop()
                        else:
                            return False
        
        # Change unlocked char to ')' 
        while lock_stack:
            lock_top = lock_stack[-1]
            if not unlock_stack:
                return False
            
            unlock_top = unlock_stack[-1]
            if lock_top < unlock_top:
                lock_stack.pop()
                unlock_stack.pop()
            else:
                return False
        
        return len(unlock_stack) % 2 == 0

