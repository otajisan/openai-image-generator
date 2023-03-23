import os
import sys
import openai

openai.apikey = os.environ['OPENAI_API_KEY']


class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RESET = '\033[0m'


def main(prompt: str, width: int, height: int):
    response = openai.Image.create(
        prompt=prompt,
        n=5,
        size=f'{width}x{height}'
    )
    image_url = response['data'][0]['url']

    image_urls = '\n'.join([f"{idx + 1}: {x['url']}" for idx, x in enumerate(response['data'])])
    print(f'{Color.GREEN}🍣 Generated image!:{Color.GREEN}\n{Color.BLUE}{image_urls}{Color.BLUE}')


if __name__ == '__main__':
    prompt = input(f'prompt: ')
    # width = int(input('width: '))
    # height = int(input('height: '))
    width = 1024
    height = 1024

    print(f'{Color.BLUE}prompt: {prompt} width: {width} height: {height}{Color.BLUE}')
    main(prompt=prompt, width=width, height=height)
