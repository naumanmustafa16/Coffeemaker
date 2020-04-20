# # Write your code here
# print(f'''For 125 cups of coffee you will need:
# {water_requirement} ml of water
# {milk_requirement} ml of milk
#{coffee_requirement} g of coffee beans''')

# water_available = int(input("Write how many ml of water the coffee machine has:\n"))
# with_water_makeable = (water_available//200)
# milk_available = int(input("Write how many ml of milk the coffee machine has:\n"))
# with_milk_makeable=milk_available//50
# coffee_available = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
# with_coffee_makeable = coffee_available//15
# makeable_cups=min(with_water_makeable,with_milk_makeable,with_coffee_makeable)
# required_cups = int(input("Write how many cups of coffee you will need: \n"))
# water_requirement = required_cups*200
# milk_requirement = required_cups*50
# coffee_requirement = required_cups*15
# more_cups = makeable_cups-required_cups
# if makeable_cups > required_cups:
#     print(f'Yes, I can make that amount of coffee (and even { more_cups} more than that)')
# elif makeable_cups == required_cups:
#     print('Yes, I can make that amount of coffee')
#
# else:
#     print(f'No, I can make only {makeable_cups} cup(s) of coffee')

# now_available_water=1200 #ml
# now_available_milk=540 #ml
# now_available_coffee=120 #g
# now_available_money=550 #$
# now_available_cups=9 #$
#
# def printer():
#     global now_available_water
#     global now_available_milk
#     global now_available_coffee
#     global now_available_money
#     global now_available_cups
#     print(f'''The coffee machine has:
#     {now_available_water} ml of water
#     {now_available_milk} ml of milk
#     {now_available_coffee} g of coffee beans
#     {now_available_cups} of disposable cups
#     {now_available_money} of money''')
#
# printer()
#
# action_chosen = input('Write action (buy, fill, take):')
# if action_chosen == 'buy':
#     coffee_type= int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
#     if coffee_type == 1: #espresso
#         now_available_water = now_available_water - 250
#         now_available_milk = now_available_milk - 0
#         now_available_coffee = now_available_coffee - 16
#         now_available_cups = now_available_cups - 1
#         now_available_money = now_available_money + 4
#         printer()
#
#     elif coffee_type == 2:
#     #latte
#         now_available_water = now_available_water - 350
#         now_available_milk = now_available_milk - 75
#         now_available_coffee = now_available_coffee - 20
#         now_available_cups = now_available_cups - 1
#         now_available_money = now_available_money + 7
#         printer()
#
#     elif coffee_type == 3:
#     #cappuccino
#         now_available_water = now_available_water - 200
#         now_available_milk = now_available_milk - 100
#         now_available_coffee = now_available_coffee - 12
#         now_available_cups = now_available_cups - 1
#         now_available_money = now_available_money + 6
#         printer()
#
# if action_chosen == 'fill':
#     added_water=int(input('Write how many ml of water do you want to add: '))
#     added_milk=int(input('Write how many ml of milk do you want to add: '))
#     added_coffee=int(input('Write how many g of coffee do you want to add: '))
#     added_cups=int(input('Write how many cups of coffee do you want to add: '))
#     now_available_water = now_available_water + added_water
#     now_available_milk = now_available_milk + added_milk
#     now_available_coffee = now_available_coffee + added_coffee
#     now_available_cups = now_available_cups + added_cups
#     printer()
#
# if action_chosen == 'take':
#     print(f'I gave you {now_available_money}')
#     now_available_money = 0
#     printer()



# now_available_water=400 #ml
# now_available_milk=540 #ml
# now_available_coffee=120 #g
# now_available_money=550 #$
# now_available_cups=9 #$
#
# def printer():
#     global now_available_water
#     global now_available_milk
#     global now_available_coffee
#     global now_available_money
#     global now_available_cups
#     print(f'''The coffee machine has:
#     {now_available_water} ml of water
#     {now_available_milk} ml of milk
#     {now_available_coffee} g of coffee beans
#     {now_available_cups} of disposable cups
#     {now_available_money} of money''')
#
# #printer()
# while True:
#     action_chosen = input('Write action (buy, fill, take, remaining, exit):')
#     if action_chosen == 'buy':
#         coffee_type= (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "))
#         if coffee_type == "1": #espresso
#             if now_available_water > 250 and now_available_coffee > 16 and now_available_cups > 1:
#                 print('I have enough resources, making you a coffee!')
#                 now_available_water = now_available_water - 250
#                 now_available_milk = now_available_milk - 0
#                 now_available_coffee = now_available_coffee - 16
#                 now_available_cups = now_available_cups - 1
#                 now_available_money = now_available_money + 4
#                 # printer()
#             else:
#                 if now_available_water < 250:
#                     print('Sorry, not enough water!')
#                 if now_available_coffee < 16:
#                     print('Sorry, not enough coffee!')
#                 if now_available_cups < 1:
#                     print('Sorry, not enough cups!')
#         elif coffee_type == "2":
#         #latte
#             if now_available_water >= 350 and now_available_milk >= 75 and now_available_coffee >= 20 and now_available_cups > 1:
#                 print('I have enough resources, making you a coffee!')
#                 now_available_water = now_available_water - 350
#                 now_available_milk = now_available_milk - 75
#                 now_available_coffee = now_available_coffee - 20
#                 now_available_cups = now_available_cups - 1
#                 now_available_money = now_available_money + 7
#                 # printer()
#             else:
#                 if now_available_water < 350:
#                     print('Sorry, not enough water!')
#                 if now_available_milk < 75:
#                     print('Sorry, not enough milk!')
#                 if now_available_coffee < 20:
#                     print('Sorry, not enough coffee!')
#                 if now_available_cups < 1:
#                     print('Sorry, not enough cups!')
#
#         elif coffee_type == "3":
#         #cappuccino
#             if now_available_water >= 200 and now_available_milk >= 100 and now_available_coffee >= 12 and now_available_cups > 1:
#                 print('I have enough resources, making you a coffee!')
#
#                 now_available_water = now_available_water - 200
#                 now_available_milk = now_available_milk - 100
#                 now_available_coffee = now_available_coffee - 12
#                 now_available_cups = now_available_cups - 1
#                 now_available_money = now_available_money + 6
#                 # printer()
#             else:
#                 if now_available_water < 200:
#                     print('Sorry, not enough water!')
#                 if now_available_milk < 100:
#                     print('Sorry, not enough milk!')
#                 if now_available_coffee < 12:
#                     print('Sorry, not enough coffee!')
#                 if now_available_cups < 1:
#                     print('Sorry, not enough cups!')
#         elif coffee_type == "back":
#             continue
#
#     if action_chosen == 'fill':
#         added_water=int(input('Write how many ml of water do you want to add: '))
#         added_milk=int(input('Write how many ml of milk do you want to add: '))
#         added_coffee=int(input('Write how many g of coffee do you want to add: '))
#         added_cups=int(input('Write how many cups of coffee do you want to add: '))
#         now_available_water = now_available_water + added_water
#         now_available_milk = now_available_milk + added_milk
#         now_available_coffee = now_available_coffee + added_coffee
#         now_available_cups = now_available_cups + added_cups
#         #printer()
#
#     if action_chosen == 'take':
#         print(f'I gave you {now_available_money}')
#         now_available_money = 0
#         #printer()
#
#     if action_chosen == 'remaining':
#         printer()
#
#     if action_chosen == 'exit':
#         break

class CoffeeMachine:
    def __init__(self,now_available_water,now_available_milk,now_available_coffee,now_available_money,now_available_cups):
        self.now_available_water = now_available_water
        self.now_available_milk = now_available_milk
        self.now_available_coffee = now_available_coffee
        self.now_available_money = now_available_money
        self.now_available_cups = now_available_cups

    def printer(self):
        # global now_available_water
        # global now_available_milk
        # global now_available_coffee
        # global now_available_money
        # global now_available_cups
        print(f'''The coffee machine has:
        {self.now_available_water} ml of water
        {self.now_available_milk} ml of milk
        {self.now_available_coffee} g of coffee beans
        {self.now_available_cups} of disposable cups
        {self.now_available_money} of money''')

    def working(self):
        while True:
            action_chosen = input('Write action (buy, fill, take, remaining, exit):')
            if action_chosen == 'buy':
                coffee_type = (
                    input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "))
                if coffee_type == "1":  # espresso
                    if self.now_available_water > 250 and self.now_available_coffee > 16 and self.now_available_cups > 1:
                        print('I have enough resources, making you a coffee!')
                        self.now_available_water = self.now_available_water - 250
                        self.now_available_milk = self.now_available_milk - 0
                        self.now_available_coffee = self.now_available_coffee - 16
                        self.now_available_cups = self.now_available_cups - 1
                        self.now_available_money = self.now_available_money + 4
                        # printer()
                    else:
                        if self.now_available_water < 250:
                            print('Sorry, not enough water!')
                        if self.now_available_coffee < 16:
                            print('Sorry, not enough coffee!')
                        if self.now_available_cups < 1:
                            print('Sorry, not enough cups!')
                elif coffee_type == "2":
                    # latte
                    if self.now_available_water >= 350 and self.now_available_milk >= 75 and self.now_available_coffee >= 20 and self.now_available_cups > 1:
                        print('I have enough resources, making you a coffee!')
                        self.now_available_water = self.now_available_water - 350
                        self.now_available_milk = self.now_available_milk - 75
                        self.now_available_coffee = self.now_available_coffee - 20
                        self.now_available_cups = self.now_available_cups - 1
                        self.now_available_money = self.now_available_money + 7
                        # printer()
                    else:
                        if self.now_available_water < 350:
                            print('Sorry, not enough water!')
                        if self.now_available_milk < 75:
                            print('Sorry, not enough milk!')
                        if self.now_available_coffee < 20:
                            print('Sorry, not enough coffee!')
                        if self.now_available_cups < 1:
                            print('Sorry, not enough cups!')

                elif coffee_type == "3":
                    # cappuccino
                    if self.now_available_water >= 200 and self.now_available_milk >= 100 and self.now_available_coffee >= 12 and self.now_available_cups > 1:
                        print('I have enough resources, making you a coffee!')

                        self.now_available_water = self.now_available_water - 200
                        self.now_available_milk = self.now_available_milk - 100
                        self.now_available_coffee = self.now_available_coffee - 12
                        self.now_available_cups = self.now_available_cups - 1
                        self.now_available_money = self.now_available_money + 6
                        # printer()
                    else:
                        if self.now_available_water < 200:
                            print('Sorry, not enough water!')
                        if self.now_available_milk < 100:
                            print('Sorry, not enough milk!')
                        if self.now_available_coffee < 12:
                            print('Sorry, not enough coffee!')
                        if self.now_available_cups < 1:
                            print('Sorry, not enough cups!')
                elif coffee_type == "back":
                    continue

            if action_chosen == 'fill':
                added_water = int(input('Write how many ml of water do you want to add: '))
                added_milk = int(input('Write how many ml of milk do you want to add: '))
                added_coffee = int(input('Write how many g of coffee do you want to add: '))
                added_cups = int(input('Write how many cups of coffee do you want to add: '))
                self.now_available_water = self.now_available_water + added_water
                self.now_available_milk = self.now_available_milk + added_milk
                self.now_available_coffee = self.now_available_coffee + added_coffee
                self.now_available_cups = self.now_available_cups + added_cups
                # printer()

            if action_chosen == 'take':
                print(f'I gave you {self.now_available_money}')
                self.now_available_money = 0
                # printer()

            if action_chosen == 'remaining':
                CoffeeMachine.printer(self)

            if action_chosen == 'exit':
                break

mycoffemachine = CoffeeMachine(400,540,120,550,9)
mycoffemachine.working()