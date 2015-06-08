#Quick python test

Please use python 3+

<h2> 1st task, word counter </h2>
<em>Implementation can be found in <code>wordcounter.py</code></em>
<h3>Usage</h3>
<p>For example, run by invoking
	<code>python wordcounter.py -s wordcounter_test.txt</code>
where source (-s) is file from which to read words</p>

<p><code>python wordcounter.py --h</code>
gives you stratup options. Together with <code>-s</code> parameter it is possible to define <code>-o</code> parameter to specify file to which result will be written.</p>

<h3>Final notes</h3>
<p>Reading of unicode files and words is not properly tested and probably should be improved.</p>
<p>In terms of separation of concerns <em>wordcounter.py</em> could be improved so that reading words is separated from processing. This would make more testable code which could plugin different data source. But this would mean looping once more through list for this specifical case where imput is expected to be file.</p>

<h2> 2nd task, paragraph cleaner </h2>
<em>Implementation can be found in <code>pcleaner.py</code></em>
<p>It is implemented as specified: clens only paragraph containing only white spaces.</p>
<p>Paragraphs with attributres (ex &lt;p style="color: red"&gt;) containing only white spaces are cleared also.</p>
<em>See comments in method clean() for different cleaning policies</em> (if you want to clean tabs and newlines for example)

<h3>Usage</h3>
<p>For example, run by invoking
	<code>python pcleaner.py -s pcleaner_test.html</code>
where source (-s) can be file or http / https URL</p>

<p><code>python pcleaner.py --h</code>
gives you stratup options. Together with <code>-s</code> parameter it is possible to define <code>-o</code> parameter to specify file to which result will be written.</p>

<h3>Testing</h3>
file <code>test_pcleaner.py</code> contains some common test cases

<h3>Final notes</h3>
Handling of source(file, URL) data coding can be improved further

<h2>3th task, caching functions return value</h2>
<em>Implementation can be found in <code>cache_decorator.py</code></em>
<p>Cache expiry time and number of hits are hardcoded as requested by task, but decorator can be changed in order to pass those two parameters as arguments.</p>
<p><em>Time triggered eviction</em> is done by one timer thread for every cached item, what simplifies the code, but may not be appropriate for large number of cached items. Anyway, evicting items after timer expires releases memory in case when some cached items are rarely hit. For real world scenario time based cache eviction policy can be rewritten differently, of course</p>

<h3>Invoking/Testing</h3>
<p>To test eviction based on number of times function was invoked, run test <code>test_cache_decorator.py</code></p>
<p>For time based eviction test scenarios, run test <code>test_cache_decorator_time.py</code> . The reason behind separating time based eviction to different test case is that it takes 10 minutes to run.</p>

<h3>Final notes</h3>
<p>If you want to see more detailed log messages, change log configuration in <code>cache_decorator.py</code> to <code>logging.basicConfig(level=logging.DEBUG)</code></p>