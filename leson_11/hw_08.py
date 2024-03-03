from abc import ABC, abstractmethod
from datetime import datetime


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


class SocialChannel(ABC):
    def __init__(self, network: str, followers: int):
        self.network = network
        self.followers = followers

    @abstractmethod
    def make_a_post(self, message: str) -> None:
        pass


class Youtube(SocialChannel):
    def make_a_post(self, message: str) -> None:
        print(f"All your {self.followers} {self.network} followers {message}")


class Facebook(SocialChannel):
    def make_a_post(self, message: str) -> None:
        print(f"All your {self.followers} {self.network} followers {message}")


class Twitter(SocialChannel):
    def make_a_post(self, message: str) -> None:
        print(f"All your {self.followers} {self.network} followers {message}")


def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.make_a_post(message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    current_time = int(datetime.now().strftime("%H"))
    for post in posts:
        message, timestamp = post.message, post.timestamp
        for channel in channels:
            if timestamp <= current_time:
                post_a_message(channel, message)


if __name__ == "__main__":
    new_posts = [
        Post(message="can see your new video now!", timestamp=1),
        Post(message="will see your new video soon!", timestamp=8),
    ]

    social_networks = [
        Youtube(network="Youtube", followers=1500),
        Facebook(network="Facebook", followers=3800),
        Twitter(network="Twitter", followers=11000),
    ]

    process_schedule(new_posts, social_networks)
