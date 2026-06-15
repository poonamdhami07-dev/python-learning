# Day 3 – Time Module & Greeting Program

## Overview

On Day 3 of my Python learning journey, I explored the **Time Module** and created a program that displays the current time and greets the user based on the time of day.

## What I Learned

- Importing modules in Python
- Using the `time` module
- Working with current date and time
- Formatting time using `strftime()`
- Conditional statements (`if`, `elif`, `else`)
- Building a real-world greeting application

## Program Features

### Display Current Time

The program fetches and displays the current system time in:

- Hours
- Minutes
- Seconds

Example:

```text
Current time: 14:35:20
14
35
20
```

### Time-Based Greeting

The program greets the user according to the current hour.

| Time Range | Greeting |
|------------|-----------|
| 5 AM – 11:59 AM | Good Morning |
| 12 PM – 4:59 PM | Good Afternoon |
| 5 PM – 8:59 PM | Good Evening |
| 9 PM – 4:59 AM | Good Night |

Example:

```text
Current time: 08:30:15
Good Morning
```

## Concepts Practiced

- `import time`
- `time.strftime()`
- `time.localtime()`
- Variables
- Type Conversion
- Conditional Statements

## Technologies Used

- Python 3

## Author

**Poonam Dhami**  
B.Tech CSE (Data Science)
