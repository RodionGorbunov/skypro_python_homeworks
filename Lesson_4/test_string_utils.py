import pytest

from string_utils import StringUtils

test = StringUtils()

@pytest.mark.positive_test_capitilize
@pytest.mark.parametrize('num, result', [('кейс', 'Кейс'), ('skypro', 'Skypro')])
def test_big_first(num, result):
    test = StringUtils()
    res = test.capitilize(num)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize('num, result', [('Morning', 'Morning')])
def test_big_first(num, result):
    test = StringUtils()
    res = test.capitilize(num)
    assert res == result

@pytest.mark.positive_test_trim
@pytest.mark.parametrize('num, result', [(' homework', 'homework'), ('   кейс', 'кейс')])
def test_spaces_first(num, result):
    test = StringUtils()
    res = test.trim(num)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_trim
@pytest.mark.parametrize('num, result', [('ca t', 'ca t')])
def test_spaces_first(num, result):
    test = StringUtils()
    res = test.trim(num)
    assert res == result


@pytest.mark.positive_test_to_list
@pytest.mark.parametrize('val, delim, result', [('a,b,c', ',', ['a','b','c']), ('1/2/3', '/',['1','2','3'])])
def test_delim_count(val, delim, result):
    test = StringUtils()
    res = test.to_list(val, delim)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_to_list
@pytest.mark.parametrize('val, delim, result', [('1,2,3,4 5', None, ['1', '2', '3', '4 5']),])
def test_delim_count(val, delim, result):
    test = StringUtils()
    res = test.to_list(val, delim)
    assert res == result

@pytest.mark.positive_test_contains
@pytest.mark.parametrize('val, symbol, result', [('a,b,c', 'b', True), ('flower', 'f', True), ('3698', '7', False)])
def test_contain_symbol(val, symbol, result):
    test = StringUtils()
    res = test.contains(val, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_contains
@pytest.mark.parametrize('val, symbol, result', [('parameter', 'P', False), ('hello', 'x', False)])
def test_contain_symbol(val, symbol, result):
    test = StringUtils()
    res = test.contains(val, symbol)
    assert res == result

@pytest.mark.positive_test_delete_symbol
@pytest.mark.parametrize('val, symbol, result', [('123', '1', '23'), ('Street', 'r', 'Steet')])
def test_symbol_del(val, symbol, result):
    test = StringUtils()
    res = test.delete_symbol(val, symbol)
    assert res == result
    
@pytest.mark.xfail
@pytest.mark.negative_test_delete_symbol
@pytest.mark.parametrize('val, symbol, result', [('spoon', 'k', 'spoon'), ('milk', '', 'milk')])
def test_symbol_del(val, symbol, result):
    test = StringUtils()
    res = test.delete_symbol(val, symbol)
    assert res == result

@pytest.mark.positive_test_starts_with
@pytest.mark.parametrize('val, symbol, result', [('table', 't', True), ('123', '1', True), ('tea', 'T', False)])
def test_start_check(val, symbol, result):
    test = StringUtils()
    res = test.starts_with(val, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_starts_with
@pytest.mark.parametrize('val, symbol, result', [('tea', 'T', False), ('eleven', 'n', False)])
def test_start_check(val, symbol, result):
    test = StringUtils()
    res = test.starts_with(val, symbol)
    assert res == result

@pytest.mark.positive_test_end_with
@pytest.mark.parametrize('val, symbol, result', [("spring", "g", True),  ('123', '3', True), ("morning", "S", False)])
def test_end_check(val, symbol, result):
    test = StringUtils()
    res = test.end_with(val, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_end_with
@pytest.mark.parametrize('val, symbol, result', [('evening', 'e', False),  ('door', 'R', False)])
def test_end_check(val, symbol, result):
    test = StringUtils()
    res = test.end_with(val, symbol)
    assert res == result

@pytest.mark.positive_test_is_empty
@pytest.mark.parametrize('val, result', [('', True),  ('   ', True), ('cat', False)])
def test_str_check(val, result):
    test = StringUtils()
    res = test.is_empty(val)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_is_empty
@pytest.mark.parametrize('val, result', [('tree', False),  ('123', False)])
def test_str_check(val, result):
    test = StringUtils()
    res = test.is_empty(val)
    assert res == result

@pytest.mark.positive_test_list_to_string
@pytest.mark.parametrize('val, delim, result', [([1,2,3,4,5], '*', '1*2*3*4*5')])
def test_str_delim(val, delim, result):
    test = StringUtils()
    res = test.list_to_string(val, delim)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_list_to_string
@pytest.mark.parametrize('val, delim, result', [([], None, ''), ([], '*', '')])
def test_str_delim(val, delim, result):
    test = StringUtils()
    res = test.list_to_string(val, delim)
    assert res == result
    