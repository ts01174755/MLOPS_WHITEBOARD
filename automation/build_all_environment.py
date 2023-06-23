import env_config
from  src.controller.build_environment import BuildEnvironment as BuildEnvironment

if __name__ == "__main__":
    BuildEnvironment.build_local_environment(RUN='all', config=env_config)
    BuildEnvironment.build_monodb_environment(RUN='all', config=env_config)
    BuildEnvironment.build_postgres_environment(RUN='all', config=env_config)
