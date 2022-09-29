import pytest
from elmer import *
import os

def test_auth():
    
    assert os.path.exists("./data/raw.csv")
