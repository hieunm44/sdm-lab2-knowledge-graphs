# SDM LAB 2 - Knowledge Graphs
<div align="center">
<a href="https://www.fib.upc.edu/en">
   <img src="https://www.fib.upc.edu/sites/fib/files/images/logo-fiblletres-upc-color.svg" height=100"/>
</a>
</div>

## Overview
This repo is our project "Lab 2 - Knowledge Graphs" in the course "Semantic Data Management (SDM)" at Universitat Politècnica de Catalunya (UPC).

## Built With
<div align="center">
<a href="https://graphdb.ontotext.com/">
   <img src="https://dbdb.io/media/logos/GraphDB.png.280x250_q85.png" height=40 hspace=10/>
</a>
<a href="https://www.semanticscholar.org/">
   <img src="https://assets-global.website-files.com/605236bb767e9a5bb229c63c/605274dd4af9b0ca8ac84182_s2-logo.svg" height=40 hspace=10/>
</a>
<a href="https://rdflib.readthedocs.io/en/stable/">
   <img src="https://rdflib.readthedocs.io/en/stable/_static/RDFlib.png" height=40 />
</a>
</div>

## Setup
1. Download GraphDB: https://www.ontotext.com/products/graphdb/download/
2. Open GraphDB, then a new browser tab should automatically open at http://localhost:7200/.
3. Follow the Setup Instructions in the file `knowledge-graphs.pdf` and create a local repository.
4. Go to https://www.semanticscholar.org/product/api and request an API key.

## Usage
1. Clone the repo
   ```sh
   git clone https://github.com/hieunm44/sdm-lab2-knowledge-graphs.git
   cd sdm-lab2-knowledge-graphs
   ```
2. Install necessary packages
   ```sh
   pip install semanticscholar
   pip install rdflib
   ```
3. Put the Semantic Scholar API key in the file `.env`, then download the dataset of papers:
   ```sh
   python3 download_dataset.py
   ```
   After the download is complete, you should have a file `dataset.json` in the folder `data`.
4. Go through the data preprocessing in the file `preprocess_data.ipynb` to generate `.csv` files.
5. Task B1 - TBOX definition
   ```sh
   python3 B1.py
   ```
6. Task B2 - ABOX definition
   ```sh
   python3 B2.py
   ```
7. Task B3 - Create the final ontology
   ```sh
   python3 B3.py
   ```
   After this step, you should have three RDF files `tbox.ttl`, `abox.ttl` and `abox_tbox_connection.ttl`. Import them to your GraphDB repository. You can run queries in the file `B3-statistics.sql` to get statistics about the knowledge graph.
8. Task B4 - Querying the ontology \
   Check the file `B4.sql` for the SPARQL queries.
