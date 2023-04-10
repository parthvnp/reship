from domain.job_listing import JobDescriptionBulletPoint
from domain.profile import Profile
from modifiers.generate_point import generate_new_bullet_point
from dotenv import load_dotenv

load_dotenv()

employment_history = [
    "Managed a team of 5 software developers to create web-based solutions.",
    "Developed and maintained a Django web application for a large e-commerce company."
]

education_history = [
    "Bachelor's degree in Computer Science from ABC University.",
]

skills = [
    "Proficient in Python, Django, and JavaScript.",
    "Experienced with database design and optimization."
]

profile = Profile(employment_history, education_history, skills)

job_bullet_point = JobDescriptionBulletPoint(
    "Design and implement single page applications using React and Redux.")

scored_bullet_points = generate_new_bullet_point(job_bullet_point.text, profile, num_alternatives=3)
for i, (bullet_point, score) in enumerate(scored_bullet_points):
    print(f"Alternative {i + 1}: {bullet_point} (Score: {score:.2f})")
