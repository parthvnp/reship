import os

from domain.profile import Profile
from domain.resume import ResumeBulletPoint
from matchers.semantic_match import semantic_similarity
import openai


def generate_new_bullet_point(job_bullet_point: str, profile: Profile, model_name: str = 'gpt-3.5-turbo',
                              num_alternatives: int = 3):
    """
    Generate new bullet points for a resume based on a job description bullet point and a profile.
    :param job_bullet_point: The job description bullet point
    :param profile: The profile context for the resume
    :param model_name: The name of the model to use for generating the bullet points
    :param num_alternatives: The number of alternative bullet points to generate
    :return: A list of tuples containing the new bullet point and its score
    """

    openai.api_key = os.environ.get("OPENAI_API_KEY")

    resume_context = profile.get_full_context()
    input_text = f"Based on the job description bullet point: '{job_bullet_point}', " \
                 f"and considering the resume context: '{resume_context}', " \
                 f"create {num_alternatives} alternative resume bullet points:"

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system",
             "content": "You are an AI that helps users create resume bullet points based on a "
                        "given job description bullet point and their resume context."},
            {"role": "user", "content": input_text},
        ],
        max_tokens=1024,
        n=num_alternatives,
        stop=None,
        temperature=1.0,
        top_p=1.0,
    )

    new_bullet_points = [choice.message["content"] for choice in response.choices]

    scored_bullet_points = []
    for point in new_bullet_points:
        score = semantic_similarity(job_bullet_point, point)  # Replace with your semantic similarity function
        scored_bullet_points.append((ResumeBulletPoint(point, context=resume_context), score))

    return scored_bullet_points

