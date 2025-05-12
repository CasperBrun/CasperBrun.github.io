---
layout: default
title: Temporal Analysis
permalink: /Temporal_Analysis/
---

# From Trends to Time – Digging Deeper into Temporal Patterns 

To understand the full delivery picture, we decided to break down the data along different time dimensions. This helps us identify peak times, seasonal trends, and potential bottlenecks that might be hidden in the overall volume.

## Seasonal and Weekly Patterns

To capture the monthly and weekly delivery rhythms, we visualized five full months from our dataset – June to October. We chose to exclude May and November as they only contain partial data, which might not give us the full picture of delivery trends.

![Calender](/assets/images/Calender Plot.png)


**A Calmer Start in June :** 
June typically starts a bit slower, even though it includes the 618 Shopping Festival, one of China’s largest mid-year sales events according to China Marketing Corporation. This festival mainly focuses on electronics and home appliances, which can create a short-term spike but doesn’t sustain high volumes like the later months. 

**The September-October Rush:**

The heatmap clearly shows a surge in delivery volumes as we move into September and October. This period aligns with the Golden Week in early October, one of the biggest shopping and travel seasons in China. According to China Daily, this week-long national holiday drives a massive spike in consumer spending, pushing up delivery volumes as people prepare for family gatherings and holiday shopping. Additionally, businesses often stock up ahead of this peak period, adding extra pressure on logistics networks.

**Weekend Deeps :**

Despite the overall growth, there are slight dips on weekends, reflecting a possible slowdown in commercial deliveries, as businesses often operate with reduced hours or close entirely.


## Hourly Pattern

After understanding the broader monthly and weekly delivery patterns, we wanted to explore the hourly dynamics of parcel movements. This helps us pinpoint exactly when the city’s logistics network is under the most pressure.

![Polar Plot Hours](/assets/images/Polar Plot Hours.png)

- The peak period from **11 AM to 5 PM** likely reflects the overlap between order placement and fulfillment during regular working hours. This is when offices receive bulk packages and restaurants handle lunchtime and early evening deliveries.

- The quiet hours from **midnight to 7 AM** show minimal activity, as most businesses are closed and fewer residential deliveries are expected.

## Project Structure
- [Overview](/)
- [Temporal Analysis](https://casperbrun.github.io/Temporal_Analysis/)
- [Spatial Insights](https://casperbrun.github.io/spatial_insights/)

