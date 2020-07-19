import sys
import math
deets = sys.argv

argsplit = deets[1].split("=")
option_list = []
value_list = []
value_as_int = []
option_value_dictionary = {}

for arg in deets[1:]:
    option_list.append(arg.split("=")[0])
    value_list.append(arg.split("=")[1])
    option_value_dictionary[arg.split("=")[0]] = arg.split("=")[1]

for item in value_list:
    try:
        value_as_int.append(int(item))
    except:
        pass

if "--type" not in option_value_dictionary.keys():
    print("Incorrect parameters - no type")
elif option_value_dictionary["--type"] == "diff" and "--payment" in option_value_dictionary.keys():
    print("Incorrect parameters - mpt")
elif "--principal" not in option_value_dictionary.keys() and option_value_dictionary["--type"] == "--diff":
    print("Incorrect parameters 3")
elif "--interest" not in option_value_dictionary.keys():
    print("Incorrect parameters 4")
elif len(option_list) < 4:
    print("Incorrect parameters 5")
elif min(value_as_int) < 0:
    print("Incorrect parameters 6")
else:
    if option_value_dictionary["--type"] == "diff":
        if argsplit[1] == "diff":
            if "--payment" in option_list:
                print("Incorrect parameters 7")
            else:
                try:
                    p = int(option_value_dictionary["--principal"])
                    i = (
                        float(option_value_dictionary["--interest"]) / 100) / 12
                    n = int(option_value_dictionary["--periods"])
                except:
                    pass

                counter = 0
                sum = 0
                for month in range(n):
                    counter += 1
                    d = math.ceil(
                        (p / n) + i * (p - ((p * (counter - 1)) / n)))
                    sum += d
                    print(f"Month {counter}: paid out {d}")

                print(f"Overpayment = {sum - p}")

    elif option_value_dictionary["--type"] == "annuity":
        try:
            if "--payment" not in option_value_dictionary.keys():
                credit_principal = int(option_value_dictionary["--principal"])

                count_of_periods = int(option_value_dictionary["--periods"])

                credit_interest_tmp = float(
                    option_value_dictionary["--interest"])
                credit_interest = (credit_interest_tmp / 100) / 12

                top = (credit_interest * (1 + credit_interest)**count_of_periods)
                bottom = (1 + credit_interest)**count_of_periods - 1
                combined = top / bottom
                annuity_payment = credit_principal * combined
                overpayment = (math.ceil(annuity_payment) *
                               count_of_periods) - credit_principal

                print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
                print(f"Overpayment = {overpayment}")

            if "--periods" not in option_value_dictionary.keys():
                credit_principal = int(option_value_dictionary["--principal"])

                annuity_payment = int(option_value_dictionary["--payment"])
                print(option_value_dictionary["--interest"])
                credit_interest_tmp = float(
                    option_value_dictionary["--interest"])
                credit_interest = (credit_interest_tmp / 100) / 12

                intermediary = annuity_payment / \
                    (annuity_payment - credit_interest * credit_principal)
                intermediary = annuity_payment / \
                    (annuity_payment - credit_interest * credit_principal)
                number_of_payments = math.ceil(
                    math.log(intermediary, 1 + credit_interest))

                overpayment = (annuity_payment *
                               number_of_payments) - credit_principal

                if 1 < number_of_payments < 12:
                    print(
                        f"You need {int(number_of_payments)} months to repay this credit!")
                    print(f"Overpayment = {overpayment}")
                elif number_of_payments == 1:
                    print(
                        f"You need {int(number_of_payments)} month to repay this credit!")
                    print(f"Overpayment = {overpayment}")
                elif (number_of_payments > 12) and (number_of_payments % 12 == 0):
                    print(
                        f"You need {int(number_of_payments / 12)} years to repay this credit!")
                    print(f"Overpayment = {overpayment}")
                elif (number_of_payments > 12) and (number_of_payments % 12 != 0):
                    if number_of_payments % 12 > 1:
                        print(
                            f"You need {int(math.floor(number_of_payments / 12))} years and {number_of_payments % 12} months to repay this credit!")
                        print(f"Overpayment = {overpayment}")
                    else:
                        print(
                            f"You need {int(math.floor(number_of_payments / 12))} years and {number_of_payments % 12} month to repay this credit!")
                        print(f"Overpayment = {overpayment}")
                elif number_of_payments == 12:
                    print("You need 1 year to repay this credit!")
                    print(f"Overpayment = {overpayment}")

            elif "--principal" not in option_value_dictionary.keys():
                annuity_payment = int(option_value_dictionary["--payment"])

                count_of_periods = int(option_value_dictionary["--periods"])

                credit_interest_tmp = float(
                    option_value_dictionary["--interest"])
                credit_interest = (credit_interest_tmp / 100) / 12
                top = (credit_interest * (1 + credit_interest)**count_of_periods)
                bottom = (1 + credit_interest)**count_of_periods - 1
                principal = annuity_payment / (top / bottom)

                overpayment = (annuity_payment * count_of_periods) - principal
                print(f"Your credit principal = {math.floor(principal)}!")
                print(f"Overpayment = {math.ceil(overpayment)}")
        except:
            print("Incorrect parameters 8")
