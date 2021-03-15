def test(): 
    squares = []
    for x in range(1,21):
        squares.append(x**2)
    print(squares)

test()

def test1():
    squares = [x**2 for x in range(1,21)]
    print(squares)

test1()

