import sys

def main():
    # gets hourly wage from input
    hourly = get_hourly(input("What is your hourly wage? ").strip())
    # ask how many hours
    hours = get_hours()
    # asks if one would like it before or after tax
    tax = get_tax()
    # asks if one would like a monthly or annual salary
    monann = get_monann()

    yearly = hourly * hours * 52
    monthly = hourly * hours * 4.34524
    if tax == "after":
        yearly = cal_incometax(yearly) - cal_nattax(monthly)

    if monann == "monthly":
        yearly = yearly / 12

    print_final(tax, monann, yearly)


def get_hourly(input):
        try:
            return float(input)
        except ValueError:
            print("Invalid usage, please try again.")
            sys.exit(1)


def get_hours():
    while True:
        try:
            return float(input("How many hours do you work in a week? ").strip())
        except ValueError:
            print("Invalid usage, please try again")
            continue


def get_tax():
    while True:
        try:
            tax = input("Would you like your wage by before or after tax? ").strip().lower()
            if tax == "before":
                return "before"
            elif tax == "after":
                return "after"
            else:
                raise ValueError
        except ValueError:
            print("Invalid usage, please try again.")
            continue


def get_monann():
    while True:
        try:
            monann = input("Would you like a monthly or annual salary? ").strip().lower()
            if monann == "monthly":
                return "monthly"
            elif monann == "annual":
                return "annual"
            else:
                raise ValueError
        except ValueError:
            print("Invalid usage, please try again.")



def cal_incometax(yearly):
    if yearly <= 12570:
        return yearly
    elif 12570 < yearly <= 50270:
        taxband1 = 12570
        taxband2 = (yearly - taxband1) * 0.8
        return taxband1 + taxband2
    elif 50270 < yearly <= 100000:
        taxband1 = 12570
        taxband2 = (yearly - taxband1) * 0.8
        taxband3 = (yearly - taxband1 - taxband2) * 0.6
        return taxband1 + taxband2 + taxband3
    elif 100000 < yearly <= 125140:
        taxband1 = 12570
        taxband2 = (yearly - taxband1) * 0.8
        taxband3 = (yearly - taxband1 - taxband2) * 0.6
        remove = ((yearly - 100000) / 2).round()
        return taxband1 + taxband2 + taxband3 - remove
    else:
        taxband1 = 12570
        taxband2 = (yearly - taxband1) * 0.8
        taxband3 = (yearly - taxband1 - taxband2) * 0.6
        taxband4 = (yearly - taxband1 - taxband2 - taxband3) * 0.55
        remove = ((yearly - 100000) / 2).round()
        return taxband1 + taxband2 + taxband3 + taxband4 - remove


def cal_nattax(monthly):
    if monthly <= 1048:
        return 0
    elif 1048 < monthly <= 4189:
        taxband1 = 1048
        taxband2 = (monthly - taxband1) * 0.12
        return taxband2 * 12
    elif 4189 < monthly:
        taxband1 = 1048
        taxband2 = (monthly - 1048) * 0.12
        taxband3 = (monthly - 1048 - 4189) * 0.02
        return (taxband2 + taxband3) * 12


def print_final(tax, monann, yearly):
    print("")
    print(f"Between the tax year of 6 April 2023 to 5 April 2024, your estimated {tax}-tax {monann} salary is around £{yearly:,.2f}.")
    print("")

if __name__ == "__main__":
    main()

