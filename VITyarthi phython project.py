import os
from datetime import datetime

class HostelHealthSystem:
    def __init__(self):
        self.data_file = "health_records.txt"
        self.records = self.load_records()

    def load_records(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    content = f.read()
                    if content.strip():
                        return eval(content)
            except:
                pass
        return []

    def save_records(self):
        with open(self.data_file, 'w') as f:
            f.write(str(self.records))

    def collect_health_record(self):
        print("\n" + "="*50)
        print("     HOSTEL HEALTH RECORD")
        print("="*50 + "\n")

        print("BASIC INFORMATION")
        print("-" * 30)
        name = input("Student Name: ").strip()
        reg_id = input("Registration ID: ").strip()
        age = input("Age: ").strip()
        contact = input("Contact Number: ").strip()

        print("\nROOM DETAILS")
        print("-" * 30)
        block = input("Block: ").strip()
        room_no = input("Room Number: ").strip()
        room_type = input("Room Type (Single/Double/Triple/Four): ").strip()

        print("\nHEALTH INFORMATION")
        print("-" * 30)
        blood_group = input("Blood Group (A+/B+/O+/AB+ etc.): ").strip()
        current_disease = input("Current Disease (if any, or press Enter): ").strip()
        allergies = input("Any Allergies? (or press Enter): ").strip()
        medications = input("Current Medications? (or press Enter): ").strip()

        print("\nDOCTOR CONSULTATION")
        print("-" * 30)
        doctor_visited = input("Visited Doctor Recently? (yes/no): ").strip().lower()
        doctor_name = ""
        if doctor_visited == "yes":
            doctor_name = input("Doctor's Name: ").strip()

        hospital_visited = input("Visited Hospital Recently? (yes/no): ").strip().lower()
        hospital_name = ""
        if hospital_visited == "yes":
            hospital_name = input("Hospital Name: ").strip()

        record = {
            "record_id": f"HR{len(self.records) + 1:04d}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": name, "reg_id": reg_id, "age": age, "contact": contact,
            "block": block, "room_no": room_no, "room_type": room_type,
            "blood_group": blood_group,
            "current_disease": current_disease if current_disease else "None",
            "allergies": allergies if allergies else "None",
            "medications": medications if medications else "None",
            "doctor_visited": doctor_visited, "doctor_name": doctor_name,
            "hospital_visited": hospital_visited, "hospital_name": hospital_name
        }
        return record

    def display_record(self, record):
        print("\n" + "="*50)
        print(f"     RECORD: {record['record_id']}")
        print("="*50)
        print(f"Date: {record['date']}")
        print(f"\nName: {record['name']}")
        print(f"Registration ID: {record['reg_id']}")
        print(f"Age: {record['age']}")
        print(f"Contact: {record['contact']}")
        print(f"\nBlock: {record['block']}")
        print(f"Room Number: {record['room_no']}")
        print(f"Room Type: {record['room_type']}")
        print(f"\nBlood Group: {record['blood_group']}")
        print(f"Current Disease: {record['current_disease']}")
        print(f"Allergies: {record['allergies']}")
        print(f"Medications: {record['medications']}")
        print(f"\nDoctor Visited: {record['doctor_visited']}")
        if record['doctor_name']:
            print(f"Doctor Name: {record['doctor_name']}")
        print(f"Hospital Visited: {record['hospital_visited']}")
        if record['hospital_name']:
            print(f"Hospital Name: {record['hospital_name']}")
        print("="*50 + "\n")

    def search_record(self, search_term):
        results = []
        search_lower = search_term.lower()
        for record in self.records:
            if (search_lower in record['name'].lower() or 
                search_lower in record['reg_id'].lower()):
                results.append(record)
        return results

    def list_all_records(self):
        if not self.records:
            print("\nNo records found.")
            return
        
        print("\n" + "="*70)
        print("                    ALL HEALTH RECORDS")
        print("="*70)
        print(f"{'ID':<10} {'Name':<20} {'Reg ID':<15} {'Room':<15}")
        print("-"*70)
        
        for record in self.records:
            rid = record['record_id']
            name = record['name'][:18]
            reg = record['reg_id'][:13]
            room = f"{record['block']}-{record['room_no']}"
            print(f"{rid:<10} {name:<20} {reg:<15} {room:<15}")
        
        print("="*70)
        print(f"Total Records: {len(self.records)}\n")

    def run_menu(self):
        while True:
            print("\n" + "="*50)
            print("     HOSTEL HEALTH SYSTEM - MENU")
            print("="*50)
            print("1. Add New Record")
            print("2. View All Records")
            print("3. Search Record")
            print("4. Exit")
            print("="*50)
            
            choice = input("\nYour choice (1-4): ").strip()
            
            if choice == "1":
                record = self.collect_health_record()
                self.records.append(record)
                self.save_records()
                self.display_record(record)
                print("Record saved successfully!")
            elif choice == "2":
                self.list_all_records()
            elif choice == "3":
                search_term = input("\nEnter name or ID to search: ").strip()
                results = self.search_record(search_term)
                if results:
                    print(f"\nFound {len(results)} record(s):")
                    for record in results:
                        self.display_record(record)
                else:
                    print("\nNo records found.")
            elif choice == "4":
                print("\nThank you for using the system!")
                break
            else:
                print("\nInvalid choice. Please enter 1-4.")

if __name__ == "__main__":
    system = HostelHealthSystem()
    system.run_menu()