import pytest
from elmer import *
import os

def test_kv():
    
    assert os.path.exists("./data/raw.csv")