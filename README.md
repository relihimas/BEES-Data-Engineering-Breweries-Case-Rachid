# <img width="127" height="51" alt="Captura de Tela 2025-11-27 às 13 12 47" src="https://github.com/user-attachments/assets/d61c7c6d-79e0-48d3-a980-1ae2e2a8fd96" />
BEES Data Engineering - Breweries Case - Rachid

The goal of this test is to assess your skills in consuming data from an API, transforming and persisting it into a data lake following the medallion architecture with three layers: raw data, curated data partitioned by location, and an analytical aggregated layer.

![image]

# Features
- Breweries Data: Using the Open Brewery DB API to fetch data, listing breweries companies: [Open Brewery DB List Breweries](https://www.openbrewerydb.org/documentation#list-breweries).
- Docker Support: Easily deployable using Docker.
- Orchestration: This project will use Airflow v4.1.0.
- DataLake Architecture: Data will follow the Medallion Architecture.
- Monitoring/Alerts: 


# Walktrough

> [!WARNING]
Deploy this application into a **Linux** Operational System.

First, start the application by building the image:

    docker build -t bees-case .

And then, run it:

    docker run -d -p 8000:8000 --name beescontainer bees-case

Also, if you do not have the Docker installed in your instance, please, follow these instructions: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

## How it works?

After correctly initialization, the server will be up and running into the deployed instance.
