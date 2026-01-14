try:
    print("dfdf")
    print("dfsdfdsf")
    try:
        a = 5 / 0
    except Exception as e:
        print(e)
except Exception as error:
    print(str(error))
finally:
    print("Finally")