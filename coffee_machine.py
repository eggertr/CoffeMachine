class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disp_cups = 9
        self.money = 550
        return None

    def cups_able_to_produce(self, teg):

        svar = ""

        if teg == "1":  # espresso
            if self.water < 250:
                svar = "water"
            elif self.beans < 16:
                svar = "beans"
        elif teg == "2":  # latte
            if self.water < 350:
                svar = "water"
            elif self.milk < 75:
                svar = "milk"
            elif self.beans < 20:
                svar = "beans"
        elif teg == "3":  # cappuccino
            if self.water < 200:
                svar = "water"
            elif self.milk < 100:
                svar = "milk"
            elif self.beans < 12:
                svar = "beans"

        if svar != "":
            return "Sorry, not enough " + svar + "!"
        else:
            return "I have enough resources, making you a coffee!"

    def take_money(self):
        #global money
        print("\nI gave you ${}".format(self.money))
        self.money = 0

    def buy_coffee(self, i):
        # global water, milk, beans, money, disp_cups

        if i == 1:  # espresso
            self.water -= 250
            self.beans -= 16
            self.money += 4
        elif i == 2:  # latte
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
        elif i == 3:  # cappuccino
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6

        self.disp_cups -= 1

    def fill_supplies(self):
        # global water, milk, beans, disp_cups

        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.disp_cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def coffee_status(self):
        print()
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.disp_cups))
        print("{} of money".format(self.money))
        return None


action = ""

# ----- start ------
c_machine = CoffeeMachine()

while action != "exit":
    # coffee_status()

    print()
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "remaining":
        c_machine.coffee_status()
    elif action == "exit":
        break
    elif action == "buy":
        coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type in ("1", "2", "3"):
            c_machine.strsorry = c_machine.cups_able_to_produce(coffee_type)
            print(c_machine.strsorry)
            if c_machine.strsorry[:5] != "Sorry":
                c_machine.buy_coffee(int(coffee_type))
        elif coffee_type != "back":
            c_machine.coffee_status()

    elif action == "fill":
        c_machine.fill_supplies()
        # coffee_status()
    elif action == "take":
        c_machine.take_money()
        # coffee_status()

