availble_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat",
                  "hdmi cable",
                  "dvd"
                  ]
current_choise = "-"
computer_parts = [] # create an empty list

while current_choise != '0':
    if current_choise in "1234567":
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
            computer_parts.append("hdmi cable")
        elif current_choise == '7':
            computer_parts.append("dvd")
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(availble_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choise = input()

print(computer_parts)
