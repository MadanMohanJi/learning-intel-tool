import os

# Get the exact path of this folder
current_location = os.getcwd()
print(f"\n--- TERMINAL LOCATION ---")
print(current_location)

print(f"\n--- FILES SEEN BY PYTHON ---")
files = os.listdir()
for f in files:
    print(f"- {f}")

# Check if 'data' folder exists
if os.path.exists('data'):
    print(f"\n--- INSIDE 'DATA' FOLDER ---")
    print(os.listdir('data'))
else:
    print(f"\n❌ 'data' folder NOT FOUND in this location.")