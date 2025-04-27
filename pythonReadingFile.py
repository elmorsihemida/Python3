fhandle = open("file.txt","r+")
#read_file = fhandle.read()
for line in fhandle:
    line=line.strip()
    if line.startswith("F"):
        print(line)

