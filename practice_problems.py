"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen_ids = set()
    for product_id in product_ids:
        if product_id in seen_ids:
            return True
        seen_ids.add(product_id)
    return False

#Testing
test_list_with_duplicates = [10, 20, 30, 20, 40]
print(f"Input: {test_list_with_duplicates}")
print(f"Output: {has_duplicates(test_list_with_duplicates)}")
print()


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: '{task}'")

    def remove_oldest_task(self):
        if not self.tasks:
            print("Queue is empty, no task to remove.")
            return None
        oldest_task = self.tasks.pop(0)
        print(f"Removed oldest task: '{oldest_task}'")
        return oldest_task
    

#Testing
print("--- Problem 2: Order Manager ---")
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.add_task("Write report")
print(f"Current tasks: {task_queue.tasks}")
print(f"Removed: {task_queue.remove_oldest_task()}")
print(f"Current tasks: {task_queue.tasks}")
print()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)
        print(f"Added value: {value}")

    def get_unique_count(self):
        return len(self.unique_values)
    
#Testing
print("--- Problem 3: Unique Value Counter ---")
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.add(30)
print(f"Unique values seen so far: {tracker.get_unique_count()}")
print()
