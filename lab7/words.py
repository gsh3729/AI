file = open("sample.txt","r")
count = 0;

char = file.read(1)
if char==" ":
	flag=0
else:
	flag=1

while char:
	char = file.read(1)
	if char!=" ":
		flag=1;
		
	if char==" " and flag==1 :
		count+=1

	if char==" " and flag==0 :
		char = file.read(1)
		while char==" ":
			char = file.read(1)


print count