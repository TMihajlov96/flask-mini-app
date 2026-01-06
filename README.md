# Minimal Flask App Example

This repository provides a minimal working example of a **Flask web application** containerized with Docker. It is based on the tutorial: [Run the simplest web app in Docker](https://medium.com/@andreajrubino/run-the-simplest-web-app-in-docker-23df528e8b8).

## Description
This lightweight application demonstrates how Flask maps URLs to Python functions. Depending on the endpoint accessed, the container will serve different text responses.

## How to Run
To pull and run the image from DockerHub, use the following command in your terminal:

First, pull the image from Docker Hub:
```bash
docker pull tmihajlov/flask-mini-app:latest
```
Before running the application, you need to build the Docker image from the source code:
```bash
docker build -t tmihajlov/flask-mini-app .
```
Then, run the container:
```bash
docker run -p 8080:8080 dockersamples/tiny-flask-app:latest
```

### Accessing the App
Once the container is running, open your web browser and navigate to the following addresses:

* **Home Page:** `http://localhost:8080`
    * *Expected output:* "You're home now!"
* **Hello World Page:** `http://localhost:8080/hello-world`
    * *Expected output:* "Hello World!"


### Key Details
* **Host Port:** 8080
* **Container Port:** 8080
* **Base Image:** Python

> **Note:** If port `8080` is already in use on your host machine, you can change the mapping by modifying the first number in the run command (e.g., `-p 9000:5000`).
