#function to fill the table and return last block as the answer
def isSubsetSum(set , n , sum):

	subset =[[False for i in range(sum + 1)] for i in range(n + 1)]

	for i in range (n+1):
		for j in range (n+1):

			if(i == 0):
				subset[i][j] = False

			if(j == 0):
				subset[i][j] = True


	for i in range (1,n+1):
		for j in range (1,sum+1):

			if(set[i-1] <= j):
				subset[i][j] = subset[i-1][j-set[i-1]] or subset[i-1][j]

			else:
				subset[i][j] = subset[i-1][j]

	# uncomment this code to print table  
	# for i in range(n + 1):
	# 	for j in range(sum + 1):
	# 		print(subset[i][j], end ="   ")
	# 	print()

	#code for debugging purpose
	# print(n)
	# print("\n")
	# print(sum)
	# print("\n")
	# print(subset[n][sum])
	# print("\n")
	return subset[n][sum]

#code for driving the program
if __name__ == '__main__':

	set = [3,4,5,2]
	sum = 6
	n = len(set)

	if(isSubsetSum(set,n,sum) == True):
		print("Found a subset with given sum")

	else:
		print("No subset found with given sum")

