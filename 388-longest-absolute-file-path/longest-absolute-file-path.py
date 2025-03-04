class Solution:
    def lengthLongestPath(self, input: str) -> int:
        items = input.split("\n")
        stack = []

        def add_node_at_depth(item, depth):
            while len(stack) > depth:
                stack.pop()
            
            item_len = len(item)
            if stack:
                top = stack[-1]
                stack.append(top+item_len+1)
            else:
                stack.append(item_len)

            return stack[-1] if "." in item else 0

        max_path = 0

        for item in items:
            depth = item.count("\t")
            item = item.lstrip("\t")
            print(depth, item)
            max_path = max(max_path, add_node_at_depth(item, depth))
        
        return max_path