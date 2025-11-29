# <img width="127" height="51" alt="Captura de Tela 2025-11-27 às 13 12 47" src="https://github.com/user-attachments/assets/d61c7c6d-79e0-48d3-a980-1ae2e2a8fd96" />
BEES Data Engineering - Breweries Case - Rachid

# 👷 Main Architecture:

<img width="1448" height="593" alt="v1" src="https://github.com/user-attachments/assets/da4e0768-cf1b-40b9-9d92-a0f742bace05" />

The goal of this test is to assess your skills in consuming data from an API, transforming and persisting it into a data lake following the medallion architecture with three layers: raw data, curated data partitioned by location, and an analytical aggregated layer.

# 📊 Project Status

- Status: Active
- Maintenance: Actively maintained by Rachid Elihimas
- Dataset Size: 9,000+ breweries

# 🔧 Requirements

- Linux with Git and Docker installed.

# Features
- Breweries Data: Using the Open Brewery DB API to fetch data, listing breweries companies: [Open Brewery DB](https://www.openbrewerydb.org/).
- Docker: Using Docker Composo with other Dockerfiles for support.
- Orchestration: This project will use Airflow v3.1.3.
- Database: Postgres SQL (already provided by Airflow).
- Programming Language: Python with PySpark.
- DataLake Architecture: Medallion Architecture.
- Monitoring/Alerts: 

## Breweries Data:

1. Main Goal:
   - Fetch Data from the [API List Breweries](https://www.openbrewerydb.org/documentation#list-breweries) and generate a view with the quantity of breweries per type and location.

2. Logic:

   - The code will extract from the MetaData API the total amount of Breweries;
   - The code will use this total amount of Breweries as variable to determinate the amount of pages for the API List Breweries;
   - The code will run the API List Breweries and extract from each page a total of 200 Breweries;
   - The code will insert the data extracted in the Bronze layer, following the best practices;
   - The code will peform treatment and transform the data to a columnar storage format such as parquet or delta, and partition it by brewery location storing it on the Silver layer;
   - The code will create an aggregated view with the quantity of breweries per type and location.

     - Retention and recovery > Can easily reprocess from the original source without relying on the external system.
     - Traceability  > Storing raw data supports traceability and regulatory compliance (LGPD). 
     - Imutability > Unaltered state of the data, ensuring you always have an immutable snapshot for reference.
     - Easy for reprocessing > Can restart the downstream transformation without new API calls.
     - Source decoupling > Reduces depency on external APIs or system, avoiding downtimes.
     - Schema evolution > Keep the original data to adapt in any case of Bronze schema changes.
     - Quality > enables comparison between raw and processed data.
      
3. Data Schema:

   Each brewery entry contains the following fields:
   
    ```json
    {
        "id": "5128df48-79fc-4f0f-8b52-d06be54d0cec",
        "name": "(405) Brewing Co",
        "brewery_type": "micro",
        "address_1": "1716 Topeka St",
        "address_2": null,
        "address_3": null,
        "city": "Norman",
        "state_province": "Oklahoma",
        "postal_code": "73069-8224",
        "country": "United States",
        "longitude": -97.46818222,
        "latitude": 35.25738891,
        "phone": "4058160490",
        "website_url": "http://www.405brewing.com",
        "state": "Oklahoma",
        "street": "1716 Topeka St"
    }
   ```
    Also, we can use the Query Parameters available on the Docs
    
    <img width="1103" height="535" alt="Captura de Tela 2025-11-27 às 13 43 47" src="https://github.com/user-attachments/assets/1268bfa7-98b2-4179-91e2-c74f1e322786" />

4. Meta Data:

    For best practice the code will add the following fields:

   ```json
   {
      "total_amount_breweries": 9.038,
      "source_endpoint": "https://api.openbrewerydb.org/v1/breweries",
      "source_query": "page=47&per_page=200",
      "creation_timestamp": "20251127 14:53:52",
      "batch_id": "8b52-d06be5",
      "bronze_target": "breweries_bronze",
   }
   ```

# Git

Be sure that you have your Git installed and up to date.

```bash
sudo apt update
sudo apt install -y git
```

# Docker Support

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -aG docker $USER
```

If you have any issue or doubt during the installation, consult the original documentation: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

# Airflow Orchestration | Spark / PySpark | Postgres SQL

Those three features will be made available through Docker Compose and Dockerfile files.
