# SIMPLEX PROBLEM
import sys
from tabulate import tabulate


F=[8,40,25] #synartisi
p=[[10,14,10,8],[4,26,12,8],[8,12,8,8]] #periorismoi


cj,zj,vasi,cb,zj_cj,th=[],[],[],[],[],[]


max=0 #max value

#thesis stoixeiwn
pos_zj_cj,pos_th=-1,-1

end=False #na jerw an teleiwse

header=[] #gia na einai pio omorfa stin emfanisi

def print_problem():
    global header
    print('\n\nPinakas\n-----------------------------------------------------')
   
    print(tabulate(p, headers=header,floatfmt=".4f"))
    print('\n')
    display_cj=[]
    for i in cj:
        display_cj.append(i)
    for i in range(len(zj)-len(cj)):
        display_cj.append(0.0)
        
    for i in zj:
        print(format(i,'.4f'),end='\t')
    print('-> Zj')
    
    for i in display_cj:
        print(format(i,'.4f'),end='\t')
    print('-> Cj')
    for i in zj_cj:
        print(format(i,'.4f'),end='\t')
    print('-> Zj-Cj')
    
    for i in th:
        print(format(i,'.4f'),end='\t')
    print('-> Thita')
    
    print('\n\n Cb (Vasi)\n'+tabulate([cb], headers=vasi,floatfmt=".4f")+'\n')
    print('-----------------------------------------------------\n')

def fix_the_lists():
    global header
    count=0 #na jerw posa exoyn mpei idi -> metavlites einai, posa X yparxoyn apo to F + posoi periorismoi yparxoyn + P
    for i in range(len(F)):
        header.append('x'+str(i+1))
        count+=1
    for i in range(len(p)):
        header.append('x'+str(i+count+1))  
        
    header.append('P')
        
    """ GIA TIN EMFANISI TOY PINAKA""" 

    for el in F:
        cj.append(el)
    for i in range(len(p)): #vaze tis voithitikes metavlites
        for j in range(len(p)):
            if(i==j):
                p[j].insert((len(p)+i),1)
            else:
                p[j].insert((len(p)+i),0)
        #ftiaxnw tin vasi
        vasi.append('x'+str((len(p)+i+1))) 
        
        cb.append(0)
        th.append(0)

        # ayto to thelw 2 fores gia na vgei 6 
        zj.append(0)
        zj.append(0)
        
    arxikopoisi_zj_cj()
    isdone()

def isdone():
    flag=False
    
    thetika=True
    for element in zj_cj:
        if(element<0):
            thetika=False
            
    if(thetika==True):
        i=-1
        thesi_sto_cb={}
        for el in vasi:
            i+=1
            if(int(el.split('x')[1])<=len(F)): #to x_i na einai mikrotero apo ton arithmo twn metavlitwn: oi periorismoi mas dinoyn kai posa voithitika x tha yparxoyn
                thesi_sto_cb[el]=i #vriskw x yparxoyn kai tin thesi toys
               
        for i in range(len(F)):
            if('x'+str(i) not in thesi_sto_cb and i>0):
                thesi_sto_cb['x'+str(i)]=-1
                
                
        for x,pos in dict(sorted(thesi_sto_cb.items())).items():
            if(pos==-1): #an dn yparxei sto vasi
                print(x+'=0')
            else:
               print(x+'='+str(p[pos][len(p[pos])-1])) #an yparxei emfanise to P tis grammis toy
    
        print('max='+str(max)) #emfanise to max
        sys.exit()

    if(end and not thetika):
        for i in cb:
            if(i!=0):
                flag=True
        if(flag):
            print('There is no solution')
        else:
            for i in cb:
                print('x'+str(i)+'='+cb[i]+'\n')
            print('max is '+max)
        sys.exit()

def arxikopoisi_zj_cj():

    global zj_cj #zj-cj
    for element in cj:
        zj_cj.append(element*-1)
    for element in range(len(p)):
        zj_cj.append(0)
        
"""
PAME NA FTIAXOYME 
TON PINAKA SIMPLEX
"""
#vres to mikrotero sto zj_cj

def find_min_zj_cj():
    global pos_zj_cj #i thesi toy
    global end
    min=1
    i=0
    for element in zj_cj:
        if(min>element and element<0):
            min=element
            pos_zj_cj=i #vriskw tin stili
        i+=1
    print('---------------------\nMIN_Zj-Cj='+str(min))
    print('Pos_zj_cj='+str(pos_zj_cj)+'\n---------------------')

    if(min==1):
        end=True
           
# yplogise to th
def calculate_th():
    global th
    i=0
    global pos_zj_cj
    for element in p:
        if(p[i][pos_zj_cj]!=0):
            th[i]=(p[i][len(p[i])-1] / p[i][pos_zj_cj])
        i+=1

#vres to mikrotero th
def find_min_Th():
    global th
    # prepei na einai thetiko
    min=10^120
    global end
    global pos_th
    i=-1
    for element in th:
        i+=1
        if(min>element and element>=0):
            min=element
            pos_th=i
    print('---------------------\nMIN_Thita='+str(min))
    print('Pos_th='+str(pos_th)+'\n---------------------')
    # EDW PERA VRISKEI TO MIKROTERO Θ, ara to pivot einai to p[pos_th][pos_zj_cj]
    if(min==10^120):
        end=True
        
#prajis    
def line_operations():
    divide_the_line()
    make_everyting_0()
    
#kane asso to pivot
def divide_the_line():
    pivot=p[pos_th][pos_zj_cj] #to stoixeio poy vrikame PIVOT
    i=0
    for element in p[pos_th]:
        try:
            p[pos_th][i]=element/pivot
            i+=1
        except:
            continue
    
#midenise ta alla stoixeia    
def make_everyting_0():
    global max
    for grammi in range(len(p)):
        if(grammi!=pos_th):
            i=0
            afairetis=p[grammi][pos_zj_cj] #me ayto tha ginoyn oi afairesis
            for element in p[grammi]:
                p[grammi][i]=element-afairetis*p[pos_th][i]
                i+=1
    
    max=max-zj_cj[pos_zj_cj]*p[pos_th][len(p[pos_th])-1]


def fix_the_base():
     # ayto poy egine assos tha mpei ws vasi
    vasi[pos_th]='x'+(str(pos_zj_cj+1))

    cb[pos_th]=cj[pos_zj_cj] #vazw tin timi stin vasi
        
# sinexise tis prajis
def find_zj_cj():

    fix_the_base()    
    calculate_zj()
    global zj_cj
    for pos in range(len(zj_cj)):
        if(pos<len(cj)):
            zj_cj[pos]=zj[pos]-cj[pos] #ypologismos toy zj-cj
        else:
            zj_cj[pos]=zj[pos]
    
def calculate_zj():
    global zj
    for i in range(len(p[0])-1):
        zj[i]=0
        for j in range(len(cb)):
            zj[i]+=cb[j]*p[j][i]


fix_the_lists()
print_problem()
iteration=1 #poses fores egine epanalipsi
while(True):
    print('Iteration:'+str(iteration))
    find_min_zj_cj()
    calculate_th()
    find_min_Th()
    print('Pivot='+str(p[pos_th][pos_zj_cj]))
    line_operations()
    find_zj_cj()
    print_problem()
    isdone()
    iteration+=1 #thelei 2 epanalipsis toy kwdika gia na vrethei i lysi

"""
TELOS SIMPLEX
"""

