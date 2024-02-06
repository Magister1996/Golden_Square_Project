from lib.date_of_birth import age_check
from dateutil.relativedelta import relativedelta
import pytest 

def test_age_check_over():
    assert age_check('2000-01-01') == 'Access Granted!'

def test_age_checkage_under():
    assert age_check('2010-01-01') == 'Access Denied!'

def test_age_checkage_bad_format():
    with pytest.raises(Exception) as e:
        age_check('01-01-2000')
    assert str(e.value) == "Type or Format Error. Expected format YYYY-MM-DD"


