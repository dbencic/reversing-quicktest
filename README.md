# reversing-quicktest
ReversingLabs quick python test

Please use python 3+

<h2> 1st task, word counter </h2>

<h2> 2nd task, paragraph cleaner </h2>
<em>Implementation can be found in <code>pcleaner.py</code></em>
<p>It is implemented as specified: clens only paragraph containing only white spaces.</p>
<p>Paragraphs with attributres (ex &lt;p style="color: red"&gt;) containing only white spaces are cleared also.</p>
<em>See comments in method clean() for different cleaning policies</em>

<h3>Usage</h3>
For example, run by invoking
	<code>python pcleaner.py -s pcleaner_test.html</code>
where source (-s) can be file or http / https URL

Invoking
	<code>python pcleaner.py --h</code>
gives you stratup options

<h3>Testing</h3>
file test_pcleaner.py contains some common test cases

<h3>Final notes</h3>
Handling of source data coding can be improved further

<h2>3th task, caching function return value</h2>
