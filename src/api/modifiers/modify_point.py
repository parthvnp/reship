from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from typing import List


def modify_bullet_point(job_bullet_point: str, resume_bullet_point: str, model_name: str = 't5-base',
                        num_alternatives: int = 3) -> List[str]:
    """
    Modify the resume bullet point to match the job description bullet point using T5
    :param job_bullet_point: A job description bullet point
    :param resume_bullet_point: A resume bullet point
    :param model_name: The model to use for resume bullet point modification
    :param num_alternatives: Number of alternatives to generate for a given a job description
    :return: A list of modified resume bullet points that match the job description and resume bullet point
    """
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    input_text = f"Rewrite the resume bullet point: '{resume_bullet_point}' to match the job description bullet point: '{job_bullet_point}'"
    inputs = tokenizer(input_text, return_tensors='pt', padding=True, truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            num_return_sequences=num_alternatives,
            max_length=128,
            temperature=1.0,
            top_k=50,
            top_p=1.0,
        )

    modified_bullet_points = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return modified_bullet_points
