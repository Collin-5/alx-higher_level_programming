#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for i in range(0, len(list)):
        if list[i][0:2] != "__":
            print(list[i])
