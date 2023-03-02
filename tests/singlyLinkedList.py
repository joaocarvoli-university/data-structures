import unittest

import sys

sys.path.append("lists")

from lists import singlyLinked

class SinglyLinkedList(unittest.TestCase):
  def test_singlyLinked():
    l = singlyLinked.SinglyLinkedList()
    
    
if __name__ == '__main__':
  unittest.main()
  