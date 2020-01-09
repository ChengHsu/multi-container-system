# multi-container-system
web service system provided by multiple docker containers using Flask and PostgreSQL

## What I've done
I took advantage of Compose, which is a tool for defining and running multi-container Docker applications. I used a YAML file to configure my two containers - db and service and start them and make them talk to each other.

## Folders Tree
```
│── docker-compose.yml
│── Dockerfile
│── app.py
│── requirements.txt
│   ├── db
│   │   └── Dockerfile
|   |   └── init.sql
|   |   └── create.sql
│   ├── templates
│   │   └── app.py
│   ├── Dockerfile
└── README.md
```

## Commands
I use the following two commands to start containers and shut down containers respectively under the project folder:
```
docker-compose up --build -d
docker-compose down
```
