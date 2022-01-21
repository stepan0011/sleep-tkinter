from time import sleep as s
def slepp(root,second):
    for i in range(second):
        for j in range(10):
            root.update()
            s(0.1)
