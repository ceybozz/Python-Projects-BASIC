# 🚗 Car Insights App

The **Car Insights App** is a command-line Python application that allows you to load, clean, analyze, and visualize car data from CSV files using `pandas`, `numpy`, `matplotlib`, and `seaborn`.

---

## 📦 Features

- Load and preview car data from `cars_data.csv`
- Drop unnecessary columns
- Rename and clean column headers
- Convert text values (e.g. brand names) to numeric codes
- Merge multiple CSVs (e.g., `cars_dat1.csv`, `cars_dat2.csv`)
- Handle missing values and outliers
- Compute summary statistics (mean, median, percentiles)
- Create visualizations:
  - Scatterplot (e.g. HP vs Price)
  - Histogram (e.g. Price distribution)
  - Correlation heatmap
- Save cleaned data to `cars_data_cleaned.csv`

---

## 🧰 Requirements

- Python 3.x
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

You can install dependencies with:
```bash
pip install pandas numpy matplotlib seaborn
```

---

## 🚀 How to Run

```bash
python main.py
```

Make sure the file `cars_data.csv` is in the **same directory** as `main.py`. If not found, the program will notify you.

---

## 📁 File Structure

```
Car Insights App/
├── main.py                # Main program logic and menu
├── cars_data.csv          # Your input dataset (place here)
├── cars_data_cleaned.csv  # Output file after cleaning
└── README.md              # This file
```

---

## 🧠 Developer Notes

- Modular design: each menu item is its own function
- Handles common edge cases like missing files or invalid input
- Easy to extend: just add more menu options and visualizations

---

## 📜 License

Free to use for educational and personal projects.
