import os
import pandas as pd

def force_create_data():
    # 1. Get the exact folder this script is in
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_path, "data")
    file_path = os.path.join(data_dir, "student_data.csv")

    # 2. Create the directory if it's missing
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    # 3. Define the data
    data = {
        'student_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        'course_id': [101]*10,
        'chapter_order': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        'time_spent': [45, 50, 120, 130, 40, 35, 110, 150, 30, 40],
        'scores': [85, 80, 30, 25, 90, 95, 20, 15, 88, 92],
        'completion_status': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    }

    # 4. Save it
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    
    # 5. Verification Check
    if os.path.exists(file_path):
        print("\n" + "="*30)
        print("✅ SUCCESS! FILE CREATED")
        print(f"LOCATION: {file_path}")
        print("="*30)
        print("\nTop 5 rows of your data:")
        print(df.head())
    else:
        print("❌ FAILED. Something is blocking the file creation.")

if __name__ == "__main__":
    force_create_data()