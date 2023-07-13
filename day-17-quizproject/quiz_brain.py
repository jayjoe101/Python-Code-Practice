class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        """returns true or false if question list still has questions"""
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        """returns current question and increments question number for next question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return current_question