from enum import Enum


class WebSearchProvidersEnum(str, Enum):
    BAIDU = "baidu"
    BING = "bing"
    WECHAT = "wechat"
    GITHUB = "github"
    GOOGLE = "google"


class GithubSearchTypesEnum(str, Enum):
    REPO = "repositories"
    CODE = "code"
    ISSUE = "issues"
    PR = "pullrequests"
    DISCUSS = "discussions"
    USER = "users"
    COMMIT = "commits"
    PACKAGE = "registrypackages"
    WIKI = "wikis"
    TOPIC = "topics"
    MARKETPLACE = "marketplace"
