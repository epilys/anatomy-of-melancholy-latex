#!/python3
from html.parser import HTMLParser
from html.entities import name2codepoint
import csv
import re
#html-tidy --enclose-text yes --enclose-block-text yes -wrap 0 < 10800-h.htm > 10800-h.html

class Element():
    def __init__(self, tag='data',name=None,lang='en',_class=None):
        self.tag = tag
        self.data = ""
        self.name = name
        self.children = []
        self._class=_class
        self.lang=lang
    def __str__(self):
        if self.tag == 'data':
            return 'textNode <' + self.data + '>'
        return str(self.tag) + " " + self.data + ", ".join([str(c) for c in self.children])
    def __repr__(self):
        return str(self)
    def children_as_tex(self):
        return ' '.join([c.as_tex() for c in self.children])
    def as_tex(self):
        if self.tag == 'data':
            return self.data
        elif self.tag == 'h1':
            return '\n\n\\chapter{'+self.children_as_tex()+'}\n'
        elif self.tag == 'h2':
            return '\n\n\\part{'+self.children_as_tex()+'}\n'
        elif self.tag == 'h3':
            return '\n\n\\chapter{'+self.children_as_tex()+'}\n'
        elif self.tag == 'h4':
            return '\n\n\\section{'+self.children_as_tex()+'}\n'
        elif self.tag == 'a':
            if self.name is not None:
                return ''
            return '\\authorfootnote{'+self.children_as_tex().replace('[','').replace(']','')+'}'
        elif self.tag == 'span' and self.lang == 'la':
            return '\\li{'+self.children_as_tex()+'}'
        elif self.tag == 'span' and self.lang == 'gr':
            return '\\textgreek{'+self.children_as_tex()+'}'
        elif self.tag == 'p':
            return '\n\n'+self.children_as_tex()
        elif self.tag == 'bibcite':
            inner = re.sub(r" ([mdclxvi]+\.)", " \\\\rn{\\1}", self.children_as_tex(), 0, re.MULTILINE)
            return '\\bibcite{' + inner + '}'
        elif self.tag == 'cite':
            return '\\bookcite{\\textlatin{' + self.children_as_tex() + '}}'
        elif self.tag == 'i':
            return '\\emph{' + self.children_as_tex() + '}'
        elif self.tag == 'div' and self._class == 'poem':
            lines = '\n\\begin{verse}%\n' + self.children_as_tex()[:-6].strip() + '\\\\!' + '\n\\end{verse}%\n'
            if self.lang == 'la':
                return '\n\n\\begin{latin}' + lines + '\\end{latin}\n\n'
            elif self.lang == 'gr':
                return '\n\n\\begin{greek}' + lines + '\\end{greek}\n\n'
            else:
                return '\n' + lines + '\n'
        elif self.tag == 'div' and self._class == 'line':
            return self.children_as_tex().strip() + '\\\\*\n'
        else:
            return self.children_as_tex()

    def append(self, data):
        if self.tag == 'data':
            self.data += data.replace('\n', ' ').replace('  ', ' ')
        elif len(self.children)>0 and self.children[len(self.children)-1].tag == 'data':
            self.children[len(self.children)-1].append(data)
        else:
            new_element = Element()
            new_element.append(data)
            self.push(new_element)

    def push(self, child):
        self.children.append(child)

"""
Start tag: span
     attr: ('lang', 'la')
Data     : Scire tuum nihil est, nisi te scire hoc
sciat alter
End tag  : span
Data     : ). I might be of Thucydides' opinion,
Start tag: a
     attr: ('href', '#note59')
Data     : [59]
End tag  : a
Data     : “to know a thing and
not to express it, is all one as if he knew it not.” When I first took this
task in hand,
Start tag: span
     attr: ('lang', 'la')
Data     : et quod ait
Start tag: a
     attr: ('href', '#note60')
Data     : [60]
End tag  : a
Data     : ille, impellents genio negotium suscepi
End tag  : span
Data     : ,
this I aimed at;
Start tag: a
     attr: ('href', '#note61')
Data     : [61]
End tag  : a
Start tag: span
     attr: ('lang', 'la')
Data     : vel ut lenirem animum scribendo
End tag  : span
"""
ignored_elements = ['br', 'hr', 'b']
phrases = {}
bibcites = []
cites = []
paragraphs = []
root = Element(tag="h1")
root.append("ROOT")
#sections = [root]

def get_current_section():
    return sections[len(sections)-1]

class MyHTMLParser(HTMLParser):
    element_stack=[root]

    def get_current_element(self):
        if len(self.element_stack) == 0:
            return None
        return self.element_stack[len(self.element_stack)-1]
    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        if tag in ignored_elements:
            return
        current_el = self.get_current_element()
        #if current_el is not None and current_el.tag == 'p' and tag not in ['a', 'span']:
        #    self.handle_endtag('p')
        lang = next((a[1] for a in attrs if a[0] == 'lang'), None)
        name = next((a[1] for a in attrs if a[0] == 'name'), None)
        if tag == 'span' and lang is not None:
            if lang not in phrases:
                phrases[lang] = []
            self.element_stack.append(Element(tag=tag,lang=lang))
            return
        elif tag == 'span' and ('class', 'bibcite') in attrs:
            self.element_stack.append(Element(tag='bibcite',lang=lang))
            return
        elif tag == 'span' and ('class', 'cite') in attrs:
            self.element_stack.append(Element(tag='cite',lang=lang))
            return
        elif tag == 'a' and name is not None:
            self.element_stack.append(Element(tag=tag, name=name, lang=lang))
            return
        elif tag == 'div' and ('class', 'poem') in attrs:
            self.element_stack.append(Element(tag=tag,lang=lang,name=name,_class='poem'))
            return
        elif tag == 'div' and ('class', 'line') in attrs:
            self.element_stack.append(Element(tag=tag,lang=lang,name=name,_class='line'))
            return
        self.element_stack.append(Element(tag=tag,lang=lang,name=name))
    def handle_endtag(self, tag):
        if tag in ignored_elements:
            return
        el = self.element_stack.pop()
        parent = self.get_current_element()
        parent.push(el)
        if el.tag == "p":
            paragraphs.append(el.data)
        elif el.tag in ['h2', 'h3', 'h4']:
            #sections.append(el)
            pass
        elif el.tag == tag and el.lang == 'en':
            # Ignored
            pass
        elif tag == 'span' and el.tag == 'bibcite':
            bibcites.append((parent, el.data))
        elif tag == 'span' and el.tag == 'cite':
            cites.append((parent, el.data))
        elif el.lang not in phrases:
            # Ignored
            pass
        else:
            # is phrase
            phrases[el.lang].append((parent, el.as_tex()))
        #print("End tag  :", tag)

    def handle_data(self, data):
        #print("Data     :", data)
        if len(self.element_stack) > 0:
            el = self.get_current_element()
            if el.lang in phrases:
                el.append(data)
            elif el.tag in ['bibcite', 'cite']:
                el.append(data)
            else:
                el.append(data)

    def handle_comment(self, data):
        #print("Comment  :", data)
        pass

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        #print("Named ent:", c)
        pass

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        #print("Num ent  :", c)
        pass

    def handle_decl(self, data):
        #print("Decl     :", data)
        pass

parser = MyHTMLParser()

text = open('./10800-h.html', 'r').read()

parser.feed(text)

for lang in phrases:
    print(lang, "= ",len(phrases[lang]))
print("stack size = ", len(parser.element_stack))
#print("stack  = ", parser.element_stack)
print("paragraphs size = ", len(paragraphs))
print("bibcites = ", len(bibcites))
#print("sections  = ", len(sections))
def process_line(line):
    line = re.sub(r'[ ]{2,}', ' ', line)
    line = re.sub(r'[ ]{2,}', ' ', line)
    line = re.sub(r'(\\authorfootnote\{\d+\}) ', r'\1', line)
    line = re.sub(r"\n[ ]", "\\n", line, 0, re.MULTILINE)
    line = line.replace('———', '------')
    line = line.replace('——', '---')
    line = line.replace('—', '--')
    line = line.replace(' , ', ', ')
    line = line.replace(' ,', ',')
    line = line.replace(' . ', '. ')
    line = line.replace(' .', '.')
    line = line.replace(' ;', ';')
    line = line.replace(' :', ':')
    line = line.replace('“ ', '"')
    line = line.replace('“', '"')
    line = line.replace(' ”', '"')
    line = line.replace('”', '"')
    line = line.replace(' !', '!')
    line = line.replace(' )', ')')
    line = line.replace('( ', '(')
    line = line.replace(' ?', '?')
    line = line.replace('&c.', '\\etc{}')
    return line

output_f = open("html_formatted2.tex", "a")
for sec in parser.element_stack:
    print("\n", file=output_f)
    #print("section  = ", sec)
    print(process_line(sec.as_tex()), file=output_f)
    for child in sec.children:
        #print("\t\tchild  = ", child)
        print(process_line(child.as_tex()), file=output_f)
        #print(child.as_tex().replace('  ', ' '), file=output_f)
    print("\n", file=output_f)
#for sec in sections:
#    print(sec[0], " ", len(sec[1]), file=open("sections.txt", "a"))

#import csv
#with open('latin.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows([[phr[0][0].data, phr[1]] for phr in phrases['la']])
#with open('greek.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows([[phr[0][0].data, phr[1]] for phr in phrases['gr']])
#with open('bibcites.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows([[b[0][0].data, b[1]] for b in bibcites])
#with open('cites.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows([[c[0][0].data, c[1]] for c in cites])
