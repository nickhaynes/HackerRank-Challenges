def split_and_join(line):
    new = line.split(" ")
    new = "-".join(new)
    return new


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)