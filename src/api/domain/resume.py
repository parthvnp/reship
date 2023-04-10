class ResumeBulletPoint:
    def __init__(self, text, context=None):
        self.text = text
        self.context = context if context else ""

    def __str__(self):
        return self.text
