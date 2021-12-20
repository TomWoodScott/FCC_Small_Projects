class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        # for function in part 2
        self.cost = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, neg_amount, description=""):
        if self.check_funds(neg_amount):
            self.balance -= neg_amount
            # for function in part 2
            self.cost -= neg_amount
            self.ledger.append({"amount": -neg_amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {transfer_category.category}")
            transfer_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def __str__(self):

        while len(self.category) < 30:
            self.category = "*" + self.category + "*"

        # for odd len category name
        self.print_text = self.category[:30]

        for i in self.ledger:
            self.print_text += '\n' + str(i["description"][0:23]).ljust(23) + \
                               "{0:.2f}".format(i["amount"]).rjust(7)

        self.print_text += '\n' f'Total: {self.balance}'

        return self.print_text


def create_spend_chart(categories):
    # categories is a list
    barchart = "Percentage spent by category" + "\n"

    long_category, tot_spent, number = 0, 0, 100

    for category in categories:
        tot_spent += category.cost

        # numbers -- need to add maths to while loop
    while number >= 0:
        barchart += str(number).rjust(3) + "| "

        for category in categories:
            if ((category.cost / tot_spent) * 100) > number:
                barchart += "o".ljust(2) + " "
            else:
                barchart += "   "
        barchart += '\n'
        number -= 10

    # long_category
    for i in range(len(categories)):
        if len(categories[i].category.strip("*")) >= long_category:
            long_category = len(categories[i].category.strip("*"))

    # bar

    barchart += " " * 4 + ("---" * (len(categories))) + "-"

    letter_list = [[] for i in range(long_category)]

    for category in categories:
        index = 0

        category = category.category.strip("*").ljust(long_category, " ")
        for letter in category:
            if index == 0:
                letter_list[index].append(letter.upper())
            else:
                letter_list[index].append(letter.lower())
            index += 1

    for entry in letter_list:
        barchart += '\n'
        for i in range(len(categories)):
            try:
                if i == 0:
                    barchart += f'{entry[i]}'.rjust(6)
                elif i == len(categories) - 1:
                    barchart += f"  {entry[i]}  "
                else:
                    barchart += f'{entry[i]}'.rjust(3)
            except:
                pass

    return barchart
