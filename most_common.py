from collections import Counter
if __name__ == "__main__":
    s = input().strip()
    number = Counter(s)
    number_string = sorted(number.items(), key=lambda x: (-x[1], x[0]))
    for c,co in number_string[:3]:
        print(c, co)
        
