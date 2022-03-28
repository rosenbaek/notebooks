import pytest
from modules.textcomparer import TextComparer
import os, glob
import shutil
from collections.abc import Iterable

urls = []
urls.append("https://www.gutenberg.org/files/84/84-0.txt")
urls.append("https://www.gutenberg.org/files/1342/1342-0.txt")
urls.append("https://www.gutenberg.org/files/1260/1260-0.txt")
urls.append("https://www.gutenberg.org/files/1400/1400-0.txt")
textComparer = TextComparer(urls)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    # A test function will be run at this point
    shutil.rmtree("./downloads")
    os.makedirs("./downloads")
    yield
    shutil.rmtree("./downloads")
    os.makedirs("./downloads")
    # Code that will run after your test, for example:
    
    

def test_download():
    textComparer.download(urls[0])
    assert len( os.listdir('./downloads')) == 1

def test_multi_download():
    textComparer.multi_download()
    assert len( os.listdir('./downloads')) == 4

def test_iter():
    my_iterable = textComparer.__iter__()
    assert isinstance(my_iterable, Iterable) == True

def test_avg_vowels():
    expected = 1
    actual = textComparer.avg_vowels("This is a test")
    assert expected == actual

def test_hardest_read():
    _filenames = ['file1.txt','file2.txt']
    with open("./downloads/"+_filenames[0], 'w') as f_2:
        f_2.write("##HI! heello ##THERE")

    with open("./downloads/"+_filenames[1], 'w') as f_2:
        f_2.write("##HIi! heelloooooooooooooooooo ##THERE")

    textComparer.filenames = _filenames

    file_with_highest_average_vowels = textComparer.hardest_read_multiprocessing()
    assert _filenames[1] == file_with_highest_average_vowels[0]