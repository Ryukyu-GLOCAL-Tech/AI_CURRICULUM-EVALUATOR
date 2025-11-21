import os
import pandas as pd
from services.evaluator_service import evaluate_answer
from models.llama_model import load_llama_model
from utils.file_utils import ensure_directory

os.environ["TRANSFORMERS_VERBOSITY"] = "info"


def main():
    """Main entry point: load model, evaluate answers, save results."""
    evaluator = load_llama_model()

    input_file = 'datasets/children_answers.csv'
    output_file = 'results/child_answers_evaluated.csv'

    # Ensure output directory exists
    ensure_directory("results")

    # Load CSV
    df = pd.read_csv(input_file)

    # Evaluate answers
    df['Score'] = [
        evaluate_answer(evaluator, row['question'], row['answer'])
        for _, row in df.iterrows()
    ]

    # Save results
    df.to_csv(output_file, index=False)
    print(f"✔ Evaluation complete! Saved to {output_file}")


if __name__ == "__main__":
    main()

