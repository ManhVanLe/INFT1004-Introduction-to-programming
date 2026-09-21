# Library Book Management System

A Python command-line project developed for INFT1004/INFT1006 coursework in 2025. The program manages book quantities by genre, with options to check out books, return books, analyse inventory, and restock.

The repository contains two stages of the project. Assignment 1 introduces inventory management using four fixed genres. Assignment 2 extends the system with dictionaries, additional genres, saved inventory and loan data, and a bar chart of available stock.

## Project structure

```text
Assignment1/
    ManhVanLe_Assign1.py
    VanManhLeAssign1.py
Assignment2/
    VanManhLe&HoanhAnhThuDinh_Assign2.py
    LibraryInventory.txt
    LoanData.txt
```

The two scripts in `Assignment1` are variants of the first assignment. The script in `Assignment2` is the extended version.

## Requirements

- Python 3
- Matplotlib for Assignment 2
- A desktop environment that can display the inventory chart

Install Matplotlib using the same Python interpreter that will run the program:

```powershell
python -m pip install matplotlib
```

Assignment 1 uses only Python's built-in functionality.

## Run Assignment 2

From the repository root:

```powershell
cd Assignment2
python "VanManhLe&HoanhAnhThuDinh_Assign2.py"
```

Run the program with `Assignment2` as the working directory because it reads and writes its data files using relative paths. Keep the script filename quoted because it contains `&`.

At startup, the program loads the saved inventory and loan counts, then displays these options:

| Option | Action |
| --- | --- |
| 1 | Add a new genre with an initial stock of 0–30 books. |
| 2 | Check out or return a specified quantity of books by genre. |
| 3 | Display stock levels and an inventory bar chart. |
| 4 | Save inventory and loan data. |
| 5 | Restock a genre within its capacity, accounting for books on loan. |
| 6 | Save both data files and quit. |

Follow the terminal prompts to select genres and enter quantities. New genre names must contain letters only. In the checkout/return prompt, enter `quit` to return to the main menu. Close the chart window to continue using the menu after inventory analysis.

### Inventory capacities

| Genre | Maximum books |
| --- | ---: |
| Fiction | 30 |
| Nonfiction | 20 |
| Science | 15 |
| History | 25 |
| Any new genre | 30 |

Assignment 2 reports available stock as **High** at 75% or more of capacity, **Ok** at 50% to below 75%, and **Low** below 50%.

### Saved data

`LibraryInventory.txt` stores available quantities, and `LoanData.txt` stores quantities currently on loan. Both use one genre and an integer count per line, separated by whitespace, with no header. For example:

```text
fiction 25
nonfiction 20
science 15
history 21
```

The program updates these files during use and saves both when you select **Save changes** or **Quit**. Copy the files before experimenting if you want to preserve their current contents.

When editing data manually, use lowercase genre names and ensure each inventory genre also has a loan entry, even if its loan count is zero. If `LoanData.txt` is missing entirely, the program starts all loaded genres with zero loans. Blank or malformed lines are not handled by the loader.

## Run Assignment 1

From the repository root:

```powershell
python "Assignment1/VanManhLeAssign1.py"
```

Alternatively, run `Assignment1/ManhVanLe_Assign1.py` to use the other variant.

Enter initial quantities for fiction, nonfiction, science, and history, then use the menu to check out or return one book at a time, analyse stock, or restock. Assignment 1 keeps its inventory in memory for the current session and does not save it to files.

## Scope

This is an educational simulation that tracks totals by genre. It does not track individual book titles, borrowers, or due dates.

## Authors

- Assignment 1: Manh Van Le
- Assignment 2: Van Manh Le and Hoang Anh Thu Dinh
