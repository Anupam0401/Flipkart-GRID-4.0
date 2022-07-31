# Flipkart-GRID-4.0
The repo contains our approach and idea to solve Level 2 problem statement (PS #3) in Flipkart GRID 4.0

**Refer [this](https://github.com/Anupam0401/Flipkart-GRID-4.0/blob/master/DTYDHTCode.pdf) document for the solution submitted by our team DTYDHTCode**

## Team DTYDHTCode:
- [Anupam Kumar](https://github.com/Anupam0401), IIT Bhilai, B.Tech, CSE
- [Ritik Dhanore](https://github.com/RitikDhanore), IIT Bhilai, B.Tech, CSE

# Extract Trends from social media data
- The official problem statement can be found [here](https://github.com/Anupam0401/Flipkart-GRID-4.0/blob/master/PS-Extract%20trends%20from%20social%20media.pdf)
- As part of this challenge, teams are expected to identify trends from social media data
- From all the products available on Flipkart identify trending products, utilize all signals available (ex. posts, sessions, check-ins, social graphs, media content, etc.). Output should also have photos, videos, gifs which can be
used on Flipkart app.
- Preferred tech: Open source
- Bonus: Signal extraction from multiple social media channels (ex. FB, Instagram, Twitter, etc.)

## Results
The results can be viewed directly on this [hosted website](https://anupam0401.github.io/Flipkart-GRID-4.0/).


## Brief Approach
- Scrape data from Twitter, Facebook, Instagram, etc.
- Extract trends from the data
- Output the trends in a format that can be used on Flipkart app

## Get Started
The data has been scrapped from from [twitter](https://twitter.com/) and some parts from [facebook](https://www.facebook.com/).
The scrapper codes be run directly and the results improve every time we add more data and get the latest trends.

### Prerequisite
- Clone the repo
- Run the following  commands in order:
    - create a virtual environment
    ```bash
    python3 -m venv env
    ```
    - Activate the virtual environment (env) by going into the following relative path
    ```bash
    \env\Scripts\activate
    ```
    - Install all the dependencies
    ```bash
    pip install -r requirements.txt
    ```
    
### Usages
The requiremensts for running the code is fulfilled and the code can be run directly by following the commands below:
- Run the following command to run the code
    ```bash
    python3 main.py
    ```
    - Run the following command to see the output
    ```bash
    python3 main.py --output
    ```
    - Run the following command to see the output in a web browser
    ```bash
    python3 main.py --output --browser
    ```
    - Run the following command to see the output in a web browser and open the output in a new tab
    ```bash
    python3 main.py --output --browser --new-tab
    ```
    

