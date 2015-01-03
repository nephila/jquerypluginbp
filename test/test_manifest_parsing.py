from generate import parse_package_manifest, PackageManifestException
import unittest

class TestManifestParsing(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_package_manifest(self):
        sample_config = """
            {
                "name": "vimeoplaylist",
                "title": "jQuery Vimeo Playlist Plugin",
                "description": "jQuery plugin for creating your playlist with Vimeo.",
                "keywords": [
                    "vimeo",
                    "playlist",
                    "video"
                ],
                "version": "0.1.0dev",
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
                    "jquery": ">=1.4.4",
                    "froogaloop": ">=2"
                }
            }
        """
        parsed_manifest = parse_package_manifest(sample_config)
        self.assertFalse(parsed_manifest['plugin_name'] == '')

    def test_parse_wrong_package_manifest(self):
        sample_config = """
            wrong package manager
        """
        parsed_manifest = self.assertRaises(PackageManifestException, parse_package_manifest, sample_config)

    def test_parse_package_manifest_with_missing_parameters(self):
        sample_config = """
            {
                "title": "jQuery Vimeo Playlist Plugin",
                "description": "jQuery plugin for creating your playlist with Vimeo."
            }
        """
        parsed_manifest = self.assertRaises(PackageManifestException, parse_package_manifest, sample_config)
