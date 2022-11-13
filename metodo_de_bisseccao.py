#Estudante: Joao Pedro
#Disciplina: Metodos Numericos
import math
def escrevendo_no_arquivo(k,j,o,p,q):
    arquivo=open('trabalho_mn.txt','w')
    arquivo.write(str('Intervalo: ['))
    arquivo.write(str(p))
    arquivo.write(str(' ; '))
    arquivo.write(str(q))
    arquivo.write(str('] \n\n'))
    for i in range(o+1):   #Tabela de iteracoes num arquivo externo
        arquivo.write(str('Iteracao: '))
        arquivo.write(str(i))
        arquivo.write(str('\nx: '))
        arquivo.write(str(k[i]))
        arquivo.write(str('\nf(x): '))
        arquivo.write(str(j[i]))
        arquivo.write(str('\n\n\n\n\n'))
    arquivo.close()
def f(x):
    return ((x**3)-(9*x)+(3.0))   #Funcao
a=(float(input("Indique o valor 'a'  do intervalo [a;b]: ")))   #Valor de 'a' (um dos extremos do intervalo)
b=(float(input("Indique o valor 'b'  do intervalo [a;b]: ")))   #Valor de 'b' (um dos extremos do intervalo)
a1=a 
b1=b
l=1*(10**(-3))   #Amplitude final
tol=1*(10**(-5))   #Tolerancia
cont=0   #Contador
nui=10**(3)   #Numero de iteracoes
c=b-a   #Amplitude de [a;b]
x0=(a+b)/2   #Ponto medio de [a;b]
v1=[]   #Vetor auxiliar 1
v2=[]   #Vetor auxiliar 2
while(c>1 or math.fabs(f(x0))>tol):
    print(cont)
    print('x:',x0)
    print('f(x):',f(x0),'\n\n')
    v1.append(x0)
    v2.append(f(x0))
    if f(a)*f(x0)< 0.0:
        b=x0
    if f(a)*f(x0)> 0.0:
        a=x0
    c=b-a
    x0=(a+b)/2
    cont=cont+1
    if(cont>=nui):
        break
v1.append(x0)
v2.append(f(x0))
print(cont)
print(x0)
print(f(x0))
escrevendo_no_arquivo(v1,v2,cont,a1,b1)   #Aplicacao dos dados num arquivo externo
print('\n\n\nRaiz: %f\niteracoes: %i\nf(%f)=(%f)'%(x0,cont,x0,f(x0)))
