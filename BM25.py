#!/usr/bin/python



from math import log
from operator import itemgetter
from itertools import groupby
import sys

##Defining constants
k1=1.2
b=0.75
k2=100
##Assume that no relevance information is available.
R=0.0
##Dictionary containing the inverted index.
dict_index={}
##'d' dictionary contains the docid as key and all the strings associated with it as values.
d={}
#Creating a data structure length_dict(dictionary) to store the tokens in order to
#calculate length of the document, length_dict is in the format {docid:length}
length_dict={}
##This list contains the input queries in the form of list, each query field is stored as different list
final_output=[]
sorted_score_lst=[]

##Retrieve all inverted lists corresponding to terms in a query.
##opening the file contaning the inverted index which we got from indexer.py
try:
	#fhand=open("indexout.txt")
	fhand=open(sys.argv[1])
except:
	print "File cannot be opened", fhand
	exit()
##Reading the inverted index file back to dictionary dict_index.
dict_index=eval(fhand.read())

##Opening the corpus file to calculate the document lenght and average document length.
try:
    
    fhandle=open("tccorpus.txt")
except:
    print "File cannot be opened", fhandle
    exit()

inp=fhandle.read()
line=inp.split()

##Splitting the corpus file into lists, the split happens at the start of each document 'beginning with #'.
split_lst=[list(group) for k, group in groupby(line,lambda x: x == '#') if not k]
for each_lst in split_lst:
    for each in each_lst:
        d[each_lst[0]]=each_lst[1:]

##Creating a data structure length_dict(dictionary) to store the tokens in order to
##calculate length of the document, length_dict is in the format {docid:length}
for k,v in d.items():
    length_dict[k]=len(v)


##Compute BM25 scores for documents in the lists.
##r= relevant documents containing term i
##n=number of docs containing term i
##N= Total number of documents in the collection
##K1, k2, K are parameters, whose values are set empirically.
##dl is the length of the document
##avdl is the average document length
##R is the relevance information
##f is the frequency of term i in the doc under consideration.
##qf is the frequency of term i in the query.

##Function to calculate the BM25 score for each term in the query.
def cal_BM25_score(r,n,N,avdl,dl,f,qf):
    K=k1*((1-b)+b*(float(dl)/float(avdl)))
    expression_1=log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))
    expression_2=((k1 + 1) * f)/(K + f)
    expression_3=((k2+1)*qf)/(k2+qf)
    return expression_1 * expression_2 * expression_3

##Function to calculate document length(dl) based on corpus.
def cal_length(docid):
    if docid in length_dict.keys():
        return length_dict[docid]
    else:
        print ('%s not found in corpus' %str(docid))

##Function to calculate average document length (avdl) based on corpus.
def cal_avg_length():
    sum=0
    for length in length_dict.values():
        sum+=length
    return float(sum)/float(len(length_dict))

##Function to process the queries from the queries.txt file and store them in a list of queries.
def process_query(filename):
    
    f=open(filename)
    lines=''.join(f.readlines())
    query_lst= [x.rstrip().split() for x in lines.split('\n')[:]]
    return query_lst

##A class containing the all related functions for BM25 score calculation
class Cal_BM25_Score_For_Query:

    def __init__(self):
        #self.query_lst=process_query('queries.txt')
        self.query_lst=process_query(sys.argv[2])

    def query_execution(self):
        results=[]
        for query in self.query_lst:
            results.append(self.bm25_for_query(query))
        return results

    def bm25_for_query(self,query):
        query_scores={} #This dictionary conains {docid:score} for each term.
        dict_term_val={}
        
        for each_term in query:
            if each_term in dict_index.keys():
                #term_val is a list of tuples that contain the docid,freq for each term
                term_val=dict_index[each_term]
                #This dictionary contains the docid and frequency for the given term
                dict_term_val=dict(term_val)
                n=len(dict_term_val)
                N=len(d)
                for docid,freq in dict_term_val.items():
                    #Calculate score
                    score=cal_BM25_score(0,n,N,cal_avg_length(),cal_length(docid),freq,1)

                    if docid not in query_scores:
                        query_scores[docid]=score
                    else:
                        query_scores[docid]+=score

        return query_scores            
        

def main():
    #process_query('queries.txt')
    process_query(sys.argv[2])
    ql=Cal_BM25_Score_For_Query()
    final_output=ql.query_execution() #final_output is of type <List>  and contains the list of dictionaries,
                                      #where each dictionary is of format {docid:score}
    print 'Queryid\tQ0\tDoc_id\tRank\tBM25_Score\tSystem_Name'
    query_id=1
    for each in final_output:
        #sorted_output sorts each element of dictionary({docid:score}), based on the scores and generates a list of tuples, where each tuple is of form (docid,score).
        sorted_output=sorted(each.items(),key=itemgetter(1),reverse=True)
        #sorted_score_lst.append(sorted_output)
        rank=1
        for each_tup in sorted_output[:int(sys.argv[3])]:
            #prints in the required format
            print '{}\tQ0\t{:>4}\t{:>2}\t{:>15}\tBM25-Server'.format(query_id,each_tup[0],rank,each_tup[1])
            rank+=1
        query_id+=1
            
        
        
        
##Calling the main function    
if __name__=='__main__':
    main()
