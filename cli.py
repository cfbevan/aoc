#!/usr/bin/env python3

import os

import click
from requests import get
from markdownify import markdownify as md
from bs4 import BeautifulSoup
from cookiecutter.main import cookiecutter

@click.group()
def cli():
    pass

@cli.command()
@click.option('-s', '--session', required=True, type=str, help="AoC session cookie.")
@click.option('-y', '--year', required=False, type=int, default=None, help="AoC year. Will use parent directory name if not provided.")
@click.option('-d', '--day', required=False, type=int, default=None, help="AoC day. Will use current directory name if not provided.")
def gen_readme(year: int | None, day: int | None, session: str):
    """Generate README.md from AoC website."""
    cwd = os.getcwd().split(os.sep)
    if year is None:
        year = int(cwd[-2])
    if day is None:
        day = int(cwd[-1][3:])
    # get html from aoc
    data = get(
        f"https://adventofcode.com/{year}/day/{day}",
        cookies={"session": session}
    )
    # parse html to get article tags with class day-desc
    soup = BeautifulSoup(data.text, 'html.parser')
    articles = soup.find_all('article', class_='day-desc')
    with open('README.md', 'w') as f:
        for article in articles:
            f.write(md(str(article)))

@cli.command()
@click.option('-s', '--session', required=True, type=str, help="AoC session cookie.")
@click.option('-y', '--year', required=False, type=int, default=None, help="AoC year. Will use parent directory name if not provided.")
@click.option('-d', '--day', required=False, type=int, default=None, help="AoC day. Will use current directory name if not provided.")
def gen_input(year: int | None, day: int | None, session: str):
    """Generate input.txt from AoC website."""
    cwd = os.getcwd().split(os.sep)
    if year is None:
        year = int(cwd[-2])
    if day is None:
        day = int(cwd[-1][3:])
    # get html from aoc
    data = get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": session}
    )
    with open('input.txt', 'w') as f:
        f.write(data.text)

@cli.command()
@click.option('-y', '--year', required=False, type=int, default=None, help="AoC year. Will use current directory name if not provided.")
@click.option('-d', '--day', required=True, type=int, help="AoC day.")
@click.option("-t", "--template", required=False, default="../template/", type=click.Path(exists=True), help="Path to template directory.")
def gen_day(year: int | None, day: int, template: str):
    """Generate day directory."""
    cwd = os.getcwd().split(os.sep)
    if year is None:
        year = int(cwd[-1])
    cookiecutter(template, extra_context={"year": year, "day": day})    


if __name__ == '__main__':
    cli()