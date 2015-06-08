# reversing-quicktest
ReversingLabs quick python test

Please use python 3+

** 1st task, word counter **

** 2nd task, paragraph cleaner **
Implementation can be found in pcleaner.py
It is implemented as specified: clens only paragraph containing only white spaces.
Paragraphs with attributres (ex &lt;p style="color: red"&gt;) containing only white spaces are cleared also.
See comments in method clean() for different cleaning policies

*Invocation*
For example, run by invoking
	python pcleaner.py -s pcleaner_test.html
where source (-s) can be file or http / https URL

Invoking
	python pcleaner.py --h
gives you stratup options

*Testing*
file test_pcleaner.py contains some common test cases

*Final notes*
Handling of source data coding can be improved further