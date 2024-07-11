# Arabic Sentiment Analysis API with Arabert Model

This repository contains a Flask-based REST API for Arabic sentiment analysis using Arabert model, Dockerized for easy deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker installed on your local machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).
- download model folder from [here](), uncompress it and put it in the your folder

<!-- ### Installing

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
``` -->

### Build the Docker Image
open command line then write these commands


```bash
cd <your-folder-path>
```

```bash
docker build --tag sentiment_analysis_ar .
```


### Run the Docker Container
Run the Docker container,

<!-- ###### *mapping your machine's port 5000 to the container's port 5000:* -->


```bash
docker run -p sentiment_analysis_ar
```
<!-- ```bash
docker run -p 5000:5000 sentiment_analysis_ar
``` -->
<!-- The API should now be running and accessible locally at http://localhost:5000. -->



## API Usage

###  **Endpoint** ( `/predict` )

- Method: POST
- Content-Type: application/json
- Input: JSON object with a text field containing the Arabic text for sentiment analysis.
- Output: JSON object with a prediction field containing the predicted sentiment (Positive, Neutral, or Negative).

### **Go to command line:**

***Write your sentence in a command like this:***
```bash
curl -X POST http://localhost:5000/predict -H 'Content-Type: application/json' -d '{"text":"المنتج حقكم مرة حلو!"}'
```
***You get a response like this:***
```json
{
  "prediction": "Positive"
}
```

### Authors
dreahim

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.


### Acknowledgments
Mention any acknowledgments or resources used that inspired you in this project.

```sql
Feel free to paste this content into your README.md file and customize it as per your specific project details and implementation.
```