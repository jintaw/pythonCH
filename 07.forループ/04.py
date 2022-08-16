from distutils.log import error


i = [25 , 10 , 24 , 1 , 77]
while True:
    number = input("number:")
    
    if number == "q":
        break
    
    try:
        number = int(number)
    except ValueError:
        print("数字を入力するか、qで終了します")    
    
    if number in i:
        print("正解！")
        break
    else:
        print("不正解！")
    
    
