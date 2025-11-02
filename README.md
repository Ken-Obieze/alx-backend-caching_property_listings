# Property Listings with Django Caching

This project demonstrates multi-level caching strategies in a Django-based property listing application. It uses Redis for caching and PostgreSQL for data persistence, all containerized with Docker.

## Features

- View-level caching with `@cache_page`
- Low-level queryset caching using Django's cache API
- Cache invalidation via Django signals
- Redis cache metrics analysis
- Dockerized PostgreSQL and Redis setup

## Tech Stack

- Django
- PostgreSQL
- Redis
- Docker
- django-redis
- psycopg2

## Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/ken-obieze/alx-backend-caching_property_listings.git
   cd alx-backend-caching_property_listings
