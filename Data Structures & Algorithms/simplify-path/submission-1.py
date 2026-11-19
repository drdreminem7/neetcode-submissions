class Solution:
    def simplifyPath(self, path: str) -> str:
        arguments = path.split("/")
        stack = []

        for arg in arguments:
            if arg == "" or arg == ".": continue
            elif arg == "..":
                if stack: stack.pop()
                else: continue
            else: stack.append(arg)
        
        return "/" + "/".join(stack)