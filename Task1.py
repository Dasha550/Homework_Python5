#Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
#Используйте знания с последней лекции. Выполните ее в виде функции. 
#Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

from pickletools import string1

string1 = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
def find_Tekst(string):
    string=string.replace("абв","")
    string=string.replace("Абв","")
    string=string.replace("аБв","")
    string=string.replace("абВ","")
    string=string.replace("АБв","")
    string=string.replace("аБВ","")
    string=string.replace("АбВ","")
    string=string.replace("АБВ","")
    return string
print(find_Tekst(string1))