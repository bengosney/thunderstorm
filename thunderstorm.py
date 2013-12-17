#!/usr/bin/env python

# Copyright Ben Gosney 2013
# bengosney@googlemail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from lxml import etree
import sys, getopt

def vcsGen(dirs):
    component = etree.Element('component')
    component.set('name', 'VcsDirectoryMappings')
    
    for d in dirs:
        mapping = etree.Element('mapping')
        mapping.set('directory', d)
        mapping.set('vcs', 'Git')
        component.append(mapping)

    project = etree.Element('project')
    project.set('version','4')
    project.append(component)

    return etree.tostring(project, pretty_print=True)

def imlGen(incDir, excludes=[]):
    content = etree.Element('content')
    content.set('url', incDir)

    for ex in excludes:
        excludeFolder = etree.Element('excludeFolder')
        excludeFolder.set('url', ex)
        content.append(excludeFolder)

    component = etree.Element('component')
    component.set('name', 'NewModuleRootManager')
    component.append(content)

    module = etree.Element('module')
    module.set('type', 'WEB_MODULE')
    module.set('version', '4')
    module.append(component)

    return etree.tostring(module, pretty_print=True)

def help():
    print 'thunderstorm.py -d <domain> -n <project name - optional>'

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hd:n:",["domain=","name="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    domain = ''
    name = ''

    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-n", "--name"):
            name = arg

    if domain == '':
        help()
        sys.exit(1)

    print imlGen(domain)
    print vcsGen(['test'])


if __name__ == "__main__":
   main(sys.argv[1:])
