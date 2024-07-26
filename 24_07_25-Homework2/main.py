# Homework 2 - Telenor Package Management

""" Package Rates"""
VALIDITY_COST = [10, 50, 150]
ONNET_COST_PER_MINUTE = 0.5
OFFNET_COST_PER_MINUTE = 1.0
DATA_COST_PER_MB = 1.0
SOCIAL_COST_PER_MB = 0.5
SMS_COST_PER_UNIT = 0.1

print('*' * 37)
print('| Welcome To My Telenor Offer Menu. |')
print('*' * 37, end='\n')

package_duration_list = [1, 7, 30]
minutes_mbs_package_list = [0, 50, 100, 200, 500]
sms_package_list = [0, 100, 200, 300, 500]


def package_duration():
    print('\nPlease select Offer Validity')
    for idx, days in enumerate(package_duration_list):
        print(f"{idx + 1}) {days} Day{'s' if days > 1 else ''}")
    try:
        selection = int(input('\nSelect: '))
        if selection == 0 or selection not in range(1, len(package_duration_list) + 1):
            print("\nInvalid selection. Exiting program.")
            exit()
        return selection - 1
    except ValueError:
        print("\nInvalid input. Exiting program.")
        exit()


def package_offer(package_list, type1, type2):
    print(f'\nPlease select{type1} {type2}')
    for idx, package in enumerate(package_list):
        print(f"{idx + 1}) {package} {type2}")
    print('0) Back')

    try:
        selection = int(input('\nSelect: '))
        if selection == 0:
            return 'back'
        elif selection in range(1, len(package_list) + 1):
            return selection - 1
        else:
            print("\nInvalid selection. Exiting program.")
            exit()
    except ValueError:
        print("\nInvalid input. Exiting program.")
        exit()


def calculate_package_cost(validity, onnet_minutes, offnet_minutes, data_mbs, social_mbs, sms):
    cost = VALIDITY_COST[validity]
    cost += ONNET_COST_PER_MINUTE * onnet_minutes
    cost += OFFNET_COST_PER_MINUTE * offnet_minutes
    cost += DATA_COST_PER_MB * data_mbs
    cost += SOCIAL_COST_PER_MB * social_mbs
    cost += SMS_COST_PER_UNIT * sms
    return cost


def package_selected(user_package_duration,
                     user_onnet_minutes,
                     user_offnet_minutes,
                     user_data_mbs,
                     user_social_mbs,
                     user_sms):
    selected_items = []

    def add_item(value, label):
        if value != 0:
            selected_items.append(f"{len(selected_items) + 1}) {value} {label}")

    add_item(sms_package_list[user_sms], "SMS")
    add_item(minutes_mbs_package_list[user_social_mbs], "Social MBs")
    add_item(minutes_mbs_package_list[user_data_mbs], "Data MBs")
    add_item(minutes_mbs_package_list[user_offnet_minutes], "Offnet Minutes")
    add_item(minutes_mbs_package_list[user_onnet_minutes], "Onnet Minutes")

    selected_items.append(f"Validity: {package_duration_list[user_package_duration]} days")

    total_cost = calculate_package_cost(user_package_duration,
                                        minutes_mbs_package_list[user_onnet_minutes],
                                        minutes_mbs_package_list[user_offnet_minutes],
                                        minutes_mbs_package_list[user_data_mbs],
                                        minutes_mbs_package_list[user_social_mbs],
                                        sms_package_list[user_sms])

    print(f'\nSirf Rs {total_cost:.2f} bama tax main hasil karen:')
    for item in selected_items:
        print(item)

    print("\n1) Activate\n2) Home\n3) Cancel")

    try:
        _final_choice = int(input('\nSelect: '))
        if _final_choice == 1:
            print("\nThank you for activating the current package.\nGood Bye!")
            exit()
        elif _final_choice == 2:
            return True
        elif _final_choice == 3:
            exit()
        else:
            print("\nInvalid selection. Exiting program.")
            exit()
    except ValueError:
        print("\nInvalid input. Exiting program.")
        exit()


def get_user_selected_package(package_list, label1, label2):
    while True:
        user_choice = package_offer(package_list, label1, label2)
        if user_choice == 'back' or user_choice in range(len(package_list)):
            return user_choice


def package_selection():
    steps = [
        (" Onnet", "Minutes", minutes_mbs_package_list),
        (" Offnet", "Minutes", minutes_mbs_package_list),
        (" Data", "MBs", minutes_mbs_package_list),
        (" Social", "MBs", minutes_mbs_package_list),
        ("", "SMS", sms_package_list)
    ]

    while True:
        _userPackageDuration = package_duration()
        if _userPackageDuration not in range(len(package_duration_list)):
            return

        user_choices = [-1] * len(steps)
        current_step = 0

        while current_step < len(steps):
            label1, label2, package_list = steps[current_step]
            user_choice = get_user_selected_package(package_list, label1, label2)
            if user_choice == 'back':
                if current_step > 0:
                    current_step -= 1
                else:
                    return
            else:
                user_choices[current_step] = user_choice
                current_step += 1

        if not package_selected(_userPackageDuration, *user_choices):
            continue


try:
    while True:
        package_selection()
except (KeyboardInterrupt, ValueError) as e:
    print("\nProgram terminated.")
    exit()
