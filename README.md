Dormitory Care Tracker 🏥

So, here is the situation. The old way was a mess. We had manual logbooks everywhere. Papers getting lost. Coffee spills on medical records. It was bad. That is why the Dormitory Care Tracker exists. It is a robust Python CLI app. It fixes the chaos.

This system replaces the paper. It is a persistent digital storage solution.

📖 The Story

You are a warden. Or maybe a health officer. You need to manage student health records. Who is in which room? Who has a peanut allergy? You need this info fast. Especially in an emergency. The Tracker lets you record and retrieve this.

It saves everything to a file called student_wellness_data.json. It is a structured JSON format. The data is persistant. It stays there even if you close the window.

✨ What It Does

It’s pretty simple.

Data Entry: You log the details. Identity, accommodation, medical profiles. It asks, you type.

Auto-Persistence: It loads records when you start. It saves when you add. Automatic.

Search: You need to find "John"? Just type it. Or use a Student ID. It finds specific entrys instantly.

Summary Dashboard: A table. It shows everyone currently tracked.

Error Handling: It is robust. We use JSON serialization. No unsafe eval here. It handles missing files without crashing.

⚙️ Requirements

You just need Python 3.x.
No external packages. Standard library only.

🚀 Get It Running

Download the script. It is probably called project.py.
Open your terminal.
Go to the folder.
Type this:

python project.py


🖥️ Using The Thing

When it opens, you see a Main Menu. It looks official.

Submit New Health Data: Follow the prompts. Name, ID, Age. Then the dorm stuff. Block, Room No. Then medical. Blood group, allergies. Don't skip the important parts.

View Summary: It displays a clean table. All the students are listed there.

Search: Enter a name or ID. It shows the full details.

Close: Saves and quits.

🔒 Privacy Note

Listen. This data is stored locally. In that .json file.
If someone gets on your computer, they see the data. Restrict access to authorized personnel. Keep the student privacy safe.
