Task 
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, . The second line contains the second integer, .

Constraints

 

Output Format

Print the three lines as explained above.

Sample Input 0

3
2
Sample Output 0

5
1
6
Explanation 0

 
 

Current Buffer (saved locally, editable)    
 
 
 
 
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    
print (a+b)
print (a-b)
print (a*b)
1
if __name__ == '__main__':
2
    a = int(raw_input())
3
    b = int(raw_input())
4
    
5
print (a+b)
6
print (a-b)
7
print (a*b)
