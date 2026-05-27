import webbrowser
import texts as t
import time


def game():
    pass

def Rules():
    print(t.rules)
    try:
        result = int(input())
    except:
        print(t.error["001"])
        Rules()
    
    if result == 1:
        webbrowser.open(url="https://hitstergame.com/en-gb/how-to-play-v3/")
    elif result == 2:
        print(t.newRules)
        time.sleep(3)
        Text()
        

def Text():
    print("\n\n\n", t.frontPage1, t.frontPage2)
    try:
        result = int(input())
    except:
        print("result:" + result)
        print(t.error["001"])
        Text()
    if result == 1:
        Rules()
    elif result == 2:
        webbrowser.open(url="https://github.com/DasherWho/Custom-Hitster-Player")
        time.sleep(3)
    elif result == 3:
        pass
    elif result == 4:
        print(t.error["002"])
        time.sleep(1)
        print("\n\n\n")
        Text()

Text()