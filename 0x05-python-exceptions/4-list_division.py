#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    newlist = []

    for i in range(list_length):
        try:
            newlist.append(my_list1[i] / my_list2[i])

        except ZeroDivisionError:
            newlist.append(0)
            print("division by 0")

        except IndexError:
            newlist.append(0)
            print("out of range")
            continue

        except TypeError:
            if newlist.append(0) != int or newlist.append(0) != float:
                print("wrong type")

        finally:
            pass
    return newlist
