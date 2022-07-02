<h1>Stage 5/8: Keep trying</h1>
<h5>Description</h5>
<p>Let&apos;s make the game iterative. In this stage, we&apos;ll adjust our game to resemble the classic version of Hangman. Players should now guess the letters in a word instead of inputting an entire word. If an attempt is successful, uncover the letter. We also need to add the lose condition &mdash; players have eight attempts to guess all letters that appear in the word. When players run out of attempts, the game ends.</p>
<p>Don&apos;t forget to get rid of the hints: replace all the letters in a word with hyphens at the beginning. Players input one lowercase letter at a time, so there is no need to worry about that.</p>
<p>Later on, we will also determine the win conditions, but in this stage, let&apos;s just see how well our player guesses the word on each attempt.</p>
<h5>Objectives</h5>
<p>Your game should work as follows:</p>
<ul>
    <li>Players have exactly eight attempts to guess the word by entering letters one by one. Asking for a letter, print:&nbsp;Input a letter:.<strong>&nbsp;</strong>If a player uncovered all the letters, but some attempts are still left, the program must continue to ask for input until all the tries are exhausted;</li>
    <li>If the letter doesn&apos;t appear in the word, the computer takes one try away &ndash; even if a user has already suggested this letter &ndash; and prints&nbsp;That letter doesn&apos;t appear in the word.;</li>
    <li>If the letter does appear in the word but a user has already suggested this letter and it&apos;s open, no need to print any messages;</li>
    <li>If all attempts are exhausted, the game ends; the program shows a final message (Thanks for playing!). Otherwise, players can continue to input letters;</li>
    <li>We continue to stick with the word list from the previous stage:&nbsp;python,&nbsp;java,&nbsp;swift,&nbsp;javascript. It ensures that your program is tested reliably. Don&apos;t worry about&nbsp;javascript. Yes, it&apos;s longer than 8 characters, but we&apos;ll keep it in the list for consistency since we&apos;re not done with developing the game yet and for now there is no win or lose.</li>
</ul>
<p><br></p>
<div>Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.</div>
<h5>Examples</h5>
<p>The greater-than symbol followed by a space (&gt;&nbsp;) represents the user input. Note that it&apos;s not part of the input. Comments after&nbsp;#&nbsp;provided for illustrative purposes and not as part of the task.</p>
<p><strong>Example 1</strong>:</p>
<pre>H A N G M A N  # 8 attempts

----------
Input a letter: &gt; a  # 7 attempts

-a-a------
Input a letter: &gt; i  # 6 attempts

-a-a---i--
Input a letter: &gt; o
That letter doesn&apos;t appear in the word.  # 5 attempts

-a-a---i--
Input a letter: &gt; z
That letter doesn&apos;t appear in the word.  # 4 attempts

-a-a---i--
Input a letter: &gt; l
That letter doesn&apos;t appear in the word.  # 3 attempts

-a-a---i--
Input a letter: &gt; p  # 2 attempts

-a-a---ip-
Input a letter: &gt; h
That letter doesn&apos;t appear in the word.  # 1 attempt

-a-a---ip-
Input a letter: &gt; k
That letter doesn&apos;t appear in the word.  # 0 attempts

Thanks for playing!</pre>
<p><strong>Example 2</strong>:</p>
<pre>H A N G M A N  # 8 attempts

----
Input a letter: &gt; j  # 7 attempts

j---
Input a letter: &gt; i
That letter doesn&apos;t appear in the word.  # 6 attempts

j---
Input a letter: &gt; g
That letter doesn&apos;t appear in the word.  # 5 attempts

j---
Input a letter: &gt; o
That letter doesn&apos;t appear in the word.  # 4 attempts

j---
Input a letter: &gt; a  # 3 attempts

ja-a
Input a letter: &gt; v  # 2 attempts

java
Input a letter: &gt; a  # 1 attempt

java
Input a letter: &gt; j  # 0 attempts

Thanks for playing!</pre>
<p><br></p>
<p><br></p>