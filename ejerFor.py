

c1,c2,c3=0
tot=int(input('total'))
for i in range(tot):
    num=int(input('numero'))
    if (num<5):
        c1+=1
    if (num>=6 and num<=10):
        c2+=1
    if (num>10):
        c3+=1
porcMen5=c1*100/tot
