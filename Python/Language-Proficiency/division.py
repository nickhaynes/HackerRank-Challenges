Task 
Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, . The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
Current Buffer (saved locally, editable)    
 
 
 
 
1
from __future__ import division
2
​
3
if __name__ == '__main__':
4
    a = int(raw_input())
5
    b = int(raw_input())
6
​
7
print a//b
8
print a/b
