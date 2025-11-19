from invoke import task

@task 
def run_mongo(c):
    c.run(
        "docker run --name mongo -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=mongoadmin -e MONGO_INITDB_DATABASE=data_storage -p 27017:27017 -d mongo"
    )

