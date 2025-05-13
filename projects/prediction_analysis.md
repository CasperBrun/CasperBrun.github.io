---
layout: default
title: Predictive Analysis
permalink: /prediction_analysis/
---

# Prediction - Estimating Delivery Times

After exploring the delivery patterns and their possible causes, we shifted our focus to predicting the delivery time for each package. Our goal was to estimate the number of minutes a delivery would take to reach its destination after the order was accepted. This is crucial for both efficient logistics planning and customer satisfaction, as accurate time estimates can reduce uncertainty and improve overall delivery experiences.
To achieve this, we first needed to identify the most important factors influencing delivery time. Using a feature importance analysis, we ranked the available features based on their impact on delivery time predictions.


![top_features](/assets/images/top_features.jpeg)

As shown in the **Top Features for Predicting Delivery Time** chart, **speed (km/h)** emerged as the most influential factor, followed by **latitude**, **distance (km)**, and **longitude**. These top features clearly indicate that geographic location and travel speed are critical for accurate delivery time predictions, while attributes like **courier ID** and **delivery day of the week** had minimal influence.Surprisingly enough, we expected to see AOI type (Residential or Business or Educational kind of zone) as one of the influential features but this did not appear to be one in real.
With these insights, we built a predictive model to estimate delivery minutes for each day from June to November 2021.



![actual_vs_predict](/assets/images/actual_vs_predict.jpeg)


## Real vs Predicted Delivery Minutes

The first plot compares the actual and predicted delivery times for each day. The blue dots represent the actual average delivery minutes, while the orange dots show the predicted delivery minutes from the model. The overall pattern indicates how closely the model's predictions match the real data over time. If the two lines track closely, it means the model is good at capturing the actual delivery patterns. However, if the lines diverge significantly, it suggests the model struggles to capture the true behavior of the delivery process.

In the early months, like June and July, the actual delivery times (blue) are often significantly higher than the predicted times (orange). For example, in early June, the actual times frequently exceeded 200 minutes, while the predictions stayed closer to 150 minutes. 
From August onwards, the actual and predicted lines start to align more closely, mostly within the 100-150 minutes range. In the final months, October and November, the model’s predictions become very close to the actual delivery times, with both mostly staying within the 100 to 150 minutes range. This suggests the model has learned the typical delivery patterns well, resulting in fewer large errors.


## Confidence vs Prediction Intervals

The first subplot adds a confidence interval (shaded in orange) around the predicted line. In simple terms, it shows the range where the average delivery time is likely to fall most of the time (around 95% of the time). If the real values mostly fall within this band, it means the model is generally accurate for average predictions. In this case, the actual values (blue) are mostly within the shaded region, indicating a reasonably accurate model for the average trend.
The second subplot introduces a prediction interval (shaded in green), which is much wider. This interval accounts for both the model's uncertainty and the natural variation in daily deliveries, capturing where individual points might fall. This is a more realistic measure of model reliability, as it considers the full range of possible outcomes.Given that the actual values still fall mostly within this band, it means the model captures the overall trend well, even if it misses some daily spikes and dips.


# Conclusion 
Predicting delivery times accurately is a challenging yet essential task for efficient logistics management. Our analysis revealed that factors like speed (km/h), distance (km), and location (latitude, longitude) play the most significant roles in determining delivery times. These key features allowed us to build a predictive model that captures the overall delivery patterns quite effectively.
However, the wide prediction intervals highlight that real-world variability, like sudden traffic jams or unexpected route changes, can still lead to significant prediction errors.Overall, the model provides a reasonable estimate for average delivery times, but its performance varies significantly depending on the season and traffic conditions, emphasizing the need for continuous refinement and perhaps even real-time data integration to improve accuracy further.



## Project Structure
- [Overview](/)
- [Temporal Analysis](https://casperbrun.github.io/Temporal_Analysis/)
- [Spatial Insights](https://casperbrun.github.io/spatial_insights/)
- [Prediction Analysis](https://casperbrun.github.io/prediction_analysis/)

