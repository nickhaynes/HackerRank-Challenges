def print_formatted(number):
    padding = number.bit_length()
    for i in range(1,number+1):
        print(str(i).rjust(padding),oct(i).split('o')[1].rjust(padding),hex(i).split('x')[1].upper().rjust(padding),bin(i).split('b')[1].rjust(padding))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)