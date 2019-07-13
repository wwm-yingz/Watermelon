#西瓜书，1.2题，第一种方法直接用itertool库的排列代码，此方法会爆内存直接报错，当k=8时通过itertool库返回的list长度已经是3亿了，k=15的时候是1w亿，会直接报错
#wwm
#wwm-yingz.github.io
#python

#去重函数，0代表任意a代表固定情况，例如，del0aa将会把Aaa，Baa从当前数组中去掉（小写a是泛指）
def del000(i,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0]==0 and tup[t][1]==0 and tup[t][2]==0:
                pass
            else:
                tup.pop(t)
                del000(i,tup)
        except:
            break

def del00a(num,tup):
    for t in range(len(tup)):
        try:
            if tup[t][2]==num and (tup[t][0]!=0 or tup[t][1]!=0):
                tup.pop(t)
                del00a(num,tup)
                pass
        except:
            break
def del0a0(num,tup):
    for t in range(len(tup)):
        try:
            if tup[t][1]==num and (tup[t][0]!=0 or tup[t][2]!=0):
                tup.pop(t)
                del0a0(num,tup)
                pass
        except:
            break
def dela00(num,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0]==num and (tup[t][1]!=0 or tup[t][2]!=0):
                tup.pop(t)
                dela00(num,tup)
                pass
        except:
            break

def del0aa(num1,num2,tup):
    for t in range(len(tup)):
        try:
            if tup[t][1] == num1 and tup[t][2] == num2 and tup[t][0] != 0:
                tup.pop(t)
                del0aa(num1,num2,tup)
                pass
        except:
            break
    pass
def dela0a(num1,num2,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0] == num1 and tup[t][2] == num2 and tup[t][1] != 0:
                tup.pop(t)
                dela0a(num1,num2,tup)
                pass
        except:
            break
    pass
def delaa0(num1,num2,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0] == num1 and tup[t][1] == num2 and tup[t][2] != 0:
                tup.pop(t)
                delaa0(num1,num2,tup)
                pass
        except:
            break
    pass

#检查单个的组合的重复性
def check(tup):
    t=0
    while(t<9):
        for i in range(len(tup)):
            try:
                if tup[i][0]==0 and tup[i][1]==0 and tup[i][2]==0:
                    del000(i,tup) #把这个tup删剩一个就完了然后可以直接退出了
                    break
                if tup[i][0]==0 and tup[i][1]==0:
                    del00a(tup[i][2],tup)
                    continue
                if tup[i][0] == 0 and                tup[i][2] == 0:
                    del0a0(tup[i][1],tup)
                    continue
                if tup[i][0] == 0 :
                    del0aa(tup[i][1],tup[i][2], tup)
                    continue
                if                 tup[i][1] == 0 and tup[i][2] == 0:
                    dela00(tup[i][0], tup)
                    continue
                if                 tup[i][1] == 0:
                    dela0a(tup[i][0],tup[i][2], tup)
                    continue
                if                                     tup[i][2] == 0:
                    delaa0(tup[i][0],tup[i][1], tup)
                    continue
            except:
                break
        t=t+1

if __
import itertools #排列组合
final=[0 for i in range(19)]#用来存最后的数据
zuhe=[] #存所有组合48种

#初始化组合
for i in range(3):
    for j in range(4):
        for k in range(4):
            zuhe.append([i,j,k])

#枚举法取东西
for i in range(18):
    all_=list(itertools.combinations(zuhe,i+1))  #all=[ (第一种组合 [],[],[],[]   )    ,()    ]
    all=[]
    for i in range(len(all_)):
        all.append(list(all_[i]))    #转list格式

    for j in range(len(all)):
        # dell=0#每次要初始话dell
        tmp=len(all[j])
        check(all[j]) #传进去的是一个list  直接对ALL[j]进行修改删除 删除冗余项
        #print(all[j])
        if len(all[j])==tmp:
            final[len(all[j])]=final[len(all[j])]+1
        #搞定

print(final)




#西瓜书，1.2题，第一种方法直接用itertool库的排列代码，此方法会爆内存，当k>8很难算了
#wwm
#python

#去重函数，0代表任意a代表固定情况，例如，del0aa将会把Aaa，Baa从当前数组中去掉（小写a是泛指）
def del000(i,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0]==0 and tup[t][1]==0 and tup[t][2]==0:
                pass
            else:
                tup.pop(t)
                del000(i,tup)
        except:
            break

def del00a(num,tup):
    for t in range(len(tup)):
        try:
            if tup[t][2]==num and (tup[t][0]!=0 or tup[t][1]!=0):
                tup.pop(t)
                del00a(num,tup)
                pass
        except:
            break
def del0a0(num,tup):
    for t in range(len(tup)):
        try:
            if tup[t][1]==num and (tup[t][0]!=0 or tup[t][2]!=0):
                tup.pop(t)
                del0a0(num,tup)
                pass
        except:
            break
def dela00(num,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0]==num and (tup[t][1]!=0 or tup[t][2]!=0):
                tup.pop(t)
                dela00(num,tup)
                pass
        except:
            break

def del0aa(num1,num2,tup):
    for t in range(len(tup)):
        try:
            if tup[t][1] == num1 and tup[t][2] == num2 and tup[t][0] != 0:
                tup.pop(t)
                del0aa(num1,num2,tup)
                pass
        except:
            break
    pass
def dela0a(num1,num2,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0] == num1 and tup[t][2] == num2 and tup[t][1] != 0:
                tup.pop(t)
                dela0a(num1,num2,tup)
                pass
        except:
            break
    pass
def delaa0(num1,num2,tup):
    for t in range(len(tup)):
        try:
            if tup[t][0] == num1 and tup[t][1] == num2 and tup[t][2] != 0:
                tup.pop(t)
                delaa0(num1,num2,tup)
                pass
        except:
            break
    pass

#检查单个的组合的重复性
def check(tup):
    t=0
    while(t<9):
        for i in range(len(tup)):
            try:
                if tup[i][0]==0 and tup[i][1]==0 and tup[i][2]==0:
                    del000(i,tup) #把这个tup删剩一个就完了然后可以直接退出了
                    break
                if tup[i][0]==0 and tup[i][1]==0:
                    del00a(tup[i][2],tup)
                    continue
                if tup[i][0] == 0 and                tup[i][2] == 0:
                    del0a0(tup[i][1],tup)
                    continue
                if tup[i][0] == 0 :
                    del0aa(tup[i][1],tup[i][2], tup)
                    continue
                if                 tup[i][1] == 0 and tup[i][2] == 0:
                    dela00(tup[i][0], tup)
                    continue
                if                 tup[i][1] == 0:
                    dela0a(tup[i][0],tup[i][2], tup)
                    continue
                if                                     tup[i][2] == 0:
                    delaa0(tup[i][0],tup[i][1], tup)
                    continue
            except:
                break
        t=t+1

if __
import itertools #排列组合
final=[0 for i in range(19)]#用来存最后的数据
zuhe=[] #存所有组合48种

#初始化组合
for i in range(3):
    for j in range(4):
        for k in range(4):
            zuhe.append([i,j,k])

#枚举法取东西
for i in range(18):
    all_=list(itertools.combinations(zuhe,i+1))  #all=[ (第一种组合 [],[],[],[]   )    ,()    ]
    all=[]
    for i in range(len(all_)):
        all.append(list(all_[i]))    #转list格式

    for j in range(len(all)):
        # dell=0#每次要初始话dell
        tmp=len(all[j])
        check(all[j]) #传进去的是一个list  直接对ALL[j]进行修改删除 删除冗余项
        #print(all[j])
        if len(all[j])==tmp:
            final[len(all[j])]=final[len(all[j])]+1
        #搞定

print(final)