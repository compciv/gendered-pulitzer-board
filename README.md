
# Gender Analysis of the Pulitzer Prize Board

This is an automated analysis of the gender makeup of the Pulitzer Prize Board membership since 1968, [according to the Pulitzer website](http://www.pulitzer.org/board/1968). 

Why 1968? Because I don't have time to reverse-engineer the [data-structure of this Angular-heavy site](http://www.pulitzer.org/cache/api/1/global.json). Even though there are webpages for every board since 1917, they don't seem to be serialized in the same way as the years [1968-and-on](pulitzer-taxonomy.csv). Oh well.


## Findings

In the time period of 1968 to the current year, an estimated __40+ women__ have served on the Pulitzer Prize board compared to __170+ men__.

The [2015 board membership](http://www.pulitzer.org/board/2015) was composed of 6 women and 12 men, according to a manual count; the automated analysis counted 6 and 11, respectively, apparently not being able to classify one of the male names. The makeup of the 2015 board is 33% women, which is the tied with 1997 as the highest rate of any year.

According to the automated analysis, the 1970s did not see a single woman on the Pulitzer Board. In the 1980s, about 10% of the board members were women.



### Methodology and Caveats

The automated analysis detects gender by using the Social Security Administration's baby name data. If a name, such as "Joseph", has more recorded baby boys than baby girls in the SSA records, than "Joseph" is considered by the algorithm to be a name likely given to a man. Yes that's how basic the algorithm is. 

No attempt at disambiguating the guess was done for close-calls (though there don't seem to be many of those) -- and people such as __C.K.McClatchy__ are just left out.

However, a quick spot-check of the Pulitzer website seems to confirm the broad generalizations of the analysis. For example, the algorithm did not find a single woman on the board in the 1970s.

For reference, this is a picture of the [1970 board membership](http://www.pulitzer.org/board/1970):

![http://www.pulitzer.org/cms/sites/default/files/1970boardpic500_0.jpg](http://www.pulitzer.org/cms/sites/default/files/1970boardpic500_0.jpg)


And this is a picture of the [1979 board membership](http://www.pulitzer.org/board/1979):

![http://www.pulitzer.org/cms/sites/default/files/1979boardphoto500.jpg](http://www.pulitzer.org/cms/sites/default/files/1979boardphoto500.jpg)


The algorithm detects its [first woman in 1980](http://www.pulitzer.org/board/1980): __Hanna H. Gray, president, University of Chicago__


![http://www.pulitzer.org/cms/sites/default/files/1980boardphoto960.jpg](http://www.pulitzer.org/cms/sites/default/files/1980boardphoto960.jpg)



-------------------------------------


## Facets of analysis

The following facets were analyzed:

### Across the overall membership


### Board membership by decade


### Board membership by year



-----------------------------------


## The scripts

Here are the scripts in this repo, in the order that they should be run from the command-line:

### fetch_gender_data.py

### wrangle_gender_data.py

### fetch_pulitzer_board_pages.py

### wrangle_pulitzer_board_data.py

### classify.py


### analyze.py





## Ancillary files

Here are some supporting files

### settings.py

### pulitzer-taxonomy.csv

### gender.py



# Printout of analyze.py

The raw printout:

~~~
Since 1968, the estimated gender breakdown for the Pulitzer Prize Board membership is:
  F: 44 20%
  M: 172 76%
  NA: 9 4%
-----------------------------------------
Now let's do a decade-by-decade breakdown
1960
  F: 0 0%
  M: 16 89%
  NA: 2 11%
1970
  F: 0 0%
  M: 32 97%
  NA: 1 3%
1980
  F: 6 9%
  M: 57 86%
  NA: 3 5%
1990
  F: 16 24%
  M: 47 71%
  NA: 3 5%
2000
  F: 17 28%
  M: 43 72%
  NA: 0 0%
2010
  F: 14 33%
  M: 28 65%
  NA: 1 2%
-----------------------------------------
Now let's do a year-by-year breakdown
1968
  F: 0 0%
  M: 11 85%
  NA: 2 15%
1969
  F: 0 0%
  M: 12 92%
  NA: 1 8%
1970
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1971
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1972
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1973
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1974
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1975
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1976
Traceback (most recent call last):
  File "analyze.py", line 95, in <module>
    ratio = round(100 * len(gendered_members)/unique_member_count)
ZeroDivisionError: division by zero
dtown ～～～(✧/✧) ~/stan/showme-examples/pulitzer-board $ python analyze.py 
Since 1968, the estimated gender breakdown for the Pulitzer Prize Board membership is:
  F: 44 20%
  M: 172 76%
  NA: 9 4%
-----------------------------------------
Now let's do a decade-by-decade breakdown
1960
  F: 0 0%
  M: 16 89%
  NA: 2 11%
1970
  F: 0 0%
  M: 32 97%
  NA: 1 3%
1980
  F: 6 9%
  M: 57 86%
  NA: 3 5%
1990
  F: 16 24%
  M: 47 71%
  NA: 3 5%
2000
  F: 17 28%
  M: 43 72%
  NA: 0 0%
2010
  F: 14 33%
  M: 28 65%
  NA: 1 2%
-----------------------------------------
Now let's do a year-by-year breakdown
1968
  F: 0 0%
  M: 11 85%
  NA: 2 15%
1969
  F: 0 0%
  M: 12 92%
  NA: 1 8%
1970
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1971
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1972
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1973
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1974
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1975
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1977
  F: 0 0%
  M: 15 100%
  NA: 0 0%
1978
  F: 0 0%
  M: 15 100%
  NA: 0 0%
1979
  F: 0 0%
  M: 15 100%
  NA: 0 0%
1980
  F: 1 6%
  M: 16 94%
  NA: 0 0%
1981
  F: 2 12%
  M: 15 88%
  NA: 0 0%
1982
  F: 2 12%
  M: 15 88%
  NA: 0 0%
1983
  F: 3 18%
  M: 14 82%
  NA: 0 0%
1984
  F: 2 11%
  M: 15 83%
  NA: 1 6%
1985
  F: 2 11%
  M: 15 83%
  NA: 1 6%
1986
  F: 2 11%
  M: 15 83%
  NA: 1 6%
1987
  F: 3 18%
  M: 13 76%
  NA: 1 6%
1988
  F: 2 12%
  M: 14 82%
  NA: 1 6%
1989
  F: 3 18%
  M: 13 76%
  NA: 1 6%
1990
  F: 4 22%
  M: 13 72%
  NA: 1 6%
1991
  F: 5 26%
  M: 13 68%
  NA: 1 5%
1992
  F: 5 26%
  M: 13 68%
  NA: 1 5%
1993
  F: 5 26%
  M: 13 68%
  NA: 1 5%
1994
  F: 5 28%
  M: 12 67%
  NA: 1 6%
1995
  F: 6 32%
  M: 12 63%
  NA: 1 5%
1996
  F: 6 32%
  M: 12 63%
  NA: 1 5%
1997
  F: 6 33%
  M: 11 61%
  NA: 1 6%
1998
  F: 5 25%
  M: 15 75%
  NA: 0 0%
1999
  F: 5 25%
  M: 15 75%
  NA: 0 0%
2000
  F: 4 20%
  M: 16 80%
  NA: 0 0%
2001
  F: 4 21%
  M: 15 79%
  NA: 0 0%
2002
  F: 3 17%
  M: 15 83%
  NA: 0 0%
2003
  F: 4 20%
  M: 16 80%
  NA: 0 0%
2004
  F: 5 24%
  M: 16 76%
  NA: 0 0%
2005
  F: 4 21%
  M: 15 79%
  NA: 0 0%
2006
  F: 4 21%
  M: 15 79%
  NA: 0 0%
2007
  F: 5 25%
  M: 15 75%
  NA: 0 0%
2008
  F: 5 26%
  M: 14 74%
  NA: 0 0%
2009
  F: 5 26%
  M: 14 74%
  NA: 0 0%
2010
  F: 5 28%
  M: 13 72%
  NA: 0 0%
2011
  F: 4 22%
  M: 13 72%
  NA: 1 6%
2012
  F: 5 25%
  M: 14 70%
  NA: 1 5%
2013
  F: 4 21%
  M: 14 74%
  NA: 1 5%
2014
  F: 6 32%
  M: 12 63%
  NA: 1 5%
2015
  F: 6 33%
  M: 11 61%
  NA: 1 6%
~~~
