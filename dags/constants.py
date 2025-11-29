url_metadata = "https://api.openbrewerydb.org/v1/breweries/meta"
url_lstbreweries = "https://api.openbrewerydb.org/v1/breweries"
postgres_conn_id = "postgres_conn"
postgres_user = "airflow"
postgres_password = "airflow"


sql_create ="""
SET search_path TO public;

CREATE TABLE IF NOT EXISTS bronze_breweries (

    id VARCHAR(36) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    brewery_type VARCHAR(50) NOT NULL,
    address_1 VARCHAR(255),
    address_2 VARCHAR(255),
    address_3 VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(100),
    state_province VARCHAR(100),
    state VARCHAR(50), 
    postal_code VARCHAR(20),
    country VARCHAR(100) NOT NULL,
    longitude NUMERIC(10, 7),
    latitude NUMERIC(10, 7),
    phone VARCHAR(50),
    website_url VARCHAR(255),
    source_json_body JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS silver_breweries (

    id VARCHAR(36) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    brewery_type VARCHAR(50) NOT NULL,
    address_1 VARCHAR(255),
    address_2 VARCHAR(255),
    address_3 VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(100),
    state_province VARCHAR(100),
    state VARCHAR(50), 
    postal_code VARCHAR(20),
    country VARCHAR(100) NOT NULL,
    longitude NUMERIC(10, 7),
    latitude NUMERIC(10, 7),
    phone VARCHAR(50),
    website_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS gold_breweries (

    id VARCHAR(36) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    brewery_type VARCHAR(50) NOT NULL,
    address_1 VARCHAR(255),
    address_2 VARCHAR(255),
    address_3 VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(100),
    state_province VARCHAR(100),
    state VARCHAR(50), 
    postal_code VARCHAR(20),
    country VARCHAR(100) NOT NULL,
    longitude NUMERIC(10, 7),
    latitude NUMERIC(10, 7),
    phone VARCHAR(50),
    website_url VARCHAR(255),
    source_json_body JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
"""