myFile = open("file.txt","r")
for line in myFile:
    line=line.rstrip()
    if not'@uct.ac.za' in line:
        continue
    print(line)