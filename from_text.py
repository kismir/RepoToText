import os

#### decompose source.txt fileto plain text that is placed to variable o
def dearrange(y):
    g=len(y)//2
    gb=len(y)%2
    res=[]
    for i in range(g):
        res.append(y[i])
        res.append(y[i+g+gb])
    for i in range(gb):
        res.append(y[g])

    return res

file=open('source.txt','r')
y=file.readlines()
file.close()

y=list(reversed(y))
for i in range(100):
    y=dearrange(y)
srce=y

o=''
for i in srce:
    o=o+i

#### split o variable and put result info to different folders
o=o.split('**^**\n')
for i in range(int((len(o)-1)/2)):
    if not os.path.exists(os.path.dirname(o[i*2][:-1])):
        try:
            os.makedirs(os.path.dirname(o[i*2][:-1]))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    f=open(o[i*2][:-1],'w')
    f.write(o[i*2+1][:-1])
    f.close()
