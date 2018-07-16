import core
import pytest
from unittest.mock import patch


class TestUniversityMember:

    def test_class_Member_should_exist(self):
        assert isinstance(core.Member, type)

    def test_Member_init_should_be_implemented(self):
        m = core.Member('a', 'b', 'c')
        assert m.name == 'a'
        assert m.address == 'b'
        assert m.email == 'c'

@pytest.mark.skip
class TestUniversityFaculty:

    def test_class_Faculty_should_exist(self):
        assert isinstance(core.Faculty, type)

    def test_class_Faculty_should_inherit_from_Member(self):
        assert issubclass(core.Faculty, core.Member)

    @patch('core.Member.__init__')
    def test_Faculty_init_calls_super_init(self, init):
        f = core.Faculty(1, 2, 3, 4)
        init.assert_called_with(1, 2, 3)

    def test_Faculty_init_sets_up_faculty_attributes(self):
        f = core.Faculty(1, 2, 3, 4)
        assert f.faculty_number == 4
        assert f.courses_teaching == []

@pytest.mark.skip
class TestUniversityStudent:

    def test_class_Student_should_exist(self):
        assert isinstance(core.Student, type)

    def test_class_Student_should_inherit_from_Member(self):
        assert issubclass(core.Student, core.Member)

    @patch('core.Member.__init__')
    def test_Student_init_calls_super_init(self, init):
        s = core.Student(1, 2, 3, 4)
        init.assert_called_with(1, 2, 3)

    def test_Student_init_sets_up_student_attributes(self):
        s = core.Student(1, 2, 3, 4)
        assert s.student_number == 4
        assert s.courses_taken == []
        assert s.courses_taking == []

@pytest.mark.skip
class TestUniversityStringOverride:

    def test_Member_str_should_be_implemented(self):
        m = core.Member('nate', 'nate home', 'nate email')
        assert str(m) == 'nate\nnate home\nnate email'

    @patch('core.Member.__str__')
    def test_Faculty_str_calls_super_str(self, super_str):
        super_str.return_value = ''
        f = core.Faculty(1, 2, 3, 4)
        str(f)
        super_str.assert_called_with()

    def test_Faculty_str_correct_for_paul(self):
        f = core.Faculty('Paul Gries', 'Ajax', 'pgries@cs.toronto.edu', '1234')
        assert str(f) == '''Paul Gries
Ajax
pgries@cs.toronto.edu
1234
Courses: '''