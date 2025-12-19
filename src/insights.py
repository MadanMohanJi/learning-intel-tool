import pandas as pd

class Generator:
    def __init__(self, df):
        self.df = df

    def get_at_risk_students(self, predictions_df):
        # Identify students predicted to drop out (0)
        predicted_drops = predictions_df[predictions_df['will_complete'] == 0]['student_id'].tolist()
        
        # Identify students with scores below 45% (Heuristic risk)
        avg_scores = self.df.groupby('student_id')['scores'].mean()
        low_scorers = avg_scores[avg_scores < 45].index.tolist()
        
        # Combine lists and remove duplicates
        return list(set(predicted_drops + low_scorers))

    def get_chapter_difficulty(self):
        # Difficulty = Average Time / Average Score
        chapters = self.df.groupby('chapter_order').agg({
            'scores': 'mean',
            'time_spent': 'mean'
        })
        
        chapters['difficulty_score'] = (chapters['time_spent'] / (chapters['scores'] + 1)) * 10
        return chapters['difficulty_score'].round(2).to_dict()