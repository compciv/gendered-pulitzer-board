
# Gender Analysis of the Pulitzer Prize Board

Analyzing the gender makeup of the Pulitzer Prize Board membership since 1968, [according to the Pulitzer website](http://www.pulitzer.org/board/1968). The gender of the 

Why 1968? Because I don't have time to reverse-engineer the [data-structure of this Angular-heavy site](http://www.pulitzer.org/cache/api/1/global.json). Even though there are webpages for every board since 1917, they don't seem to be serialized in the same way as the years [1968-and-on](pulitzer-taxonomy.csv). Oh well.


## Findings

In the time period of 1968 to the current year, an estimated __40+ women__ have served on the Pulitzer Prize board compared to __170+ men__.

Note that the gender detection algorithm for this project was extremely basic: literally, determining if the first name of each board member was more likely to belong to a man versus a woman, according to how babies are named, via the Social Security Administration data. No attempt was done for close-calls (though there don't seem to be many of those) -- and people such as __C.K.McClatchy__ are just left out.

However, a quick spot-check of the Pulitzer website seems to confirm the broad generalizations of the analysis. For example, the algorithm did not find a single woman on the board in the 1970s.

For reference, this is a picture of the [1970 board membership](http://www.pulitzer.org/board/1970):

![http://www.pulitzer.org/cms/sites/default/files/1970boardpic500_0.jpg](http://www.pulitzer.org/cms/sites/default/files/1970boardpic500_0.jpg)


And this is a picture of the [1979 board membership](http://www.pulitzer.org/board/1979):

![http://www.pulitzer.org/cms/sites/default/files/1979boardphoto500.jpg](http://www.pulitzer.org/cms/sites/default/files/1979boardphoto500.jpg)


The algorithm detects its [first woman in 1980](http://www.pulitzer.org/board/1980): __Hanna H. Gray, president, University of Chicago__


![http://www.pulitzer.org/cms/sites/default/files/1980boardphoto960.jpg](http://www.pulitzer.org/cms/sites/default/files/1980boardphoto960.jpg)






## Facets of analysis

The following facets were analyzed:

### Across the overall membership


### Board membership by decade


### Board membership by year


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
  F: 42
  M: 172
  F/M: 24%
-----------------------------------------
Now let's do a decade-by-decade breakdown
1960
  F: 0
  M: 16
  F/M: 0%
1970
  F: 0
  M: 32
  F/M: 0%
1980
  F: 6
  M: 57
  F/M: 11%
1990
  F: 16
  M: 47
  F/M: 34%
2000
  F: 17
  M: 43
  F/M: 40%
2010
  F: 12
  M: 28
  F/M: 43%
-----------------------------------------
Now let's do a year-by-year breakdown
1968
  F: 0
  M: 11
  F/M: 0%
1969
  F: 0
  M: 12
  F/M: 0%
1970
  F: 0
  M: 13
  F/M: 0%
1971
  F: 0
  M: 13
  F/M: 0%
1972
  F: 0
  M: 13
  F/M: 0%
1973
  F: 0
  M: 13
  F/M: 0%
1974
  F: 0
  M: 13
  F/M: 0%
1975
  F: 0
  M: 13
  F/M: 0%
1976
  F: 0
  M: 0
  F/M: 0%
1977
  F: 0
  M: 15
  F/M: 0%
1978
  F: 0
  M: 15
  F/M: 0%
1979
  F: 0
  M: 15
  F/M: 0%
1980
  F: 1
  M: 16
  F/M: 6%
1981
  F: 2
  M: 15
  F/M: 13%
1982
  F: 2
  M: 15
  F/M: 13%
1983
  F: 3
  M: 14
  F/M: 21%
1984
  F: 2
  M: 15
  F/M: 13%
1985
  F: 2
  M: 15
  F/M: 13%
1986
  F: 2
  M: 15
  F/M: 13%
1987
  F: 3
  M: 13
  F/M: 23%
1988
  F: 2
  M: 14
  F/M: 14%
1989
  F: 3
  M: 13
  F/M: 23%
1990
  F: 4
  M: 13
  F/M: 31%
1991
  F: 5
  M: 13
  F/M: 38%
1992
  F: 5
  M: 13
  F/M: 38%
1993
  F: 5
  M: 13
  F/M: 38%
1994
  F: 5
  M: 12
  F/M: 42%
1995
  F: 6
  M: 12
  F/M: 50%
1996
  F: 6
  M: 12
  F/M: 50%
1997
  F: 6
  M: 11
  F/M: 55%
1998
  F: 5
  M: 15
  F/M: 33%
1999
  F: 5
  M: 15
  F/M: 33%
2000
  F: 4
  M: 16
  F/M: 25%
2001
  F: 4
  M: 15
  F/M: 27%
2002
  F: 3
  M: 15
  F/M: 20%
2003
  F: 4
  M: 16
  F/M: 25%
2004
  F: 5
  M: 16
  F/M: 31%
2005
  F: 4
  M: 15
  F/M: 27%
2006
  F: 4
  M: 15
  F/M: 27%
2007
  F: 5
  M: 15
  F/M: 33%
2008
  F: 5
  M: 14
  F/M: 36%
2009
  F: 5
  M: 14
  F/M: 36%
2010
  F: 5
  M: 13
  F/M: 38%
2011
  F: 4
  M: 13
  F/M: 31%
2012
  F: 5
  M: 14
  F/M: 36%
2013
  F: 2
  M: 14
  F/M: 14%
2014
  F: 4
  M: 12
  F/M: 33%
2015
  F: 4
  M: 11
  F/M: 36%
~~~
