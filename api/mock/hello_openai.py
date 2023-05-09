import os
import openai


def auth():
    openai.api_key = os.getenv("OPENAI_API_KEY")


def show_model_list():
    print(openai.Model.list())


if __name__ == "__main__":
    auth()
    show_model_list()
