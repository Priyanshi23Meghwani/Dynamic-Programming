import math
#function to fill the table and return last block as the answer
def isSubsetSum(set , n , sum):
	sum = math.floor(sum)
	#print(sum)

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
	# code used for debugging
	# print(n)
	# print("\n")
	# print(sum)
	# print("\n")
	# print(subset[n][sum])
	# print("\n")
	return subset[n][sum]

if __name__ == '__main__':

	set = [1,5,11,5]
	n = len(set)
	sum = 0
	for i in range(0,n):
		sum = sum + set[i]

	#print(sum)
	print("\n")
	if(sum % 2 != 0 ):
		print("FALSE..equal sum partition is not possible")

	else:
		if(isSubsetSum(set, n , sum/2) == False):
			print("FALSE..equal sum partition is not possible")

		else:
			print("TRUE..equal sum partition is possible")