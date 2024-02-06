# rexzhang.com

## Live Preview

```shell
pelican --autoreload --listen
```

```shell
cd theme-rexzhang/static/css
sass -w style.scss style.css
```

## Export .css from pygments

```shell
pygmentize -S default -f html -a .highlight > default.css
```
