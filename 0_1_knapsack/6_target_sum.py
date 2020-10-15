#Let S1 & S2 be first and second subset respectively. Then,
# S1 - S2 = difference
# S1 + S2 = sum (sum of all elements of given set)
# on adding the above two equations
# 2*S1 = difference + sum
# S1 = (diff + sum)/2

#function to fill the table and return last block as the count
import math
def countSubsetSum(set , n , sum):

	subset =[[0 for i in range(sum + 1)] for i in range(n + 1)]

	for i in range (n+1):
		for j in range (n+1):

			if(i == 0):
				subset[i][j] = 0

			if(j == 0):
				subset[i][j] = 1


	for i in range (1,n+1):
		for j in range (1,sum+1):

			if(set[i-1] <= j):
				subset[i][j] = subset[i-1][j-set[i-1]] + subset[i-1][j]

			else:
				subset[i][j] = subset[i-1][j]

	# uncomment this code to print table  
	# for i in range(n + 1):
	# 	for j in range(sum + 1):
	# 		print(subset[i][j], end ="   ")
	# 	print()

	#code for debugging purpose
	# print(n)
	# print(sum)
	# print(subset[n][sum])
	return subset[n][sum]

#code for driving the program
if __name__ == '__main__':

	set = [1,1,2,3]
	given_sum = 1

	n = len(set)
	sum = 0
	for i in range(0,n):
		sum = sum + set[i]

	S1 = 0
	S1 = math.floor((given_sum + sum)/2)
	print("Count of possible combinations:" )
	print(countSubsetSum(set,n,S1))
		

	




