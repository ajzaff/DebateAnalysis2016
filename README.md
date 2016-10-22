# I analyzed every word of the Presidential debates using NLP.  Here's what I found...

## Introduction

I'm sad to admit this linguistic analysis did not give me any grand insight, or reveal any hidden patterns.  I guess it's true how they say your model is only as good as your data ;).  But, I had loads of fun processing this and I wanted to share it.

## Data

<table>
<tr>
<th></th>
<th>CLINTON</th>
<th>TRUMP</th>
</tr>
<tr>
<th>total tokens      (tokens)</th>
<td>2881</td>
<td>3718</td>
</tr>
<tr>
<th>total utterances   (lines)</th>
<td>94</td>
<td>129</td>
</tr>
<tr>
<th>vocab size        (tokens)</th>
<td>1210</td>
<td>1110</td>
</tr>
<tr>
<th>lexical diversity      (%)</th>
<td>42.00</td>
<td>29.85</td>
</tr>
<tr>
<th>average utterance (tokens)</th>
<td>30</td>
<td>28</td>
</tr>
<tr>
<th>positivity score       (%)</th>
<td>46.73</td>
<td>47.06</td>
</tr>
<tr>
<th>cut off other  (instances)</th>
<td>4</td>
<td>26</td>
</tr>
<tr>
<th>cut off moder  (instances)</th>
<td>8</td>
<td>29</td>
</tr>
<tr>
<th>applause       (instances)</th>
<td>4</td>
<td>5</td>
</tr>
<tr>
<th>laughter       (instances)</th>
<td>4</td>
<td>1</td>
</tr>
<tr>
<th colspan="2">top unigrams      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>39 think</td>
<td>53 country</td>
</tr>
<tr>
<th>2</th>
<td>36 well</td>
<td>47 going</td>
</tr>
<tr>
<th>3</th>
<td>33 people</td>
<td>44 look</td>
</tr>
<tr>
<th>4</th>
<td>30 donald</td>
<td>39 just</td>
</tr>
<tr>
<th>5</th>
<td>28 know</td>
<td>38 think</td>
</tr>
<tr>
<th>6</th>
<td>27 going</td>
<td>37 said</td>
</tr>
<tr>
<th>7</th>
<td>23 need</td>
<td>36 people</td>
</tr>
<tr>
<th>8</th>
<td>22 one</td>
<td>32 say</td>
</tr>
<tr>
<th>9</th>
<td>22 us</td>
<td>32 will</td>
</tr>
<tr>
<th>10</th>
<td>21 will</td>
<td>30 know</td>
</tr>
<tr>
<th>11</th>
<td>20 want</td>
<td>28 many</td>
</tr>
<tr>
<th>12</th>
<td>20 really</td>
<td>27 get</td>
</tr>
<tr>
<th>13</th>
<td>18 said</td>
<td>27 secretary</td>
</tr>
<tr>
<th>14</th>
<td>18 lot</td>
<td>25 one</td>
</tr>
<tr>
<th>15</th>
<td>17 good</td>
<td>24 want</td>
</tr>
<tr>
<th colspan="2">top positive      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>36 well</td>
<td>22 like</td>
</tr>
<tr>
<th>2</th>
<td>17 good</td>
<td>22 well</td>
</tr>
<tr>
<th>3</th>
<td>15 work</td>
<td>20 good</td>
</tr>
<tr>
<th>4</th>
<td>10 important</td>
<td>16 great</td>
</tr>
<tr>
<th>5</th>
<td>8 wealthy</td>
<td>13 right</td>
</tr>
<tr>
<th>6</th>
<td>8 support</td>
<td>12 better</td>
</tr>
<tr>
<th>7</th>
<td>6 better</td>
<td>7 work</td>
</tr>
<tr>
<th>8</th>
<td>6 right</td>
<td>7 greatest</td>
</tr>
<tr>
<th>9</th>
<td>6 worked</td>
<td>6 important</td>
</tr>
<tr>
<th>10</th>
<td>5 fair</td>
<td>6 endorsed</td>
</tr>
<tr>
<th>11</th>
<td>5 top</td>
<td>5 approve</td>
</tr>
<tr>
<th>12</th>
<td>4 like</td>
<td>4 love</td>
</tr>
<tr>
<th>13</th>
<td>4 benefit</td>
<td>4 tough</td>
</tr>
<tr>
<th>14</th>
<td>4 best</td>
<td>4 best</td>
</tr>
<tr>
<th>15</th>
<td>4 clear</td>
<td>4 advantage</td>
</tr>
<tr>
<th colspan="2">top negative      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>8 debt</td>
<td>16 bad</td>
</tr>
<tr>
<th>2</th>
<td>6 problems</td>
<td>13 wrong</td>
</tr>
<tr>
<th>3</th>
<td>5 criminal</td>
<td>7 worst</td>
</tr>
<tr>
<th>4</th>
<td>4 hack</td>
<td>7 losing</td>
</tr>
<tr>
<th>5</th>
<td>4 issues</td>
<td>6 problem</td>
</tr>
<tr>
<th>6</th>
<td>4 worst</td>
<td>6 mess</td>
</tr>
<tr>
<th>7</th>
<td>4 hard</td>
<td>5 killed</td>
</tr>
<tr>
<th>8</th>
<td>4 attacks</td>
<td>5 disaster</td>
</tr>
<tr>
<th>9</th>
<td>3 crime</td>
<td>5 debt</td>
</tr>
<tr>
<th>10</th>
<td>3 lose</td>
<td>5 terrible</td>
</tr>
<tr>
<th>11</th>
<td>3 racist</td>
<td>4 excuse</td>
</tr>
<tr>
<th>12</th>
<td>3 unfortunately</td>
<td>3 concerned</td>
</tr>
<tr>
<th>13</th>
<td>3 recession</td>
<td>3 terror</td>
</tr>
<tr>
<th>14</th>
<td>3 problem</td>
<td>3 hard</td>
</tr>
<tr>
<th>15</th>
<td>3 lie</td>
<td>3 fault</td>
</tr>
<tr>
<th colspan="2">top bigrams    (token x 2)</th>
</tr>
<tr>
<th>1</th>
<td>26 #BEGIN# well</td>
<td>22 secretary clinton</td>
</tr>
<tr>
<th>2</th>
<td>7 new jobs</td>
<td>14 #BEGIN# well</td>
</tr>
<tr>
<th>3</th>
<td>5 middle class</td>
<td>7 law order</td>
</tr>
<tr>
<th>4</th>
<td>5 #BEGIN# #END#</td>
<td>7 right now</td>
</tr>
<tr>
<th>5</th>
<td>5 tax returns</td>
<td>7 sean hannity</td>
</tr>
<tr>
<th>6</th>
<td>5 united states</td>
<td>7 will tell</td>
</tr>
<tr>
<th>7</th>
<td>5 criminal justice</td>
<td>6 trade deals</td>
</tr>
<tr>
<th>8</th>
<td>5 well think</td>
<td>6 country #END#</td>
</tr>
<tr>
<th>9</th>
<td>4 want see</td>
<td>6 #BEGIN# wrong</td>
</tr>
<tr>
<th>10</th>
<td>4 trade deals</td>
<td>6 middle east</td>
</tr>
<tr>
<th>11</th>
<td>4 want us</td>
<td>6 long time</td>
</tr>
<tr>
<th>12</th>
<td>4 secretary state</td>
<td>6 president obama</td>
</tr>
<tr>
<th>13</th>
<td>4 #BEGIN# think</td>
<td>6 inner cities</td>
</tr>
<tr>
<th>14</th>
<td>4 justice system</td>
<td>6 20 trillion</td>
</tr>
<tr>
<th>15</th>
<td>4 nuclear weapons</td>
<td>5 take look</td>
</tr>
<tr>
<th colspan="2">top trigrams   (token x 3)</th>
</tr>
<tr>
<th>1</th>
<td>5 #BEGIN# well think</td>
<td>4 need law order</td>
</tr>
<tr>
<th>2</th>
<td>4 criminal justice system</td>
<td>4 bring money back</td>
</tr>
<tr>
<th>3</th>
<td>3 jobs rising incomes</td>
<td>3 #BEGIN# well first</td>
</tr>
<tr>
<th>4</th>
<td>2 nine million people</td>
<td>3 #BEGIN# wrong wrong</td>
</tr>
<tr>
<th>5</th>
<td>2 million people lost</td>
<td>3 kind thinking country</td>
</tr>
<tr>
<th>6</th>
<td>2 federal income tax</td>
<td>3 like secretary clinton</td>
</tr>
<tr>
<th>7</th>
<td>2 justice system just</td>
<td>3 #BEGIN# say #END#</td>
</tr>
<tr>
<th>8</th>
<td>2 #BEGIN# well just</td>
<td>3 bring back jobs</td>
</tr>
<tr>
<th>9</th>
<td>2 5 trillion debt</td>
<td>3 obama fault #END#</td>
</tr>
<tr>
<th>10</th>
<td>2 #BEGIN# well actually</td>
<td>3 wrong wrong #END#</td>
</tr>
<tr>
<th>11</th>
<td>2 million new jobs</td>
<td>3 20 trillion debt</td>
</tr>
<tr>
<th>12</th>
<td>2 3 5 million</td>
<td>3 president obama fault</td>
</tr>
<tr>
<th>13</th>
<td>2 want us invest</td>
<td>3 thinking country needs</td>
</tr>
<tr>
<th>14</th>
<td>2 new jobs will</td>
<td>3 secretary clinton #END#</td>
</tr>
<tr>
<th>15</th>
<td>2 add 5 trillion</td>
<td>3 #BEGIN# wait minute</td>
</tr>
</table>
<table>
<tr>
<th></th>
<th>CLINTON</th>
<th>TRUMP</th>
</tr>
<tr>
<th>total tokens      (tokens)</th>
<td>2738</td>
<td>3067</td>
</tr>
<tr>
<th>total utterances   (lines)</th>
<td>37</td>
<td>64</td>
</tr>
<tr>
<th>vocab size        (tokens)</th>
<td>1131</td>
<td>1004</td>
</tr>
<tr>
<th>lexical diversity      (%)</th>
<td>41.31</td>
<td>32.74</td>
</tr>
<tr>
<th>average utterance (tokens)</th>
<td>74</td>
<td>47</td>
</tr>
<tr>
<th>positivity score       (%)</th>
<td>49.39</td>
<td>38.56</td>
</tr>
<tr>
<th>cut off other  (instances)</th>
<td>0</td>
<td>1</td>
</tr>
<tr>
<th>cut off moder  (instances)</th>
<td>1</td>
<td>2</td>
</tr>
<tr>
<th>applause       (instances)</th>
<td>1</td>
<td>1</td>
</tr>
<tr>
<th>laughter       (instances)</th>
<td>0</td>
<td>0</td>
</tr>
<tr>
<th colspan="2">top unigrams      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>46 people</td>
<td>50 people</td>
</tr>
<tr>
<th>2</th>
<td>34 want</td>
<td>39 going</td>
</tr>
<tr>
<th>3</th>
<td>33 donald</td>
<td>35 will</td>
</tr>
<tr>
<th>4</th>
<td>32 think</td>
<td>34 know</td>
</tr>
<tr>
<th>5</th>
<td>28 lot</td>
<td>33 country</td>
</tr>
<tr>
<th>6</th>
<td>27 get</td>
<td>32 look</td>
</tr>
<tr>
<th>7</th>
<td>27 country</td>
<td>27 hillary</td>
</tr>
<tr>
<th>8</th>
<td>24 will</td>
<td>27 said</td>
</tr>
<tr>
<th>9</th>
<td>23 president</td>
<td>27 like</td>
</tr>
<tr>
<th>10</th>
<td>23 said</td>
<td>25 say</td>
</tr>
<tr>
<th>11</th>
<td>17 just</td>
<td>22 now</td>
</tr>
<tr>
<th>12</th>
<td>17 know</td>
<td>21 great</td>
</tr>
<tr>
<th>13</th>
<td>16 insurance</td>
<td>21 one</td>
</tr>
<tr>
<th>14</th>
<td>16 going</td>
<td>20 think</td>
</tr>
<tr>
<th>15</th>
<td>15 first</td>
<td>20 get</td>
</tr>
<tr>
<th colspan="2">top positive      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>14 well</td>
<td>27 like</td>
</tr>
<tr>
<th>2</th>
<td>13 important</td>
<td>21 great</td>
</tr>
<tr>
<th>3</th>
<td>13 like</td>
<td>11 well</td>
</tr>
<tr>
<th>4</th>
<td>13 work</td>
<td>9 respect</td>
</tr>
<tr>
<th>5</th>
<td>11 supreme</td>
<td>8 right</td>
</tr>
<tr>
<th>6</th>
<td>10 great</td>
<td>7 good</td>
</tr>
<tr>
<th>7</th>
<td>9 right</td>
<td>6 proud</td>
</tr>
<tr>
<th>8</th>
<td>8 worked</td>
<td>6 wonderful</td>
</tr>
<tr>
<th>9</th>
<td>7 good</td>
<td>6 important</td>
</tr>
<tr>
<th>10</th>
<td>6 affordable</td>
<td>5 endorsed</td>
</tr>
<tr>
<th>11</th>
<td>6 proud</td>
<td>4 fair</td>
</tr>
<tr>
<th>12</th>
<td>5 respect</td>
<td>4 safe</td>
</tr>
<tr>
<th>13</th>
<td>5 support</td>
<td>4 effective</td>
</tr>
<tr>
<th>14</th>
<td>5 better</td>
<td>4 honest</td>
</tr>
<tr>
<th>15</th>
<td>4 best</td>
<td>3 fine</td>
</tr>
<tr>
<th colspan="2">top negative      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>6 lost</td>
<td>16 bad</td>
</tr>
<tr>
<th>2</th>
<td>5 hard</td>
<td>14 disaster</td>
</tr>
<tr>
<th>3</th>
<td>5 mistake</td>
<td>7 killing</td>
</tr>
<tr>
<th>4</th>
<td>4 sorry</td>
<td>7 problem</td>
</tr>
<tr>
<th>5</th>
<td>4 wrong</td>
<td>6 lied</td>
</tr>
<tr>
<th>6</th>
<td>3 worried</td>
<td>6 problems</td>
</tr>
<tr>
<th>7</th>
<td>2 catastrophic</td>
<td>6 subpoena</td>
</tr>
<tr>
<th>8</th>
<td>2 loophole</td>
<td>5 lost</td>
</tr>
<tr>
<th>9</th>
<td>2 issues</td>
<td>5 horrible</td>
</tr>
<tr>
<th>10</th>
<td>2 concerns</td>
<td>5 expensive</td>
</tr>
<tr>
<th>11</th>
<td>2 loopholes</td>
<td>5 worse</td>
</tr>
<tr>
<th>12</th>
<td>2 dark</td>
<td>4 irredeemable</td>
</tr>
<tr>
<th>13</th>
<td>2 problem</td>
<td>4 disagree</td>
</tr>
<tr>
<th>14</th>
<td>2 terrible</td>
<td>4 lie</td>
</tr>
<tr>
<th>15</th>
<td>2 dangerous</td>
<td>3 hate</td>
</tr>
<tr>
<th colspan="2">top bigrams    (token x 2)</th>
</tr>
<tr>
<th>1</th>
<td>11 supreme court</td>
<td>13 hillary clinton</td>
</tr>
<tr>
<th>2</th>
<td>10 #BEGIN# well</td>
<td>12 united states</td>
</tr>
<tr>
<th>3</th>
<td>8 donald trump</td>
<td>10 inner cities</td>
</tr>
<tr>
<th>4</th>
<td>8 health insurance</td>
<td>9 take look</td>
</tr>
<tr>
<th>5</th>
<td>5 never apologized</td>
<td>9 will tell</td>
</tr>
<tr>
<th>6</th>
<td>5 care act</td>
<td>6 bernie sanders</td>
</tr>
<tr>
<th>7</th>
<td>5 affordable care</td>
<td>6 make america</td>
</tr>
<tr>
<th>8</th>
<td>5 30 years</td>
<td>6 president obama</td>
</tr>
<tr>
<th>9</th>
<td>5 make sure</td>
<td>6 bad judgment</td>
</tr>
<tr>
<th>10</th>
<td>4 want see</td>
<td>5 know nothing</td>
</tr>
<tr>
<th>11</th>
<td>4 insurance companies</td>
<td>5 people will</td>
</tr>
<tr>
<th>12</th>
<td>4 hillaryclinton com</td>
<td>5 33 000</td>
</tr>
<tr>
<th>13</th>
<td>4 go hillaryclinton</td>
<td>5 carried interest</td>
</tr>
<tr>
<th>14</th>
<td>4 secretary state</td>
<td>5 energy companies</td>
</tr>
<tr>
<th>15</th>
<td>4 president will</td>
<td>4 take care</td>
</tr>
<tr>
<th colspan="2">top trigrams   (token x 3)</th>
</tr>
<tr>
<th>1</th>
<td>5 affordable care act</td>
<td>4 gonna make america</td>
</tr>
<tr>
<th>2</th>
<td>4 go hillaryclinton com</td>
<td>4 locker room talk</td>
</tr>
<tr>
<th>3</th>
<td>4 want supreme court</td>
<td>3 make america great</td>
</tr>
<tr>
<th>4</th>
<td>2 get health insurance</td>
<td>3 3 o clock</td>
</tr>
<tr>
<th>5</th>
<td>2 people get health</td>
<td>3 o clock morning</td>
</tr>
<tr>
<th>6</th>
<td>2 people used arguments</td>
<td>3 hillary clinton wants</td>
</tr>
<tr>
<th>7</th>
<td>2 30 years public</td>
<td>3 old post office</td>
</tr>
<tr>
<th>8</th>
<td>2 middle class families</td>
<td>2 pay hundreds millions</td>
</tr>
<tr>
<th>9</th>
<td>2 time president will</td>
<td>2 carried interest provision</td>
</tr>
<tr>
<th>10</th>
<td>2 respect one another</td>
<td>2 done effective senator</td>
</tr>
<tr>
<th>11</th>
<td>2 get health care</td>
<td>2 subpoena united states</td>
</tr>
<tr>
<th>12</th>
<td>2 20 million people</td>
<td>2 putting energy companies</td>
</tr>
<tr>
<th>13</th>
<td>2 supreme court justices</td>
<td>2 delete 33 000</td>
</tr>
<tr>
<th>14</th>
<td>2 court will stick</td>
<td>2 rid carried interest</td>
</tr>
<tr>
<th>15</th>
<td>2 one another will</td>
<td>2 gold standard said</td>
</tr>
</table>
<table>
<tr>
<th></th>
<th>CLINTON</th>
<th>TRUMP</th>
</tr>
<tr>
<th>total tokens      (tokens)</th>
<td>3090</td>
<td>2817</td>
</tr>
<tr>
<th>total utterances   (lines)</th>
<td>67</td>
<td>94</td>
</tr>
<tr>
<th>vocab size        (tokens)</th>
<td>1250</td>
<td>910</td>
</tr>
<tr>
<th>lexical diversity      (%)</th>
<td>40.45</td>
<td>32.30</td>
</tr>
<tr>
<th>average utterance (tokens)</th>
<td>46</td>
<td>29</td>
</tr>
<tr>
<th>positivity score       (%)</th>
<td>46.60</td>
<td>38.65</td>
</tr>
<tr>
<th>cut off other  (instances)</th>
<td>1</td>
<td>9</td>
</tr>
<tr>
<th>cut off moder  (instances)</th>
<td>4</td>
<td>16</td>
</tr>
<tr>
<th>applause       (instances)</th>
<td>1</td>
<td>1</td>
</tr>
<tr>
<th>laughter       (instances)</th>
<td>0</td>
<td>2</td>
</tr>
<tr>
<th colspan="2">top unigrams      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>43 will</td>
<td>72 going</td>
</tr>
<tr>
<th>2</th>
<td>38 think</td>
<td>53 people</td>
</tr>
<tr>
<th>3</th>
<td>37 people</td>
<td>36 will</td>
</tr>
<tr>
<th>4</th>
<td>34 going</td>
<td>31 now</td>
</tr>
<tr>
<th>5</th>
<td>31 donald</td>
<td>29 country</td>
</tr>
<tr>
<th>6</th>
<td>30 said</td>
<td>26 know</td>
</tr>
<tr>
<th>7</th>
<td>28 well</td>
<td>25 look</td>
</tr>
<tr>
<th>8</th>
<td>25 women</td>
<td>24 get</td>
</tr>
<tr>
<th>9</th>
<td>25 country</td>
<td>24 think</td>
</tr>
<tr>
<th>10</th>
<td>24 know</td>
<td>23 say</td>
</tr>
<tr>
<th>11</th>
<td>23 want</td>
<td>23 just</td>
</tr>
<tr>
<th>12</th>
<td>23 get</td>
<td>22 many</td>
</tr>
<tr>
<th>13</th>
<td>23 president</td>
<td>21 take</td>
</tr>
<tr>
<th>14</th>
<td>23 make</td>
<td>20 way</td>
</tr>
<tr>
<th>15</th>
<td>20 just</td>
<td>19 go</td>
</tr>
<tr>
<th colspan="2">top positive      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>28 well</td>
<td>19 great</td>
</tr>
<tr>
<th>2</th>
<td>15 work</td>
<td>17 well</td>
</tr>
<tr>
<th>3</th>
<td>11 clear</td>
<td>16 right</td>
</tr>
<tr>
<th>4</th>
<td>10 like</td>
<td>10 like</td>
</tr>
<tr>
<th>5</th>
<td>9 great</td>
<td>7 strong</td>
</tr>
<tr>
<th>6</th>
<td>8 right</td>
<td>6 tougher</td>
</tr>
<tr>
<th>7</th>
<td>7 important</td>
<td>6 respect</td>
</tr>
<tr>
<th>8</th>
<td>6 good</td>
<td>6 good</td>
</tr>
<tr>
<th>9</th>
<td>6 wealthy</td>
<td>5 thank</td>
</tr>
<tr>
<th>10</th>
<td>5 supported</td>
<td>5 better</td>
</tr>
<tr>
<th>11</th>
<td>5 reform</td>
<td>4 greatest</td>
</tr>
<tr>
<th>12</th>
<td>5 support</td>
<td>3 fame</td>
</tr>
<tr>
<th>13</th>
<td>5 supreme</td>
<td>3 love</td>
</tr>
<tr>
<th>14</th>
<td>4 intelligence</td>
<td>3 important</td>
</tr>
<tr>
<th>15</th>
<td>4 protect</td>
<td>3 proud</td>
</tr>
<tr>
<th colspan="2">top negative      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>11 debt</td>
<td>18 bad</td>
</tr>
<tr>
<th>2</th>
<td>9 undocumented</td>
<td>10 disaster</td>
</tr>
<tr>
<th>3</th>
<td>5 hard</td>
<td>6 wrong</td>
</tr>
<tr>
<th>4</th>
<td>4 issue</td>
<td>4 worse</td>
</tr>
<tr>
<th>5</th>
<td>4 attacks</td>
<td>4 false</td>
</tr>
<tr>
<th>6</th>
<td>4 terrible</td>
<td>4 fiction</td>
</tr>
<tr>
<th>7</th>
<td>4 dangerous</td>
<td>4 sad</td>
</tr>
<tr>
<th>8</th>
<td>4 conflict</td>
<td>3 criminal</td>
</tr>
<tr>
<th>9</th>
<td>3 issues</td>
<td>3 worst</td>
</tr>
<tr>
<th>10</th>
<td>3 worst</td>
<td>3 killed</td>
</tr>
<tr>
<th>11</th>
<td>3 recession</td>
<td>3 lost</td>
</tr>
<tr>
<th>12</th>
<td>2 kill</td>
<td>3 horrible</td>
</tr>
<tr>
<th>13</th>
<td>2 loophole</td>
<td>3 problem</td>
</tr>
<tr>
<th>14</th>
<td>2 dark</td>
<td>3 terrible</td>
</tr>
<tr>
<th>15</th>
<td>2 lost</td>
<td>3 lied</td>
</tr>
<tr>
<th colspan="2">top bigrams    (token x 2)</th>
</tr>
<tr>
<th>1</th>
<td>24 #BEGIN# well</td>
<td>11 #BEGIN# well</td>
</tr>
<tr>
<th>2</th>
<td>7 second amendment</td>
<td>9 second amendment</td>
</tr>
<tr>
<th>3</th>
<td>6 united states</td>
<td>9 take look</td>
</tr>
<tr>
<th>4</th>
<td>6 president obama</td>
<td>8 millions people</td>
</tr>
<tr>
<th>5</th>
<td>6 donald thinks</td>
<td>7 united states</td>
</tr>
<tr>
<th>6</th>
<td>5 roe v</td>
<td>6 open borders</td>
</tr>
<tr>
<th>7</th>
<td>5 supreme court</td>
<td>6 right now</td>
</tr>
<tr>
<th>8</th>
<td>5 new jobs</td>
<td>6 going get</td>
</tr>
<tr>
<th>9</th>
<td>5 v wade</td>
<td>6 hillary clinton</td>
</tr>
<tr>
<th>10</th>
<td>4 planned parenthood</td>
<td>5 #BEGIN# wrong</td>
</tr>
<tr>
<th>11</th>
<td>4 well first</td>
<td>5 wrong #END#</td>
</tr>
<tr>
<th>12</th>
<td>4 make sure</td>
<td>5 strong borders</td>
</tr>
<tr>
<th>13</th>
<td>4 want us</td>
<td>5 one thing</td>
</tr>
<tr>
<th>14</th>
<td>4 will stand</td>
<td>4 6 billion</td>
</tr>
<tr>
<th>15</th>
<td>4 tax cuts</td>
<td>4 trade deals</td>
</tr>
<tr>
<th colspan="2">top trigrams   (token x 3)</th>
</tr>
<tr>
<th>1</th>
<td>5 roe v wade</td>
<td>5 #BEGIN# wrong #END#</td>
</tr>
<tr>
<th>2</th>
<td>4 #BEGIN# well first</td>
<td>4 #BEGIN# well first</td>
</tr>
<tr>
<th>3</th>
<td>3 federal income tax</td>
<td>4 wants open borders</td>
</tr>
<tr>
<th>4</th>
<td>3 #BEGIN# well chris</td>
<td>3 #BEGIN# say #END#</td>
</tr>
<tr>
<th>5</th>
<td>2 17 intelligence agencies</td>
<td>3 going make america</td>
</tr>
<tr>
<th>6</th>
<td>2 released tax returns</td>
<td>3 make america great</td>
</tr>
<tr>
<th>7</th>
<td>2 30 years experience</td>
<td>3 put american flag</td>
</tr>
<tr>
<th>8</th>
<td>2 plan think will</td>
<td>2 fisher house build</td>
</tr>
<tr>
<th>9</th>
<td>2 know president obama</td>
<td>2 sanders said bad</td>
</tr>
<tr>
<th>10</th>
<td>2 add penny debt</td>
<td>2 1 7 billion</td>
</tr>
<tr>
<th>11</th>
<td>2 get ahead stay</td>
<td>2 gave 1 7</td>
</tr>
<tr>
<th>12</th>
<td>2 middle class families</td>
<td>2 wants give amnesty</td>
</tr>
<tr>
<th>13</th>
<td>2 massive tax cuts</td>
<td>2 baby rip baby</td>
</tr>
<tr>
<th>14</th>
<td>2 mother taken account</td>
<td>2 iran taking iraq</td>
</tr>
<tr>
<th>15</th>
<td>2 affordable care act</td>
<td>2 #BEGIN# criminal enterprise</td>
</tr>
</table>
<table>
<tr>
<th></th>
<th>KAINE</th>
<th>PENCE</th>
</tr>
<tr>
<th>total tokens      (tokens)</th>
<td>3852</td>
<td>3783</td>
</tr>
<tr>
<th>total utterances   (lines)</th>
<td>192</td>
<td>214</td>
</tr>
<tr>
<th>vocab size        (tokens)</th>
<td>1294</td>
<td>1283</td>
</tr>
<tr>
<th>lexical diversity      (%)</th>
<td>33.59</td>
<td>33.91</td>
</tr>
<tr>
<th>average utterance (tokens)</th>
<td>20</td>
<td>17</td>
</tr>
<tr>
<th>positivity score       (%)</th>
<td>51.03</td>
<td>53.50</td>
</tr>
<tr>
<th>cut off other  (instances)</th>
<td>39</td>
<td>47</td>
</tr>
<tr>
<th>cut off moder  (instances)</th>
<td>3</td>
<td>19</td>
</tr>
<tr>
<th>applause       (instances)</th>
<td>0</td>
<td>0</td>
</tr>
<tr>
<th>laughter       (instances)</th>
<td>0</td>
<td>1</td>
</tr>
<tr>
<th colspan="2">top unigrams      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>82 trump</td>
<td>61 clinton</td>
</tr>
<tr>
<th>2</th>
<td>72 donald</td>
<td>51 hillary</td>
</tr>
<tr>
<th>3</th>
<td>56 said</td>
<td>50 trump</td>
</tr>
<tr>
<th>4</th>
<td>45 hillary</td>
<td>47 donald</td>
</tr>
<tr>
<th>5</th>
<td>39 governor</td>
<td>45 senator</td>
</tr>
<tr>
<th>6</th>
<td>35 clinton</td>
<td>43 going</td>
</tr>
<tr>
<th>7</th>
<td>33 pence</td>
<td>40 american</td>
</tr>
<tr>
<th>8</th>
<td>32 will</td>
<td>38 people</td>
</tr>
<tr>
<th>9</th>
<td>29 just</td>
<td>35 just</td>
</tr>
<tr>
<th>10</th>
<td>26 want</td>
<td>34 said</td>
</tr>
<tr>
<th>11</th>
<td>24 elaine</td>
<td>31 well</td>
</tr>
<tr>
<th>12</th>
<td>23 plan</td>
<td>25 state</td>
</tr>
<tr>
<th>13</th>
<td>23 get</td>
<td>25 know</td>
</tr>
<tr>
<th>14</th>
<td>23 know</td>
<td>24 states</td>
</tr>
<tr>
<th>15</th>
<td>22 going</td>
<td>24 united</td>
</tr>
<tr>
<th colspan="2">top positive      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>16 work</td>
<td>31 well</td>
</tr>
<tr>
<th>2</th>
<td>14 like</td>
<td>12 thank</td>
</tr>
<tr>
<th>3</th>
<td>14 well</td>
<td>11 great</td>
</tr>
<tr>
<th>4</th>
<td>13 great</td>
<td>10 reform</td>
</tr>
<tr>
<th>5</th>
<td>13 worked</td>
<td>9 right</td>
</tr>
<tr>
<th>6</th>
<td>11 support</td>
<td>8 work</td>
</tr>
<tr>
<th>7</th>
<td>11 important</td>
<td>7 like</td>
</tr>
<tr>
<th>8</th>
<td>10 intelligence</td>
<td>7 stronger</td>
</tr>
<tr>
<th>9</th>
<td>9 good</td>
<td>6 good</td>
</tr>
<tr>
<th>10</th>
<td>8 right</td>
<td>6 faith</td>
</tr>
<tr>
<th>11</th>
<td>8 trust</td>
<td>5 freedom</td>
</tr>
<tr>
<th>12</th>
<td>8 top</td>
<td>4 better</td>
</tr>
<tr>
<th>13</th>
<td>7 better</td>
<td>4 safe</td>
</tr>
<tr>
<th>14</th>
<td>5 smart</td>
<td>4 strong</td>
</tr>
<tr>
<th>15</th>
<td>5 strong</td>
<td>4 support</td>
</tr>
<tr>
<th colspan="2">top negative      (tokens)</th>
</tr>
<tr>
<th>1</th>
<td>8 dangerous</td>
<td>13 criminal</td>
</tr>
<tr>
<th>2</th>
<td>5 issues</td>
<td>7 bias</td>
</tr>
<tr>
<th>3</th>
<td>4 death</td>
<td>5 failed</td>
</tr>
<tr>
<th>4</th>
<td>4 hard</td>
<td>5 hard</td>
</tr>
<tr>
<th>5</th>
<td>4 poverty</td>
<td>5 debt</td>
</tr>
<tr>
<th>6</th>
<td>4 threat</td>
<td>5 tragedy</td>
</tr>
<tr>
<th>7</th>
<td>4 terrorism</td>
<td>5 nonsense</td>
</tr>
<tr>
<th>8</th>
<td>3 penalty</td>
<td>4 avalanche</td>
</tr>
<tr>
<th>9</th>
<td>3 killed</td>
<td>4 weak</td>
</tr>
<tr>
<th>10</th>
<td>3 bad</td>
<td>4 overrun</td>
</tr>
<tr>
<th>11</th>
<td>3 obsolete</td>
<td>3 struggling</td>
</tr>
<tr>
<th>12</th>
<td>3 recession</td>
<td>3 loss</td>
</tr>
<tr>
<th>13</th>
<td>3 problem</td>
<td>3 feckless</td>
</tr>
<tr>
<th>14</th>
<td>3 punish</td>
<td>3 bad</td>
</tr>
<tr>
<th>15</th>
<td>3 criminal</td>
<td>3 false</td>
</tr>
<tr>
<th colspan="2">top bigrams    (token x 2)</th>
</tr>
<tr>
<th>1</th>
<td>71 donald trump</td>
<td>51 hillary clinton</td>
</tr>
<tr>
<th>2</th>
<td>27 hillary clinton</td>
<td>47 donald trump</td>
</tr>
<tr>
<th>3</th>
<td>23 governor pence</td>
<td>24 united states</td>
</tr>
<tr>
<th>4</th>
<td>16 vladimir putin</td>
<td>24 #BEGIN# well</td>
</tr>
<tr>
<th>5</th>
<td>15 nuclear weapons</td>
<td>14 american people</td>
</tr>
<tr>
<th>6</th>
<td>13 #BEGIN# elaine</td>
<td>12 senator kaine</td>
</tr>
<tr>
<th>7</th>
<td>12 united states</td>
<td>11 president united</td>
</tr>
<tr>
<th>8</th>
<td>10 #BEGIN# well</td>
<td>10 law enforcement</td>
</tr>
<tr>
<th>9</th>
<td>10 tax returns</td>
<td>10 secretary state</td>
</tr>
<tr>
<th>10</th>
<td>10 #BEGIN# donald</td>
<td>10 barack obama</td>
</tr>
<tr>
<th>11</th>
<td>9 secretary state</td>
<td>9 states america</td>
</tr>
<tr>
<th>12</th>
<td>9 #BEGIN# governor</td>
<td>9 clinton foundation</td>
</tr>
<tr>
<th>13</th>
<td>8 running mate</td>
<td>8 foreign policy</td>
</tr>
<tr>
<th>14</th>
<td>8 trump said</td>
<td>7 clinton barack</td>
</tr>
<tr>
<th>15</th>
<td>7 weapons program</td>
<td>7 #BEGIN# senator</td>
</tr>
<tr>
<th colspan="2">top trigrams   (token x 3)</th>
</tr>
<tr>
<th>1</th>
<td>9 #BEGIN# donald trump</td>
<td>11 president united states</td>
</tr>
<tr>
<th>2</th>
<td>8 donald trump said</td>
<td>9 united states america</td>
</tr>
<tr>
<th>3</th>
<td>7 nuclear weapons program</td>
<td>7 hillary clinton barack</td>
</tr>
<tr>
<th>4</th>
<td>6 #BEGIN# governor pence</td>
<td>7 clinton barack obama</td>
</tr>
<tr>
<th>5</th>
<td>5 iranian nuclear weapons</td>
<td>5 clinton tim kaine</td>
</tr>
<tr>
<th>6</th>
<td>4 defend running mate</td>
<td>5 hillary clinton tim</td>
</tr>
<tr>
<th>7</th>
<td>4 hillary clinton secretary</td>
<td>5 security american people</td>
</tr>
<tr>
<th>8</th>
<td>4 without firing shot</td>
<td>5 safety security american</td>
</tr>
<tr>
<th>9</th>
<td>4 clinton secretary state</td>
<td>4 #BEGIN# well first</td>
</tr>
<tr>
<th>10</th>
<td>4 governor pence #END#</td>
<td>4 #BEGIN# donald trump</td>
</tr>
<tr>
<th>11</th>
<td>4 donald trump donald</td>
<td>4 criminal justice reform</td>
</tr>
<tr>
<th>12</th>
<td>4 trump donald trump</td>
<td>4 syrian refugee program</td>
</tr>
<tr>
<th>13</th>
<td>4 vladimir putin great</td>
<td>4 operation iraqi freedom</td>
</tr>
<tr>
<th>14</th>
<td>4 mexicans rapists criminals</td>
<td>4 america place world</td>
</tr>
<tr>
<th>15</th>
<td>4 release tax returns</td>
<td>4 private server #END#</td>
</tr>
</table>


## Credits

All debate transcripts are &copy; their respective owners.

- *First Debate*: Washington Post Online: http://www.nytimes.com/2016/09/27/us/politics/transcript-debate.html
- *Second Debate*: NY Times Online: http://www.nytimes.com/2016/10/10/us/politics/transcript-second-debate.html
- *Third Debate*: Politico: http://www.politico.com/story/2016/10/full-transcript-third-2016-presidential-debate-230063
- *VP Debate*: Washington Post Online: https://www.washingtonpost.com/news/the-fix/wp/2016/10/04/the-mike-pence-vs-tim-kaine-vice-presidential-debate-transcript-annotated/

The sentiment corpus was produced by a research team from University of Illinois at Chicago.

- *Sentiment Word Lists*: Jeffrey Breen: https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107

```Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
  Proceedings of the ACM SIGKDD International Conference on Knowledge 
  Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
  Washington, USA,```

```Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
  and Comparing Opinions on the Web." Proceedings of the 14th 
  International World Wide Web conference (WWW-2005), May 10-14, 
  2005, Chiba, Japan.```

License included in `data/vendor/LICENSE`