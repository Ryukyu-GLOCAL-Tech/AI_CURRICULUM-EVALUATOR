from transformers import pipeline
from config import HF_TOKEN


def load_llama_model():
    model_name = "meta-llama/Llama-3.1-8B-Instruct"

    evaluator = pipeline(
        task="text-generation",
        model=model_name,
        device_map="auto",
        torch_dtype="auto",
        token=HF_TOKEN,
    )
    
    print(f"✔ Loaded model: {model_name}")
    return evaluator

