#28.09.2018
'''
Testing w/o using the setUp() method: have to instantiate class/responses each time, not ideal
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
'''

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""
    def setUp(self):
        """
        Create a survey and a set of responsee for use in all test methods.
        """
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question) #instantiate class
        self.responses = ['English', 'Spanish', 'Mandarin'] #create list of responses to pull from
        
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0]) #from instance of my_survey, call store_response method, with index of the pre-built response list as the argument of new response
        self.assertIn(self.responses[0], self.my_survey.responses) #assert that that arg, index[0] of pre-built list, is in the list my_survery.responses (as in it got appended correctly)
        
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response) 
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            
        
unittest.main()
