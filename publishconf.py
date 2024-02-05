# Pelican 网站正式发布设置
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa F403

SITEURL = "https://rexzhang.com"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True


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
