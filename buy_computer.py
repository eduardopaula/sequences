current_choise = "-"
computer_parts = [] # create an empty list

while current_choise != '0':
    if current_choise in "123456":
        print("Adding {}".format(current_choise))
        if current_choise == '1':
            computer_parts.append("computer")
        elif current_choise == '2':
            computer_parts.append("monitor")
        elif current_choise == '3':
            computer_parts.append("keyboard")
        elif current_choise == '4':
            computer_parts.append("mouse")
        elif current_choise == '5':
            computer_parts.append("mouse mat")
        elif current_choise == '6':
            computer_parts.append("hdmi")
    else:
        print("Please add options from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("6: hdmi")
        print("0: to finish")

    current_choise = input()

print(computer_parts)
