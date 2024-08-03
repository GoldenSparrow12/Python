import time


def searcher():
    book = "This is Harshit book or it is a great book everyone can read it."
    time.sleep(3)

    while True:
        text = (yield)
        if text == book:
            print("Yes")
        else:
            print("No")


search = searcher()
print("Start book searcher")
next(search)
input("press Enter key")
search.send("Harshit")
search.close()
