def captcha(s):
	
	sum=0
	
	s=s+s[0]
	for i in range(0,len(s)-1):
		if s[i]==s[i+1]:
			sum+=int(s[i])
	
	print(sum)

if __name__=="__main__":
	captcha(input())