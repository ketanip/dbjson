<p align="center" width="100%">
    <img width="33%" src="https://i.imgur.com/gbT5IKBm.jpg">
</p>

### Getting started with DBJson

![](https://i.imgur.com/Jp68wmK.jpg)

## What is DBJson?

Read the [DBJson docs here](https://ketanip.github.io/dbjson/) .

This is a simple flat file database which stores its data in filesystem ( folders and JSONfiles ).
It is NOT INTENTED TO USE IN PRODUCTION.
It can be used times when you are too lazy to write a schema and do other stuff for a ORM like SQLAlchemy.

Data is structured as follows:

Collections : contains records.
records: contains key value pair.
key value pair ( key: str, value: dictionary ).

### What can it Do ?

It can do all the basic things that a database can do, which includes:

1. creating records
2. reading records
3. updating records
4. deleting records
5. filter records

### Why was it made ?

Sometimes I am to lazy to setup database make database models and all that stuff, and I like key-value pair databases for small fun projects. So I could not find in python so I decided to make one for myself.

Hope you guys like it.😊

Read the [DBJson docs here](https://ketanip.github.io/dbjson/) .
