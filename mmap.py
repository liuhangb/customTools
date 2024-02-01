f = open("mmapsData.txt")
line = f.readline()
size = 0
while line:
    contents = line.split(" ")[0]
    pSplit = contents.split("-")
    start = int(pSplit[0], 16)
    end = int(pSplit[1], 16)
    size += end - start
    # print("start:%d,end:%d", start, end)
    #
    # print(line.split(" ")[0])
    # print (line)
    line = f.readline()
print("total Size:", size)
f.close()