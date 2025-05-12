if __name__ == '__main__':
    
    action_list = {
        'insert': 'arr.insert({},{})',
        'print': 'print(arr)',
        'remove': 'arr.remove({})',
        'append': 'arr.append({})',
        'sort': 'arr.sort()',
        'pop': 'arr.pop()',
        'reverse': 'arr.reverse()',
    }
    arr = []

    for _ in range(int(input())):
        commands = input()
        command = commands.split()
        eval(action_list.get(command[0]).format(*command[1:]))