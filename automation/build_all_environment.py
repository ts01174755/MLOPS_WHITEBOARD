import env_config
import subprocess
from  src.controller.build_environment import BuildEnvironment as BuildEnvironment

if __name__ == "__main__":
    print("Building all environments")

    BuildEnvironment.build_local_environment(RUN='all', config=env_config)
    # BuildEnvironment.build_monodb_environment(RUN='all', config=env_config)
    # BuildEnvironment.build_postgres_environment(RUN='all', config=env_config)

    subprocess.run("pip3 freeze > requirment.txt", shell=True)
