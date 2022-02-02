import CN07
import pytest

def test_method():
    cn07Object = CN07.CardValidator("378282246310005","Gaurav","123","22/09/2022")
    assert cn07Object.isValidNumber("378282246310005")==True
    assert cn07Object.isValidName("Gaurav Mishra")==True