class MealCard:
    cafeteria_name = "Campus Cafe"
    min_balance = 5
    total_cards = 0
    def __init__(self, student, balance=0, transactions=None):
        self.student = student
        self.balance = balance
        self.transactions = transactions if transactions is not None else []
        MealCard.total_cards += 1
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"+{amount}")
            print(f"Deposited {amount}. Balance: {self.balance}")
    def purchase(self, amount):
        if self.balance - amount >= MealCard.min_balance:
            self.balance -= amount
            self.transactions.append(f"-{amount}")
            print(f"Purchased meal for {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance for purchase")
    
    def display_card(self):
        print(f"Student: {self.student}, Balance: {self.balance}, Cafeteria: {MealCard.cafeteria_name}")
    def show_transactions(self):
        for i in self.transactions:
            print(i)
        print(f"Total cards: {MealCard.total_cards}")

student1 = MealCard("Malika", 15)
student1.display_card()
student1.deposit(30)
student1.purchase(12)
student1.purchase(10)
student1.show_transactions()


'''
Student: Malika, Balance: 15, Cafeteria: Campus Cafe
Deposited 30. Balance: 45
Purchased meal for 12. Balance: 33
Purchased meal for 10. Balance: 23
+30
-12
-10
Total cards: 1
'''
