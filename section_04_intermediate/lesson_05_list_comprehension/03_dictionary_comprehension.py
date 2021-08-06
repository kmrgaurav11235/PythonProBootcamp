# Dictionary Comprehension
# new_dict = {new_key:new_value for item in iterable}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

valar_list = ["Manwe", "Varda", "Ulmo", "Aule", "Yavanna", "Orome", "Vana"]

valar_scores = {name: random.randint(1, 100) for name in valar_list}
print(f"Valar Scores: {valar_scores}")

passed_valar = {name:score for (name, score) in valar_scores.items() if score >= 60}
print(f"Passed Valar: {passed_valar}")