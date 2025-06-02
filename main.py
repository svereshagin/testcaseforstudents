import time

user_logged = False
while not user_logged:
    reply = input("Вы хотите зарегестрироваться ?")
    if reply.lower() in ['да', 'yes', 'конечно']:
        print("Отлично! Продолжаю регистрацию")
        #сделайте здесь логику для регистрации в БД 
        #(считывание и добавление логики регистрации)
        time.sleep(3)
        print("Успех!")

while True:
    
    user_input = list(map(str, input().split()))
    print(user_input)
    if 'hello' in user_input or 'hey' in user_input:
        ...
        #some logic algo to handle msg conversation
