# INSTALLATION STEPS

## Step 1 : Install NLTK

Please follow steps on [NLTK Install page](http://www.nltk.org/_sources/install.txt)

###### TEST
```
$ python
Python 2.7.10 (default, Feb  7 2017, 00:08:15) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> print(nltk.__version__)
3.2.4
```

## Step 2 : Install punkt sentence tokenizer
To download a particular dataset/models, use the nltk.download() function, e.g. if you are looking to download the punkt sentence tokenizer, use:

```
$ python
>>> import nltk
>>> nltk.download('punkt')
```

# EXECUTION STEPS

## USE PYTHON
```
$ python test.py <INPUT_FILENAME> <SIGMA>
$ python test.py retail_25k.dat 4
Input File : retail_25k.dat
Co-Occurrence Freq. : 4
Output File : retail_25k_4.out
```


## USE SHELL SCRIPT
```
$./test.sh retail_25k.dat 3
Input File : retail_25k.dat
Co-Occurrence Freq. : 3
Output File : retail_25k_3.out
```
