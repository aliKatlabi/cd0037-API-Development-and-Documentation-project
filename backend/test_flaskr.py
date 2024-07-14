import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
    
        self.database_name = "trivia_test"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format("postgres","alika",'localhost:5432', self.database_name)
        
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })

        self.client = self.app.test_client

        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
            self.new_question = {
                'id': 1,
                'question': 'what is the meaning of life',
                'answer': 'opt for speculations',
                'difficulty': 5,
                'category': 4
            }

            self.invalid_question = {
                'id': 1,
                'question': 'what is the meaning of life',
                'answer': None,
                'difficulty': 5,
                'category': 4
            }

            self.new_category = {
                'type': "some type"
            }

            self.invalid_category = {
                'type': None
            }

    def tearDown(self):
        """Executed after reach test"""
        pass

############ categories related ############

    def test_retrieve_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_get_category_question(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    def test_create_new_category(self):
        res = self.client().post('/categories', json=self.new_category)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
## FAILES 
    def test_get_category_question_fails(self):
        res = self.client().get('/categories/36/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_category_fails(self):
        res = self.client().post('/categories', json=self.invalid_category)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'request cannot be processed')

############ quizzes related ############
    def test_get_quiz(self):
        res = self.client().post('/quizzes',
                                 json={"previous_questions": [], "quiz_category": {'id': 2, 'type': 'Art'}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
## FAILES 
    def test_get_quiz_fails(self):
        res = self.client().post('/quizzes',
                                 json={"previous_questions": [], "quiz_category": {'id': 18, 'type': 'Invalid category'}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

############ Questions related ############
 
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))

    
    def test_delete_question(self):
        # to test delete 27,28,29
        id = 28
        res = self.client().delete(f'/questions/{id}')
        data = json.loads(res.data)

        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], id)


    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_search_term(self):
        res = self.client().post('/questions', json={"searchTerm": "What"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

## FAILES 
    def test_get_search_term_fails(self):
        res = self.client().post(
            '/questions', json={"invalidSearchTermKey": None})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'request cannot be processed')

    def test_get_paginated_questions_fails(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_question_fails(self):
        res = self.client().post('/questions', json=self.invalid_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'request cannot be processed')

    def test_delete_question_fails(self):
        res = self.client().delete('/questions/800')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


if __name__ == "__main__":
    unittest.main()