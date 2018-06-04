#Given an array of integers, find the sum of its elements.

#Input Format

#The first line contains an integer, n, denoting the size of the array. 
#The second line contains n space-separated integers representing the array's elements.

#Output Format

#Print the sum of the array's elements as a single integer.

#Sample Input

#6
#1 2 3 4 10 11

#Sample Output

#31

#Explanation

#We print the sum of the array's elements: .

#
# Complete the simpleArraySum function below.
#

def simpleArraySum(ar):
    n=len(ar)
    i=0
    p=0
    while i<n:
        p=p+ar[i]
        i+=1
    return p
