def makeFile(filename):
    with open(filename,"r") as file:
        data=file.read()
        data=data.split()
        return data

def writeIn(output,out):
    with open(output,"a") as file:
        file.write(out)
        file.write("\n")

def decimalToBinary(dec):
    string=""
    while(dec!=0):
        string=str(dec%2)+string
        dec=int(dec/2)
    if(len(string)>8):
        print("immediate value out of range")
        return " ";
    while(len(string)<8):
        string="0"+string

    return string

codes={"add":{"type":1,"code":"10000"},"sub":{"type":1,"code":"10001"},"mul":{"type":1,"code":"10110"},"xor":{"type":1,"code":"11010"},"or":{"type":1,"code":"11011"},"and":{"type":1,"code":"11100"},"mov":{"type":2,"code":"10010"},"rs":{"type":2,"code":"11000"},"ls":{"type":2,"code":"11001"},"mov":{"type":3,"code":"10011"},"div":{"type":3,"code":"10111"},"not":{"type":3,"code":"11101"},"cmp":{"type":3,"code":"11110"},"ld":{"type":4,"code":"10100"},"st":{"type":4,"code":"10101"},"jmp":{"type":5,"code":"11111"},"jlt":{"type":5,"code":"01100"},"jgt":{"type":5,"code":"01101"},"je":{"type":5,"code":"01111"},"hlt":{"type":6,"code":"01010"},}
registers={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}

filename="test1"
file=makeFile(filename)
output="output.txt"
temp=file[0]
print(file)
index=0

while(temp not in codes):
    if(file[index][:5]=="label"):
        if(file[index] in registers):
            print(f"variable already declared and cannot be used as label name in line {index/2 +1}")
            temp="hlt"
            f=open(output,"w").close()
        registers[file[index]]=file[index]
        index+=1
        temp=file[index]
        break
   registers[temp]=file[index+1]
    if(temp!="var"):
        print(f"Undefined variable at line {(index/2)+1}")
        temp="hlt"
        f=open(output,"w").close()
    else:

        index+=2;
        temp=file[index]
line=index/2 +1



while(index<len(file)):
    
    if(file[index]!="hlt" and file[index+2]=="FLAGS" and file[index]!="mov"):
            print(f"inappropriate use of FLAGS in line {line}")
            
            f=open(output,"w").close()
            break
    if(temp=="var"):
        print(f"syntax error in line {line}: Variables should be declared at the top")
        f=open(output,"w").close()
        break

    if(file[index][:5]=="label"):
        if(file[index] in registers):
            print(f"variable already declared and cannot be used as label name in line {index/2 +1}")
            break
            f=open(output,"w").close()
        registers[file[index]]=file[index]
        index+=1
        temp=file[index]
        continue

        
    typev=codes[temp]["type"]
    out=codes[temp]["code"]
    print(temp)
    if(temp=="mov"):
        if(file[index+1]=="FLAGS"):
            print(f"invalid use of FLAGS at line {line}")
            break
        if(file[index+2][0]=="$"):
            typev=2
            out="10010"
        else:
            out="10011"
            typev=3
    
    index+=1
    if(typev==1):
        out+="00"
        try:
            out+=registers[file[index]]+registers[file[index+1]]+registers[file[index+2]]
        except:
            print(f"invalid inputs for the command at line {line}")
            break
        line+=1 
        index+=3


    elif(typev==2):
        try:
            out+=registers[file[index]]
            index+=1
            out+=decimalToBinary(int(file[index][1:]))
        except:
            print(f"invalid inputs for the command at line {line}")
       

        if(len(out)<16):
            print(line)
            break
        index+=1
        line+=1


    elif(typev==3):
        try:
            out+="00000"
            out+=registers[file[index]]+registers[file[index+1]]
        except:
            print(f"invalid inputs for the command at line {line}")
            break
        index+=2
        line+=1
    elif(typev==4):
        try:
            out+=registers[file[index]]
            index+=1
            if(file[index] in registers):
                out+=registers[file[index]]
            else:
                if(len(file[index])==8):
                    out+=file[index]
                else:
                    print(f"wrong input for the memory addr at line {line}")

            
        except:
            print(f"invalid inputs for the command at line {line}")
            break
        index+=1
        line+=1
    elif(typev==5):
        out+="000"
        try:

            out+=file[index]
        except:
            print(f"invalid inputs for the command at line {line}")
            break
        index+=1
        line+=1
    elif(typev==6):
        index+=1
        out+="00000000000"
        writeIn(output,out)
        break
    else:
        print("wrong input")
        break

    
    writeIn(output,out)
    temp=file[index]


# if(temp!="hlt"or index<len(file)):
#   print("inappropriate use of hlt")
#   f=open(output,"w").close()

