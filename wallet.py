class Wallet:
    def __init__(self):
        self.balance = 500000000

    def show_balance(self):
        print(f"Bilancio attuale: {self.balance} BTC")

    def deposit(self, amount):
        self.balance += amount
        print(f"Hai depositato {amount} BTC")
        self.show_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Hai prelevato {amount} BTC")
        else:
            print("Fondi insufficienti")
        self.show_balance()

def main():
    my_wallet = Wallet()
    my_wallet.show_balance()

    while True:
        print("\nMenu:")
        print("1. Visualizza bilancio")
        print("2. Deposita")
        print("3. Preleva")
        print("4. Esci")
        
        choice = input("Seleziona un'opzione: ")

        if choice == "1":
            my_wallet.show_balance()
        elif choice == "2":
            amount = float(input("Inserisci l'importo da depositare: "))
            my_wallet.deposit(amount)
        elif choice == "3":
            amount = float(input("Inserisci l'importo da prelevare: "))
            my_wallet.withdraw(amount)
        elif choice == "4":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()
