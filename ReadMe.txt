INSTRUCTIONS FOR COMPILING THE PYTHON FILES:
--------------------------------------------

**********************************************************************************************
A SMALL SEARCH ENGINE BASED ON BM25 RANKING ALGORITHM. THE CODE HAS BEEN WRITTEN IN PYTHON.
**********************************************************************************************

1) The first part of this project is to create inverted index from the given corpus file.
A python script 'indexer.py' is used for this purpose. This file takes the corpus file 'tccorpus.txt'
as input through command line.

How to run this file:
----------------------

First open a command prompt and go to a location where Python bin is installed. In Windows for e.g. C:\Python27\ and save all the required files here:
NOTE: You can check if python is installed here and its version by giving 'python' command.

1)indexer.py
2)tccorpus.txt

indexer.py <given_corpus_file>

Executing in this fashion will generate a outfile 'indexout.txt' having the required inverted index. 
The file is created at the location, where this script is located.
------------------------
indexer.py tccorpus.txt
------------------------

However you can also redirect the output to any file by following below syntax.
Example to redirect output to a file 'result.txt':
------------------------------------
indexer.py tccorpus.txt > result.txt
------------------------------------

**************************************************************************************************************************************************************************

2) Once we have the required inverted index file, next step is to execute the BM25.py script. This script requires the 'indexout.txt' (output of indexer.py) , queries.txt(file
containing the query) and Max_Number_of_document_result_required(a integer) as input through command line.

This file generates the outputfile in the required format.

How to run this file:
----------------------

First open a command prompt and go to a location where Python bin is installed. In Windows for e.g. C:\Python27\ and save all the required files here:
NOTE: You can check if python is installed here and its version by giving 'python' command.

1)indexer.py
2)tccorpus.txt
3)indexout.txt
4)queries.txt
5)BM25.py

NOTE: For BM25.py the corpus file must be named as 'tccorpus.txt' as for taking input for corpus file, the script will not prompt user and should be at same location as of script.

BM25.py <inverted_index_file(txt file)> <File_containing_query(txt file)> <Max_Number_of_document_result_required(a integer)>

Executing in this fashion will generate the output in the required format at te command prompt window itself.

------------------------------------
BM25.py indexout.txt queries.txt 100
------------------------------------

However you can also redirect the output to any file by following below syntax.
Example for redirecting output to a file 'results.txt':
---------------------------------------------------
BM25.py indexout.txt queries.txt 100 > results.txt
---------------------------------------------------

***************************************************************************************************************************************************************************