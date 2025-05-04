# 🍎 Fruit Inventory Manager App

The **Fruit Inventory Manager App** is a simple command-line application that helps users manage a list of fruits, their quantities, and prices. Data is persistently stored in a binary file using Python's `pickle` module.

## 🧰 Features

- Add new fruits with name, quantity, and price
- Search for existing fruits
- View all fruit names and detailed information
- Update fruit quantity and price
- Calculate total inventory value
- Delete specific fruits or clear the entire list
- Persistent storage via `fruit_list.dat`

## 🚀 How to Run

1. Clone or download the folder `fruit_inventory_manager_App`
2. Make sure `main.py` and `fruits.py` are in the same folder
3. Run from terminal:
   ```bash
   python main.py
   ```

> All fruit data will be saved in the same folder as `main.py` via `fruit_list.dat`.

## 📁 Folder Structure

```
fruit_inventory_manager_App/
│
├── main.py              # Main logic and menu interface
├── fruits.py            # Fruit class with properties
├── shopping.py          # Optional: Shopping item model
├── fruit_list.dat       # (auto-created) Persistent data file
└── README.md            # This file
```

## 👨‍💻 Developer Notes

- Fully documented with comments for learning and collaboration
- Object-oriented design with encapsulation
- Easy to extend with more item types (e.g., vegetables, products)

## 📜 License

This project is free to use for educational and non-commercial purposes.
