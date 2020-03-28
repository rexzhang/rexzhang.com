#!/usr/bin/env python
# -*- coding: utf-8 -*- #


import json
from string import Template
from pathlib import Path

META_FORMAT = """
:author: {author}
:date: {data}
:modified: {modified}
:status: {status}
"""
# :category: {category}
# :tags: {tags}


ReST_TEMPLATE = """
$title

$meta

$content
"""


def create_restructuredtext_file(post):
    title = post['title']
    if title is None:
        title = 'None\n####'
    else:
        a = ['#' for _ in range(len(title) * 2)]
        title = '{}\n{}'.format(title, ''.join(a))
    author = post['author']

    data = post['created_time']
    modified = post['published_time']
    if post['published']:
        status = 'published'
    else:
        status = 'draft'
    slug = post['id']

    if len(post['terms']['category']) >= 1:
        category = post['terms']['category'][0]
    else:
        category = None
    if category == '无类可归':
        category = None
    tags = post['terms']['tag']
    if len(tags) == 0:
        tags = None
    else:
        tags = ', '.join(tags)

    meta = META_FORMAT.format(
        author=author,
        data=data, modified=modified, status=status, slug=slug,
        category=category, tags=tags,
    )
    if category:
        meta = '{}:category: {}\n'.format(meta, category)
    if tags:
        meta = '{}:tags: {}\n'.format(meta, tags)

    content = post['content']
    if post['type'] == 'blog':
        content_type = 'posts'
    else:
        content_type = 'pages'

    path = Path('content/{}'.format(content_type))
    filename = 'content/{}/{}{}-{}.rst'.format(
        content_type, post['created_time'][:4], post['created_time'][5:7], post['id']
    )
    file_content = Template(ReST_TEMPLATE).substitute(
        title=title,
        meta=meta,
        content=content
    )

    path.mkdir(exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(file_content)

    return


def import_from_rpress(file):
    with open(file) as f:
        data = json.load(f)

    if data is None:
        return

    for post in data.get('posts'):
        create_restructuredtext_file(post)

    return


if __name__ == '__main__':
    import_from_rpress('/Users/rex/Documents/TEMP/blog/rexzhang.com.2020-03-28.06-36-10.801917.rpress.json')
