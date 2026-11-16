# Contact Book

A command-line contact book written in Python. Contacts are stored in a CSV file, and every name, phone number and email address is validated before it's saved.

Built as the final project for *Fundamentals of Python Programming 2* (COMP H1031) in my first year at TU Dublin.

---

## 📂 Repository Structure

```
contact_book/
├── src/
│   ├── main.py              # Menu and user input
│   └── core_logic.py        # Validation and contact operations
├── tests/
│   └── test_core_logic.py   # Unit tests for the validation functions
└── requirements.txt         # No external libraries needed
```

---

## ✨ Features

The menu in `main.py` calls the functions in `core_logic.py`, so the user interface is kept separate from the logic.

- **View** all contacts
- **Search** by name, phone number, email address or address (not case-sensitive)
- **Add** a contact
- **Delete** a contact by phone number
- **Update** a contact by phone number

Each contact has a name, phone number, email address and address, stored in `contacts.csv`. The file is created the first time the program runs, and is never overwritten if it already exists.

---

## ✅ Input Validation

| Field | Rules |
|-------|-------|
| Name | 1 to 20 characters |
| Phone number | Digits, with an optional `+` at the start, and hyphens, brackets or spaces. Between 3 and 15 digits. Must not already be in the contact book |
| Email address | Checked against a regular expression for the `name@domain.tld` format. Between 6 and 254 characters. Must not already be in the contact book |

Menu input is validated too: anything that isn't a whole number from 1 to 6 gives an error message and the menu is shown again. File errors are caught and reported instead of crashing the program.

---

## 🧪 Tests

`tests/test_core_logic.py` has unit tests for the validation functions, with valid and invalid examples for each. The two uniqueness checks read from the CSV file, so their tests use `unittest.mock` (`mock_open` and `patch`) to stand in for the file. That way the tests don't depend on a real `contacts.csv`.

---

## ▶️ Running It

It needs Python 3 and no external libraries.

```
cd src
python main.py
```
