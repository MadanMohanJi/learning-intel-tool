import argparse
import json
import os
import pandas as pd
from src.model import Predictor
from src.insights import Generator
from src.processor import DataProcessor

def main():
    parser = argparse.ArgumentParser(description="AI Learning Intelligence Tool")
    parser.add_argument('--input', type=str, required=True, help="Path to input CSV")
    parser.add_argument('--output', type=str, default="report.json", help="Output JSON file name")
    args = parser.parse_args()

    # 0. Check if model exists before starting
    model_path = 'models/completion_model.joblib'
    if not os.path.exists(model_path):
        print(f"❌ Error: Model file '{model_path}' not found.")
        print("Please run 'python train_model.py' first to train the AI.")
        return

    try:
        # 1. Load Data
        processor = DataProcessor()
        raw_df = processor.load_data(args.input)
        print(f"--- Processing {len(raw_df)} rows of data ---")

        # 2. ML Prediction (Inference)
        predictor = Predictor(model_path=model_path)
        predictions_df = predictor.predict(raw_df)

        # 3. Insight Generation
        engine = Generator(raw_df)
        risky_students = engine.get_at_risk_students(predictions_df)
        difficulty_map = engine.get_chapter_difficulty()

        # 4. Construct Final Report
        report = {
            "summary": {
                "total_students_analyzed": int(len(predictions_df)),
                "at_risk_count": int(len(risky_students))
            },
            "risk_list": [int(x) for x in risky_students], # Ensure JSON serializable
            "chapter_insights": difficulty_map
        }

        # 5. Output results
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=4)
        
        print(f"✅ Analysis complete. Report saved to {args.output}")

    except Exception as e:
        print(f"❌ An error occurred during execution: {e}")

if __name__ == "__main__":
    main()