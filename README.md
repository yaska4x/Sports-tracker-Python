# Sports Tracker (Python)

A simple command-line Sports Tracker built with Python.  
It allows users to log sports activities, track time spent, and view statistics — perfect for beginners and small projects.

---

## Features
- Add sports activities (sport, duration, date)  
- View logged activities  
- See total time spent per sport  
- Data saved locally using CSV  
- Easy to extend and customize  
- Lightweight, no external libraries required  

---

## Requirements
- Python 3.8+  
- Standard Python libraries: `csv`, `collections`, `datetime`  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sports-tracker.git
Navigate into the project directory:
cd sports-tracker

Run the program:
python sports_tracker.py
Usage

After running the program, you will see the main menu:
Sports Tracker
1. Add activity
2. View activities
3. View statistics
4. Exit
Add activity: Enter the sport name, duration (minutes), and date (YYYY-MM-DD) or press Enter to use today’s date.
View activities: Lists all activities you have logged.
View statistics: Shows total time spent per sport.
Exit: Close the program.

Data Storage
All activities are saved in the CSV file:
sports_data.csv
This file is automatically created when you add your first activity.
Each row in the file contains: Sport, Duration (minutes), Date.
Example Activities
Here is an example of what logged activities may look like:
Sport	Duration (min)	Date
Soccer	60	2025-12-23
Basketball	45	2025-12-22
Running	30	2025-12-21
