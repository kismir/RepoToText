import os

#### name of your folder
mapath='exp'

#### get structure of your files
a=os.listdir(mapath)
malist=[]
def tree_mk(a,malist,thepath):
    for i in a:
        curpath=thepath+'//'+i
        try:
            h=os.listdir(curpath)
            malist=tree_mk(h,malist,curpath)       
        except:
            det=curpath#,str(os.path.getmtime(curpath))
            malist.append(det)
            
    return malist

ml=tree_mk(a,malist,mapath)

#### get list of all lines of all your files, files divided by symbol **^**
srce_atom=[]
for i in ml:
    f=open(i,'r')
    u=f.readlines()
    f.close()
    srce_atom.append(i+'\n')
    srce_atom.append('**^**\n')
    for j in u:
        srce_atom.append(j)
    srce_atom.append('**^**\n')

#### write plain text to source_base.txt in simple form
file=open('source_base.txt','w')
for i in srce_atom:
    file.write(i)
file.close()

#### rearrange file and save to source.txt
def rearrange(srce_atom):
    st_po=[]
    en_po=[]
    for i,el in enumerate(srce_atom):
        if i % 2 == 0:
            st_po.append(el)
        else:
            en_po.append(el)
    new_srce_atom=st_po+en_po

    return new_srce_atom

new_srce_atom=srce_atom
for i in range(100):
    new_srce_atom=rearrange(new_srce_atom)
new_srce_atom=reversed(new_srce_atom)

file=open('source.txt','w')
for i in new_srce_atom:
    file.write(i)
file.close()
    

