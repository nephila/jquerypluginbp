import argparse
import io
import json
import os
import pystache

class PackageManifestException(Exception):
    pass

def parse_package_manifest(package_manifest_json):
    manifest = {}
    parameters = {}
    try:
        manifest = json.loads(package_manifest_json)
    except ValueError:
        raise PackageManifestException('Invalid package manifest.')
    required_attributes = ['name', 'description', 'version', 'author', 'licenses']
    for required_attribute in required_attributes:
        if required_attribute not in manifest:
            raise PackageManifestException('Invalid package manifest. Missing {0} attribute.'.format(required_attribute))
    if 'name' not in manifest['author']:
        raise PackageManifestException('Missing field "name" in "author".')
    if not isinstance(manifest['licenses'], list):
        raise PackageManifestException('Field "license" is not a list.')

    parameters['plugin_name'] = manifest['name'] or ''
    parameters['plugin_name_cc'] = manifest['name'].title() or ''
    parameters['plugin_description'] = manifest['description'] or ''
    parameters['plugin_version'] = manifest['version'] or ''
    parameters['plugin_author'] = manifest['author']['name'] or ''
    parameters['plugin_license'] = ''
    for license in manifest['licenses']:
        if 'type' not in license:
            raise PackageManifestException('Missing field "type" in "license".')
        parameters['plugin_license'] += license['type'] + ','
    parameters['plugin_license'] = parameters['plugin_license'][:-1]
    return parameters

def substitute(content, parameters):
    return pystache.render(content, parameters)

def generate_files(package_json_path='package.json', dest_path='.'):
    package_manifest_content = io.open(package_json_path, encoding='utf-8').read()
    parameters = parse_package_manifest(package_manifest_content)
    for root, dirs, files in os.walk('boilerplate'):
        new_root = root.replace('boilerplate', '')
        if new_root.startswith("/"):
            new_root = new_root[1:]
        new_path = os.path.join(dest_path, new_root)
        for file_ in files:
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            new_file_path = os.path.join(new_path, substitute(str(file_), parameters))
            old_file_path = os.path.join(root, str(file_))
            io.open(new_file_path, 'w', encoding='utf-8').write(substitute(io.open(old_file_path, encoding='utf-8').read(), parameters))
    new_json_manifest_path = os.path.join(dest_path, parameters['plugin_name'] + '.jquery.json')
    if not os.path.exists(new_json_manifest_path):
        io.open(new_json_manifest_path, 'w', encoding='utf-8').write(io.open(package_json_path, encoding='utf-8').read())

def install_dependencies(dest_path):
    os.system('cd {0} && bower install qunit'.format(dest_path))
    os.system('cd {0} && bower install jquery'.format(dest_path))
    os.system('cd {0} && npm install'.format(dest_path))

def generate(package_json_path='jquery.json', dest_path='.'):
    try:
        generate_files(package_json_path, dest_path)
        install_dependencies(dest_path)
    except OSError as ex:
        print (ex)

def main():
    parser = argparse.ArgumentParser(description='Generate Jquery plugin boilerplate')
    parser.add_argument('manifest', help='Jquery package manifest.')
    parser.add_argument('-d', '--dest', default='./', help='Destination plugin folder path.')
    args = parser.parse_args()
    generate(args.manifest, args.dest)

if __name__ == '__main__':
    main()