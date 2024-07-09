# Docker Web Server and Database Project

This project is a practical exercise designed to familiarize with Docker by implementing a web server, a simple web application, and a connected database using Docker and Docker Compose.

## Project Overview

### Web Server
- Image Used: nginx
- Features:
  - Hosts an HTML page with group members' names and student numbers.
  - Acts as a reverse proxy for a simple web application.

### Web Application
- Features:
  - Serves content from a folder outside the Docker container.
  - Connects to a database for data storage and retrieval.

### Database
- Image Used: PostgreSQL
- Features:
  - Provides persistent data storage accessible by the web application.
  - Configured with authentication (username and password).

## Docker Compose
- docker-compose.yml:
  - Ensures stateful containers with persistent data.
  - Allocates specific CPU and RAM resources.
  - Automatically restarts on system reboot.
  - Builds and pushes images to Docker Hub.

## Getting Started

1. Clone this repository.
2. Build and run the Docker containers using Docker Compose:
  
   docker-compose up --build
   
3. Access the web server to view the HTML page and use the web application.

## Docker Hub Images
- Links to the built Docker images are provided in the documentation.

## Authors
- Tahmine Tavakoli, Elham Armin, Alireza Amini

---

Feel free to adjust any specific details to match your project setup and choices.
