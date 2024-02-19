# Pelican 网站基础设置
# - https://docs.getpelican.com/en/latest/settings.html

# Basic settings
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "无类可归"
DELETE_OUTPUT_DIRECTORY = True
PATH = "content"
SITENAME = "RexZhang.com"
SITEURL = "http://127.0.0.1:8000"
STATIC_PATHS = [
    # "images",
    "key",
    "favicon/rexzhang-balloon.ico",
]
TYPOGRIFY = True
# PYGMENTS_RST_OPTIONS = []

# URL settings
RELATIVE_URLS = True
ARTICLE_URL = "posts/{date:%Y}/{slug}"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

# Time and Date
TIMEZONE = "Asia/Shanghai"
DEFAULT_DATE_FORMAT = "%Y/%m/%d"

# Metadata
AUTHOR = "Rex Zhang"
EXTRA_PATH_METADATA = {
    "favicon/rexzhang-balloon.ico": {"path": "favicon.ico"},
}

# Feed settings
FEED_ATOM = "feeds/atom.xml"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = "feeds/category/{slug}.atom.xml"
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10

# Pagination
DEFAULT_PAGINATION = True
PAGINATED_TEMPLATES = {"index": 10, "tag": 10, "category": 10, "author": None}

# Translations
DEFAULT_LANG = "zh-Hans"
TRANSLATION_FEED_ATOM = None


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Themes
THEME = "theme-rexzhang"
# THEME = "notmyidea"  # 自带的
# THEME = 'themes/apricot'  # 字体非常漂亮
# THEME = 'themes/basic'
# THEME = 'themes/brutalist'
# THEME = 'themes/bootstrap'
# THEME = 'themes/clean-blog'
# THEME = 'themes/Flex'
# THEME = 'themes/gum'
# THEME = 'themes/hyde'
# THEME = 'themes/iris'
# THEME = 'themes/jesuislibre'  # 字体样式
# THEME = 'themes/nest'
# THEME = 'themes/nikhil-theme' # --
# THEME = 'themes/pujangga'  # error
# THEME = 'themes/SoMA2'
# THEME = 'themes/voce  # 漂亮 不能用

SITESUBTITLE = "从记录到不仅仅是记录"
DISQUS_SITENAME = None
GITHUB_URL = "https://github.com/rexzhang/rexzhang.com"

# TODO: remove it!
ANALYTICS = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VJSBKX9EGM"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-VJSBKX9EGM');
</script>
"""
