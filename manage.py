import os
import shutil

keyword_to_week = {
    'phonebook': 'Week 21',
    'fileio': 'Week 21',
    'exception': 'Week 21',
    'json': 'Week 22',
    'api': 'Week 22',
    'random': 'Week 22',
    'slot': 'Week 22',
    'module': 'Week 23',
    'organizer': 'Week 23',
    'venv': 'Week 23',
    'git': 'Week 23',
    'oop': 'Week 24',
    'fastapi': 'Week 24',
    'sqlite': 'Week 25',
    'sqlalchemy': 'Week 25',
}

base_dir = os.getcwd()
script_name = os.path.basename(__file__)  # current script name

# Create folders
for week in set(keyword_to_week.values()):
    os.makedirs(os.path.join(base_dir, week), exist_ok=True)

# Move matching files (but not the script itself)
for filename in os.listdir(base_dir):
    if filename.endswith('.py') and filename != script_name:
        matched = False
        for keyword, week in keyword_to_week.items():
            if keyword.lower() in filename.lower():
                shutil.move(
                    os.path.join(base_dir, filename),
                    os.path.join(base_dir, week, filename)
                )
                print(f"✅ Moved {filename} → {week}")
                matched = True
                break
        if not matched:
            print(f"⚠️ Skipped {filename}: No keyword match")
