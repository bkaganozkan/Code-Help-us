import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


def format(color, style='', bd_color='white'):
    """
    Return a QTextCharFormat with the given attributes.
    """
    _color = QColor()
    _bd_color = QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)
    if type(bd_color) is not str:
        _bd_color.setRgb(bd_color[0], bd_color[1], bd_color[2])
    else:
        _bd_color.setNamedColor(bd_color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    _format.setBackground(_bd_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages

STYLES = {
    'character': format([255, 0, 0], 'bold'),
    'line': format([0, 0, 0],'bold','red'),
}


class Highlighter(QSyntaxHighlighter):

    keywords = ["T","t","s","f"]

    # Python operators
    operators = [
        "\.", ",", "!"]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)


        rules = []
        self.rules = []

        # Keyword, operator, and brace rules
        for w in Highlighter.keywords:
            rules += [(r'%c' % w, 0, STYLES['character'])]
        for o in Highlighter.operators:
            rules += [(r'%s' % o, 0, STYLES['line'])]



        # Build a QRegExp for each pattern

        for (pat, index, fmt) in rules:
            self.rules.append([(QRegExp(pat), index, fmt)])
    def highlightBlock(self, text):
        for rule in self.rules:
            for expression, nth, format in rule:
                # After unmatch line
                if expression == QRegExp("!"):
                    index = expression.indexIn(text,0)
                    if expression.cap(nth) == "!":
                        print("Ünlem bastın")
                        length = len(text)
                        self.setFormat(0,length,format)
                #Unmatch Char
                else:
                    print("sa")
                    index = expression.indexIn(text, 0)
                    while index >= 0:
                        index = expression.pos(nth)
                        length = len(expression.cap(nth))
                        self.setFormat(index, length, format)
                        index = expression.indexIn(text,index+length)



        self.setCurrentBlockState(0)

