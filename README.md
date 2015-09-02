jQueryPluginBP
==============
[![Build Status][travis-image]][travis-url] [![Coveralls Status][coveralls-image]][coveralls-url]
[![Latest Version](https://img.shields.io/pypi/v/jquerypluginbp.svg)](https://pypi.python.org/pypi/jquerypluginbp/)
[![Supported Python versions](https://img.shields.io/badge/python-2.7%2C%202.8%2C%203.3%2C%203.4-blue.svg)](https://pypi.python.org/pypi/jquerypluginbp/)
[![Downloads](https://img.shields.io/pypi/dm/jquerypluginbp.svg)](https://pypi.python.org/pypi/jquerypluginbp/)

Nephila's internal tool for generating jQuery plugins boilerplate code

## Install

    pip install jquerypluginbp

## Usage

First of all you need to define your plugin.json manifest file. A real life example:

    {
        "name": "vimeoplaylist",
        "title": "jQuery Vimeo Playlist Plugin",
        "description": "jQuery plugin for creating your playlists with Vimeo.",
        "keywords": [
            "vimeo",
            "playlist",
            "video"
        ],
        "version": "0.2.0",
        "author": {
            "name": "Nephila"
        },
        "maintainers": [
            {
                "name": "Andrea Stagi",
                "email": "stagi.andrea@gmail.com",
                "url": "http://github.com/astagi"
            }
        ],
        "licenses": [
            {
                "type": "MIT",
                "url": "https://github.com/nephila/jquery-vimeoplaylist/blob/master/LICENSE"
            }
        ],
        "bugs": "https://github.com/nephila/jquery-vimeoplaylist/issues",
        "homepage": "https://github.com/nephila/jquery-vimeoplaylist",
        "download": "https://github.com/nephila/jquery-vimeoplaylist",
        "dependencies": {
            "jquery": ">=1.7"
        }
    }
    
Now you can run jquerypluginbp:

    $ jquerypluginbp yourmanifest.plugin.json

You can also specify the destination path:

    $ jquerypluginbp yourmanifest.plugin.json -d destination_path

[travis-url]: https://travis-ci.org/nephila/jquerypluginbp
[travis-image]: http://img.shields.io/travis/nephila/jquerypluginbp.svg

[coveralls-url]: https://coveralls.io/r/nephila/jquerypluginbp
[coveralls-image]: http://img.shields.io/coveralls/nephila/jquerypluginbp/master.svg
