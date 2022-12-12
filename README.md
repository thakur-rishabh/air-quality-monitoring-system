# Air Quality Monitoring System

Prior studies have shown that people tend to be less satisfied with indoor air quality, report more acute health symptoms (such as headaches and mucosal irritation), work a little bit slower, and miss more days of work or school when indoor CO2 levels are higher. Evidence for the hypothesis that building characteristics and resultant indoor environmental quality affects health outcomes continues to accumulate. These health outcomes also include Sick Building Syndrome symptoms, allergy and asthma symptoms, and respiratory illnesses. CO2 concentrations in buildings typically range from 350 to 2,500 ppm and becomes hazardous when consistently range between 3000 to 5000 ppm.

To monitor and control our indoor air calibre we propose a DIY air quality monitoring system using easily available and affordable sensors for input source and a cost-effective cloud implemented monitoring system. The application produces a graphical analysis of the CO2 level and provides daily, weekly and monthly reports for the user to make well-informed decisions. The user is also intimated through alert message on peak occurrences of CO2 ppm level and hence bestows diligent assistance in self indoor air quality management.

# Architecture

![Alt text](/Architecture/architecture.png?raw=true)

# GCP Components
1.  PubSub - perfect for handling incoming IoT data events.
2.  Cloud function - transfer data events from PubSub to BigQuery.
3.  Cloud storage - Store batch data.
4.  Cloud Dataflow - taking data from cloud storage and sending to PubSub. Here we use cloud function to pull data from Pub/Sub and push to BigQuery as we are not doing filteration.
5.  Google Cloud BigQuery - Data warehouse to store enormous data and make valuable insights.

