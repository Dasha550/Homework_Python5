#3. Вот вам текст:
#«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. 
#Ну,эээ, в общем, было лето, кажется. Как бы тепло. 
#Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. 
#Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. 
#В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
#Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. 
#Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. 
#В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. 
#Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
#Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
#Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

string1 = "Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил"
def find_Tekst(string):
    string=string.replace("Ну,","")
    string=string.replace("Ну","")
    string=string.replace(", ну,","")
    string=string.replace(", ну.","")
    string=string.replace(", ну","")
    string=string.replace("ну","")

    string=string.replace("Короче говоря,","")
    string=string.replace("Короче говоря","")
    string=string.replace(", короче говоря,","")
    string=string.replace(", короче говоря.","")    
    string=string.replace(", короче говоря","")
    string=string.replace("короче говоря","")    

    string=string.replace("Короче,","")
    string=string.replace("Короче","")
    string=string.replace(", короче,","")
    string=string.replace(", короче","")
    string=string.replace(", короче.","")
    string=string.replace("короче","")          

    string=string.replace("В общем,","")
    string=string.replace("В общем","")
    string=string.replace(", в общем,","")
    string=string.replace(", в общем.","")
    string=string.replace(", в общем","")
    string=string.replace("в общем","")

    string=string.replace("Кажется,","")
    string=string.replace("Кажется","")
    string=string.replace(", кажется,","")
    string=string.replace(", кажется.","")
    string=string.replace(", кажется","")
    string=string.replace("кажется","")

    string=string.replace("Кстати,","")
    string=string.replace("Кстати","")
    string=string.replace(", кстати,","")
    string=string.replace(", кстати.","")
    string=string.replace(", кстати","")
    string=string.replace("кстати","")    

    string=string.replace("Ясен пень,","")
    string=string.replace("Ясен пень","")
    string=string.replace(", ясен пень,","")
    string=string.replace(", ясен пень.","")
    string=string.replace(", ясен пень","")
    string=string.replace("ясен пень","")

    string=string.replace("Эээээ,","")
    string=string.replace("Эээээ","")
    string=string.replace(", эээээ,","")
    string=string.replace(", эээээ","")    
    string=string.replace("эээээ","") 

    string=string.replace("Ээээ,","")
    string=string.replace("Ээээ","")
    string=string.replace(", ээээ,","")
    string=string.replace(", ээээ","")    
    string=string.replace("ээээ","") 

    string=string.replace("Эээ,","")
    string=string.replace("Эээ","")    
    string=string.replace(", эээ,","")
    string=string.replace(", эээ","")
    string=string.replace("эээ","")

    string=string.replace("Как бы,","")
    string=string.replace("Как бы","")    
    string=string.replace(", как бы,","")
    string=string.replace(", как бы.","")
    string=string.replace(", как бы","")
    string=string.replace("как бы","")

    string=string.replace("…","")
    string=string.replace("… .","")    
    string=string.replace("...","")   

    return string
print(find_Tekst(string1))