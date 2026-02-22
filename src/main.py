import json
from pathlib import Path
from src.rag_agent import create_simple_rag_agent
from src.evaluation import evaluate_responses
from src.config import TESTSET_PATH

def main():
    # Load test set
    with open(TESTSET_PATH, encoding="utf-8") as f:
        test_cases = json.load(f)

    print(f"Loaded Ssensoft inc {len(test_cases)} test questions.\n")

    # Create your agent (replace with real RAG implementation)
    agent = create_simple_rag_agent()

    # Evaluate
    scores = evaluate_responses(agent, test_cases)

    # Print nice summary
    print("\n" + "="*60)
    print("EVALUATION RESULTS")
    print("="*60)
    for metric, value in scores.items():
        print(f"{metric:22} : {value:.4f}")
    print("="*60)

    # Optional: save to file
    output_path = Path("evaluation_results.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({k: float(v) for k, v in scores.items()}, f, indent=2)
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()