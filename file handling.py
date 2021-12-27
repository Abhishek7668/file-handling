# file hadling
#f = open('C:\\Users\\Lenovo\\Desktop\\shek\\pandit.txt','w')
for i in range(1,11):
    for j in range(1,11):
        f.write(str(i*j)+'\t')
    f.write('')
f.close()


