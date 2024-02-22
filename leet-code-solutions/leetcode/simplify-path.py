class Solution:
    def simplifyPath(self, path: str) -> str:
        # split by /
        # if . ignore
        # if .. clear stack
        # else add it to stack

        path = path.split("/")
        answer = []

        for p in path:
            if p == "..":
                if len(answer) >0:
                    answer.pop()
                    answer.pop()
            elif p == "." or p == "":
                continue
            else:
                answer.append("/")
                answer.append(p)
            # print(answer)
        answer = "".join(answer)
        return answer if answer != "" else "/"
