# Copy this into a `recipe.md` in your project and fill it out.

# ## 1. Describe the Problem

As a user, so that I can keep track of my tasks, I would like to check if a text includes the string `#TODO`.

So sort a list of tasks by urgency, marked by 'TODO'

# 2. Design the Function Signature

def list_sort(list_input):
    seperate the list into strings
    check those strings for TODO

    return a second list of TODO tasks


# ## 3. Create Examples as Tests
Example1:

list = ['first_task#TODO', 'second_task#TODO', 'third_task#completed', 'fourth_task#completed']

return = ['first_task#TODO', 'second_task#TODO']


Example2:

list = ['first_task#completed', 'second_task#completed', 'third_task#completed', 'fourth_task#completed']

return = []


Example3:

list = ['first_task#TODO', 'second_task#TODO', 'third_task#TODO', 'fourth_task#TODO']

return the whole list


# ## 4. Implement the Behaviour

