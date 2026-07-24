# 📂 Python File Handling Journey

A step-by-step log of my journey learning Python File Handling by building practical mini-projects. This repository documents my progress from basic file operations to working with the `os` module, CSV files, JSON files, exception handling, and persistent data storage.

---

##  Topics Covered

###  File Handling Fundamentals
- Opening files using `open()`
- File Modes (`r`, `w`, `a`, `x`)
- Reading files using `read()`, `readline()`, and file iteration
- Writing files using `write()`
- Appending data to existing files
- Using the `with` statement
- File Pointer Methods (`tell()` & `seek()`)
- Exception Handling with Files (`FileNotFoundError`)
- Persistent data storage using text files

###  Upcoming Topics
- `os` Module
- CSV File Handling
- JSON File Handling
- File & Folder Management
- Real-world File Handling Projects

---

# 📈 Concept 1: File Handling Fundamentals

### 📖 Concepts Learned

- Opening and closing files
- Understanding file modes (`r`, `w`, `a`, `x`)
- Reading complete files using `read()`
- Reading files line-by-line
- Writing and appending data using `write()`
- Using the `with` statement for automatic file management
- File Pointer Methods (`tell()` and `seek()`)
- Handling file-related exceptions
- Building menu-driven applications using text files
- Persistent data storage

---

##  daily_journal.py

### Description

A digital journal application that allows users to write and save their daily thoughts inside a text file. Every new journal entry is appended without overwriting previous records, allowing users to maintain a continuous journal history. Users can also choose to display all previously saved journal entries after writing.

### Concepts Demonstrated

- File opening using `open()`
- Append Mode (`a`)
- Read Mode (`r`)
- `write()`
- `read()`
- `with` Statement
- Exception Handling (`try` & `except`)
- `FileNotFoundError`
- Persistent Text File Storage
- User Input Handling

---

##  todo_manager.py

### Description

A menu-driven To-Do Manager that stores user tasks inside a text file. Users can add new tasks, view all previously saved tasks with automatic numbering, and safely handle situations where the task file does not exist or is empty.

### Concepts Demonstrated

- Append Mode (`a`)
- Read Mode (`r`)
- Writing user input to files
- Reading files using file iteration
- `with` Statement
- `os.path.exists()`
- `os.path.getsize()`
- Functions
- Menu-driven Programming
- Persistent Task Storage

---

##  file_analyzer.py

### Description

A text file analyzer that reads any user-specified file and generates useful statistics such as the total number of lines, words, and characters. The program also demonstrates Python's file pointer methods by displaying the cursor position before and after reading the file, then resetting the cursor using `seek()` to reread the first line.

### Concepts Demonstrated

- File opening using `open()`
- Read Mode (`r`)
- `read()`
- `readline()`
- File Pointer Methods (`tell()` & `seek()`)
- String Processing (`split()` & `splitlines()`)
- Character, Word, and Line Counting
- Exception Handling (`FileNotFoundError`)
- User Input Handling

---

## Skills Gained

By completing these projects, I learned how to:

- Build applications that permanently store user data.
- Read, write, and append information using different file modes.
- Analyze text files by calculating lines, words, and character counts.
- Work with file pointers using `tell()` and `seek()`.
- Handle missing files gracefully using exception handling.
- Build interactive, menu-driven console applications backed by text files.
- Organize file operations using Python's `with` statement.

---

## 📁 Repository Structure

```text
python-file-handling/
│
├── 01-File-Handling/
│   ├── daily_journal.py
│   ├── todo_manager.py
│   ├── file_analyzer.py
│
└── README.md
```

---

## 🛠 Technologies Used

- Python 3
- Text Files (`.txt`)
- File Handling
- Exception Handling
- OS Module (Basics)

---

## 📌 Upcoming Projects

-  file_manager.py
-  student_csv_manager.py
-  student_json_database.py
-  library_management_system.py

---

## 🎯 Learning Goal

The objective of this repository is to strengthen my understanding of Python File Handling by implementing every major concept through practical, real-world mini-projects while following clean coding practices and maintaining consistent GitHub documentation.