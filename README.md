<div style="text-align: justify">

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
<p>
The COVID-19 pandemic, in its severity, has exposed the weakness in policy making under a crisis. In the past, policy decisions on health issues were often well-surveyed across the population to understand the impacts of how a policy affects the public positively. However, the ongoing COVID pandemic has not afforded policymakers the luxury of time to assess the implication of a health policy decision and to arrive at a consensus with the general public. In some countries where public trust and political legitimacy are lacking, the implementation of strict COVID rules can exacerbate political discontent against an authoritarian government perceived to exert more control over the state. As a result, sociopolitical tensions can quickly spill over into mass street protests, leading to a congregation of a large number of people and facilitating the spread of COVID. Thus far, policy responsiveness towards covid has been a simple case of bringing down as many COVID cases in the shortest amount of time, excluding the impacts of the psychological effect strict COVID restriction can have on the population
due to social isolation.
</p>

<p>
On this front, the team recognizes the potential of social platforms that can be utilised to perform sentiment analysis to uncover insights on how the public perceives the current COVID situation and is of the view that such data can be used to furnish policymakers with the information necessary to implement the appropriate COVID policy with regards to public sentiments.
</p>

## Project Description

Raw tweets from Singapore, Hong Kong and Australia are collected using Twitter's developer APIs. Labels are obtained from the [COVID-19 Twitter Dataset](https://doi.org/10.3886/E120321V11).

The raw tweets are preprocessed and used to train the sentiment analysis model. The final model selected is a SVM model trained with Spark-NLP.

Tweets are streamed from Twitter in real time into 3 separate Kafka topics for each country. A consumer group is setup for each topic to processes these tweets, predict the sentiment, and store them into MongoDB.

These reults are then aggregated and served from our API server.

The user interface visualizes this data in a time series graph.

## Usage
Requirements:
1. `docker` installed
2. `docker-compose` installed
3.  `npm` installed

To run backend components, you have to first replace the placeholders with your Twitter API details in the `producer` components of the `docker-compose.yml` file. 
```yaml {.line-numbers}
53   producer:
54    build: producer
55    container_name: producer
56    depends_on:
57      broker:
58        condition: service_healthy
59    environment:
60      CONSUMER_KEY: {CONSUMER_KEY}
61      CONSUMER_SECRET: {CONSUMER_SECRET}
62      ACCESS_TOKEN: {ACCESS_TOKEN}
63      ACCESS_TOKEN_SECRET: {ACCESS_TOKEN_SECRET}
64      KAFKA_BROKER_CONNECT: 'broker:9092'
```
Then run the following command to bring up **all** the components:
```bash
$ docker-compose up -d --build
```
To run only the MongoDB server and API server (without streaming components):
```bash
$ docker-compose up -d --build mongo api
```
To run frontend:
```bash
$ cd frontend
$ npm install # will install packages stated in package.json
$ npm start
```

Teardown:
```bash
$ docker-compose down
```
</div>

## API Documentation
The full API specifications can be viewed either on the [online Swagger generator](https://generator.swagger.io/) by pasting the link to the OpenAPI yaml file (https://raw.githubusercontent.com/wenhaohaoo/cs5425-project/master/backend/openapi.yaml) in the top bar and click explore, or at http://localhost:5000/ui after all backend components are up and running.

1. GET /sentiment/{country}?start={YYYY-MM-DD}&end{YYYY-DD-MM} \
Returns a list of aggregated sentiments per day for the queried country and date range.
2. GET /sentiment/{country}/past-24h \
Returns aggregated sentiment for the past 24 hours for the queried country.
3. GET /sentiment/{country}/past-7-days \
Returns aggregated sentiment for the past 7 days for the queried country.
4. GET /sentiment/{country}/past-30-days \
Returns aggregated sentiment for the past 30 days for the queried country.


## Acknowledgement

Twitter for the raw data and providing elevated access to developer APIs

Gupta, Raj, Vishwanath, Ajay, and Yang, Yinping. COVID-19 Twitter Dataset with Latent Topics, Sentiments and Emotions Attributes. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2021-11-04. https://doi.org/10.3886/E120321V11
