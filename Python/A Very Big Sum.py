#Calculate and print the sum of the elements in an array, keeping in mind that some 
#of those integers may be quite large.

#Input Format

#The first line of the input consists of an integer . 
#The next line contains  space-separated integers contained in the array.

#Output Format

#Print the integer sum of the elements in the array.

#Constraints 

#1 <= n <= 10
#0 <= ar[i] <= 10**10

#Sample Input

#5
#1000000001 1000000002 1000000003 1000000004 1000000005

#Output

#5000000015

#
# Complete the aVeryBigSum function below.
#

def aVeryBigSum(n, ar):
    i=0
    p=0
    while i < n and 1 <= n <= 10 and 0 <= ar[i] <= 10**10:
        p=p+ar[i]
        i += 1
    return p
