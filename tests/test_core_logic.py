import sys
sys.path.append('/content/drive/MyDrive/contact_book/src')
from core_logic import *
import unittest
from unittest.mock import mock_open, patch


#test function for valid_name_len():
def test_valid_name_len():
  assert valid_name_len("Roisin") == True
  assert valid_name_len("") == False
  assert valid_name_len("abcdefghijklmnopqrstuvwxyz") == False

#test function for valid_number_char():
def test_valid_number_char():
  assert valid_number_char("+1 815-347-9051") == True
  assert valid_number_char("(083) 374 9642") == True
  assert valid_number_char("") == False
  assert valid_number_char("abc") == False

#test function for valid_number_len():
def test_valid_number_len():
  assert valid_number_len("456123789") == True
  assert valid_number_len("+353 (83) 815-347-9051") == True
  assert valid_number_len("12") == False
  assert valid_number_len("01234567890123456789") == False

#test function for valid_number_uniq():
def test_valid_number_uniq():
  mock_csv = (
    "Name,Number,Email,Address\n"
    "Alan,987321654,alan@gmail.com,123 Main Street\n"
  )
  mock_valid = mock_open(read_data=mock_csv).return_value
  mock_invalid = mock_open(read_data=mock_csv).return_value

  with patch("builtins.open", side_effect=[mock_valid, mock_invalid]):
    assert valid_number_uniq("234561765") == True
    assert valid_number_uniq("987321654") == False


#test function for valid_email_char():
def test_valid_email_char():
  assert valid_email_char("John.Smith_1986@gmail.com") == True
  assert valid_email_char("john_smith@e-mail.co.uk") == True
  assert valid_email_char("") == False
  assert valid_email_char("john") == False
  assert valid_email_char("john@smith") == False
  assert valid_email_char("john.smith") == False
  assert valid_email_char("john@.smith") == False

#test function for valid_email_len():
def test_valid_number_len():
  assert valid_email_len("john@gmail.com") == True
  assert valid_email_len("a@a.a") == False

#test function for valid_email_uniq():
def test_valid_email_uniq():
  mock_csv = (
    "Name,Number,Email,Address\n"
    "Alan,987321654,alan@gmail.com,123 Main Street\n"
  )
  mock_valid = mock_open(read_data=mock_csv).return_value
  mock_invalid = mock_open(read_data=mock_csv).return_value

  with patch("builtins.open", side_effect=[mock_valid, mock_invalid]):
    assert valid_email_uniq("bob@gmail.com") == True
    assert valid_email_uniq("alan@gmail.com") == False

if __name__ == '__main__':
  test_valid_name_len()
  test_valid_number_char()
  test_valid_number_len()
  test_valid_number_uniq()
  test_valid_email_char()
  test_valid_number_len()
  test_valid_email_uniq()
  print("All tests passed!")
