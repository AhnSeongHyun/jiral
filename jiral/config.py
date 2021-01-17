from dataclasses import asdict, dataclass
from os.path import expanduser

import ujson


@dataclass(frozen=True)
class Config:
    server: str
    user: str
    token: str


def save_config(config: Config):
    config_path = f"{expanduser('~')}/.jiral"
    with open(config_path, "w+") as f:
        f.write(ujson.dumps(asdict(config)))


def load_config() -> Config:
    config_path = f"{expanduser('~')}/.jiral"
    with open(config_path, "r") as f:
        data = ujson.loads(f.read())
        return Config(server=data["server"], user=data["user"], token=data["token"])
