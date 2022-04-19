# CS5425 Project
Analysis on public sentiment from social media to assist policy-makers on COVID related policies

<b>Group Members</b>:
- Akhil Venkateswaran Lakshminarayanan
- Ankireddy Monica Aiswarya
- Kwek Kee En
- Lau Wen Hao
- Niranjana Anand Unnithan
- Ong Fang See Christopher

## Introduction
The COVID-19 pandemic, in its severity, has exposed the weakness in policy making under a crisis. In the past, policy decisions on health issues were often well-surveyed across the population to understand the impacts of how a policy affects the public positively. However, the ongoing COVID pandemic has not afforded policymakers the luxury of time to assess the implication of a health policy decision and to arrive at a consensus with the general public. In some countries where public trust and political
legitimacy are lacking, the implementation of strict COVID rules can exacerbate political discontent against an authoritarian government perceived to exert more control over the state. As a result, sociopolitical tensions can quickly spill over into mass street protests, leading to a congregation of a large number of people and facilitating the spread of COVID. Thus far, policy responsiveness towards covid has been a simple case of bringing down as many COVID cases in the shortest amount of time, excluding the impacts of the psychological effect strict COVID restriction can have on the population
due to social isolation.

On this front, the team recognizes the potential of social platforms that can be utilised to perform sentiment analysis to uncover insights on how the public perceives the current COVID situation and is of the view that such data can be used to furnish policymakers with the information necessary to implement the appropriate COVID policy with regards to public sentiments.

## Project Description

Raw tweets from Singapore, Hong Kong and Australia are collected using Twitter's developer APIs. Labels are obtained from the [COVID-19 Twitter Dataset](https://doi.org/10.3886/E120321V11).

The raw tweets are preprocessed and used to train the sentiment analysis model. The final model selected is a SVM model trained with Spark-NLP.

Tweets are streamed from Twitter in real time into 3 separate Kafka topics for each country. A consumer group is setup for each topic to processes these tweets, predict the sentiment, and store them into MongoDB.

These reults are then aggregated and served from our backend API.

## Usage
Requirements:
1. `docker` installed
2. `docker-compose` installed
```
docker-compose up -d -build
```

Teardown:
```
docker-compose down
```

## Acknowledgement

Twitter for the raw data and providing elevated access to developer APIs

Gupta, Raj, Vishwanath, Ajay, and Yang, Yinping. COVID-19 Twitter Dataset with Latent Topics, Sentiments and Emotions Attributes. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2021-11-04. https://doi.org/10.3886/E120321V11