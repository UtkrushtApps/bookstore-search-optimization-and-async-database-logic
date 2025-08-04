#!/bin/bash

cd /root/task
docker-compose up -d

until docker exec bookstore_postgres pg_isready -U postgres; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

docker exec -u postgres bookstore_postgres psql -c "CREATE USER store_user WITH PASSWORD 'store_pass';"
docker exec -u postgres bookstore_postgres psql -c "CREATE DATABASE bookstore_db OWNER store_user;"
docker exec -u postgres bookstore_postgres psql -d bookstore_db -U postgres -f /root/task/schema.sql
docker exec -u postgres bookstore_postgres psql -d bookstore_db -U postgres -f /root/task/data/sample_data.sql
docker exec -u postgres bookstore_postgres psql -d bookstore_db -U postgres -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO store_user;"
docker exec -u postgres bookstore_postgres psql -d bookstore_db -U postgres -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO store_user;"

for i in {1..15}; do
  HTTP_STATUS=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8000/docs)
  if [ "$HTTP_STATUS" == "200" ]; then
    echo "FastAPI is up and running!"
    exit 0
  else
    echo "Waiting for FastAPI..."
    sleep 2
  fi
done

echo "Error: FastAPI did not start in time."
exit 1
