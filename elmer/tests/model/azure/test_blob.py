import pytest
from elmer import *
import os

def test_blob():
    
    assert os.path.exists("./data/raw.csv")