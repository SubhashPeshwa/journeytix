import pytest
from elmer import *
import os

def test_init():
    
    assert os.path.exists("./data/raw.csv")
