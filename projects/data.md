---
layout: default
title: Data
permalink: /data/
published: false
---

# Diving Into Our Data 

For this project, we used the LaDe-D dataset, a large-scale public data source provided by Cainiao Network, one of China’s leading logistics platforms. This dataset captures the complex dance of last-mile deliveries in Shanghai over a six-month period in 2021. It includes over 1.48 million unique orders, each with rich details like the location of depots, customer coordinates, order acceptance times, and delivery durations. You can find the original dataset [here](https://huggingface.co/datasets/Cainiao-AI/LaDe-D/viewer/default/delivery_sh).


The initial dataset was quite basic, mainly containing order IDs, courier IDs, Timings, and coordinates, Encoded values for Area of Interest(AOI) etc. After clearing up the outliers, we decide to feature engineer some added layer in order to uncover deeper insights. For example, using a Shanghai shapefile, we assigned each coordinate point to a nearby landmarks, then grouping areas based on those landmark as business complexes, residential zones, educational areas, and industrial hubs.We further divided the 16 administrative districts into broader  zones – Urban, Suburban, and Isolated Island Areas – based on economic infrastructure, and general living standards.

Adding these layers allows us to go beyond raw data and explore critical questions, like which areas experience the heaviest delivery pressure, when congestion peaks, and how urban dynamics shape delivery efficiency.


# Primary Data Exploration

Before diving deeper, we took a quick look at our dataset to spot some early patterns.It’s like taking a quick walk through a warehouse before deciding how to organize the shelves.

![AOI types](/assets/images/AOI_types.jpg)

First, we checked the distribution of delivery tasks by AOI type. As the first bar chart shows, one AOI type dominates, handling over a million tasks. This made us wonder – what kind of places fall into this category, and why are they so much busier than others?

![Delivery speed](/assets/images/distribution.jpg)


Next, we looked at how fast these deliveries are happening. This time distribution plot adds another layer to the story. It shows that most deliveries happen within a single day, aligning well with Alibaba’s Cainiao Network promise of “next-day” or even “half-day” delivery for many urban areas. This efficiency reflects the strategic placement of distribution hubs and the use of advanced logistics to reduce last-mile times. You can read more about their delivery model [here](https://www.reuters.com/business/retail-consumer/chinese-e-commerce-giants-make-expensive-bets-fast-deliveries-2025-05-12/).



![Number og deliveries](/assets/images/num_of_deliveries.jpg)


Moving on,, we looked at daily delivery volumes over the six-month period. 
*The line plot reveals a clear upward trend, with some sharp peaks around late September. These spikes might be tied to major sales events or busy shopping seasons, which can put a lot of pressure on the delivery network*.


