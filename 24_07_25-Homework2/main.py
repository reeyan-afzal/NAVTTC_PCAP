print('*' * 37)
print('| Welcome To My Telenor Offer Menu. |')
print('*' * 37, end='\n')

threeOptions = [1, 2, 3]
fiveOptions = [1, 2, 3, 4, 5]

package_duration_list = [1, 7, 30]

minutes_mbs_duration_list = [0, 50, 100, 200, 500]

sms_duration_list = [0, 100, 200, 300, 500]

VALIDITY_COST = [10, 50, 150]
ONNET_COST_PER_MINUTE = 0.5
OFFNET_COST_PER_MINUTE = 1.0
DATA_COST_PER_MB = 1.0
SOCIAL_COST_PER_MB = 0.5
SMS_COST_PER_UNIT = 0.1


def package_duration():
    print('\nPlease select Offer Validity.'
          '\n1)', package_duration_list[0], 'Day',
          '\n2)', package_duration_list[1], 'Days',
          '\n3)', package_duration_list[2], 'Days')

    return int(input('\nSelect: '))


def minutes_mbs_offer(type1, type2):
    print('\nPlease select ' + type1 + ' ' + type2,
          '\n1)', minutes_mbs_duration_list[0], type2,
          '\n2)', minutes_mbs_duration_list[1], type2,
          '\n3)', minutes_mbs_duration_list[2], type2,
          '\n4)', minutes_mbs_duration_list[3], type2,
          '\n5)', minutes_mbs_duration_list[4], type2,
          '\n0) Back')

    selection = int(input('\nSelect: '))
    if selection == 0:
        return 'back'
    return selection


def sms_offer():
    print('\nPlease select SMS.'
          '\n1)', sms_duration_list[0], 'SMS',
          '\n2)', sms_duration_list[1], 'SMS',
          '\n3)', sms_duration_list[2], 'SMS',
          '\n4)', sms_duration_list[3], 'SMS',
          '\n5)', sms_duration_list[4], 'SMS',
          '\n0) Back')

    selection = int(input('\nSelect: '))
    if selection == 0:
        return 'back'
    return selection


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
    counter = 1

    if user_sms != 0:
        selected_items.append(f"{counter}) {sms_duration_list[user_sms]}")
        counter += 1

    if user_social_mbs != 0:
        selected_items.append(f"{counter}) {minutes_mbs_duration_list[user_social_mbs]} Social MBs")
        counter += 1

    if user_data_mbs != 0:
        selected_items.append(f"{counter}) {minutes_mbs_duration_list[user_data_mbs]} Data MBs")
        counter += 1

    if user_offnet_minutes != 0:
        selected_items.append(f"{counter}) {minutes_mbs_duration_list[user_offnet_minutes]} Offnet Minutes")
        counter += 1

    if user_onnet_minutes != 0:
        selected_items.append(f"{counter}) {minutes_mbs_duration_list[user_onnet_minutes]} Onnet Minutes")
        counter += 1

    selected_items.append(f"Validity: {package_duration_list[user_package_duration]}")

    total_cost = calculate_package_cost(user_package_duration,
                                        minutes_mbs_duration_list[user_onnet_minutes],
                                        minutes_mbs_duration_list[user_offnet_minutes],
                                        minutes_mbs_duration_list[user_data_mbs],
                                        minutes_mbs_duration_list[user_social_mbs],
                                        sms_duration_list[user_sms])

    print(f'\nSirf Rs {total_cost:.2f} bama tax main hasil karen:')
    for item in selected_items:
        print(item)

    print("\n1) Activate\n2) Cancel")

    _final_choice = int(input('\nSelect: '))
    print("\nThank you for activating the current package.\nGood Bye!") if _final_choice == 1 else exit()


try:
    while True:
        _userPackageDuration = package_duration()

        if _userPackageDuration in threeOptions:
            while True:
                _userOnnetMinutes = minutes_mbs_offer("Onnet", "Minutes")
                if _userOnnetMinutes == 'back':
                    break

                if _userOnnetMinutes in fiveOptions:
                    while True:
                        _userOffnetMinutes = minutes_mbs_offer("Offnet", "Minutes")
                        if _userOffnetMinutes == 'back':
                            break

                        if _userOffnetMinutes in fiveOptions:
                            while True:
                                _userDataMBs = minutes_mbs_offer("Data", "MBs")
                                if _userDataMBs == 'back':
                                    break

                                if _userDataMBs in fiveOptions:
                                    while True:
                                        _userSocialMBs = minutes_mbs_offer("Social", "MBs")
                                        if _userSocialMBs == 'back':
                                            break

                                        if _userSocialMBs in fiveOptions:
                                            while True:
                                                _userSMS = sms_offer()
                                                if _userSMS == 'back':
                                                    break

                                                if _userSMS in fiveOptions:
                                                    package_selected(_userPackageDuration - 1,
                                                                     _userOnnetMinutes - 1,
                                                                     _userOffnetMinutes - 1,
                                                                     _userDataMBs - 1,
                                                                     _userSocialMBs - 1,
                                                                     _userSMS - 1)
                                                    exit()
                                                elif _userSMS == '0':
                                                    break
                                        elif _userSocialMBs == '0':
                                            break
                                elif _userDataMBs == '0':
                                    break
                        elif _userOffnetMinutes == '0':
                            break
                elif _userOnnetMinutes == '0':
                    break
        else:
            exit()
except (KeyboardInterrupt, ValueError) as e:
    exit()
