import yfinance as yf
import tkinter as tk
from tkinter import ttk

class StockPortfolioTrackerGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("Stock Portfolio Tracker")

        self.portfolio = {}

        tk.Label(root, text="Stock Symbol:").grid(row=0, column=0, padx=5, pady=5)

        tk.Label(root, text="Quantity:").grid(row=0, column=2, padx=5, pady=5)

        self.symbol_entry = tk.Entry(root)

        self.symbol_entry.grid(row=0, column=1, padx=5, pady=5)

        self.quantity_entry = tk.Entry(root)

        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)


        tk.Button(root, text="Add Investment", command=self.add_investment).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Remove Investment", command=self.remove_investment).grid(row=1, column=2, columnspan=2, pady=10)

        tk.Button(root, text="Track Performance", command=self.track_performance).grid(row=2, column=0, columnspan=4, pady=10)

        self.tree = ttk.Treeview(root, columns=('Symbol', 'Quantity', 'Current Price'))

        self.tree.heading('#0', text='Symbol')

        self.tree.heading('Symbol', text='Symbol')

        self.tree.heading('Quantity', text='Quantity')

        self.tree.heading('Current Price', text='Current Price')

        self.tree.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def add_investment(self):

        symbol = self.symbol_entry.get()

        quantity = int(self.quantity_entry.get())

        if symbol in self.portfolio:

            self.portfolio[symbol] += quantity

        else:

            self.portfolio[symbol] = quantity

        self.update_portfolio_tree()

    def remove_investment(self):

        symbol = self.symbol_entry.get()

        quantity = int(self.quantity_entry.get())

        if symbol in self.portfolio:

            if quantity >= self.portfolio[symbol]:

                del self.portfolio[symbol]

            else:

                self.portfolio[symbol] -= quantity

        self.update_portfolio_tree()

    def track_performance(self):

        prices = {}

        for symbol in self.portfolio.keys():

            stock_data = yf.Ticker(symbol)

            current_price = stock_data.history(period='1d')['Close'].iloc[-1]

            prices[symbol] = current_price

        for item in self.tree.get_children():

            self.tree.delete(item)


        for symbol, quantity in self.portfolio.items():

            current_price = prices[symbol]

            self.tree.insert('', 'end', values=(symbol, quantity, "${:.2f}".format(current_price)))

    def update_portfolio_tree(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        for symbol, quantity in self.portfolio.items():

            self.tree.insert('', 'end', values=(symbol, quantity, ""))

def main():
    root = tk.Tk()

    app = StockPortfolioTrackerGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()
