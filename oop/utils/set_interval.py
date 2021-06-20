import threading


def set_interval(func, args, sec):
    def func_wrapper():
        set_interval(func, args, sec)
        func(*args)

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def michael(on_roof_top, bluffing):
    if on_roof_top and bluffing:
        print("Dwight you ignorant sl**")
    elif not bluffing:
        print("Not michael")


# set_interval(michael, [True, False], 1)
