# LEAKS_COMBINED WORDLIST

This project started after `hashes.org` went ofline...

I combined all wordlists from `hashes.org` which I had downloaded in the past to one gigantic wordlist. Over time I found other big wordlists and included them into my wordlist. I also recogniced that the old `hashes.org` wordlists where pretty messy and they contain all kind of unwanted data like email addresses, uncracked hashes, etc.

I created a few scripts to automate a rough cleanup of the wordlists and the merging. As latest addition to the wordlist I downloaded the famous Breach-Compilation (`magnet:?xt=urn:btih:7FFBCD8CEE06ABA2CE6561688CF68CE2ADDCA0A3&dn=BreachCompilation`) and parsed the data to extract the passwords. 

Actually the wordlist contain **790,216,259 passwords**.

## Usage of the scripts to extend the wordlist

**1. Cleaning of wordlists**

```
┌─[mark@parrot]─[~/leaks_combined_wordlist]
└──╼ $python3 filter_wordlist.py hashes_org.txt filtered.txt 
...

┌─[mark@parrot]─[~/leaks_combined_wordlist]
└──╼ $python3 filter_wordlist.py breach_comp.txt filtered.txt 
...

┌─[mark@parrot]─[~/leaks_combined_wordlist]
└──╼ $python3 filter_wordlist.py more_passwords.txt filtered.txt 
...
```

This script remove hashes in hexadecimal notation, email addresses and other unwanted values.

It appends the filtered content of the first file to the 2nd file...

**2. Sorting and merging**

```
┌─[mark@parrot]─[~/leaks_combined_wordlist]
└──╼ $python3 split_filter_uniq.py filtered.txt 
 0.0 GB processed ...
 0.1 GB processed ...
 ...
24.9 GB processed ...
25.0 GB processed ...

SORTING 0.tmp
REMOVING DUPLICATES FROM 0.tmp
SORTING 1.tmp
REMOVING DUPLICATES FROM 1.tmp
...
SORTING z.tmp
REMOVING DUPLICATES FROM z.tmp
SORTING %.tmp
REMOVING DUPLICATES FROM %.tmp

COMPRESSING leaks_combined.txt ...
  adding: leaks_combined.txt (deflated 68%)

PROCESSING DONE IN: 83 MIN.!
```

