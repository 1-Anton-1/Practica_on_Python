file=open('data/text.txt','r')
l=file.read().split('  ')
file.close()
for i in range(len(l)):
    l[i]=int(l[i])
if l[3]<l[1]:
    print(l[0])
else:
    print(l[0]+(l[3]-l[1])*l[2])