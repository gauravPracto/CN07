import CN07
import pytest

def test_method():
    cn07Object = CN07.CardValidator("378282246310005","Gaurav","123","22/09/2022")
    
    # test for the valid number 
    assert cn07Object.isValidNumber("378282246310005")==True
    # test for invalid number
    assert cn07Object.isValidNumber("378282246310075")==False
    # test for the valid Name
    assert cn07Object.isValidName("Gaurav Mishra")==True
    #test for the invalid Name
    assert cn07Object.isValidName("Gaurav  1 Mishra")==False
    #test the starting number False with String
    assert cn07Object.isValidStart("45")==False
    #test the starting number True
    assert cn07Object.isValidStart([4,5])==True
    #test the starting number False
    assert cn07Object.isValidStart([9,5])==False
    #test for getting wrong input
    assert cn07Object.getCardDigits(134)==[1,3,4]
    assert cn07Object.getCardDigits(13//4)==[3]
    assert cn07Object.getCardDigits("13ddd4")==[1,3,4]
    # test for getting correct input
    assert cn07Object.getCardDigits("134")==[1,3,4]
    # test for wrong digit sum input
    assert cn07Object.digitSum('jk')==-1
    #  test for correct digit sum input
    assert cn07Object.digitSum(1234)==10
    # luhsAlgo take wrong card digit
    assert cn07Object.luhnAlgorithm([1,2,3,5])==False
    # luhsAlgo take correct card digit
    assert cn07Object.luhnAlgorithm([0,0])==True
    # invalid CVV
    assert cn07Object.isValidCVV("123a")==False
    # small CVV
    assert cn07Object.isValidCVV(12)==False
    # long CVV
    assert cn07Object.isValidCVV(1989892)==False
    # correct CVV
    assert cn07Object.isValidCVV(123)==True
    # invalid date datatype
    assert cn07Object.isValidDate(123433)==False
    # invalid date format
    assert cn07Object.isValidDate("220188")==False
    # invalid backslash
    assert cn07Object.isValidDate("22-//0188")==False
    #  

