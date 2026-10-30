# Print() command in python 

**What is the print command in python**

Think of a real life printer 🖨️ , you give it what to print something on a paper and it,will print it out. 

Just like that in python think the print command like a printer and the output (or what the printer gives out) is given not on a paper but in the terminal or on the screen.

# Python `print()` Function Guide

The **`print()` function** is how you tell your computer to talk back to you. Think of it exactly like a **digital desk printer**: instead of printing ink onto physical paper, it prints text onto your computer screen.

---

## 1. The Printer Analogy

To understand how `print()` works, look at this quick comparison:

| The Action | A Real Printer 🖨️ | The Python `print()` Function 💻 |
| :--- | :--- | :--- |
| **What you print** | text , pictures and more | Strings (text), numbers, or variables (you will learn later what is a variable) |
| **Where it goes** | Onto a blank piece of paper | Onto your computer screen (terminal) |
| **The Blueprint** | You load paper and press "Print". | `print("Hello World")` sends the text to the screen. |

---

## 2. Basic Usage

As said before think the print() as a printer and the terminal or screen as a paper , think whatever you keep in between the brackets is what you give the printer to print the print on a paper , you wrap the text you keep in quotes ("") so that python understands it is text. you do not need quotes for numbers.

```python
# Printing text (Use quotes so Python knows it's text)
print("Hello, World!") # the output of this would be: Hello, World!

# Printing numbers (No quotes needed for math)
print(42) #output: 42 

# Printing text and numbers at a same time needs you to type the text wrapped in quotes with a comma after
 it and a number 
print("My lucky number is", 7) # output: My lucky number is 7 | here python combined both the number and text and
displayed the output, it there is no comma in between like print("hi my age is" 7) , this would show an error
```

---

## 3. The Custom Settings (Adding Options)

Just like a real printer has settings (like "Double-Sided" or "Color"), Python's printer has built-in settings you can tweak.

### Changing the Separator (`sep`)
By default, the printer puts a single space between items. You can change this to commas, dashes, or anything else.

```python
# Default setting (space)
print("Apple", "Banana", "Cherry")  
# Output: Apple Banana Cherry

# Custom setting: separating with a dash
print("Apple", "Banana", "Cherry", sep=" - ")  
# Output: Apple - Banana - Cherry
```

### Changing the End Behavior (`end`)
Normally, after printing a line, the printer advances the paper down to a **new line** (like hitting 'Enter'). You can tell it to stay on the same line instead.

```python
# Tell the printer to end with a space instead of a new line
print("Hello", end=" ")
print("World!")

# Output: Hello World!
# (Both statements print out on the exact same line)
```

---

## 4. Filling Out Forms (F-Strings)

Imagine printing a template form where you just fill in the blanks (like a name or age). In Python, we use **F-strings** to slide variables directly into our text.

```python
visitor_name = "Alice"
ticket_number = 104

# The 'f' before the quotes tells Python to look for the {} blanks
print(f"Welcome {visitor_name}! Your ticket number is {ticket_number}.")

# Output: Welcome Alice! Your ticket number is 104.
```

