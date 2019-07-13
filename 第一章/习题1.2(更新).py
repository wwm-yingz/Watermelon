#西瓜书，1.2题 重写了排列的代码，这样子不用到itertool库，不会爆内存，因为用完就会删除不保存list，但是循环数量级当k=8时已经是亿级，当k=15时会达到万亿次循环，算不出来的
#wwm
#wwm-yingz.github.io
#python
#修改第157行的c值可以算不同的k值的结果
import itertools #排列组合
final=[0 for i in range(19)]#用来存最后的数据
zuhe=[] #存所有组合48种

#下面的check瞎几把写的 看ipad
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

def check(tup):#检查单个的组合的重复性
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




#初始话组合
for i in range(3):
    for j in range(4):
        for k in range(4):
            zuhe.append([i,j,k])

# if __name__=="__main__":
#     # 枚举法取东西
#     i=0  #代表选几个数0-17
#     for i in range(18):
#         all_=list(itertools.combinations(zuhe,i+1))  #all=[ (第一种组合 [],[],[],[]   )    ,()    ]
#         all=[]
#         for i in range(len(all_)):
#             all.append(list(all_[i]))    #转list格式
#
#         for j in range(len(all)):
#             # dell=0#每次要初始话dell
#             tmp=len(all[j])
#             check(all[j]) #传进去的是一个list  直接对ALL[j]进行修改删除 删除冗余项
#             #print(all[j])
#             if len(all[j])==tmp:
#                 final[len(all[j])]=final[len(all[j])]+1
#             #搞定
#
#         print(final)
#[0, 48, 931, 10341, 72647, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def add(tmp,now):#now传进来的时候是-1 代表tmp的0123 的3 最后一位   这个位置最大也只能取3 tmp只能曲0123
    if tmp[now]+1==len(all)+now+1  :#3 4 5     4就是len(all）   即已经取到最大那个数最大那个数 当前是3 下一个是4要进位了 范围012
        if now-1>=-len(tmp):
            add(tmp,now-1)
        max=tmp[0]
        for m in tmp[:now]:
            if max<m:
                max=m
        tmp[now] = max+1#tmp now  取之前的最大那个  如果还是爆了  retun  不然继续
        if tmp[now] >=len(all)+now+1:
            return False
        return True#可以增加
    else:
        tmp[now]=tmp[now]+1
        return True  #可以增加

all=zuhe#[[1,2],[2],[3,5],[4,6],[5]]  #需要排列的数组
c=2#需要取的个数取3个
t = 0  # 计数
tmp1=list(range(c))  #012
while True:
    now=[]#当前的

    for i in range(len(tmp1)):#长度3
        now.append(all[tmp1[i]])
    #print(now)#搞定now的赋值
    tmp = len(now)
    check(now)  # 传进去的是一个list  直接对ALL[j]进行修改删除 删除冗余项
    # print(all[j])
    if len(now) == tmp:
        final[len(now)] = final[len(now)] + 1
    t=t+1#计数加一

    #tmp要进一
    if not add(tmp1,-1):#结束了就出去
        break
print(t)
print(final)