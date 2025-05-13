---
layout: default
title: Spatial Insights
permalink: /spatial_insights/
---

# From Time to Territory – Mapping the Hotspots
After exploring the temporal and hourly patterns, it’s clear that delivery demand in Shanghai follows a distinct rhythm, peaking during certain hours and months. But to truly understand where the pressure points lie, we need to move beyond just when deliveries happen and start looking at where they happen.
This naturally leads us to the next phase – spatial analysis. This is where our hotspot maps come in, highlighting the most active delivery regions and the possible factors driving these patterns. 


<iframe src="/assets/interactive/Hotspot map.html" width="100%" height="600px" style="border:none;"></iframe>


*This interactive heatmap highlights the busiest regions in red and orange, while cooler tones like blue indicate lower delivery volumes. Use this map to explore different districts, zoom in to the street level, or pan across the city to find interesting patterns.*

- **Heart of the Action – Central Core**
As you move your cursor over the city center, you’ll notice Huangpu, Pudong, and Xuhui glowing in deep red. These are Shanghai’s economic powerhouses, home to financial hubs like Lujiazui in Pudong, and bustling retail streets like Nanjing Road in Huangpu. According to [China Daily](https://www.chinadaily.com.cn/a/202308/19/WS64dfb3f4a31035260b81cffa.html), Lujiazui alone drives a massive share of the city’s economic activity, making it a prime delivery zone.

- **Busy Suburbs – Minhang**
If you scroll slightly to the southwest, you’ll find Minhang, another high-intensity zone. Known for its dense residential clusters, shopping centers, and logistics hubs.

- **Residential and Commercial Hubs – Xuhui and Huangpu**
Moving a bit to the west, you’ll see the hotspots in Xuhui, home to the bustling Huaihai Road and high-density residential neighborhoods. These areas benefit from a well-connected metro and elevated road network, like the Yan’an Elevated Road, which speeds up last-mile deliveries ([Shanghai Metro, 2024](https://en.wikipedia.org/wiki/Shanghai_Metro)), that can justify a  high volume of delivery.

- **Cooler, Calmer Outskirts**
As you pan further out to the **west** and **northwest**, the colors start to cool. Districts like **Songjiang**, **Qingpu**, and **Jiading** have lighter tones, reflecting their more suburban character. These areas typically focus on **manufacturing**, **warehousing**, and **bulk cargo**, resulting in lower parcel density and longer average delivery times.



# Congestion Map: Where Speed Meets Pressure 
After finding the busiest delivery zones, the next step is to see **how fast** couriers can actually move through them. High volume doesn’t always mean slow speeds, and quiet areas can still have traffic challenges. Mapping congestion helps us spot these real-world delivery obstacles.

<iframe src="/assets/interactive/congestion_map.html" width="100%" height="600px" style="border:none;"></iframe>


- **Slow Zones – High Pressure, Low Speed**:

Zoom into the city center, and you’ll find dense, slow zones like Changning and Hongqiao, where speeds often dip below 2.0 km/h. These areas are packed with offices, residential blocks, and major transit hubs, creating constant traffic jams and frequent stops.


- **Medium Speed Zones – Balancing the Load**:

Moving slightly **west**, areas like **Xujing** and **Gumei** show medium speeds. These are transitional zones, blending residential and industrial traffic, which can slow things down even without extreme volumes.


- **Fast Zones – Open Roads, High Speeds**:

As you pan out to the suburbs, zones like Gangqiao, Zhoupu, and Sheshan stand out with speeds above 4.0 km/h. These areas benefit from fewer stops, wider roads, and proximity to major highways like the G1503 Ring Expressway.

*Interestingly enough, despite being further from the city center, these zones often handle lower volumes but still maintain higher speeds, showing that distance alone doesn’t determine congestion, rather traffic inside the busy urban zone does.*

We  can surely conclude that, AOI types clearly influence speed, with postal centers and business complexes often achieving higher speeds, while mixed-use and residential zones face more frequent delays.


- **Get Closer – Explore the Details**:

*As you zoom in further, individual delivery points reveal detailed information on AOI types, average speeds, and delivery volumes. Use this to uncover surprising slow spots even in the outer districts, where complex traffic or waterway barriers can still slow things down.*



# Exploring AOI Types Across Different Zones – Interactive Insights

To capture the diverse character of Shanghai, we grouped its 16 administrative districts into broader zone groups based on population density, economic activity, and infrastructure. The Central Urban Core includes high-density, high-income areas like Huangpu, Jing'an, Xuhui, and Changning, known for their financial hubs and luxury shopping streets. The Expanding Urban Core covers fast-growing districts like Pudong New Area and Minhang, which are home to tech parks and modern business centers. Inner Suburbs like Baoshan, Jiading, and Fengxian balance residential and industrial activity, while Outer Suburbs like Songjiang, Jinshan, and Qingpu include quieter residential communities and large-scale manufacturing hubs. Finally, Rural and Isolated Areas like Chongming stand apart, characterized by lower population density and agricultural landscapes.

Grouping these districts helps us see how delivery patterns and purchase power vary across the city. Taller bars in these plots generally indicate areas with higher economic activity and stronger purchase power, while shorter bars might reflect residential or industrial zones with less frequent orders.

<iframe src="/assets/interactive/new_single_plot_with_dropdown.html" width="100%" height="500px" style="border:none;"></iframe>
*Use the dropdown menu to switch between zone groups and hover over the bars to compare delivery volume and average accept times across different AOI types.*


## AOI Patterns Across Zones – What to Look For
When you select the Central Urban Core, you’ll notice that Mixed-Use and Business Hubs dominate the scene. This makes sense, as these areas include dense commercial districts like Jing’an and Huangpu, where businesses, offices, and high-rise apartments are tightly packed, creating a constant flow of deliveries.
Switching to the Outer Suburbs reveals a different picture, with Warehousing and Industrial Zones becoming more prominent. These areas, like Songjiang and Jinshan, serve as the city’s logistics backbone, handling bulk shipments and acting as critical nodes in the supply chain.


## Delivery Times Within the Same Zone
After identifying the broader AOI patterns across Shanghai’s different zones, it’s clear that each area has its own unique delivery dynamics. But volume alone doesn’t tell the full story – we also need to consider delivery times and how they vary across different AOI types within the same zone.
In the Expanding Urban Core (like Pudong and Minhang), Business Hubs often handle high volumes but also face longer average delivery times. This is likely due to dense office clusters, complex road networks, and high traffic volumes. However, Mixed-Use areas in the same zone tend to have shorter delivery times despite high volumes, benefiting from more efficient routes and better infrastructure, which allow for faster, more direct deliveries.
In the Outer Suburbs (like Songjiang and Qingpu), the pattern flips. Industrial Zones here handle high volumes but often manage to keep delivery times shorter, thanks to wide roads, less congestion, and more optimized bulk shipments. On the other hand, Residential Areas in these suburbs might see fewer but slower deliveries, as narrow streets, complex housing layouts, and lower route optimization slow down couriers.



# Mapping Shanghai’s Delivery Landscape – The Big Picture

<iframe src="/assets/interactive/stacked_bar_with_legend.html" width="100%" height="400px" style="border:none;"></iframe>

Bringing all zone groups together, this stacked bar chart captures the full spectrum of Shanghai’s delivery dynamics. High-density, high-income areas like the Central Urban Core and Expanding Urban Core show strong volumes in Business Hubs and Mixed-Use zones, reflecting intense commercial activity and higher purchasing power. Meanwhile, Outer Suburbs and Rural Areas lean more towards Warehousing, Postal Centers, and Residential Areas, reflecting their roles in supporting long-distance logistics and bulk shipments.
With this, we wrap up our exploration, revealing how zone types, infrastructure, and consumer behavior come together to shape the complex world of last-mile delivery in Shanghai.


## Project Structure
- [Overview](/)
- [Temporal Analysis](https://casperbrun.github.io/Temporal_Analysis/)
- [Spatial Insights](https://casperbrun.github.io/spatial_insights/)
- [Prediction Analysis](https://casperbrun.github.io/prediction_analysis/)

