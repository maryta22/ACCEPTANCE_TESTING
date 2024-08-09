from behave import given, when, then
from todo_list import ToDoListManager

@given('the to-do list is empty')
def step_given_todo_list_is_empty(context):
    context.manager = ToDoListManager()
    context.manager.clear_list()

@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    context.manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_then_todo_list_should_contain_task(context, task):
    tasks = context.manager.list_tasks()
    task_names = [t["task"] for t in tasks]
    assert task in task_names, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    context.manager = ToDoListManager()
    for row in context.table:
        context.manager.add_task(row['Task'])
        if 'Status' in row and row['Status'] == "Completed":
            context.manager.mark_task_completed(row['Task'])

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.tasks = context.manager.list_tasks()

@then('the output should contain')
def step_then_output_should_contain(context):
    task_names = [row['Tasks'] for row in context.table]
    for task in task_names:
        assert task in [t["task"] for t in context.tasks], f'Task "{task}" not found in the output'

@then('the to-do list should contain only one "{task}"')
def step_then_todo_list_should_contain_only_one(context, task):
    tasks = context.manager.list_tasks()
    task_names = [t["task"] for t in tasks]
    assert task_names.count(task) == 1, f"Duplicate task '{task}' found in the to-do list"

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    try:
        context.manager.mark_task_completed(task)
        context.error_message = None
    except ValueError as e:
        context.error_message = str(e)

@then('the to-do list should show task "{task}" as completed')
def step_then_todo_list_should_show_task_completed(context, task):
    tasks = context.manager.list_tasks()
    for t in tasks:
        if t["task"] == task:
            assert t["status"] == "Completed", f'Task "{task}" is not marked as completed'
            return
    assert False, f'Task "{task}" not found in the to-do list'

@then('the system should return an error stating "{message}"')
def step_then_system_should_return_error(context, message):
    assert context.error_message == message, f"Expected error message '{message}', but got '{context.error_message}'"

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.manager.clear_list()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    tasks = context.manager.list_tasks()
    assert len(tasks) == 0, "The to-do list is not empty"
