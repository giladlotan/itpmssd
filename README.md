# Making Sense of Social Data

- NYU - ITP
- Fall 2015
- Gilad Lotan | danah boyd

---
### Description
Data are created and collected all around us, trails left from interactions in social media, accessible through streams, feeds, APIs, and data-stores. These data are used to power a growing number of services, modeled not only off our own interactions but also interactions of our friends and larger network of connections. While well intended, and many times well functioning, the growing range of uses of systems that algorithmically score content means there are a growing number of unintended consequences and inherent biases. In order to untangle some of these issues, we’ll dive into the literature, while building our own algorithmically-driven data services.

In this class we will explore various computational and social science approaches to understanding networked users. We’ll collect data by talking to people, as well as use Python scripts to access data from APIs such as Twitter and Instagram. We’ll learn how to make sense of these different data, touching topics such as qualitative interviewing, ethnographic observation, content analysis, natural language processing, content classification, authority ranking, and clustering. We’ll also be using a number of open source tools that help us make sense of networks, including Gephi and Python’s networkx library. And we'll be diving into literature from various fields - including sociology and media studies - to make sense of social data that we gather along the way.

---
<p align="right"><a href="https://github.com/giladlotan/itpmssd/blob/master/Week_1/README.md"> Week 1 </a> --> </p>

### Schedule

- [[9/4] (https://github.com/giladlotan/itpmssd/blob/master/Week_1/README.md)]   1. Class Intro: Models, Python, Amazon AWS
- [[9/11] (https://github.com/giladlotan/itpmssd/blob/master/Week_2/README.md)]  2. Participant-Observation, Loading data into pandas DataFrames
- [[9/18] (https://github.com/giladlotan/itpmssd/blob/master/Week_3/README.md)]  3. Exploratory Data Analysis, Simple Stats
- [[9/25] (https://github.com/giladlotan/itpmssd/blob/master/Week_4/README.md)]  4. Social Media & Networked Publics
- [[10/2]  (https://github.com/giladlotan/itpmssd/blob/master/Week_5/README.md)] 5. Social Network Analysis & Networkx
- [[10/9]  (https://github.com/giladlotan/itpmssd/blob/master/Week_6/README.md)] 6. Interviews, Trust & Regulation | Network Analysis (Part II), Gephi
- [10/16] ---> NO CLASS
- [[10/23] (https://github.com/giladlotan/itpmssd/blob/master/Week_7/README.md)] 7. Power & Manipulation | Intro to Bots
- [[10/30] (https://github.com/giladlotan/itpmssd/blob/master/Week_8/README.md)] 8. Bots Continued
- [11/6]  ---> NO CLASS
- [[11/13] (https://github.com/giladlotan/itpmssd/blob/master/Week_9/README.md)] 9. Bot Assignment Due
- [[11/20] (https://github.com/giladlotan/itpmssd/blob/master/Week_10/README.md)] 10. Classification, or Modern Day Magic
- [11/27] ---> NO CLASS
- [[12/4]  (https://github.com/giladlotan/itpmssd/blob/master/Week_11/README.md)] 11. Topic TBD | Unintended Consequences
- [12/11] ---> NO CLASS
- [[12/18] (https://github.com/giladlotan/itpmssd/blob/master/Week_12/README.md)] 12. Present Final Projects

---
### Logistics

- Class: Fridays, 9am-12pm
- Office Hours: by request 30 minutes before or afer class or via Skype
- Slack: itpmssd.slack.com
  - If you haven't already signed up to our Slack group, please do so here - [itpmssd.slack.com] (https://itpmssd.slack.com).
  - We'll be using Slack for class-related communications: questions, thoughts, answers. We'll also use it to share interesting and relevant articles we find. Most importantly, we'll be relying on Slack to create and test our Bot creations. (More on that l8trz)
  - Private communications (e.g., class absences, personal concerns) should be communicated through email.
- Assignments:
  - _Reading_: 
    - Each week, there will be some form of reading. We are keeping the reading short and accessible so please do it. 
    - The required readings are available via Dropbox or through an online link, as indicated in the assignment section of each week.  
    - We strongly recommend acquiring a copy of ["Learning from Strangers"] (http://www.amazon.com/Learning-Strangers-Qualitative-Interview-Studies/dp/0684823128/)
    - We recommend acquiring a copy of ["Data Science from Scratch"] (http://www.amazon.com/Data-Science-Scratch-Principles-Python/dp/149190142X) as a supplemental resource for all technical topics covered in class.
  - _Coding_
    - We'll use a shared dropbox folder for submitting coding homework assignments. 
- Evaluation: 
  - On-time attendance and class participation: 25%
  - Assignments: 25%
  - Mid-term Bot Project: 25%
  - Final Project: 25%
  - _Note: Showing up more than 10 minutes late without prior notice is an unexcused absence. More than 2 unexcused absences results in automatic failure._

---

### Final Project

You now have different tools in your belt to make sense of social data.  For the final project, we want you to leverage these to tell a story that matters.  Independently or in groups of up to four, we want you to mix qualitative and computational skills to analyze data and report what you learn in a written or visual form.  

You may use data from any source - Instagram, Twitter, open data sets.  (For example, you may appreciate government data sets: https://www.data.gov/ )  The data that you choose should be large enough to require analysis using your machine.  Ideally, you will use data from multiple data sets as part of your analysis.  

You should construct a question that can be asked of the data you’re working with.  This question should have value to someone other than you.  Keeping in mind an audience is an important part of this process because you want the story you’re telling to matter. 

In order to provide broader perspective, you should also incorporate a qualitative method in what you’re doing.  For example, qualitatively analyze a sample of the data or interview people about the issue you’re trying to analyze. Get beyond the numbers to focus on why, how, and in what context.

Your question may require network analysis, statistical methods, cluster analysis, or any other technique that you’ve learned in the class.  If there’s a new technique that you’d like to learn to help you ask your question, let Gilad and danah know by Thursday, November 19 so that they can plan accordingly for class.

You do not need to visualize the data, but you do need to analyze the data to tell a story. You will be asked to write a Medium article that tells a story using data. For examples of stories that Gilad has written using data, see:
- https://medium.com/i-data/israel-gaza-war-data-a54969aeb23e
- http://giladlotan.com/2012/03/data-viz-kony2012-see-how-invisible-networks-helped-a-campaign-capture-the-worlds-attention/
- https://medium.com/i-data/fake-friends-with-real-benefits-eec8c4693bd3

For a sense of last year’s classes’ stories, see: 
- https://medium.com/i-data/towards-a-homeostasis-of-continuous-7e4ddfc8b923
- https://medium.com/i-data/finding-patterns-in-protests-6f6331c94897
- https://medium.com/i-data/understanding-the-common-core-debate-using-twitter-data-57b5502acf7b


By November 24, please send Gilad and danah: 
- A blurb about your final project direction, including what question or problem space you want to pursue, the analysis method you will be using
- A list of the team
- What kind of output you are hoping to produce
