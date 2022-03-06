from datetime import datetime

import pytest
import pdb

from testy_pokazowka import add, analyze_pesel


class TestAddFunction:

    @pytest.mark.parametrize("a,b,result", [
        (1, 1, 2),
        (5, 1, 6),
        (10, -10, 0), ]
                             )
    def test_add(self, a, b, result):
        assert add(a, b) == result

    def test_add_below_zero(self):
        with pytest.raises(ValueError) as err:
            add(-1, 0)
        assert err.value.args[0] == 'Babol'


class TestAnalizePesel:

    @pytest.mark.parametrize('pesel',
                             ['54092638764', '50060386217', '57082429355', '88050224625',
                              '05260274266', '60070828315', '84042519467', '96102366696',
                              '06322184716', '99061133114'])
    def test_pesel(self, pesel):
        result = analyze_pesel(pesel)
        assert result['pesel'] == pesel

    @pytest.mark.parametrize('pesel',
                             ['54092638764', '50060386217', '57082429355', '88050224625',
                              '05260274266', '60070828315', '84042519467', '96102366696',
                              '06322184716', '99061133114'])
    def test_valid(self, pesel):
        result = analyze_pesel(pesel)
        assert result['valid']

    @pytest.mark.parametrize('pesel',
                             ['02292169476', '55092529793', '52071944554', '60112379199',
                              '70021117872', '76012385257', '53102775996',
                              '91020483357', '52031454251', '71050966637'])
    def test_sex(self, pesel):
        result = analyze_pesel(pesel)
        assert result['gender'] == "male"

    @pytest.mark.parametrize('pesel',
                             ['72011569368', '98101288562', '82040551148', '87121368842',
                              '82032485523', '04291726348', '02272273881', '94112165865',
                              '52092516222', '99013016926'])
    def test_sex_female(self, pesel):
        result = analyze_pesel(pesel)
        assert result['gender'] == "female"

    @pytest.mark.parametrize('pesel, date',
     [('72011569368', datetime(1972, 1, 15)),
      ('98101288562', datetime(1998, 10, 12)),
      ('87121368842', datetime(1987, 12, 13)),
      ('04291726348', datetime(2004, 9, 17)),
      ('02272273881', datetime(2002, 7, 22)), ])
    def test_birth_date(self, pesel, date):
        result = analyze_pesel(pesel)
        assert result['birth_date'] == date
