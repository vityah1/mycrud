from datetime import datetime

# from random import randrange


def myLog(data="", show=0):
    if show == 1:
        print(data)

    fn = __file__.split("/")[-1] + ".log"

    curr_date = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(f"""{curr_date}, {data}\n""")
