# Reship

This project aims to help users optimize their resumes for specific job descriptions. It uses natural language
processing techniques and the OpenAI API to parse job descriptions, compare them with existing resume bullet points, and
generate new or modified bullet points to better match the job requirements.
Features

- Parsing job descriptions to extract keywords
- Rewriting existing resume bullet points to fit job descriptions
- Generating new bullet points based on job descriptions and user's profile context
- Scoring bullet points based on semantic similarity to job description
- Creating a simple Applicant Tracking System (ATS) for resume scanning and rating

## Usage

1. Create a Profile object with the user's employment history, education history, and skills
2. Parse a job description using the JobDescriptionParser and store the result in a JobDescription object
3. Compare existing resume bullet points with the job description using generate_modified_bullet_points
4. Generate new bullet points if needed using generate_new_bullet_point
5. Score the modified and new bullet points with score_bullet_points
6. Use the results to optimize the user's resume for the specific job description

## Requirements

1. Python 3.10 or later
2. beautifulsoup4 and requests packages for parsing job descriptions
3. An OpenAI API key for using GPT-3 or other compatible models