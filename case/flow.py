from models import CaseFoo, CaseCorge

from rules import foo_to_corge

FLOW = {
    'foo_activity': {
        'name': 'Foo Activity',
        'model': CaseFoo,
        'role': 'Submitter',
        'transitions': {
            'corge_activity': foo_to_corge,
        }
    },
    'corge_activity': {
        'name': 'Corge Activity',
        'model': CaseCorge,
        'role': 'Reviewer',
        'transitions': None
    }
}

INITIAL = 'foo_activity'

TITLE = 'Test Workflow'
DESCRIPTION = 'Description of workflow goes here'