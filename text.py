import webbrowser
import texts as t


def Rules():


def Text():
    print(t.frontPage1, t.frontPage2)
    try:
        result = int(input())
    except:
        print(t.error001)
        Text()
    if result == 1:
