

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from itertools import count
from unittest import result
from tqdm import tqdm
from urllib.parse import urlparse
import requests
import os
import multiprocessing

class TextComparer():
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []
        
        
    def download(self, url):
        path = urlparse(url).path
        filename = os.path.basename(path)

        response = requests.get(url, stream = True)
        if(response.status_code == 404):
            raise NotFoundException(url)
        else:
            savedPath = f"./downloads/{filename}"
            with open(savedPath,"wb") as text_file:
                for chunk in tqdm(response.iter_content(chunk_size=1024)):
                    text_file.write(chunk)
            self.filenames.append(filename) #used becauuse we need this in the next method

    def multi_download(self):
        with ThreadPoolExecutor(len(self.url_list)) as ex:
            for url in self.url_list:
                ex.submit(self.download,url)
    
    def urllist_generator(self):
        for url in self.url_list:
            yield url

 
    def avg_vowels(self,text):
        vowels = "aeiou"
        words = text.split()
        words_amount = len(words)

        total_vowels = 0
        for word in words:
            total_vowels = total_vowels + len([char for char in word.lower() if char in vowels]) 
        return total_vowels / words_amount

    def hardest_read(self):
        res = []
        for file in self.filenames:
            with open("./downloads/"+file, "r") as text:
                contents = text.read()
            res.append((file, self.avg_vowels(contents)))
        return sorted(res, key=lambda x:x[1], reverse=True)[0] #Sort and get the first element which is the highest in vowels
    

    def hardest_read_multiprocessing(self):
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
            res = ex.map(self.open_file_and_count_vowels, self.filenames)
        return sorted(list(res), key=lambda x:x[1], reverse=True)


    def open_file_and_count_vowels(self,filename):
        with open("./downloads/"+filename,'r') as file:
                data = file.read()
                average_vowels = self.avg_vowels(data)
                return (filename,average_vowels)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        while self.x < len(self.filenames):
            filename = self.filenames[self.x]
            self.x +=1
            return filename
        raise StopIteration

class NotFoundException(Exception): 
    def __init__(self,url):
        self.url = url
        super().__init__(f"ERROR - URL : {self.url} - responded with 404")