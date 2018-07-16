import functions
from pytest import approx
from bcca.test import should_print


def test_add_em_up():
    assert functions.add_em_up(1, 2, 3) == 6
    assert functions.add_em_up(4, 5, 6) == 15


def test_sub_sub_hubbub():
    assert functions.sub_sub_hubbub(1, 2, 3) == -4


def test_square_area():
    assert functions.square_area(5, 5) == 25
    assert functions.square_area(3, 5) == 15
    assert functions.square_area(2, 2) == 4


def test_circle_area():
    assert functions.circle_area(1) == approx(3.14)
    assert functions.circle_area(5) == approx(78.5)


def test_kilometers_to_miles():
    assert functions.kilometers_to_miles(1) == approx(0.6214)
    assert functions.kilometers_to_miles(.5) == approx(0.3107)
    assert functions.kilometers_to_miles(0) == approx(0.0)
    assert functions.kilometers_to_miles(40) == approx(24.855999999999998)


@should_print
def test_sales_tax_1(output):
    functions.sales_tax(1)

    assert output == """
Purchase Amount: 1
State Sales Tax: 0.04
County Sales Tax: 0.02
Total Sales Tax: 0.06
Total Cost: 1.06
"""


@should_print
def test_sales_tax_99_99(output):
    functions.sales_tax(99.99)

    assert output == """
Purchase Amount: 99.99
State Sales Tax: 3.9996
County Sales Tax: 1.9998
Total Sales Tax: 5.9994
Total Cost: 105.98939999999999
"""


@should_print
def test_sales_tax_5_95(output):
    functions.sales_tax(5.95)

    assert output == """
Purchase Amount: 5.95
State Sales Tax: 0.23800000000000002
County Sales Tax: 0.11900000000000001
Total Sales Tax: 0.35700000000000004
Total Cost: 6.307
"""


def test_min_insurance():
    assert functions.min_insurance(100000) == approx(80000.0)
    assert functions.min_insurance(123456789) == approx(98765431.2)
    assert functions.min_insurance(0) == approx(0.0)
    assert functions.min_insurance(-54317890) == approx(-43454312.0)


@should_print
def test_property_tax_10000(output):
    functions.property_tax(10000)

    assert output == '''
Assessment Value: 6000.0
Property Tax: 38.4
'''


@should_print
def test_property_tax_99999_95(output):
    functions.property_tax(99999.95)

    assert output == '''
Assessment Value: 59999.969999999994
Property Tax: 383.999808
'''


def test_bmi():
    assert functions.bmi(160, 67) == approx(25.05680552)
    assert functions.bmi(200, 72) == approx(27.12191358)
    assert functions.bmi(120, 60) == approx(23.43333333)


def test_calories():
    assert functions.calories(5, 20) == 125
    assert functions.calories(1, 1) == 13


def test_earnings():
    assert functions.earnings(100, 100, 100) == 3600
    assert functions.earnings(50, 75, 100) == 2550
    assert functions.earnings(0, 1000, 79) == 12711


@should_print
def test_paint_job_estimator(output):
    functions.paint_job_estimator(50, 10)

    assert output == '''
Gallons of paint required: 0.43478260869565216
Hours of labor required: 3.4782608695652173
Cost of paint: 4.3478260869565215
Cost of labor: 69.56521739130434
Total Cost: 73.91304347826086
'''


@should_print
def test_paint_job_estimator_2(output):
    functions.paint_job_estimator(750, 15.95)

    assert output == '''
Gallons of paint required: 6.521739130434782
Hours of labor required: 52.17391304347826
Cost of paint: 104.02173913043477
Cost of labor: 1043.4782608695652
Total Cost: 1147.5
'''


@should_print
def test_monthly_sales_tax(output):
    functions.monthly_sales_tax(123456.79)

    assert output == '''
Monthly sales: 123456.79
State sales tax: 4938.2716
County sales tax: 2469.1358
Total sales tax: 7407.4074
'''


@should_print
def test_monthly_sales_tax_2(output):
    functions.monthly_sales_tax(4321567.21)

    assert output == '''
Monthly sales: 4321567.21
State sales tax: 172862.6884
County sales tax: 86431.3442
Total sales tax: 259294.03260000004
'''
