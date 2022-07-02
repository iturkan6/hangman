<h1 style='line-height: 1.15em; font-weight: bold; color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; margin-top: 15px;'>Stage 7/8: Error</h1>
<h5 style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Description</h5>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>The skeleton of the game is ready; let&apos;s put some more gameplay meat on it.</p>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>In the previous stage, if players entered the same letter twice or more, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. This doesn&rsquo;t seem fair, right? Players gain nothing, and the number of attempts gets smaller. Let&apos;s fix it!</p>
<h5 style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Objectives</h5>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>To complete this stage, follow the suggested order of the required checks:</p>
<ul style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>
    <li>Check whether players enter exactly one letter. If not, print&nbsp;<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">Please, input a single letter.</span></span>. Remember that when players input nothing or non-letter characters, it shouldn&apos;t count as a correct input either;</li>
    <li>Make sure that the player entered a lowercase English letter. If not, the program should print&nbsp;<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">Please, enter a lowercase letter from the English alphabet.</span></span>;</li>
    <li>If users enter the same letter twice (doesn&apos;t matter whether it appears in the word or not), then the program should output&nbsp;<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">You&apos;ve already guessed this letter.</span></span>. Do not decrease the number of attempts in this case;</li>
    <li>None of the three errors described above should reduce the number of remaining attempts!</li>
    <li>When players win, print&nbsp;<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">You guessed the word &lt;word&gt;!</span></span>, where&nbsp;<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">&lt;word&gt;</span></span> should be substituted with the uncovered word, and the winning message. Each one should be on a new line.</li>
</ul>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'><br></p>
<div class="alert alert-warning" style='background-color: rgb(172, 121, 32); border: 1px solid transparent; position: relative; padding: 0.75rem 1.25rem; margin-bottom: 1rem; border-radius: 0.375rem; line-height: 1.5; color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.</div>
<h5 style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Examples</h5>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>The greater-than symbol followed by a space (<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">&gt;&nbsp;</span></span>) represents the user input. Note that it&apos;s not part of the input. Comments after&nbsp;<span class="code" style='font-family: "Courier New", monospace; background-color: rgb(44, 44, 44); font-size: 12px; padding: 4px; border-radius: 5px;'><span style="color: rgb(169, 183, 198);">#</span></span> provided for illustrative purposes and not as part of the task.</p>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'><strong>Example 1</strong>:</p>
<p><span class="code-block" style="background-color: rgb(44, 44, 44); font-size: 12px; line-height: 17px; display: block; color: rgb(186, 186, 186); font-family: &quot;Segoe UI&quot;, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"></span></p>
<pre style="white-space: pre-wrap; min-width: 250px;"><span style="color: rgb(169, 183, 198);">H A N G M A N  # 8 attempts</span>

<span style="color: rgb(169, 183, 198);">----------</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; a</span>

<span style="color: rgb(169, 183, 198);">-a-a------</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; i</span>

<span style="color: rgb(169, 183, 198);">-a-a---i--</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; o</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 7 attempts</span>

<span style="color: rgb(169, 183, 198);">-a-a---i--</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; o</span>
<span style="color: rgb(169, 183, 198);">You&apos;ve already guessed this letter.</span>

<span style="color: rgb(169, 183, 198);">-a-a---i--</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; p</span>

<span style="color: rgb(169, 183, 198);">-a-a---ip-</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; p</span>
<span style="color: rgb(169, 183, 198);">You&apos;ve already guessed this letter.</span>

<span style="color: rgb(169, 183, 198);">-a-a---ip-</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; h</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 6 attempts</span>

<span style="color: rgb(169, 183, 198);">-a-a---ip-</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; k</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 5 attempts</span>

<span style="color: rgb(169, 183, 198);">-a-a---ip-</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; a</span>
<span style="color: rgb(169, 183, 198);">You&apos;ve already guessed this letter.</span>

<span style="color: rgb(169, 183, 198);">-a-a---ip-</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; z</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 4 attempts</span>

<span style="color: rgb(169, 183, 198);">-a-a---ip-</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; t</span>

<span style="color: rgb(169, 183, 198);">-a-a---ipt</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; x</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 3 attempts</span>

<span style="color: rgb(169, 183, 198);">-a-a---ipt</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; b</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 2 attempts</span>

<span style="color: rgb(169, 183, 198);">-a-a---ipt</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; d</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 1 attempt</span>

<span style="color: rgb(169, 183, 198);">-a-a---ipt</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; w</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 0 attempts</span>

<span style="color: rgb(169, 183, 198);">You lost!</span></pre>
<p></p>
<p style='color: rgb(186, 186, 186); font-family: "Segoe UI", sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(60, 63, 65); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'><strong>Example 2</strong>:</p>
<p><span class="code-block" style="background-color: rgb(44, 44, 44); font-size: 12px; line-height: 17px; display: block; color: rgb(186, 186, 186); font-family: &quot;Segoe UI&quot;, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"></span></p>
<pre style="white-space: pre-wrap; min-width: 250px;"><span style="color: rgb(169, 183, 198);">H A N G M A N  # 8 attempts</span>

<span style="color: rgb(169, 183, 198);">----</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; j</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; i</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 7 attempts</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; +</span>
<span style="color: rgb(169, 183, 198);">Please, enter a lowercase letter from the English alphabet.</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; A</span>
<span style="color: rgb(169, 183, 198);">Please, enter a lowercase letter from the English alphabet.</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; ii</span>
<span style="color: rgb(169, 183, 198);">Please, input a single letter.</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; ++</span>
<span style="color: rgb(169, 183, 198);">Please, input a single letter.</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt;</span>
<span style="color: rgb(169, 183, 198);">Please, input a single letter.</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; g</span>
<span style="color: rgb(169, 183, 198);">That letter doesn&apos;t appear in the word.  # 6 attempts</span>

<span style="color: rgb(169, 183, 198);">j---</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; a</span>

<span style="color: rgb(169, 183, 198);">ja-a</span>
<span style="color: rgb(169, 183, 198);">Input a letter: &gt; v</span>
<span style="color: rgb(169, 183, 198);">You guessed the word java!</span>
<span style="color: rgb(169, 183, 198);">You survived!</span></pre>
<p></p>