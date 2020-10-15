#function to fill the table and return last block as the answer
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

	set = [2,3,5,6,8,10]
	sum = 10
	n = len(set)

	print(countSubsetSum(set,n,sum))
		

	

