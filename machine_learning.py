'''
FIAP ( Faculdade de Informática e Admnistração Paulista )
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio Henrique Cabrini
Atividade: CheckPoint 3 ; Machine Learning;
Gabriel Pionte Paulino - RM84539
'''
from sklearn.tree import DecisionTreeClassifier
vgrupo = [[71,99,109], [87,100,111], [79,95,120], [69,133,117], [81,122,109], [75,91,100], [93,139,119], [91,127,123], [95,124,122], [89,120,119],
          [100,140,120], [107,143,131], [101,149,123], [111,157,133], [116,168,138], [119,159,117], [123,171,112], [111, 177, 130], [115,183,127], [126,199,119],
          [126,200,137], [130,203,140], [127,207,132], [125,211,110], [131,220,121], [151,218,212], [142,231,200],[157,252,202], [169,245,217], [171,277,205]]
lgrupo = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
classif = DecisionTreeClassifier()
classif.fit(vgrupo, lgrupo)
mgdlJJ = float(input("Digite o valor da glicose em Jejum: "))
mgdlGD = float(input("Digite o valor da glicose em Pós-Sobrecarga: "))
mgdlGC = float(input("Digite o valor casual da glicose no sangue: "))
print("Valor em Jejum: {0} mg/dL\n Valor em Pós-Sobrecarga: {1} mg/dL\n Valor casual: {2} mg/dL".format(mgdlJJ, mgdlGD, mgdlGC))
x = classif.predict([[mgdlJJ, mgdlGD, mgdlGC]])
if x == 0:
    print("Sua diabate está normal")
elif x == 1:
    print("Tolerância a glicose diminuida!!")
else:
    print("Diabate Mellitus, consulte um médico!!")