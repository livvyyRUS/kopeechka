from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

if __name__ == '__main__':
    setup(
        name='kopeechka',
        version='7.0',
        description='This code is a representation of the kopeechka.store API in Python',
        project_urls={
            "Source": "https://github.com/livvyyRUS/kopeechka",
        },
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=['kopeechka'],
        install_requires=["requests", "aiohttp"],
        author_email='rem.game.on@gmail.com'
    )
