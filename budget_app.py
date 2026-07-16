class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = self.name.center(30, "*")
        result = title + "\n"

        for item in self.ledger:
            result += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"

        result += f"Total: {self.get_balance():.2f}"
        return result


def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    spent = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        spent.append(total)

    total_spent = sum(spent)

    percentages = []
    for amount in spent:
        percentages.append(int((amount / total_spent) * 100 // 10 * 10))

    for percent in range(100, -1, -10):
        result += f"{percent:3}| "
        for p in percentages:
            if p >= percent:
                result += "o  "
            else:
                result += "   "
        result += "\n"

    result += "    -" + "---" * len(categories) + "\n"

    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        result += "     "
        for name in names:
            if i < len(name):
                result += name[i] + "  "
            else:
                result += "   "
        result += "\n"

    return result.rstrip("\n")
