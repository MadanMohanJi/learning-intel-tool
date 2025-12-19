import os
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from src.processor import DataProcessor

def ensure_data_exists(data_path):
    """Creates the data folder and file if they are missing."""
    if not os.path.exists(data_path):
        print(f"⚠️ Data not found at {data_path}. Creating synthetic data now...")
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        
        # Create a small sample dataset so the model can train
        data = {
            'student_id': list(range(1, 21)) * 2,
            'course_id': [101] * 40,
            'chapter_order': [1] * 20 + [2] * 20,
            'time_spent': np.random.randint(20, 150, 40),
            'scores': np.random.randint(30, 100, 40),
            'completion_status': np.random.randint(0, 2, 40)
        }
        pd.DataFrame(data).to_csv(data_path, index=False)
        print(f"✅ Created: {data_path}")

def train():
    # 1. SETUP ABSOLUTE PATHS
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, 'data', 'student_data.csv')
    MODEL_DIR = os.path.join(BASE_DIR, 'models')
    MODEL_PATH = os.path.join(MODEL_DIR, 'completion_model.joblib')

    # 2. SELF-HEALING: Ensure data exists before proceeding
    ensure_data_exists(DATA_PATH)

    # 3. LOAD & PREPROCESS
    try:
        df = pd.read_csv(DATA_PATH)
        processor = DataProcessor()
        features = processor.prepare_features(df)
        
        # Target: Completion status of the student
        target = df.groupby('student_id')['completion_status'].last()

        # 4. TRAIN MODEL
        print("⏳ Training AI Model (Random Forest)...")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(features, target)

        # 5. SAVE MODEL
        os.makedirs(MODEL_DIR, exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        print(f"✅ SUCCESS: Model saved at {MODEL_PATH}")

    except Exception as e:
        print(f"❌ Error during training: {e}")

if __name__ == "__main__":
    train()