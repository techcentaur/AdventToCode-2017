
def cal(t):
	sum=0
	for i in t:
		j=l_n_s(i)
		sum+=j[0]-j[1]
	return sum

def l_n_s(i):
	l=int(i[0])
	s=int(i[0])
	for p in i:
		if int(p)>l:
			l=int(p)
		if int(p)<s:
			s=int(p)
	return [l,s]



if __name__=="__main__":

	filename=input("filename?")

	text=[]
	with open(filename,'r') as f:
		for line in f:
			tok=[]
			tok=line[:-1].split("\t")
			text.append(tok)
	s = cal(text)
	print(s)
