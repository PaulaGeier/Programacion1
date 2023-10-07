import pytest
from FUNCIONES.PYTEST.programa_principal import *
@pytest.mark.parametrize('a,res',[
    ({1000:0.10,2000:0.20,3000:0.30,1500:0.10,2500:0.20,3500:0.30},10400),
    ({1500:0.15,2500:0.25,3500:0.35,1550:0.15,2550:0.25,3550:0.35},10962.5)
])
def test_purchase_total(a,res):
    assert purchase_total(a)==res