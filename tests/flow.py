""" Test Flow Definition"""

from models import Foo, Corge

from rules import foo_to_corge

FLOW = {
    'foo_activity': {
        'name': 'Foo Activity',
        'model': Foo,
        'role': 'Submitter',
        'transitions': {
            'corge_activity': foo_to_corge,
        }
    },
    'corge_activity': {
        'name': 'Corge Activity',
        'model': Corge,
        'role': 'Reviewer',
        'transitions': None
    }
}

INITIAL = 'foo_activity'

TITLE = 'Test Workflow'
DESCRIPTION = 'Description of workflow goes here'
