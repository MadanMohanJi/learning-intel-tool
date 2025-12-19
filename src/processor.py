import pandas as pd
import os

class DataProcessor:
    def __init__(self):
        self.required_columns = ['student_id', 'course_id', 'chapter_order', 'time_spent', 'scores', 'completion_status']

    def load_data(self, file_path):
        # FIX: Convert the path to an absolute path
        abs_path = os.path.abspath(file_path)
        
        if not os.path.exists(abs_path):
            # This will print the EXACT location Python is looking at
            print(f"DEBUG: Python is looking here: {abs_path}")
            raise FileNotFoundError(f"Input file not found at: {abs_path}")
        
        return pd.read_csv(abs_path)

    def prepare_features(self, df):
        # Feature engineering logic
        features = df.groupby('student_id').agg({
            'time_spent': 'sum',
            'scores': 'mean',
            'chapter_order': 'max'
        })
        features.columns = ['total_time', 'avg_score', 'furthest_chapter']
        return features