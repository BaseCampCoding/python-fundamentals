import core
import pytest


class TestAtom:
    def test_class_Atom_should_exist(self):
        assert isinstance(core.Atom, type)

    def test_Atom_init_is_implemented(self):
        atom = core.Atom(1, 2, 3, 4, 5)
        assert atom.number == 1
        assert atom.center == (3, 4, 5)
        assert atom.symbol == 2

    def test_Atom_str_is_implemented(self):
        atom = core.Atom(1, 2, 3, 4, 5)
        assert str(atom) == '(2, 3, 4, 5)'

    def test_Atom_repr_is_implemented(self):
        atom = core.Atom(1, 2, 3, 4, 5)
        assert repr(atom) == 'Atom(1, "2", 3, 4, 5)'

    def test_Atom_translate_is_implemented(self):
        atom = core.Atom(1, 2, 3, 4, 5)
        atom.translate(1, 2, 3)
        assert atom.center == (4, 6, 8)


class TestMolecule:
    def test_class_Molecule_should_exist(self):
        assert isinstance(core.Molecule, type)

    def test_Molecule_init_is_implemented(self):
        m = core.Molecule('AMMONIA')
        assert m.name == 'AMMONIA'
        assert m.atoms == []

    def test_add_is_implemented(self):
        atom = core.Atom(1, 'N', 0.257, -0.363, 0.000)
        m = core.Molecule('AMMONIA')
        m.add(atom)
        assert m.atoms == [atom]

    def test_Molecule_str_is_implemented(self):
        m = core.Molecule('AMMONIA')
        m.add(core.Atom(1, "N", 0.257, -0.363, 0.0))
        m.add(core.Atom(2, "H", 0.257, 0.727, 0.0))
        m.add(core.Atom(3, "H", 0.771, -0.727, 0.890))
        m.add(core.Atom(4, "H", 0.771, -0.727, -0.890))
        assert str(m) == ('(AMMONIA, '
                          '((N, 0.257, -0.363, 0.0), '
                          '(H, 0.257, 0.727, 0.0), '
                          '(H, 0.771, -0.727, 0.89), '
                          '(H, 0.771, -0.727, -0.89)))')

    def test_Molecule_repr_is_implemented(self):
        m = core.Molecule('AMMONIA')
        m.add(core.Atom(1, "N", 0.257, -0.363, 0.0))
        m.add(core.Atom(2, "H", 0.257, 0.727, 0.0))
        m.add(core.Atom(3, "H", 0.771, -0.727, 0.890))
        m.add(core.Atom(4, "H", 0.771, -0.727, -0.890))
        assert repr(m) == ('Molecule("AMMONIA", '
                           '(Atom(1, "N", 0.257, -0.363, 0.0), '
                           'Atom(2, "H", 0.257, 0.727, 0.0), '
                           'Atom(3, "H", 0.771, -0.727, 0.89), '
                           'Atom(4, "H", 0.771, -0.727, -0.89)))')
