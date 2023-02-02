**ABSTRACT**

Online social media have been widely used in daily life as a way to express individual attitudes and emotions and communicate with friends. Information about many significant events in society often spreads on the Internet first. As a typical representative, Twitter has become one of the most popular website applications for micro-blogging services, fully demonstrating its strength as an effective medium. Numerous people publish and share information on Twitter, and local discussions launched by several users can cause public responses and propagate via a global scope. Research on Twitter can thus provide valuable insight into understanding information diffusion on social networking sites. To understand and model the spread of information, in this paper we leveraged the EXO-SIR model(Susceptible, Infected and Recovered) epidemiological model to describe the underlying process and delineate the spread of information on Twitter. The EXO-SIR model is an extension of the SIR model and other few variants of the model. Firstly, we obtained data from Twitter covering the period from 1st January 2022 to 29th December 2022, with a focus on trending hashtags. Second, using python libraries, we try to calculate the average time it takes for an infected person to get fully recovered. Our analysis shows the information can be modelled using the concept of epidemiology. We demonstrate that our approach is accurate at capturing diffusion in these events. Our approach can be fruitfully combined with other strategies that use content modelling and graph theoretic features to detect (and possibly disrupt) rumours.

**INTRODUCTION**

**The area of work**

In recent times, social media has become one of the most important sources of information for information consumers all over the world. According to a Pew Research report, the number of Americans who obtain their news through social media instead of print newspapers has drastically increased. In this race of different social medias Twitter due to its popularity, accessibility, low-barrier for publication and crowd-sourced nature, Twitter is faced with the risk of rapid dissemination of misinformation. The ability to post information on Twitter immediately after an event occurs, or even as it is occurring, causes the reliability of the news to potentially be questionable.

The area of work in the context of Twitter and the exo-SIR information spread model is the study of the spread of information on social media platforms, specifically Twitter, through endogenous (local) and exogenous (external) factors. The aim is to understand and model the information diffusion process in order to predict and mitigate the spread of false or harmful information.

**Problem Addressed**

We are trying to study the spread of information on social media by applying epidemiological models. In this project we try to implement the EXO-SIR model on the dataset to calculate the average time between the transition of a person from infected to recovered state by using different python libraries

**Existing System**

→ **Information diffusion**

Significant work has gone into research on information diffusion on social media. Gomez-Rodriguez et al. [6] built a cascade transmission model to track cascading process taking place over a network; they traced overall blogs and news for a one-year period and found that the top 1000 media sites and blogs tend to have a core-periphery structure.

→ **Epidemiological models**

Mathematical modelling of disease spread not only provides vital information about the propagation of the disease in a human network, but also offers insight into the strategies that can be used to control them **.** There has been many researches in this context applying different models such as SIEZ( susceptible (S), exposed (E), infected (I), and recovered (R) )and SIS(susceptible (S), infected (I)and susceptible) states on various social media platforms and in especially twitter dataset .

→ **Rumour Modelling**

As far as we know, Daley first proposed the similarity between epidemics and rumours using mathematical analysis. Some researchers have studied rumour propagation modelling in different network topologies however, they do not provide any discussion of propagation differences between news and rumours. In Budak et al. prove that minimising the spread of the misinformation (i.e., rumours) in social networks is an NP-hard problem and also provide a greedy approximate solution.

**Works on Epidemics models used for the study of information diffusion in social media**

Epidemic models are a crucial tool in the study of information diffusion in social media. These models aim to simulate the spread of information in a social network and understand the underlying mechanisms that govern the process. The models used in this field are often adaptations of classical epidemiology models, such as the Susceptible-Infected-Recovered (SIR) and Susceptible-Exposed-Infected-Recovered (SEIR) models, to suit the context of information diffusion. Other popular models include the Independent Cascade Model, the Linear Threshold Model, the Time-Dependent SEIR Model, the Multi-Group SIR Model, the Contact Network Model, the Bond Percolation Model, the Exponential Random Graph Model (ERGMs), and the Hawkes Process Model. These models provide valuable insights into the spread of information in social media and can inform the design of effective strategies for information dissemination and control.

An interesting research shown by Stanford on (Modelling retweet cascades on Twitter) where , they argue that this simple epidemiological view, though analytically compelling, is not the entire story. https://cs.stanford.edu/people/hongyang/viral\_twitter.pdf

Another research on (COVID19 pandemic and information diffusion analysis on Twitter) where they explore whether there are similarities in the simulated SIR model (SIRsim), observed SIR model based on actual COVID19 cases (SIRemp), and observed information cascades on Twitter about the virus (INFOcas) by using network analysis and diffusion modelling. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7645904/#pra2252-bib-0005](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7645904/#pra2252-bib-0005)

The SIS model has been implemented in (An information diffusion model based on retweeting mechanism for online social media). https://kd.nsfc.gov.cn/paperDownload/1000003559280.pdf

**Motivation to study the "recovery" - how to define it in diffusion in social media**

The study of information diffusion in social media has been of significant interest in recent years, with a particular focus on the understanding of the spread of information through various networks. One important aspect of this study is the concept of "recovery" which refers to the state in which the spread of information comes to a halt. In the context of social media, defining the recovery part has proven to be a challenging task, and therefore, a deeper investigation into this area is of utmost importance to gain a better understanding of the information diffusion process. The study of the recovery part is important to control or predict the spread of misinformation, rumours and conspiracy theories.

In this study, we define the recovery state of a user with regards to a specific hashtag as the time elapsed between the initial tweet containing that hashtag and the final tweet containing that hashtag in the defined closed time period of 1st January 2022 to 29th December 2022. The recovery of a user from a specific hashtag is established once the final tweet containing that hashtag is posted before or on 29th December 2022. It is important to note that this definition of recovery is specific to the particular hashtag in question and does not reflect the recovery state of the user in regard to other potential infections.

**Problem Statement**

The problem statement for the issue being addressed in this study is to understand the diffusion and recovery process of information in social media.

In this project, we would be researching what we can know about an infected to recovered state and when we can say a user has recovered from a particular infection, which in this case is a hashtag.

**Objective**

Using the EXO-SIR model, which is an epidemiological model that computes the number of contagious illnesses in a closed population over time, The name of this class of models derives from the fact that they involve coupled equations relating the number of susceptible people, the number of people, and the number of people who have recovered, which helps us to determine the average time between all the states, the spread of information is to be studied. We specifically focus on the infected-to-recoverable stages, i.e. when, how and why a user stops tweeting the particular hashtag.

To do this, we find a specific pattern (representing the infected to recovery) from a number of tweets randomly generated for the recovery and try to apply it on the dataset we generate and then calculate the efficiency and correctness of the model on the general Twitter usage.

This pattern here is the average of time a person takes to recover.

**Dataset Description**

In this research, we obtained data from Twitter covering the period from 1st January 2022 to 29th December 2022, with a focus on trending hashtags. By extracting the trending hashtags, we generated a list of users who utilised these hashtags. This information, along with the hashtag, username, time difference between the first and last tweet containing that hashtag, and the time of all tweets was recorded and stored in our dataset, which has a total of 10445 rows.

The dataset is a pseudorandom dataset, as the user list that was used to get the tweets were the users who posted those trending hashtags. Note that the tweets that do not contain any hashtag are not in the scope of our discussion, nor in the domain of our whole study.

We had to do the tedious process of getting a user list and then getting tweets for those users as Tweepy(python Twitter library) does not have the function to get random tweets data without bias.

![](RackMultipart20230202-1-oelx4g_html_2626bd0a947321c8.png)

**Methodology**

[**Link to Code**](https://github.com/SanketAgwl/Exo-sir-mini)

For our research, we are using the Elevated access of Twitter API version 1 to extract data related to our project. Now to get data we would be using Tweepy which is an open source Python package that gives you a very convenient way to access the Twitter API with Python. Tweepy includes a set of classes and methods that represent Twitter's models and API endpoints, and it transparently handles various implementation details, such as:

- Data encoding and decoding
- HTTP requests
- Results pagination
- OAuth authentication
- Rate limits
- Streams

1. **Getting the Dataset**

In our study, the code get\_dataset.py was implemented to obtain an unbiased dataset of trending hashtags on Twitter in India. The Tweepy and random packages were utilised to retrieve queries and random information from the platform. Elevated access of the Twitter API was obtained through the API key, API key secret, API token, and API token secret, allowing for the retrieval of up to 2 million tweets per month and 50 requests per 15 minutes. The code get\_dataset was utilised to retrieve trending hashtags in India using the Where on Earth Identifier (WOEID) via the get\_place\_trends function. The WOEID provides a unique identifier for each country, allowing for the extraction of information from specific regions.

![](RackMultipart20230202-1-oelx4g_html_b92fd3d0f0b20704.png)

We have obtained a set of trending hashtags in India through the "query" data structure. Utilising these hashtags, we have generated a "usernamelist" that comprises of all the users who utilised these trending hashtags in their tweets. For each user in the "usernamelist", a sample of 1000 tweets from their timeline is extracted.

![](RackMultipart20230202-1-oelx4g_html_3d4423b167a61421.png)

We established a dataframe that contains three columns: username, hashtag, and difference. The difference column stores the time interval between the first and last tweet that contains a specific hashtag. The times of all tweets column records the timestamps of all tweets that contain the hashtag. Our analysis is restricted to tweets that were posted between January 1st, 2022 and December 29th, 2022, which are captured in the list\_tweets object.

A hashtag and its associated tweet object were paired as a key-value pair. Tweets containing the same hashtag were appended to the same value. For each user and each hashtag used, the time difference between the initial and final tweets of the hashtag was calculated. This time difference represents the infected to recovered state time period. The dataset generated by this study consisted of 10445 rows, with each row representing a user's hashtag usage and its associated attributes.

We had to do the tedious process of getting a user list and then getting tweets for those users as Tweepy(python Twitter library) does not have the function to get random tweets data without bias.

1. **Testing the Dataset**

We have constructed a dataset with 10445 entries. Our approach to calculate the average duration from infected to recovered state involves the following steps:

1. Determine the time elapsed between the earliest and latest tweet for a particular hashtag used by a user.
2. Sum the time differences for that user and calculate their average duration from infected to recovered state by dividing the sum by the number of hashtags used.
3. Repeat the above two steps for n number of users and calculate the final average duration by dividing the average time differences for all users by n.

Observation: The dataset heavily contains the difference close to zero.

![](RackMultipart20230202-1-oelx4g_html_ced74edeb7c6c8ea.png)

**Note** : The average of the dataset is different from the average we are using. The dataset average is simply the average of all the time difference in the dataset. The average we need is the **group by** average, which is group by user and then averaged out in all the users. This helps us in studying the information with respect to each user and no with respect to each user-hashtag pair which our dataset is using as the primary key for uniqueness.

df\_mean = df.groupby(['username'])['difference'].mean().mean()

**Results**

- Considering the outliers

- **Our average time period is 369686.77 seconds which is**  **4.28 days**  **which means that an average user takes 4.28 days to recover from a specific hashtag**.
- **Standard deviation** is 2093720.166 seconds which is **24.23 days**.
- **Median** of the dataset is 422 seconds, which is **7.03 minutes**.
- **1st Quartile** is **0 days** and **3rd quartile** is 172526 seconds which is **1.996 days**.
- **Standard error with mean including outliers** is 2103231.399 seconds which is **24.34 days**. So, the person could recover from infection with an average of 4.28 ± 24.34 days. **The range could be that the person instantly recovers, i.e. it is his first and last tweet with that hashtag, or could take till 30 days on an average to recover.**

Many data belongs to bots and news channels, which we don't want to study. We remove those outliers by removing all points that lie outside the range defined by the quartiles +/- 1.5 \* IQR.

- After Removing Outliers

- After removing outliers from our dataset, we have **8532 rows** out of **10446 rows.**
- **Maximum** value of difference is 431181.0 seconds which is **4.99 days.**
- **Our average time period is 31707.611 seconds which is**  **0.37 days**  **which means that an average user takes 4.28 days to recover from a specific hashtag**.
- **Standard deviation** is 84528.407 seconds which is **0.98 days**.
- **Median** of the dataset is **0 days**. **More than 50% result reports hashtag has been tweeted once.**
- **1st Quartile** is **0 days** and **3rd quartile** is 10945 seconds which is **0.127 days**.
- **Standard error** of the dataset without outliers is 84629.15 seconds which is **0.979 day.**  **The range could be that the person instantly recovers, i.e. it is his first and last tweet with that hashtag, or could take up to 2 days on an average to recover.** This signifies that a general user usually gets bored of tweeting the same hashtag or just tweets it once.

**Bibliography**

1.M. Cha, H. Haddadi, F. Benevenuto, and K. P. Gummadi. Measuring user influence in twitter: The million follower fallacy. In ICWSM'10, volume 14, page 8, 2010

2.D. J. Daley and D. G. Kendall. Epidemics and rumours. Nature, 204(4963):1118–1118, 1964.

3.M. Nekovee, Y. Moreno, G. Bianconi, and M. Marsili. Theory of rumour spreading in complex social networks. PHYSICA A, 374(1):457–470, 2007

4.L. Zhao, H. Cui, X. Qiu, X. Wang, and J. Wang. Sir rumour spreading model in the new media age. PHYSICA A, 392(4):995–1003, 2012.

5.J. Yang and S. Counts. Predicting the speed, scale, and range of information diffusion in twitter. Proc. AAAI'10, 2010

6 .An information diffusion model based on retweeting mechanism for online social media Fei Xiong a,∗, Yun Liu a, Zhen-jiang Zhang a, Jiang Zhu b, Ying Zhang b
