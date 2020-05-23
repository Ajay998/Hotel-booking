class Hotelcal:

    def __init__(self):
        self.data = {}
        self.addHotel()

    def addHotel(self):
        name = input("Enter Hotel name: ")
        if self.data.get(name, True):
            self.data[name] = {}
            self.addRoom(name)

    def addRoom(self, name):
        roomno = input("Enter the room no you want to added")
        self.data[name][roomno] = {"items": [], "itemsList": [], "cost": 0}
        self.addAllItems(name, roomno)

    def addAllItems(self, name, roomno):
        i = 0
        while i < 5:
            items = input("Enter the items you want to added")
            price = input("Enter the item price in $")
            self.data[name][roomno]["items"].append({items: price})
            self.data[name][roomno]["itemsList"].append(items)
            self.data[name][roomno]["cost"] += int(price)
            i += 1
        self.addroomagain(name)

    def addroomagain(self, name):
        add_room = input("Do you want to add more Room(Yes/No): ")
        if add_room.lower() == "yes":
            self.addRoom(name)
        else:
            self.display()

    def display(self, budget=0):
        for name, info in self.data.items():
            context = "\nRoom No {0} items are  {1}, and rent is ${2}."
            if budget == 0:
                data = '\n\n\n{0} Hotel have following rooms\n'.format(name)
                for room, items_info in info.items():
                    facility = ', '.join(items_info['itemsList'])
                    cost = items_info['cost']
                    data += context.format(room, facility, cost)
                print(data)
            else:
                data = '\n\n\n{0} Hotel room matching your budget\n'.format(name)
                a = False
                for room, items_info in info.items():
                    cost = items_info['cost']
                    if cost <= budget:
                        facility = ', '.join(items_info['itemsList'])
                        a = True
                        data += context.format(room, facility, cost)
                if a:
                    print(data)
                else:
                    print("\n\n\nNo room available  in hotel {0}".format(name))
        if budget == 0:
                self.askBudget()

    def askBudget(self):
        budget = int(input("Please enter your budget: "))
        if budget > 1:
            self.display(budget)
        else:
            print("No Budget range ")



Hotelcal()
