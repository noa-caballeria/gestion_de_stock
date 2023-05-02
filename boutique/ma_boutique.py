import tkinter as tk
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "boutique"
)


class Products():
    def __init__(self, db):
        self.db = db 
        self.root = tk.Tk()
        self.root.title("Ma Boutique")


        tk.Label(self.root, text="Nom :").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Description :").grid(row=1, column=0)
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Quantité :").grid(row=2, column=0)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Prix :").grid(row=3, column=0)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Catégorie :").grid(row=4, column=0)
        self.category_entry = tk.Entry(self.root)
        self.category_entry.grid(row=4, column=1)

        self.add_button = tk.Button(self.root, text="Ajouter", command=self.add_product)
        self.add_button.grid(row=5, column=0)

        self.delete_button = tk.Button(self.root, text="Supprimer", command=self.delete_product)
        self.delete_button.grid(row=5, column=1)

        self.products_table = tk.Listbox(self.root)
        self.products_table.grid(row=6, column=0, columnspan=2)

        self.get_products()
        self.root.mainloop()



    def get_products(self):
        self.products_table.delete(0, tk.END)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM produit")
        products = cursor.fetchall()
        for product in products:
            self.products_table.insert(tk.END, f"{product[0]} - {product[1]} - {product[2]} - {product[3]} - {product[4]}")



    def add_product(self):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO produit (nom, description, quantite, prix, id_categorie) VALUES (%s, %s, %s, %s, %s)", (self.name_entry.get(), self.description_entry.get(), self.quantity_entry.get(), self.price_entry.get(), self.category_entry.get()))
        self.db.commit()
        self.get_products()



    def delete_product(self):
        selected_product = self.products_table.get(tk.ACTIVE)
        product_id = selected_product.split(" - ")[0]
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM produit WHERE id = %s", (product_id,))
        self.db.commit()
        self.get_products()

app = Products(db)
