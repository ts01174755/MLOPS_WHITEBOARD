import os
import time
import subprocess
from model.docker_command import DockerCommand

class BuildEnvironment:
    @classmethod
    def build_local_environment(cls, RUN, config):
        pip_pkg_list = config.PROJECT_LOCAL_PIP_INSTALL_PYTHON_PACKAGE
        brew_pkg_list = config.PROJECT_LOCAL_BREW_INSTALL_PACKAGE

        if RUN == 'init' or RUN == 'all':
            subprocess.run("pip install --upgrade pip", shell=True)

        if RUN == 'pip' or RUN == 'all':
            for pkg_ in pip_pkg_list:
                subprocess.run(f"pip install {pkg_}", shell=True)

        if RUN == 'brew' or RUN == 'all':
            for pkg_ in brew_pkg_list:
                subprocess.run(f"brew install {pkg_}", shell=True)
    
    @classmethod
    def build_monodb_environment(cls, RUN, config):
        if RUN == 'images' or RUN == 'all':
            # DockerCommand pull Images
            DockerCommand.dockerPull(tag=config.IMAGE_MONGODB_TAG)
            DockerCommand.dockerPull(tag=config.IMAGE_MONGODB_EXPRESS_TAG)

        if RUN == 'build' or RUN == 'all':
            # DockerCommand 建立網路
            DockerCommand.dockerNetworkRemove(name=f'{config.CONTAINER_MONGO_POSTGRES_NET}')
            DockerCommand.dockerNetworkCreate(name=f'{config.CONTAINER_MONGO_POSTGRES_NET}')

            # subprocess.run(f"mkdir -p {config.CONTAINER_MONGODB_ROOT_MAP}", shell=True)
            # subprocess.run(f"mkdir -p {config.CONTAINER_MONGODB_EXPRESS_ROOT_MAP}", shell=True)

            # DockerCommand run mongodb
            DockerCommand.dockerRun(
                tag=config.IMAGE_MONGODB_TAG,
                name=config.CONTAINER_MONGODB_NAME,
                port=config.CONTAINER_MONGODB_PORT_LIST,
                volume=f'{config.CONTAINER_MONGODB_ROOT_MAP}:{config.CONTAINER_MONGODB_ROOT}',
                envDict=config.CONTAINER_MONGO_ENV_DICT,
                network=config.CONTAINER_MONGO_POSTGRES_NET,
                detach=True, interactive=False, TTY=False
            )

            # DockerCommand run dpage/pgadmin4:6.20
            DockerCommand.dockerRun(
                tag=config.IMAGE_MONGODB_EXPRESS_TAG,
                name=config.CONTAINER_MONGODB_EXPRESS_NAME,
                port=config.CONTAINER_MONGODB_EXPRESS_PORT_LIST,
                volume=f'{config.CONTAINER_MONGODB_EXPRESS_ROOT_MAP}:{config.CONTAINER_MONGODB_EXPRESS_ROOT}',
                envDict=config.CONTAINER_MONGO_EXPRESS_ENV_DICT,
                network=config.CONTAINER_MONGO_POSTGRES_NET,
                detach=True, interactive=False, TTY=False
            )

            time.sleep(5)
            os.system(f'open http://localhost:{config.CONTAINER_MONGODB_EXPRESS_PORT_LIST[0].split(":")[0]}')

        if RUN == 'OTHER':
            pass
    
    @classmethod
    def build_postgres_environment(cls, RUN, config):
        if RUN == 'images' or RUN == 'all':
            # DockerCommand pull Images
            DockerCommand.dockerPull(tag=config.IMAGE_POSTGRES_TAG)
            DockerCommand.dockerPull(tag=config.IMAGE_PGADMIN_TAG)

        if RUN == 'build' or RUN == 'all':
            # subprocess.run(f"mkdir -p {config.CONTAINER_POSTGRES_ROOT_MAP}", shell=True)
            # subprocess.run(f"mkdir -p {config.CONTAINER_PGADMIN_ROOT_MAP}", shell=True)

            # DockerCommand run mongodb
            DockerCommand.dockerRun(
                tag=config.IMAGE_POSTGRES_TAG,
                name=config.CONTAINER_POSTGRES_NAME,
                port=config.CONTAINER_POSTGRES_PORT_LIST,
                volume=f'{config.CONTAINER_POSTGRES_ROOT_MAP}:{config.CONTAINER_POSTGRES_ROOT}',
                envDict=config.CONTAINER_POSTGRES_ENV_DICT,
                network=config.CONTAINER_MONGO_POSTGRES_NET,
                detach=True, interactive=False, TTY=False
            )

            # DockerCommand run dpage/pgadmin4:6.20
            DockerCommand.dockerRun(
                tag=config.IMAGE_PGADMIN_TAG,
                name=config.CONTAINER_PGADMIN_NAME,
                port=config.CONTAINER_PGADMIN_PORT_LIST,
                volume=f'{config.CONTAINER_PGADMIN_ROOT_MAP}:{config.CONTAINER_PGADMIN_ROOT}',
                envDict=config.CONTAINER_PGADMIN_ENV_DICT,
                network=config.CONTAINER_MONGO_POSTGRES_NET,
                detach=True, interactive=False, TTY=False
            )

            time.sleep(5)
            os.system(f'open http://localhost:{config.CONTAINER_PGADMIN_PORT_LIST[0].split(":")[0]}')

        if RUN == 'OTHER':
            # DockerCommand postgres:15.2 - 建立資料庫
            DockerCommand.dockerExec(
                name=config.CONTAINER_POSTGRES_NAME,
                cmd=f"psql -U postgres -c \'CREATE DATABASE {config.CONTAINER_POSTGRES_DB1};\'",
                detach=False, interactive=True, TTY=False
            )  # 建立資料庫 crawlerdb
