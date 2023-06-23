from src.model.mongodb import MongoDB
from src.model.postgres import Postgres


MONGODB_DOCKER = MongoDB(
    user_name="mongodb",
    user_password="mongodb",
    port=27017,
    host="mongodb",
    database_name="originaldb",
)
MONGODB_LOCAL = MongoDB(
    user_name="mongodb",
    user_password="mongodb",
    port=27017,
    host="localhost",
    database_name="originaldb",
)
POSTGRESDB_DOCKER = Postgres(
    user="postgres",
    password="postgres",
    host="postgres15.2",  # route 在 Docker 部署的Host
    port="5432",
    database="originaldb",
)
POSTGRESDB_LOCAL = Postgres(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="originaldb",
)
