# ooham-api
Ooham" is an app used to estimate project details based on proper descriptions. This information helps provide an overview of the project's complexity and how long it will take

Run Docker using docker from docker-compose file : docker-compose up  

Run Migrations : alembic init migrations for creating migration folder already done
# create a migration from current models
alembic revision --autogenerate -m "initial models"

# apply migrations to DB
alembic upgrade head