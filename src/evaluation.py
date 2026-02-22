from typing import List, Dict, Any
from tqdm import tqdm
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
    answer_correctness
)
from datasets import Dataset
from langchain_core.runnables import Runnable

def prepare_ragas_dataset(
        questions: List[str],
        answers: List[str],
        ground_truths: List[str],
        contexts: List[List[str]] = None
) -> Dataset:
    """Minimal dataset for ragas evaluation"""
    if contexts is None:
        # If you don't have real contexts, use empty list or fake one
        contexts = [[""] for _ in questions]

    return Dataset.from_dict({
        "question": questions,
        "answer": answers,
        "ground_truth": ground_truths,
        "contexts": contexts,
    })


def evaluate_responses(agent: Runnable, test_cases: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Run agent on all questions and evaluate with ragas
    """
    questions = []
    ground_truths = []
    answers = []
    contexts = []  # ← you can collect real contexts if your agent returns them

    print("Running agent on test questions...")

    for case in tqdm(test_cases):
        q = case["question"]
        gt = case["ground_truth"]

        try:
            response = agent.invoke({"question": q})
            if isinstance(response, dict) and "answer" in response:
                answer = response["answer"]
            else:
                answer = str(response).strip()
        except Exception as e:
            print(f"Error on question '{q}': {e}")
            answer = ""

        questions.append(q)
        ground_truths.append(gt)
        answers.append(answer)
        contexts.append([])  # ← add real context retrieval if possible

    dataset = prepare_ragas_dataset(questions, answers, ground_truths, contexts)

    print("\nRunning RAGAS evaluation...")
    result = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            answer_correctness,
            # context_precision,  # only if you have real contexts
            # context_recall,
        ]
    )

    return result