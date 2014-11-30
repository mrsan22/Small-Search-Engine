#!/usr/bin/python



from itertools import groupby
from operator import itemgetter
import sys

##Required Data Structures:
##'d' dictionary contains the docid as key and all the strings associated with it as values.
d={}
line=[]
##lst_tup is a list of tuple, where each tuple has tha data in format of (word,docid,frequency)
lst_tup=[]
##dict_freq is a dictionary containing data in format of word:frequency
dict_freq={}
t=tuple()
index_dict={}
#Creating a data structure length_dict(dictionary) to store the tokens in order to
#calculate length of the document, length_dict is in the format {docid:length}
new_dict={}

##opening a file
#fname=raw_input("Enter the corpus filename:")

##Taking the corpus file as the input through commmand line
try:
    
    fhand=open(sys.argv[1])
except:
    print "File cannot be opened", fhand
    exit()

inp=fhand.read()
line=inp.split()

##Splitting the corpus file into lists, the split happens at the start of each document 'beginning with #'.
split_lst=[list(group) for k, group in groupby(line,lambda x: x == '#') if not k]
for each_lst in split_lst:
    for each in each_lst:
        ##'d' dictionary contains the docid as key and all the strings associated with it as values.
        d[each_lst[0]]=each_lst[1:]

##Creating a data structure new_dict(dictionary) to store the tokens in order to
##calculate length of the document, new_dict is in the format {docid:length}
for k,v in d.items():
    new_dict[k]=len(v)

##Sorting a dictionary 'd' generates a list of tuples of key value pair
#sorted_d=sorted(d.items(),key=itemgetter(0),reverse=True)

##dict_freq is a dictionary containing data in format of word:frequency
for key,each_lst in d.items():
    for each in each_lst:
        
        if each not in dict_freq:
            dict_freq[each]=1
           
        else:
            dict_freq[each]+=1
            
    for k,val in dict_freq.items():
        
        lst_tup.append((k,key,val))
    dict_freq={}
    
##lst_tup is a list of tuple, where each tuple has tha data in format of (word,docid,frequency)


##Here we create the required the inverted index, which is in the format {'word':[('docid',freq),('docid',freq), ....]}
for i,j,k in lst_tup:
    index_dict.setdefault(i,[]).append((j,k,))

##This dictionary is the required the inverted index that we need for our search engine.
print index_dict

##To write the index_dict to a txt file
indexout=open("indexout.txt",'w+')
indexout.write(str(index_dict))
indexout.close()
