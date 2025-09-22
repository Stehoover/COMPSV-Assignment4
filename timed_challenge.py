# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
# 10. Remove by Value
# Remove the first occurrence of a given value from a sequence.
# Input: [10, 20, 30, 20], Remove 20
# Output: [10, 30, 20]

def remove_first_occurrence(lst, value_to_remove):
    try:
        index_to_remove = lst.index(value_to_remove)
        # Create a new list without found number
        return lst[:index_to_remove] + lst[index_to_remove+1:]
    except ValueError:
       # Returns Orignal list if value not found
        print(f"Value '{value_to_remove}' not found in the list.")
        return lst
    

#Testing
original_list = [10, 20, 30, 20, 50, 60, 20 ,22, 13]
value_to_remove = 20
new_list = remove_first_occurrence(original_list, value_to_remove)
print(f"Original list: {original_list}")
print(f"Value to remove: {value_to_remove}")
print(f"New list: {new_list}")

print("-" * 20)