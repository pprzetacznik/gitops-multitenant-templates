from argparse import Namespace, ArgumentParser
from abc import ABC, abstractmethod
from gitops_configserver.config import setup_logger, Config


class AbstractArgumentsHandler(ABC):
    """Command pattern interface"""

    @abstractmethod
    def execute(self, args) -> None:
        pass

    @abstractmethod
    def add_parser(self, subparsers):
        pass


class ConfigGeneratorHandler(AbstractArgumentsHandler):
    def execute(self, args):
        config = Config()
        print("HELLO WORLD")

    def add_parser(self, subparsers):
        parser_config_generator = subparsers.add_parser("config_gen")
        parser_config_generator.set_defaults(func=self.execute)
        parser_config_generator.add_argument(
            "--config_dir",
            type=str,
            help="Config directory",
            dest="config_dir",
            required=True,
        )


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="GitOps multitenancy templates generator"
    )
    subparsers = parser.add_subparsers(required=True)
    ConfigGeneratorHandler().add_parser(subparsers)
    return parser.parse_args()


def main() -> None:
    setup_logger()
    args = parse_arguments()
    args.func(args)


if __name__ == "__main__":
    main()
