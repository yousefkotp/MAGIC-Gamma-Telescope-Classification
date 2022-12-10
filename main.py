import random
file = open('balanced_dataset.data', 'r')
lines = file.readlines()
file.close()
# cnt=0
# g=[]
# h=[]
# for line in lines :
#      if(line[len(line)-2]=="g"):
#         g.append(line)
#      else :
#          h.append(line)
#
# print(len(g))
# print(len(h))

training_split=[]
test_split=[]
cntg=0
cnth=0
n=len(lines)-1
while len(test_split) < 4012:
    x = random.randint(0, n)
    if(lines[x][len(lines[x])-2]=="g" and cntg <2006):
        cntg+=1
        test_split.append(lines[x])
        lines.remove(lines[x])
    elif (lines[x][len(lines[x])-2]=="h" and cnth <2006) :
        cnth+=1
        test_split.append(lines[x])
        lines.remove(lines[x])
    n-=1

# print(len(test_split))
# print(len(lines))

training_split_g=0
training_split_h=0
test_g=0
test_h=0
for  line in lines:
    if(line[len(line)-2]=="g"):
        training_split_g+=1
    else:
        training_split_h+=1

for  line in test_split:
    if(line[len(line)-2]=="g"):
        test_g+=1
    else:
        test_h+=1


print("------------------")
print(test_h)
print(test_g)
print(training_split_h)
print(training_split_g)
print(len(lines))
print(len(test_split))
file1 = open('training_split.data', 'w')
file1.writelines((lines))
file1.close()

file2 = open('test_split.data', 'w')
file2.writelines((test_split))
file2.close()






