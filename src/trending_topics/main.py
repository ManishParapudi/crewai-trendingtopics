#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from trending_topics.crew import TrendingTopics

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'subject': 'Airlines',
        'date': str(datetime.now().date())
    }
    
    try:
        result = TrendingTopics().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    

if __name__ == "__main__":
    run()