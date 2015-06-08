import unittest
import pcleaner

class TestParagraphCleaner(unittest.TestCase):

    def test_paragraph_without_content(self):
        html = "<html><p>One paragraph with content</p><p></p></html>"
        self.assertEqual(pcleaner.clean(html), "<html><p>One paragraph with content</p></html>")

    def test_paragraph_with_one_blank(self):
        html = "<html><p>One paragraph with content</p><p> </p></html>"
        self.assertEqual(pcleaner.clean(html), "<html><p>One paragraph with content</p></html>")    

    def test_paragraph_with_some_blanks(self):
        html = "<html><p>One paragraph with content</p><p>        </p></html>"  
        self.assertEqual(pcleaner.clean(html), "<html><p>One paragraph with content</p></html>")

    def test_more_blank_paragraphs(self):
        html = "<html><p>One paragraph with content</p><p>        </p><p> </p><p></p><p>other par</p></html>"  
        self.assertEqual(pcleaner.clean(html), "<html><p>One paragraph with content</p><p>other par</p></html>")
  
    def test_blank_paragraphs_with_attributes(self):
        html = "<html><p>One paragraph with content</p><p>        </p><p style='margin: 5'> </p><p></p><p>other par</p></html>"
        self.assertEqual(pcleaner.clean(html), "<html><p>One paragraph with content</p><p>other par</p></html>")    

    def test_paragraphs_with_newline_remains(self):
        html = "<html><p>One paragraph with content</p><p>\n        </p><p style='margin: 5'> </p><p></p><p>other par</p></html>"
        self.assertEqual(pcleaner.clean(html), "<html><p>One paragraph with content</p><p>\n        </p><p>other par</p></html>")    

if __name__ == '__main__':
  unittest.main()
