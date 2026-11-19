class Solution:
    def simplifyPath(self, path: str) -> str:
        arguments = path.split("/")
        stack = []

        for arg in arguments:
            if arg == "..":
                if stack: stack.pop()
            elif arg != "" and arg != ".": stack.append(arg)
        
        return "/" + "/".join(stack)