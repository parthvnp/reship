from transformers import DistilBertTokenizer, DistilBertModel
import torch
import numpy as np
from scipy.spatial.distance import cosine

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')


def get_embeddings(text: str) -> np.ndarray:
    """
    Get the embeddings for a given text using DistilBERT
    :argument text: The text to get the embeddings for
    :return: The embeddings for the text
    :rtype: numpy.ndarray
    """
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)

    embeddings = outputs.last_hidden_state[:, 0, :].numpy().reshape(-1)
    return embeddings


def semantic_similarity(job_description, bullet_point, threshold=0.5):
    """
    Check if the bullet point matches the job description using semantic similarity with DistilBERT.
    :param job_description: A job description bullet point
    :param bullet_point: A resume bullet point
    :param threshold: Threshold for the semantic similarity
    :return: True if the similarity is above the threshold, False otherwise
    """
    job_description_embedding = get_embeddings(job_description)
    bullet_point_embedding = get_embeddings(bullet_point)

    similarity = 1 - cosine(job_description_embedding, bullet_point_embedding)

    return similarity >= threshold
