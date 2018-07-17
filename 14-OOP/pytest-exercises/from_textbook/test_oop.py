import core
import pytest


class TestCountry:
    def test_Country_should_exist(self):
        assert isinstance(core.Country, type)

    @pytest.mark.skip
    def test_Country_init_works(self):
        c = core.Country('a', 1, 2)
        assert c.name == 'a'
        assert c.population == 1
        assert c.area == 2

    @pytest.mark.skip
    def test_is_larger_works(self):
        a = core.Country('a', 3, 4)
        b = core.Country('b', 1, 3)
        assert a.is_larger(b) == True

    @pytest.mark.skip
    def test_population_density_works(self):
        a = core.Country('wow', 100, 200)
        assert a.population_density() == 0.5

    @pytest.mark.skip
    def test_str_works(self):
        a = core.Country('a', 4, 21)
        assert str(a) == 'a has a population of 4 and is 21 square km.'

    @pytest.mark.skip
    def test_repr_works(self):
        a = core.Country('a', 45, 20)
        assert repr([a]) == "[Country('a', 45, 20)]"


class TestContinent:
    @pytest.mark.skip
    def test_Continent_should_exist(self):
        assert isinstance(core.Continent, type)

    @pytest.mark.skip
    def test_total_population_works(self):
        canada = core.Country('Canada', 34482779, 9984670)
        mexico = core.Country('Mexico', 112336538, 1943950)
        usa = core.Country('United States of America', 313914040, 9826675)
        na = core.Continent("North America", [canada, mexico, usa])
        assert na.total_population() == 460733357

    @pytest.mark.skip
    def test_str_works(self):
        canada = core.Country('Canada', 34482779, 9984670)
        mexico = core.Country('Mexico', 112336538, 1943950)
        usa = core.Country('United States of America', 313914040, 9826675)
        na = core.Continent("North America", [canada, mexico, usa])
        assert str(na) == '''North America
Canada has a population of 34482779 and is 9984670 square km.
Mexico has a population of 112336538 and is 1943950 square km.
United States of America has a population of 313914040 and is 9826675 square km.'''
