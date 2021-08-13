#!/usr/bin/env python3

from survey import AnnonymusSurvey

question = 'date to gain independence?'
my_survey = AnnonymusSurvey(question)
my_survey.show_question()

print("Enter 'q' to exit survey")
while True:
    response = input("Input date: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)
print('Tkank you to everyone who participated in the survey')
my_survey.show_results()

