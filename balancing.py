import random

file1 = open('balanced_dataset.data', 'r')
lines = file1.readlines()
cnt=0
for line in lines :
     if(line[len(line)-2]=="g"):
        print(line)
        cnt+=1

n=len(lines)-1
while cnt>6688:
    x = random.randint(0, n)
    print(x)
    print(len(lines))
    if(lines[x][len(lines[x])-2]=="g"):
        lines.remove(lines[x])
        n-=1
        cnt-=1
#data check
# g=0
# h=0
# for line in lines :
#      if(line[len(line)-2]=="g"):
#         g+=1
#      else:
#         h+=1
#
# print(g)
# print(h)

# new file
file1 = open('balanced_dataset.data', 'w')
file1.writelines((lines))
file1.close()
