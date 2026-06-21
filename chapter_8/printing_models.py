unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until none left"""
    """Move each design to completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing: {current_design.title()}")
        completed_models.append(current_design.title())

def show_completed_models(completed_models):
    """Show all completed models"""
    print("\nThe following models have been completed: ")
    for completedModel in completed_models:
        print(completedModel)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)