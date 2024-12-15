# solution_task_729.py
class SolutionTask729:
    @staticmethod
    def add_list(list1, list2):
        return [x + y for x, y in zip(list1, list2)]

add_list = SolutionTask729.add_list
