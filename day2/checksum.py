def checksum(m):
	sum=0
	
	for i in len(m[]):
		(l,s)=largest_smallest(m[i][])
		sum+=l-s
	
	print(sum)



def largest_smallest(l):
	larg=l[0]
	small=l[0]
	
	for i in l:
		if int(i)>l:
			larg=int(i)
		if int(i)<s:
			small=int(i)

	return (larg,small)

if __name__="__main__":
	m=[][]
	checksum(m)