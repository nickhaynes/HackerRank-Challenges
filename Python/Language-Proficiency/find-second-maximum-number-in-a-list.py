Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

Current Buffer (saved locally, editable)    
 
 
 
 
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

arr.sort()
i = arr[n-1]

for x in arr:
    if x != arr[n-1]:
        if x < arr[n-1]:
            i = x

print i
1
if __name__ == '__main__':
2
    n = int(raw_input())
3
    arr = map(int, raw_input().split())
4
​
5
arr.sort()
6
i = arr[n-1]
7
​
8
for x in arr:
9
    if x != arr[n-1]:
10
        if x < arr[n-1]:
11
            i = x
12
​
13
print i
14
​
