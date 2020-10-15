#function to fill the table and return last block as the answer
def minSubsetSum(set , n , sum):

	subset =[[False for i in range(sum + 1)] for i in range(n + 1)]

	for i in range (n+1):
		for j in range (sum+1):

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
	limit = 0
	if(sum % 2 == 0):
		limit = sum/2
	else:
		limit = ((sum-1)/2)
	#print(limit)
	limit = int(limit)

	new=[]
	#new list to store the possible candidates for S1(sum of first subset) till halfway
	for i in range(n+1):
		for j in range(limit+1):
			if(i == n and subset[i][j] == True):

				new.append(j)
	#print(new)

	till = len(new)
	mn = sum
	#print(sum)
	print("Minimum subset sum difference is ")
	for i in range(0,till):
		mn = min(mn,sum-(2*new[i]))
	print(mn)

	#code for debugging purpose
	# print(n)
	# print(sum)
	# print(subset[n][sum])
	return subset[n][sum]

#code for driving the program
if __name__ == '__main__':

	set = [1,6,11,5]
	n = len(set)
	sum = 0
	for i in range(0,n):
		sum = sum + set[i]
	minSubsetSum(set,n,sum)

