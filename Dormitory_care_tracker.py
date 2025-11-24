# health_manager.py - A Simple System for Managing Student Health Records

import os
from datetime import datetime
import json # Changed file handling from 'eval' to 'json' for better safety and standard practice

# --- Core Class for Health Data Management ---
class DormitoryCareTracker:
    """Manages student health records, loading from and saving to a JSON file."""
    
    def __init__(self):
        # Using a more descriptive name for the data file
        self.record_storage_file = "student_wellness_data.json"
        # Holds all health dictionary records in a list
        self.health_entries = self.retrieve_entries()

    # Changed method name from 'load_records'
    def retrieve_entries(self):
        """Loads records from the JSON file."""
        if os.path.exists(self.record_storage_file):
            try:
                with open(self.record_storage_file, 'r') as f:
                    content = f.read()
                    if content.strip():
                        # Use json.loads instead of eval() - much safer!
                        return json.loads(content)
            except (json.JSONDecodeError, FileNotFoundError):
                # Handle cases where the file is corrupt or empty
                print(f"Warning: Could not read {self.record_storage_file}. Starting with empty records.")
                pass
        return []

    # Changed method name from 'save_records'
    def persist_entries(self):
        """Saves current health entries list back to the JSON file."""
        # Using json.dump with indentation for readability in the file
        with open(self.record_storage_file, 'w') as f:
            json.dump(self.health_entries, f, indent=4)

    # Changed method name from 'collect_health_record'
    def gather_student_data(self):
        """Prompts the user to input data for a new health record."""
        print("\n" + "#"*60)
        print("                 NEW STUDENT HEALTH ENTRY")
        print("#"*60 + "\n")

        # Use more student-like/simple variable names
        print("👤 IDENTITY DETAILS")
        print("-" * 30)
        s_name = input("Student's Full Name: ").strip()
        s_id = input("Student ID (e.g., U12345): ").strip()
        s_age = input("Age in Years: ").strip()
        s_phone = input("Emergency Contact No.: ").strip()

        print("\n🏠 ACCOMMODATION INFO")
        print("-" * 30)
        dorm_block = input("Dormitory Block (A, B, C...): ").strip()
        room_num = input("Room Number: ").strip()
        # Changed 'room_type' to 'occupancy'
        occupancy = input("Room Occupancy (e.g., Single/Shared): ").strip()

        print("\n🏥 MEDICAL PROFILE")
        print("-" * 30)
        b_group = input("Blood Group (e.g., O+, A-): ").strip()
        # Changed 'current_disease' to 'illness_present'
        illness_present = input("Current Illness/Symptoms (If any, or N/A): ").strip()
        # Changed 'allergies' to 'known_sensitivities'
        known_sensitivities = input("Known Allergies? (Food, Drug, etc., or N/A): ").strip()
        current_pills = input("Prescribed Medications? (Name/Dosage, or N/A): ").strip()

        print("\n👨‍⚕️ RECENT CONSULTATIONS")
        print("-" * 30)
        saw_doc = input("Consulted a Doctor Recently? (y/n): ").strip().lower()
        doc_name = ""
        if saw_doc == "y":
            doc_name = input("Doctor's Name: ").strip()

        went_to_hosp = input("Visited a Clinic/Hospital Recently? (y/n): ").strip().lower()
        hosp_name = ""
        if went_to_hosp == "y":
            hosp_name = input("Hospital/Clinic Name: ").strip()

        # Constructing the record dictionary
        new_entry = {
            # Simple, student-like record ID generation
            "data_id": f"WEL-{len(self.health_entries) + 1:04d}",
            "submission_date": datetime.now().strftime("%Y-%m-%d @ %H:%M"),
            "full_name": s_name, 
            "student_reg_id": s_id, 
            "student_age": s_age, 
            "phone_contact": s_phone,
            "block_id": dorm_block, 
            "room_number": room_num, 
            "room_occupancy": occupancy,
            "blood_type": b_group,
            # Cleaner way to handle empty inputs
            "illness_details": illness_present if illness_present else "None Reported",
            "allergy_info": known_sensitivities if known_sensitivities else "None Reported",
            "medication_list": current_pills if current_pills else "None Reported",
            "doctor_consulted": "Yes" if saw_doc == "y" else "No", 
            "consulting_doctor_name": doc_name,
            "hospital_visited_flag": "Yes" if went_to_hosp == "y" else "No", 
            "hospital_location_name": hosp_name
        }
        return new_entry

    # Changed method name from 'display_record'
    def show_entry_details(self, entry):
        """Prints a single health record in a formatted way."""
        print("\n" + "="*50)
        print(f"     HEALTH DATA ID: {entry['data_id']}")
        print("="*50)
        print(f"Date Submitted: {entry['submission_date']}")
        
        print("\n-- Personal Info --")
        print(f"Name: {entry['full_name']}")
        print(f"Student ID: {entry['student_reg_id']}")
        print(f"Age: {entry['student_age']}")
        print(f"Contact: {entry['phone_contact']}")
        
        print("\n-- Dorm Info --")
        print(f"Block: {entry['block_id']}")
        print(f"Room No: {entry['room_number']}")
        print(f"Occupancy: {entry['room_occupancy']}")
        
        print("\n-- Health Vitals --")
        print(f"Blood Group: {entry['blood_type']}")
        print(f"Current Illness: {entry['illness_details']}")
        print(f"Allergies: {entry['allergy_info']}")
        print(f"Medications: {entry['medication_list']}")
        
        print("\n-- Consultation Log --")
        print(f"Doctor Consulted: {entry['doctor_consulted']}")
        if entry['consulting_doctor_name']:
            print(f"Doctor Name: {entry['consulting_doctor_name']}")
        print(f"Hospital Visit: {entry['hospital_visited_flag']}")
        if entry['hospital_location_name']:
            print(f"Hospital Name: {entry['hospital_location_name']}")
        print("="*50 + "\n")

    # Changed method name from 'search_record'
    def find_entry_by_term(self, key_word):
        """Searches records by name or student ID."""
        found_results = []
        search_lower = key_word.lower()
        for entry in self.health_entries:
            # Check for matches in full_name or student_reg_id
            if (search_lower in entry['full_name'].lower() or 
                search_lower in entry['student_reg_id'].lower()):
                found_results.append(entry)
        return found_results

    # Changed method name from 'list_all_records'
    def display_all_summary(self):
        """Prints a summary table of all stored health entries."""
        if not self.health_entries:
            print("\nDatabase is empty. No health entries found.")
            return
        
        print("\n" + "="*75)
        print("                     COMPREHENSIVE HEALTH ENTRY SUMMARY")
        print("="*75)
        # Adjusted column headers and widths
        print(f"{'Data ID':<10} {'Student Name':<25} {'Student ID':<15} {'Dorm Location':<15}")
        print("-"*75)
        
        for entry in self.health_entries:
            data_id = entry['data_id']
            # Truncate names for clean display
            s_name = entry['full_name'][:23].ljust(23)
            s_reg = entry['student_reg_id'][:13].ljust(13)
            dorm_loc = f"{entry['block_id']}-{entry['room_number']}"
            print(f"{data_id:<10} {s_name:<25} {s_reg:<15} {dorm_loc:<15}")
        
        print("="*75)
        print(f"Total Entries in System: {len(self.health_entries)}\n")

    # Changed method name from 'run_menu'
    def start_program_loop(self):
        """The main menu loop for the application."""
        while True:
            print("\n" + "="*50)
            print("       DORMITORY CARE TRACKER - MAIN MENU")
            print("="*50)
            print("1. Submit New Health Data")
            print("2. View Summary of All Entries")
            print("3. Search for a Specific Entry")
            print("4. Close Program and Save Data") # Clearer exit description
            print("="*50)
            
            user_action = input("\nEnter your choice (1-4): ").strip()
            
            if user_action == "1":
                new_data = self.gather_student_data()
                self.health_entries.append(new_data)
                self.persist_entries() # Save immediately after adding
                self.show_entry_details(new_data)
                print("✅ New health record successfully added and saved!")
            elif user_action == "2":
                self.display_all_summary()
            elif user_action == "3":
                search_key = input("\nEnter Student Name or ID to find: ").strip()
                results = self.find_entry_by_term(search_key)
                if results:
                    print(f"\nFound {len(results)} matching entry(ies):")
                    for entry in results:
                        self.show_entry_details(entry)
                else:
                    print("\n❌ No entries matched your search criteria.")
            elif user_action == "4":
                self.persist_entries() # Final save on exit
                print("\nGoodbye! All records have been securely saved to the file.")
                break
            else:
                print("\n⚠️ Invalid choice. Please enter a number between 1 and 4.")

# --- Execution Block ---
if __name__ == "__main__":
    # Changed variable and class name for instantiation
    dorm_system = DormitoryCareTracker()
    dorm_system.start_program_loop()
