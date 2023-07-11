if __name__ == '__main__':
    
    N = int(input())
    integers = []
    all_commands = []
    
    for index in range(0,N):
        stdin = input().split(" ")
        all_commands.append(stdin)
        
    for command in all_commands:
        if "insert" in command:
            integers.insert(int(command[1]), int(command[2]))
        elif "print" in command:
            print(integers)
        elif "remove" in command:
            integers.remove(int(command[1]))
        elif "append" in command:
            integers.append(int(command[1]))
        elif "sort" in command:
            integers.sort()
        elif "pop" in command:
            integers.pop()
        else:
            integers.reverse()
