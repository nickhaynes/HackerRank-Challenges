if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
my_tuple = ()
for x in integer_list:
    my_tuple += (x,)
print(hash(my_tuple))