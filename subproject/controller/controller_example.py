
from subproject.model.model_example import ModelExample

class ControllerExample:

    @classmethod
    def controllerExample(cls):
        model_example = ModelExample()
        print(model_example)


if __name__ == "__main__":
    print('HERE IS CONTROLLER_EXAMPLE.PY TEST')
    ControllerExample.controllerExample()
    