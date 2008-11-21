
import os, sys

myTagsFile = '/home/rtfb/projects/vim-dox/tags-sample'
myIndexXml = '/home/rtfb/projects/vim-dox/index-sample.xml'

def getWordListFromTags (tagsFile):
    tags = open (tagsFile).readlines ()
    tags = filter (lambda l: not l.startswith ('!'), tags)
    words = []

    for t in tags:
        items = t.split ('\t')
        word = items[0]
        file = items[1]
        base, ext = os.path.splitext (file)

        if ext[1:] in ['c', 'cpp', 'cc', 'cxx', 'h', 'fdf']:
            words.append (word)

    return words

def writeWordList (list, file):
    f = open (file, 'w')

    for w in list:
        f.write (w + '\n')

def getText(nodelist):
    rc = ''

    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data

    return rc

def parseDoxygenIndex (file):
    import xml.dom.minidom

    contents = open (file).read ()
    dom = xml.dom.minidom.parseString (contents)
    compounds = dom.getElementsByTagName ('compound')
    groupNames = []

    for c in compounds:
        if c.attributes['kind'].nodeValue == 'group':
            groupNames.append (getText (c.getElementsByTagName ('name')[0].childNodes))

    return groupNames

def writeEmptySplFile (homeDir):
    emptySplFile = 'VIMspell2\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    emptySplFilePath = homeDir + '/.vim/spell/fromtags.utf-8.spl'
    open (emptySplFilePath, 'wb').write (emptySplFile)

def main ():
    wordList = getWordListFromTags (myTagsFile)
    print 'tags read.'
    homeDir = os.environ['HOME']
    groupList = parseDoxygenIndex (myIndexXml)
    print 'doxygen index read.'
    dictFile = homeDir + '/.vim/spell/fromtags.utf-8.add'
    writeWordList (wordList + groupList, dictFile)
    print 'word list written.'

    writeEmptySplFile (homeDir)
    cmd = 'vim -cmd ' + '":mkspell! %s"' % (dictFile) + ' --cmd ":q"'
    os.system (cmd)
    print 'spl generated.'
    print 'Done.'

if __name__ == '__main__':
    main ()

