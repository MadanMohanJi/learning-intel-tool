import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from src.processor import DataProcessor

def train():
    # 1. Setup Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, 'data', 'student_data.csv')
    MODEL_DIR = os.path.join(BASE_DIR, 'models') # Define the folder
    MODEL_PATH = os.path.join(MODEL_DIR, 'completion_model.joblib')
    
    print(f"Reading data from: {DATA_PATH}")
    
    # 2. Load & Train
    df = pd.read_csv(DATA_PATH)
    processor = DataProcessor()
    features = processor.prepare_features(df)
    target = df.groupby('student_id')['completion_status'].last()

    print("⏳ Training the AI model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(features, target)

    # 3. SAVE (The Fix is here!)
    # This line forces the computer to create the 'models' folder if it doesn't exist
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
        print(f"📁 Created missing folder: {MODEL_DIR}")

    joblib.dump(model, MODEL_PATH)
    print("✅ SUCCESS: AI Model trained and saved!")

if __name__ == "__main__":
    train()
    