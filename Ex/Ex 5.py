import datetime


def getdate():
    return datetime.datetime.now()


def log(fx, name):
    date = getdate()
    fx = fx
    name = name

    if fx == 1:
        data = input("Type Here\n")
        if name == 1:
            with open("H_E", "a") as f:
                f.write(str([str(date)]) + ": " + data + "\n")
            print("Succesful Write")
        elif name == 2:
            with open("R_E", "a") as f:
                f.write(str([str(date)]) + ": " + data + "\n")
            print("Succesful Write")
        elif name == 3:
            with open("HA_E", "a") as f:
                f.write(str([str(date)]) + ": " + data + "\n")
            print("Succesful Write")
        else:
            print("Invild Input For Name")
    elif fx == 2:
        data = input("Type Here\n")
        if name == 1:
            with open("H_F", "a") as f:
                f.write(str([str(date)]) + ": " + data + "\n")
            print("Succesful Write")
        elif name == 2:
            with open("R_F", "a") as f:
                f.write(str([str(date)]) + ": " + data + "\n")
            print("Succesful Write")
        elif name == 3:
            with open("HA_F", "a") as f:
                f.write(str([str(date)]) + ": " + data + "\n")
            print("Succesful Write")
        else:
            print("Invild Input For Name")
    else:
        print("Invaild For Food And Exercise")


def retrive(fx, name):
    fx = fx
    name = name
    if fx == 1:
        if name == 1:
            with open("H_E") as f:
                print(f.read())
        elif name == 2:
            with open("R_E") as f:
                print(f.read())
        elif name == 3:
            with open("HA_E") as f:
                print(f.read())
        else:
            print("Invild Input For Name")
    elif fx == 2:
        if name == 1:
            with open("H_F") as f:
                print(f.read())
        elif name == 2:
            with open("R_F") as f:
                print(f.read())
        elif name == 3:
            with open("HA_F") as f:
                print(f.read())
        else:
            print("Invild Input For Name")
    else:
        print("Invaild Input For Food And Exercise")


def longretrive():
    lr = int(input(''' 
        What You Want?
            1.Log
            2.Retrieve\n'''))

    name = int(input('''
        Which Person For? 
            1.Harry
            2.Rohan
            3.Hammad\n'''))

    fx = int(input(''' 
        For What
            1.Exercise
            2.Food\n'''))
    if lr == 1:
        log(fx, name)
        again()
    elif lr == 2:
        retrive(fx, name)
        again()
    else:
        print("Invaild Input for Log And Retrieve")
        again()


def again():
    ag = input('''
    Do You Done Opration Again?
    Type y for Yes Or n For No.
    ''')
    if ag == "y":
        longretrive()
    elif ag == "n":
        print("See You Later")
    else:
        again()


longretrive()
