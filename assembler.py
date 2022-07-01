codes={"add":{"type":1,"code":"10000"},"sub":{"type":1,"code":"10001"},"mul":{"type":1,"code":"10110"},"xor":{"type":1,"code":"11010"},"or":{"type":1,"code":"11011"},"and":{"type":1,"code":"11100"},"mov":{"type":2,"code":"10010"},"rs":{"type":2,"code":"11000"},"ls":{"type":2,"code":"11001"},"mov":{"type":3,"code":"10011"},"div":{"type":3,"code":"10111"},"not":{"type":3,"code":"11101"},"cmp":{"type":3,"code":"11110"},"ld":{"type":4,"code":"10100"},"st":{"type":4,"code":"10101"},"jmp":{"type":5,"code":"11111"},"jlt":{"type":5,"code":"01100"},"jgt":{"type":5,"code":"01101"},"je":{"type":5,"code":"01111"},"hlt":{"type":6,"code":"01010"},}
resistors={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","R7":"111"}

filename="stdin.txt"
file=makeFile(filename)
temp=file[0];
index=0;
while(temp not in codes):
	
	resistors[temp]=resistors[file[index+1]]

	index+=2;
	temp=file[index]


while(len(file)!=0):
	typev=codes[temp]["type"]
	if(temp=="mov"):
		if(file[index+2][0]=="0" or file[index+2][0]=="0"):
			typev=2
		else:
			typev=3
	out=codes[temp]["code"]

	if(typev==1):
		out+="00"
		index+=1
		out+=resistors[index]+resistors[index+1];
		index+=2
		
	elif(typev==2):
	elif(typev==3):
	elif(typev==4):
	elif(typev==5):
	elif(typev==6):
	else:




