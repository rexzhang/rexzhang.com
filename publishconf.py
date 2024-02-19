# Pelican 网站正式发布设置
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.as_posix())
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
