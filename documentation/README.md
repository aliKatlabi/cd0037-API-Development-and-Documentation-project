# API DOCUMENTATION FOR TRIVIA API


`GET '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

---
### Paginated Questions

`GET '/questions?page=${integer}'`

- Fetches a paginated set of questions, along with the total number of questions, all available categories, and the current category string.
- Request Arguments: `page` (integer)
- Returns: 

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 2
    }
  ],
  "totalQuestions": 100,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": "History"
}
```

---
### Questions by Category

`GET '/categories/${id}/questions'`

- Retrieves questions for a specific category based on the provided category ID.
- Request Arguments: `id` (integer)
- Returns: An object with questions for the specified category, total questions, and current category string

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 4
    }
  ],
  "totalQuestions": 100,
  "currentCategory": "History"
}
```

---
### Delete a Question

`DELETE '/questions/${id}'`

- Deletes a specified question using the question ID.
- Request Arguments: `id` (integer)
- Returns: No specific data; only the appropriate HTTP status code.

---
### Get Next Quiz Question

`POST '/quizzes'`

- Sends a post request to get the next quiz question.
- Request Body:

```json
{
    "previous_questions": [1, 4, 20, 15],
    "quiz_category": "current category"
 }
```

- Returns: a single new question object

```json
{
  "question": {
    "id": 1,
    "question": "question",
    "answer": "answer",
    "difficulty": 5,
    "category": 4
  }
}
```

---
### Add a New Question

`POST '/questions'`

- Sends a post request to add a new question.
- Request Body:

```json
{
  "question": "new question",
  "answer": "new answer",
  "difficulty": 3,
  "category": 4
}
```

- Returns: No specific data returned.

---

---
### Add a New Category

`POST '/categories'`

- Sends a post request to add a new Category.
- Request Body:

```json
{
  "type": "science"
}
```

- Returns: No specific data returned.

---

### Search for Questions

`POST '/questions'`

- Searches for questions based on a specified search term.
- Request Body:

```json
{
  "searchTerm": "this is the term the user is looking for"
}
```

- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 5
    }
  ],
  "total_questions": 100,
  "currentCategory": "Entertainment"
}
```

## SAMPLE CURL REQUEST 

```bash
curl http://127.0.0.1:5000/questions
````

```bash
curl -X GET  http://127.0.0.1:5000/questions/search?search=What
````


```bash
curl -X DELETE http://127.0.0.1:5000/questions/23
````

```bash
curl -X POST -H "Content-Type: application/json" -d "{'answer': 'news','category': 3,'difficulty': 3, 'id': 15,'question': 'question?'}" http://127.0.0.1:5000/questions 
````

