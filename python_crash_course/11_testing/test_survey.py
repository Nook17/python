#!/usr/bin/env python3

import unittest
from survey import AnnonymusSurvey

class TestAnnonymusSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = 'date to gain independence'
        my_survey = AnnonymusSurvey(question)
        my_survey.store_response('1914')
        self.assertIn('1914', my_survey.responses)

if __name__ == '__main__':
    unittest.main()

