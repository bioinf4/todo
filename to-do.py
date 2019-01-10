def viewtodo():
    lst = open("to-do.txt", "r")
    to_do_lst = lst.readlines()
    print("This is the to-do list for today:\n")
    count1 = -1
    lststr = ""
    count2 = 1
    for i in to_do_lst:
        lststr += str(count2) + ". " + i + "\n"
        count2 += 1
    print(lststr)
    
def addtodo(act):
    lst = open("to-do.txt", "r")
    to_do_lst = lst.readlines()
    new_lst = []
    for i in to_do_lst:
        new_lst.append(i)
    lst_of_nums = []
    count = -1
    for i in new_lst:
        count += 1
        lst_of_nums.append(count)
    if int(act[0]) in lst_of_nums and act[-1] == "d":
        new_lst.pop(int(act[0]))
    elif int(act[0]) in lst_of_nums and act[-1] == "u":
        new_val = input("Input new task: ")
        new_lst[int(act[0]) - 1] = act[0] + ". " + new_val

def master():
    viewtodo()
    print("Choose Action")
    print("-------------")
    print("Number [SPACE] d: Delete element")
    print("Number [SPACE] u: Update element")
    print("c: Close")
    action = input()
    if action = "c":
        return
    else:
        addtodo(action)
        viewtodo()


    
        

