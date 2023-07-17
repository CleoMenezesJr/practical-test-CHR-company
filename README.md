# Practical test for CHR company

In this repository you will find both resolute tasks and can prove them in a practical way.

## Requirements

- docker or podman
- docker-compose or podman-compose

## Setup

First you need to rename `.env.sample` file to `.env`.
For practical purposes. All information in .env.sample is already the necessary information for it to work. Of course, you have to double check Django's SECRET_KEY.

- Setup on Development

`docker-compose up --build`

- Setup on Production

`docker-compose -f docker-compose.prod.yml up --build`

## Test task resolution

- Task 1

`http://0.0.0.0:8000/jurisprudence/`

- Task 2

`http://0.0.0.0:8000/concessions/`
