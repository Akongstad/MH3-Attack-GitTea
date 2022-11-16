import requests as req
import time as t
import re

def find_answer(r):
    pattern = r'<h2.*class=\"(.*)\">.*<\/h2>'
    regex = re.compile(pattern)
    matches = re.findall(regex, r.text)
    return matches[0] if len(matches) > 0 else " "

def main():
    r = req.get("https://erdetfredag.dk")
    print(find_answer(r))

if __name__ == "__main__":
    main()
