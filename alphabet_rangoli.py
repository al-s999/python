def print_rangoli(size):
    import string
    
    #string.ascii_lowercase returns  'abcdefghijklmnopqrstuvwxyz' and get size and finaly reverse the string (ex: abc -> cba)
    alphabet = string.ascii_lowercase[:size][::-1]

    lines = []
    for i in range(size):
        
        #create pattern like "c-b-a" for index 2 in size 3
        pattern = "-".join(alphabet[:i + 1])
        
        #create a reverse pattern without the last element like 'b-c' for 'c-b' and mix tith pattern and set pattern in the midle of long 4 x size - 3
        lines.append((pattern + pattern[-2::-1]).center(4 * size - 3, "-"))
        
    #get element for lines start with indeks 2 for the last and mix with lines (ex: [A, B, C] -> [B, A])')
    print("\n".join(lines + lines[-2::-1]))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
# example : input = 2
#           output = --b--
#                    b-a-b
#                    --b--
#  note : why '4 x size - 3'
#  if size = 3, 4 * 3 - 3 = 9
# so the length in center line is 9