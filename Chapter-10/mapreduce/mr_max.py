'''
MIT License

Copyright (c) 2019 Arshdeep Bahga and Vijay Madisetti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Most visited page in each month of year 2014 
 
from mrjob.job import MRJob 
 
class MRmyjob(MRJob): 
    def mapper1(self, _, line): 
        #Split the line with tab separated fields 
        data=line.split('\t') 
 
        #Parse line 
        date = data[0].strip() 
        time = data[1].strip() 
        url = data[2].strip() 
        ip = data[3].strip() 
         
        #Extract year from date 
        year=date[0:4] 
        month=date[5:7] 
         
        #Emit (month,url) pair and 1 if year is 2014 
        if year=='2014': 
            yield (month,url), 1 
 
 
    def reducer1(self, key, list_of_values): 
        yield key[0], (sum(list_of_values), key[1]) 
     
     
    def reducer2(self, key, list_of_values):        
        yield key, max(list_of_values) 
 
 
    def steps(self): 
        return [self.mr(mapper=self.mapper1,  
        reducer=self.reducer1), self.mr(reducer=self.reducer2)] 
 
 
if __name__ == '__main__': 
    MRmyjob.run() 
