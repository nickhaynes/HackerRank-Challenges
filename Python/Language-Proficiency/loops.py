Task 
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16
Current Buffer (saved locally, editable)    
 
 
 
 
print (i*i)
        i = i + 1
1
if __name__ == '__main__':
2
    n = int(raw_input())
3
​
4
i = 0
5
while i < n:
6
    if (n >= 1 and n <=20):
7
        print (i*i)
8
        i = i + 1
