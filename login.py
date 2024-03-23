def log():
    while True:
        user_name=input("enter username:")
        password=input("enter password:")
        if user_name==password:
            print("successful login")
            break
        else:
            print("invalid login")   

log()            