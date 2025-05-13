---
layout: default
title: Overview
description: "An overview of the project and its objectives."
permalink: /
---

# Introduction
The rise of e-commerce has transformed the way goods move across the world, and China stands at the forefront of this digital retail revolution. With billions of packages delivered every year, the country's logistics network has become one of the most complex and high-volume systems globally. But what does the scenario look like really up close?

For our project, we want to explore Shanghai – a city where the pulse of online shopping beats fast and loud. It’s one of the world’s busiest and most complex urban structure, with crowded streets, tall skyscrapers, and a blend of old neighborhoods and shiny new business districts. With its dense population, high spending power, and rapidly changing neighborhoods, delivery drivers must navigate a maze of tight lanes, traffic jams, and income divides.

In this data story, we'll dive deep into the complexities of Shanghai's delivery ecosystem, uncovering patterns in volume, speed, timing, and geography to shed light on what makes this massive logistical machine tick. 

The following image is a bar chart with data sourced from the [China State Post Bureau](https://www.euronews.com/next/2021/08/27/china-tech-giant-alibaba-says-delivery-robots-are-the-future-here-are-4-charts-that-explai). It shows the rapid growth in package deliveries in China from 2013 to 2020. The bars are colored in a bright orange, increasing steadily each year, reflecting the explosive rise in e-commerce over the past decade. The chart highlights how parcel volumes surged from just over 10 billion in 2013 to nearly 80 billion in 2020, emphasizing the scale of China’s booming online shopping industry.



![Plot 1](/assets/images/intro.jpg)


# Diving Into Our Data 

For this project, we used the LaDe-D dataset, a large-scale public data source provided by Cainiao Network, one of China’s leading logistics platforms. This dataset captures the complex dance of last-mile deliveries in Shanghai over a six-month period in 2021. It includes over 1.48 million unique orders, each with rich details like the location of depots, customer coordinates, order acceptance times, and delivery durations. You can find the original dataset [here](https://huggingface.co/datasets/Cainiao-AI/LaDe-D/viewer/default/delivery_sh).


The initial dataset was quite basic, mainly containing order IDs, courier IDs, Timings, and coordinates, Encoded values for Area of Interest(AOI) etc. After clearing up the outliers, we decide to feature engineer some added layer in order to uncover deeper insights. For example, using a Shanghai shapefile, we assigned each coordinate point to a nearby landmarks, then grouping areas based on those landmark as business complexes, residential zones, educational areas, and industrial hubs.We further divided the 16 administrative districts into broader  zones – Urban, Suburban, and Isolated Island Areas – based on economic infrastructure, and general living standards.

Adding these layers allows us to go beyond raw data and explore critical questions, like which areas experience the heaviest delivery pressure, when congestion peaks, and how urban dynamics shape delivery efficiency.


# Primary Data Exploration

Before diving deeper, we took a quick look at our dataset to spot some early patterns.It’s like taking a quick walk through a warehouse before deciding how to organize the shelves.

![AOI types](/assets/images/AOI_types.jpg)

First, we checked the distribution of delivery tasks by AOI type. AOI type means area of interest. In general, the online delivery services have their own way of labelling area types based on common features or landmarks around. It is encoded by the company but different numbers actually mean areas like Residential, Business Hub, Educational Zone etc. Based on the bar chart displayed above, one AOI type dominates, handling over a million tasks. This made us wonder – what kind of places fall into this category, and why are they so much busier than others?

![Delivery speed](/assets/images/speed_minutes.jpeg)


Next, we looked at how fast these deliveries are happening. This time and speed distribution plot adds another layer to the story. The majority of couriers operate below 10 km/h, reflecting the dense, traffic-heavy nature of urban areas like Shanghai, where congested roads and pedestrian zones slow down last-mile deliveries. This can be a major factor impacting overall delivery times.It shows that most deliveries happen within a single day, aligning well with Alibaba’s Cainiao Network promise of “next-day” or even “half-day” delivery for many urban areas. This efficiency reflects the strategic placement of distribution hubs and the use of advanced logistics to reduce last-mile times. You can read more about their delivery model [here](https://www.reuters.com/business/retail-consumer/chinese-e-commerce-giants-make-expensive-bets-fast-deliveries-2025-05-12/).



![Number og deliveries](/assets/images/num_of_deliveries.jpg)


Moving on, we looked at daily delivery volumes over the six-month period. 
*The line plot reveals a clear upward trend, with some sharp peaks around late September. These spikes might be tied to major sales events or busy shopping seasons, which can put a lot of pressure on the delivery network*.






## Project Structure
- [Overview](/)
- [Temporal Analysis](https://casperbrun.github.io/Temporal_Analysis/)
- [Spatial Insights](https://casperbrun.github.io/spatial_insights/)
- [Prediction Analysis](https://casperbrun.github.io/prediction_analysis/)
