Dormitory Care Tracker 🏥

A robust, Python-based Command Line Interface (CLI) application designed to manage student health records, accommodation details, and medical histories in dormitory settings. This system replaces manual logbooks with a persistent, digital storage solution.

📖 Overview

The Dormitory Care Tracker allows hostel wardens or health officers to digitally record and retrieve student information. It ensures that vital data—such as emergency contacts, allergies, and recent illnesses—is safely stored and easily accessible during emergencies.

Data is persisted locally in a structured JSON format (student_wellness_data.json), ensuring that records are saved even after the program is closed.

✨ Features

📝 Data Entry: comprehensive logging of student identity, accommodation (Block/Room), and medical profiles.

💾 Auto-Persistence: Automatically loads existing records on startup and saves new entries immediately.

🔍 Search Functionality: Find specific student records instantly using their Name or Student ID.

📊 Summary Dashboard: View a tabular overview of all students currently tracked in the system.

🛡️ Robust Error Handling: Uses JSON for safe data serialization (replacing unsafe eval methods) and handles missing files gracefully.

⚙️ Requirements

Python 3.x (Standard library only; no external packages required).

🚀 How to Run

Download the script:
Ensure you have the main script file, likely named project.py or health_manager.py.

Open your terminal/command prompt.

Navigate to the directory containing the script.

Execute the application:

python project.py


📂 File Structure

project.py: The main application source code containing the DormitoryCareTracker class and logic.

student_wellness_data.json: (Auto-generated) The database file where all student records are stored. If deleted, the program starts with an empty database.

🖥️ Usage Guide

Upon running the program, you will see the Main Menu:

==================================================
             DORMITORY CARE TRACKER - MAIN MENU
==================================================
1. Submit New Health Data
2. View Summary of All Entries
3. Search for a Specific Entry
4. Close Program and Save Data
==================================================


1. Submit New Health Data

Follow the prompts to enter:

Identity: Name, ID, Age, Phone.

Accommodation: Dorm Block, Room No, Occupancy.

Medical: Blood Group, Illnesses, Allergies, Medications.

Consultation: Recent doctor/hospital visits.

2. View Summary

Displays a clean table listing all students with their Data IDs and Locations.

3. Search

Enter a name (e.g., "John") or an ID (e.g., "U12345") to see full details for matching records.

🔒 Data Privacy Note

This system stores data locally in a .json file. Ensure access to the computer is restricted to authorized personnel to maintain student privacy.
