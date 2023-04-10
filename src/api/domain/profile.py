class Profile:
    """
    A profile is a collection of information about a person that can be used to generate a resume to match a job
    listing.
    """

    def __init__(self, employment_history=None, education_history=None, skills=None):
        self.employment_history = employment_history if employment_history else []
        self.education_history = education_history if education_history else []
        self.skills = skills if skills else []

    def get_full_context(self):
        full_context = self.employment_history + self.education_history + self.skills
        return ' '.join(full_context)
