# Running a Dockerfile

This repository contains a Dockerfile that allows you to create a Docker container for a specific application or service. Follow the steps below to build and run the Docker container.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- [Docker](https://www.docker.com/get-started) - Make sure Docker is installed and running on your machine.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Gidrian/capstone
  
   cd capstone
   ```

2. Then you can build the docker image with:
```bash
    docker compose up --build
```

3. You should now be able to access the web app at http://0.0.0.0/home