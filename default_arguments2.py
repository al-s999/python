class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    results = []
    for _ in range(n):
        results.append(stream.get_next())
    return results

queries = int(input())
output = []
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        output.extend(print_from_stream(n))
    else:
        output.extend(print_from_stream(n, OddStream()))
        
for number in output:
    print(number)
