with open("testingout.txt","r") as file:
    data=file.read()
    data=data.split()
    print(len(data))