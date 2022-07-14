from random import choice, randint
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(eq=True, frozen=True)
class Document(object):
    title: str
    url: str
    filetype: str
    source: Optional[str]
    published: datetime


class DocBuilder(object):
    @staticmethod
    def build_html(url, title, content):
        return f"""\
            <!-- Insert Comment Here -->
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <title>{title}</title>
                    <style>
                        body {{
                            color: black;
                            overflow-x: hidden;
                        }}
                    </style>
                </head>
                <body>
                    <nav id="fresh-navbar">
                        <a href="{url}">Home</a>
                    </nav>
                    <!-- 339200193029 -->
                    <main>
                        <p class="content">
                            {content}
                        </p>
                        <h1 id="339200193029">
                        </h1>
                    </main>
                    <footer>
                        <p id="cool-footer">Ring Ring, Lets go above</p>
                    </footer>
                </body>
            </html>
        """

    @staticmethod
    def build_url() -> str:
        # Subdomains Domain TLD Directory File
        domains = [
            [ "www", "ww3", "service", "forum", "community", "help" ],
            [ "friends", "people-hub", "code-space", "kata-warrior", "ninja" ],
            [ "com", "org", "space", "net", "shop", "ninja" ],
            [ "home", "help", "profile", "support" ],
            [ "settings", "login", "items", "robots" ]
        ]

        return f"https://{'.'.join(choice(domain) for domain in domains[:3])}/{choice(domains[3])}/{choice(domains[4])}"

    @staticmethod
    def build_title() -> str:
        return choice([
            "How to get bonus points",
            "What's love?",
            "Coding! A choice or suffering?",
            "How to repair a broken pc without repairing it?",
            "Love Test",
            "Google Dorking - Zero to Hero",
            "Does he / she love me?",
            "Python or JavaScript? Suck Java",
            "Whats 6 * 6(9)0"
            "Why purple is the best color",
            "Can I cheat in this Kata?",
            "TV? Who watches that",
            "Math | 14 + 6 = 20"
        ])

    @staticmethod
    def build_content() -> str:
        return choice([
            "Is it a lie or not? Would be nice to know, Mr. You",
            "Can you trust a code? Studies say no, hence we are all lost!",
            "Python vs JS! Are there any differences? Lemme me know in the comments",
            "My password is 1234567890, is it safe?",
            "100 Warriors failed on google dorking. You too?",
            "I loved my crush but she didn't love me, it sucked",
            "RegEx are powerful, at least I think so",
            "HTML is a programming language, change my mind",
            "Cars make vrum vrum, you make nothing"
        ])

    @classmethod
    def build(cls) -> Document:
        return Document(
            title=cls.build_title(),
            url=cls.build_url(),
            filetype=(ext := choice(["html", "htm", "php", "txt", "pdf"])),
            source=None if ext == "pdf" else cls.build_content(),
            published=datetime.fromisoformat(f"{randint(1970, 2022)}-0{randint(1, 9)}-{randint(10, 28)} 01:01:01")
        )

    def __init__(self, n: int):
        self.documents = [self.build() for _ in range(n)]

    def __iter__(self):
        yield from self.documents
