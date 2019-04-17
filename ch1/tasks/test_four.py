"""Test the Task data type."""

from collections import namedtuple, OrderedDict

Task = namedtuple('Task',['summary', 'owner','done','id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task()
    t_dict = t_task._asdict()

    assert type(t_dict) == OrderedDict

def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10,done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected

def test_include_summary():
    """A task created with default args should have all fields, with
    correct field names """
    t_task = Task()
    t_dict = t_task._asdict()
    for field in ['summary', 'owner', 'done', 'id']:
        assert field in t_dict

def test_no_extra_fields():
    """A task created with defaults should not have extra fields"""
    t_task = Task()
    t_dict = t_task._asdict()
    assert len(t_dict) <= 4

def test_create_two_independent_tasks():
    """Two independent tasks, with different fields, should not leak field"""
    task1 = Task("print book","Fabio",True,1)
    task2 = Task("buy book", "Elisa", False, 2)

    assert task1.summary != task2.summary
