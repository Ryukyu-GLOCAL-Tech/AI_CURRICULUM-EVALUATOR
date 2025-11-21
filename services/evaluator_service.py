import re

def evaluate_answer(evaluator, question: str, answer: str):
    """
    Use the LLaMA evaluator to score a child's answer.

    Args:
        evaluator: Hugging Face pipeline object.
        question (str): The question asked.
        answer (str): Child's answer.

    Returns:
        str or None: Score in the format "X/10", or None if parsing fails.
    """
    prompt = f"""
    Question: {question}
    Child's Answer: {answer}

    Please give:
    - A score from 0 to 10
    Format your response as: Score: X/10
    """

    response = evaluator(prompt, max_new_tokens=200, do_sample=False)
    text = response[0]["generated_text"].strip()

    match = re.search(r"Score:\s*(\d{1,2}/10)", text)
    return match.group(1) if match else None

