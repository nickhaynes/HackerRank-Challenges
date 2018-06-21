Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123
Current Buffer (saved locally, editable)    
 
 
 
 
)
1
from __future__ import print_function
2
​
3
if __name__ == '__main__':
4
    n = int(raw_input())
5
​
6
i = 0
7
x = ''
8
​
9
while i < n:
10
    i = i + 1
11
    x = x + str(i)
12
print (x)
