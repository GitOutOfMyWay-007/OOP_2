# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
#              " you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament,"
#              "you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# List of dictionaries with same key{text} for ques text and answer{answer}


# This is the basic syntax which is being followed to create the above dicts inside a list
#     # Creating a list of dictionaries
#     list_of_dicts = [
#         {"key1": "value1", "key2": "value2"},
#         {"key3": "value3", "key4": "value4"},
#         # Add more dictionaries as needed
#     ]

# we want this question data to be in the main.py file but in form of list of dictionaries
# but as a form of list of question objects.

question_data = [
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Sound can travel through a vacuum.", "correct_answer": "False",
     "incorrect_answers": ["True"]
     },
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "The Neanderthals were a direct ancestor of modern humans.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Scientists accidentally killed the once known world&#039;s oldest living creature, a mollusc, known to be aged as 507 years old.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "A defibrillator is used to start up a heartbeat once a heart has stopped beating.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "The most frequent subconscious activity repeated by the human body is blinking.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Anatomy considers the forms of macroscopic structures such as organs and organ systems.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "In the periodic table, Potassium&#039;s symbol is the letter K.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "The &quot;Gympie Stinger&quot; is the deadliest plant in the world.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "A person can get sunburned on a cloudy day.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "&quot;Tachycardia&quot; or &quot;Tachyarrhythmia&quot; refers to a resting heart-rate near or over 100 BPM.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "The Doppler effect applies to light.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "The planet Mars has two moons orbiting it.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Shrimp can swim backwards.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Hippopotomonstrosesquippedaliophobia is the irrational fear of long words.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]
