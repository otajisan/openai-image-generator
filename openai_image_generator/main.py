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


def main(prompt: str, width: int, height: int, number: int):
    response = openai.Image.create(
        prompt=prompt,
        n=number,
        size=f'{width}x{height}'
    )

    image_urls = '\n'.join([f"{idx + 1}: {x['url']}" for idx, x in enumerate(response['data'])])
    print(f'{Color.GREEN}🍣 Generated image!:{Color.RESET}\n{Color.BLUE}{image_urls}{Color.RESET}')


if __name__ == '__main__':
    prompt = input(f'prompt: ')
    # width = int(input('width: '))
    # height = int(input('height: '))
    # number = int(input('number: '))
    width = 1024
    height = 1024
    number = 5

    print(
        f'{Color.BLUE}[parameters]\nprompt: {prompt}\n'
        f'width: {width}\n'
        f'height: {height}\n'
        f'number: {number}{Color.RESET}'
    )
    main(prompt=prompt, width=width, height=height, number=number)
