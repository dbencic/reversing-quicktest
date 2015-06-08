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
file <code>test_pcleaner.py</code> contains some common test cases

<h3>Final notes</h3>
Handling of source(file, URL) data coding can be improved further

<h2>3th task, caching functions return value</h2>
<em>Implementation can be found in <code>cache_decorator.py</code></em>
<p>Cache expiry time and number of hits are hardcoded as requested by task, but decorator can be changed in order to pass those two parameters as arguments</p>
<p>Time triggered eviction is done by one timer thread for every cache item, what simplifies the code, but may not be appropriate for large number of cached items. Anyway evicting items after timer expires releases some memory in case when some cached items are rarely hit. For real world scenario time based cache eviction policy can be written differently, of course</p>

<h3>Invoking/Testing</h3>
<p>for number of hits test scenarios, run test <code>test_cache_decorator.py</code></p>
<p>for timebased eviction test scenarios, run test <code>test_cache_decorator_time.py</code> . The reason behind separating time based eviction to different test is that it takes 10 minutes to run</p>