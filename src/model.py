import joblib
import pandas as pd
# Import the class directly from the processor module
from src.processor import DataProcessor 

class Predictor:
    def __init__(self, model_path):
        try:
            self.model = joblib.load(model_path)
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None
        self.processor = DataProcessor()

    def predict(self, df):
        if self.model is None:
            raise Exception("AI Model not found in models/ folder. Run train_model.py first.")
            
        features = self.processor.prepare_features(df)
        predictions = self.model.predict(features)
        
        results = pd.DataFrame({
            'student_id': features.index,
            'will_complete': predictions
        })
        return results