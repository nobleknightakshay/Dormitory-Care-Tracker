Project Statement: Dormitory Care Tracker

1. Introduction

In large residential educational institutions, managing the health and well-being of students residing in dormitories is a critical responsibility. Traditional paper-based methods for tracking medical history, emergency contacts, and recent illnesses are often inefficient, prone to damage, and difficult to search quickly during emergencies. The Dormitory Care Tracker is designed to solve these issues by providing a digitized, lightweight solution for dormitory wardens and health officers.

2. Problem Statement

The current manual systems for recording student health data suffer from several drawbacks:

Data Redundancy: Information is often duplicated across different logbooks.

Slow Retrieval: Finding a specific student's medical history or emergency contact during a crisis is time-consuming.

Lack of Persistence: Physical records can be easily misplaced or destroyed.

Inconsistency: Handwritten records may be illegible or incomplete.

3. Proposed Solution

The Dormitory Care Tracker is a Python-based Command Line Interface (CLI) application developed to streamline the management of student health records. It offers a centralized digital repository where student details, accommodation information, and medical profiles are stored securely in a structured JSON format.

Key Objectives

Digitalization: Convert physical health logs into digital records.

Accessibility: Provide instant access to student health data via ID or Name search.

Persistence: Ensure data survives program restarts using file-based storage.

User-Friendliness: Offer a simple, menu-driven interface for non-technical staff.

4. Technical Overview

The system is built using standard Python libraries, ensuring high portability and minimal dependencies.

Programming Language: Python 3.x

Data Storage: JSON (JavaScript Object Notation) for human-readable and structured data persistence (student_wellness_data.json).

Core Libraries:

json: For serializing and deserializing health records.

os: For file existence checks and path management.

datetime: For timestamping entry submissions.

5. System Features

The application supports the following core operations:

Data Entry: Allows users to input detailed student profiles, including:

Identity: Name, ID, Age, Emergency Contact.

Accommodation: Dorm Block, Room Number, Occupancy type.

Medical Profile: Blood Group, Current Illnesses, Allergies, Medications.

Consultation History: Recent doctor visits or hospitalizations.

Data Persistence: Automatically loads existing records upon startup and saves new entries immediately to preventing data loss.

Search Functionality: Enables users to query the database by Student Name or Registration ID to find specific records.

Summary View: Displays a tabular summary of all students currently tracked in the system.

6. Conclusion

The Dormitory Care Tracker provides a robust foundation for health management in student housing. By transitioning from paper to a digital system, the project ensures better data integrity, faster response times in emergencies, and easier administrative oversight.
