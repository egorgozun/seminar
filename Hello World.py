print("Hello!", "Bye bye!")
print("Привет!", end="");print("Как дела?")                                     #end попросту не переносит после print на новую строку
print("Тест1", end="\n"); print("Test2")                                        #sep="\n" -- \n = new line

max(1,3,4,5,6)                                                                  # , -- перечислять переменные при print, перечислять переменные внутри фукции [max/min/etc.]

print("Hello World!!", 45, -10)
print("Hello World!!", 45, -10, sep="-=-")                                      #separator помогает выводить результат 

Test_10=max(1,2,3,4,5,6,7,7,8,9,1,12,-3,-5,-8) 
print("Количество людей в группе = ", Test_10)

x=20 ; y="Длина шеи" ; z="см."
print("{} у Егора = {} {}" .format(y,x,z))

a=10; b=1000; a1="чай"; b1="кальян" 
print("{:<20} {:>11}".format(a1,a)); print("{:<20} {:>11}".format(b1,b))    # :> - выравнивание по правой стороне, :< по левой, :^по центру