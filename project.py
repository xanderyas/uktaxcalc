import sys


class Taxpayer:
    def __init__(self, name=None, hourly=None, hours=None, wage=0):
        self.name = name
        self.hourly = hourly
        self.hours = hours
        self.wage = wage


    def __str__(self):
        return f"\nDear {self.name},\n\nBetween the tax year of 6 April 2023 to 5 April 2024, your estimated UK taxed salary is around £{self.wage:,.2f}.\n\nThank you :)\n"


    @classmethod
    def get_info(cls):
        name = input("What is your name? ").strip()
        while True:
            try:
                hourly = float(input("What is your hourly wage? ").strip())
            except ValueError:
                print("Invalid usage, please try again")
                sys.exit(1)
            break

        while True:
            try:
                hours = float(input("How many hours do you work? ").strip())
            except ValueError:
                print("Invalid usage, please try again")
                continue
            break
        return cls(name, hourly, hours)


def tax(hourly, hours):
        wage = hourly * hours * 52
        if wage <= 12570:
            wage = wage
        elif 12570 < wage <= 50270:
            taxband1 = 12570
            taxband2 = (wage - taxband1) * 0.8
            wage = taxband1 + taxband2
        elif 50270 < wage <= 100000:
            taxband1 = 12570
            taxband2 = (wage - taxband1) * 0.8
            taxband3 = (wage - taxband1 - taxband2) * 0.6
            wage = taxband1 + taxband2 + taxband3
        elif 100000 < wage <= 125140:
            taxband1 = 12570
            taxband2 = (wage - taxband1) * 0.8
            taxband3 = (wage - taxband1 - taxband2) * 0.6
            remove = round(((wage - 100000) / 2))
            wage = taxband1 + taxband2 + taxband3 - remove
        else:
            taxband1 = 12570
            taxband2 = (wage - taxband1) * 0.8
            taxband3 = (wage - taxband1 - taxband2) * 0.6
            taxband4 = (wage - taxband1 - taxband2 - taxband3) * 0.55
            remove = round(((wage - 100000) / 2))
            wage = taxband1 + taxband2 + taxband3 + taxband4 - remove

        return wage


def nattax(hourly, hours):
        monthly = hourly * hours * 4.34524
        if monthly <= 1048:
            removal = 0
        elif 1048 < monthly <= 4189:
            taxband1 = 1048
            taxband2 = (monthly - taxband1) * 0.12
            removal = taxband2 * 12
        else:
            taxband1 = 1048
            taxband2 = (monthly - 1048) * 0.12
            taxband3 = (monthly - 1048 - 4189) * 0.02
            removal = (taxband2 + taxband3) * 12

        return removal



def main():
    taxpayer = Taxpayer.get_info()
    taxpayer.wage = tax(taxpayer.hourly, taxpayer.hours) - nattax(taxpayer.hourly, taxpayer.hours)
    print(taxpayer)



if __name__ == "__main__":
    main()

