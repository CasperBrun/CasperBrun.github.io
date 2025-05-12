---
layout: page
title: Data
permalink: /data/
---

# Diving Into Our Data 

For this project, we used the LaDe-D dataset, a large-scale public data source provided by Cainiao Network, one of China’s leading logistics platforms. This dataset captures the complex dance of last-mile deliveries in Shanghai over a six-month period in 2021. It includes over 1.48 million unique orders, each with rich details like the location of depots, customer coordinates, order acceptance times, and delivery durations. You can find the original dataset [here](https://huggingface.co/datasets/Cainiao-AI/LaDe-D/viewer/default/delivery_sh).

Initially, the dataset looked quite raw, containing just the basics – order IDs, courier IDs, and geographical coordinates. But to truly understand the story behind these deliveries, we needed to add more layers to this data.

Here’s what we did:

**Time Insights**: We extracted useful time features, like the day of the week, month, and speed of each delivery, along with the minutes taken from acceptance to delivery. This helps us see which days and hours are the busiest.

**Location Context**: Using domain knowledge, we grouped each delivery area (AOI type) into meaningful labels like business complexes, educational zones, residential blocks, and industrial areas based on nearby landmarks and typical activities.

**Lifestyle Zones**: We also grouped the 16 administrative districts into 5 broader lifestyle zones based on their economic status, infrastructure, and general living standards – like upscale city centers, growing suburbs, and busy commercial hubs.

Why did we go through all this effort? Because just looking at raw coordinates or IDs doesn’t tell the full story. By adding these layers, we can start to see the bigger picture – like which areas face the most pressure, when the delivery crunch hits, and how lifestyle differences impact the speed and efficiency of deliveries.

This approach will help us uncover patterns in our data story, revealing the hidden connections between location, income, and delivery efficiency in Shanghai’s fast-paced logistics world.

![Number og deliveries](/assets/images/num_of_deliveries.png)

![AOI types](/assets/images/AOI_types.png)

