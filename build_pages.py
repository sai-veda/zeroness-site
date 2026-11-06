"""Builds the content pages from one template. Run: python3 build_pages.py"""
import json

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://zeroness.io{path}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Zeroness">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://zeroness.io{path}">
<meta property="og:image" content="https://zeroness.io/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@500;600&family=Instrument+Serif:ital@0;1&display=swap">
<link rel="stylesheet" href="/home.css">
{ld}
</head>
<body>
<header class="nav"><div class="wrap"><a class="brand" href="/"><img src="/logo-120.png" alt="">Zeroness</a><nav aria-label="Site"><a href="/features/">Features</a><a href="/superhuman-alternative/">Compare</a><a href="/pricing/">Pricing</a><a class="btn btn-ink" href="mailto:sai@appliedcrew.com?subject=Zeroness%20early%20access" style="height:34px;padding:0 14px;font-size:13.5px">Get early access</a></nav></div></header>
<main class="wrap doc">
"""
FOOT = """
  <div class="cta-row"><a class="btn btn-ink" href="mailto:sai@appliedcrew.com?subject=Zeroness%20early%20access">Get early access</a><a class="btn btn-quiet" href="/">See it work</a></div>
</main>
<footer><div class="wrap"><span>© 2026 Applied Crew, Inc.</span><span><a href="/features/">Features</a><a href="/superhuman-alternative/">Zeroness vs Superhuman</a><a href="/inbox-zero/">Inbox zero guide</a><a href="/gmail-keyboard-shortcuts/">Gmail shortcuts</a><a href="/best-superhuman-alternatives/">Superhuman alternatives</a><a href="/superhuman-pricing/">Superhuman pricing</a><a href="/superhuman-cost-calculator/">Superhuman cost calculator</a><a href="/notion-mail-alternative/">Notion Mail alternative</a><a href="/pricing/">Pricing</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></span></div></footer>
</body>
</html>
"""

def crumbs(name, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Zeroness", "item": "https://zeroness.io/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"https://zeroness.io{path}"}]}

def page(path, title, desc, body, lds, ogtype="website"):
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    html = HEAD.format(title=title, desc=desc, path=path, ld=ld, ogtype=ogtype) + body + FOOT
    open(f".{path}index.html", "w").write(html)

def faq(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

# ---------- Features ----------
page("/features/", "Features · Zeroness", "Everything Zeroness does: AI sorting, replies that check what you decided, plain-English commands, sign-in codes at the top, reminders, follow-ups and keyboard shortcuts for every action.", """
  <span class="kicker">Features</span>
  <h1 class="serif">Everything Zeroness does.</h1>
  <p class="intro">Zeroness is an email app for web and iPhone that works with Gmail and Google Workspace. It reads every thread first, so the inbox you open holds only what needs you.</p>

  <h2>Sorted before you open it</h2>
  <p>Every thread lands in one of five places: <strong>Important</strong> for people who need you, <strong>Team</strong> for colleagues, <strong>Calendar</strong> for invites, <strong>News</strong> for newsletters and <strong>Other</strong> for receipts, notifications and cold pitches. Zeroness decides from the sender and the conversation, not from a list of rules you maintain. Each split is a tab you can clear on its own, and you can turn any of them off.</p>

  <h2>Replies that know what you decided</h2>
  <p>When someone is waiting on you, Zeroness writes the reply in your voice, from the whole conversation and the way you usually write to that person. Before it writes, it searches the rest of your mail for the same matter: a contract you signed, a vendor you already chose, a meeting already booked. So a follow-up from a supplier you passed on gets a polite no, not a counter-offer. Drafts never send themselves.</p>

  <h2>Ask in plain words</h2>
  <p>Press <strong>⌘K</strong> and type what you want: “archive every GitHub notification older than a week”, “who still owes me a reply?”, “what did we agree with Northwind on price?”. For actions, Zeroness shows exactly what it will change, such as “Mark 38 threads Done”, and waits for you. For questions, it answers from your mail and links the threads it used. Every command still has its key.</p>

  <h2>Sign-in codes at the top</h2>
  <p>A new verification code appears above your inbox with a Copy button, one per sender, so you never open the email. It disappears ten minutes after it arrived.</p>

  <h2>Remind me, in plain words</h2>
  <p>Press <strong>H</strong> and type “monday 9am”, “in 2 days” or “after the weekend”. The thread leaves your inbox and comes back when you said. Reminders can also fire only if nobody replies.</p>

  <h2>Follow up on time</h2>
  <p>When you are waiting on someone and three days pass without an answer, the thread asks if you want to nudge them, with the follow-up already written.</p>

  <h2>Finished conversations clear themselves</h2>
  <p>A refund request that was declined as final, an invite for a meeting that has passed, a read receipt. Zeroness moves threads like these to Done, the same as archiving. Done lists everything it cleared, and one click brings it all back.</p>

  <h2>Labels written for you</h2>
  <p>Zeroness tags threads with short labels such as pitch, news, receipts, invoices, travel and legal. You choose which ones skip the inbox entirely.</p>

  <h2>Long threads in one line</h2>
  <p>A fourteen-message thread opens with one line on who needs what, and by when.</p>

  <h2>Undo send, every account, iPhone</h2>
  <p>Every send waits a few seconds so you can take it back. Personal and work addresses live in one inbox, or one at a time. The iPhone app has the same inbox, with swipes for Done and Snooze and one-tap sending of a drafted reply.</p>

  <h2>Keyboard shortcuts</h2>
  <div class="tbl"><table>
    <tr><th>Key</th><th>Action</th></tr>
    <tr><td>E</td><td>Mark done</td></tr>
    <tr><td>H</td><td>Remind me</td></tr>
    <tr><td>R / A / F</td><td>Reply, reply all, forward</td></tr>
    <tr><td>J / K</td><td>Next and previous thread</td></tr>
    <tr><td>⌘K</td><td>Ask or run any command</td></tr>
    <tr><td>⌘J</td><td>Rewrite the draft</td></tr>
    <tr><td>/</td><td>Search</td></tr>
    <tr><td>Z</td><td>Undo</td></tr>
    <tr><td>G then D, R, S</td><td>Go to Done, Reminders, Sent</td></tr>
  </table></div>
""", [crumbs("Features", "/features/")])

# ---------- Superhuman alternative ----------
sh_faq = [
    ("Is Zeroness a Superhuman alternative?", "Yes. Zeroness covers the core Superhuman workflow for Gmail and Google Workspace (split inbox, keyboard shortcuts, reminders, AI drafts) at $9.99 a month, with AI included on every plan and free work email during launch."),
    ("How much cheaper is Zeroness than Superhuman?", "Zeroness Personal is $9.99 a month, or $30 for the first year at launch. Superhuman lists Starter at $25 and Business at $33 per member a month billed annually (about $30 and $40 billed monthly) as of November 2026."),
    ("What does Superhuman have that Zeroness does not?", "As of November 2026, Superhuman supports Outlook, read statuses, team comments and a built-in calendar. Zeroness supports Gmail and Google Workspace, with Outlook and calendar planned."),
]
page("/superhuman-alternative/", "Zeroness vs Superhuman: an affordable Superhuman alternative", "How Zeroness compares with Superhuman on price, AI, sorting, commands and platforms, including what Superhuman does that Zeroness does not yet.", """
  <span class="kicker">Compare</span>
  <h1 class="serif">Zeroness vs Superhuman.</h1>
  <p class="intro">Superhuman made fast, keyboard-first email a category. Zeroness is built for the same kind of person, costs a third as much, and leans harder on AI that acts on what it reads.</p>
  <p class="meta-line">Last checked November 5, 2026, from each product's public pages.</p>
  <div class="note-box">The first 100 people to connect get Zeroness free until January 31, 2027, then $5 a month for life. That is $60 a year against Superhuman's $300 to $396 per seat.</div>

  <div class="tbl"><table>
    <tr><th></th><th>Zeroness</th><th>Superhuman</th></tr>
    <tr><td>Price</td><td>$9.99 a month, or $30 for the first year at launch. Free for work email during launch. $1 a month for students.</td><td>Starter $25 and Business $33 per member a month, billed annually (17% more billed monthly).</td></tr>
    <tr><td>AI on every plan</td><td>Yes. Drafts, summaries, Ask and sorting on every plan.</td><td>Auto Drafts and Ask AI are on the Business plan.</td></tr>
    <tr><td>Split inbox</td><td>Five AI-sorted splits, no rules to maintain.</td><td>Split inbox with custom splits.</td></tr>
    <tr><td>Commands</td><td>⌘K takes plain English and previews the change before acting.</td><td>⌘K command palette that matches command names.</td></tr>
    <tr><td>Drafts that check other mail</td><td>Searches related threads for decisions already made before writing.</td><td>Auto Drafts use your tone and conversation history.</td></tr>
    <tr><td>Clearing old mail</td><td>Clears finished conversations and past invites by reading them, with undo.</td><td>Auto Archive by label and a one-time cleanup of older mail.</td></tr>
    <tr><td>Email providers</td><td>Gmail and Google Workspace. Outlook planned.</td><td>Gmail, Google Workspace and Outlook.</td></tr>
    <tr><td>Platforms</td><td>Web and iPhone.</td><td>Web, Mac, Windows, iPhone and Android.</td></tr>
    <tr><td>Read statuses, team comments, calendar</td><td>Not yet.</td><td>Yes.</td></tr>
  </table></div>

  <h2>Choose Zeroness if</h2>
  <ul>
    <li>You use Gmail or Google Workspace and want Superhuman’s speed for a third of the price.</li>
    <li>You want AI that does more than write: sort, clear finished threads, and act on plain-English requests.</li>
    <li>You get a lot of vendor, investor or customer mail where an AI draft has to know what you already decided.</li>
  </ul>

  <h2>Choose Superhuman if</h2>
  <ul>
    <li>You need Outlook, Android or a desktop app today.</li>
    <li>Your team relies on shared comments, read statuses or a calendar inside the email app.</li>
  </ul>

  <h2>Switching</h2>
  <p>There is nothing to migrate. Zeroness connects to your existing Gmail or Google Workspace account, and your labels, archive and sent mail stay exactly where they are. You can use both apps side by side while you decide.</p>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in sh_faq), [crumbs("Zeroness vs Superhuman", "/superhuman-alternative/"), faq(sh_faq)])

# ---------- Inbox zero guide ----------
guide = {"@context": "https://schema.org", "@type": "Article", "headline": "How to get to inbox zero, and stay there", "datePublished": "2026-11-04", "dateModified": "2026-11-04", "author": {"@type": "Person", "name": "Sai Veda"}, "publisher": {"@type": "Organization", "name": "Zeroness", "logo": {"@type": "ImageObject", "url": "https://zeroness.io/logo-120.png"}}, "mainEntityOfPage": "https://zeroness.io/inbox-zero/"}
page("/inbox-zero/", "How to get to inbox zero, and stay there · Zeroness", "A practical method for inbox zero: decide once per email, use four actions, clear the backlog in one pass and keep newsletters and notifications out of the inbox.", """
  <span class="kicker">Guide</span>
  <h1 class="serif">How to get to inbox zero, and stay there.</h1>
  <p class="intro">Inbox zero is not an empty mailbox. It is an inbox that holds nothing you have not already decided about. Here is the method we built Zeroness around, and it works in any email app.</p>
  <p class="meta-line">By Sai Veda · November 4, 2026</p>

  <h2>1. Decide once, then act</h2>
  <p>Every email gets one decision the first time you open it. Re-reading the same message three times is what makes email feel endless. If you cannot decide now, that is a decision too: set a time to come back.</p>

  <h2>2. Use four actions, and only four</h2>
  <ul>
    <li><strong>Done</strong>: nothing more to do. Archive it. It stays searchable.</li>
    <li><strong>Reply</strong>: if it takes under two minutes, answer now.</li>
    <li><strong>Remind me</strong>: it needs you, but later. Pick a specific time, not “someday”.</li>
    <li><strong>Waiting</strong>: you asked someone for something. Set a follow-up if they do not answer in a few days.</li>
  </ul>

  <h2>3. Clear the backlog in one pass</h2>
  <p>If you have thousands of emails, do not work through them one by one. Archive everything older than two weeks that is read and not starred, then work only the recent mail. Anything important from the old pile will reach you again. In Zeroness this step reads each thread instead of using the date, so a conversation still waiting on you stays even if it is old.</p>

  <h2>4. Keep the inbox for people</h2>
  <p>Most email is newsletters, receipts and notifications. Give them their own place so they never sit between you and a person waiting on an answer. Unsubscribe from anything you skip three times in a row.</p>

  <h2>5. Work in two or three sessions a day</h2>
  <p>Checking email every few minutes means deciding the same things over and over. Pick two or three times a day, go to zero each time, and close the app in between.</p>

  <h2>6. Let the drafts start themselves</h2>
  <p>The slowest emails are the ones you have to write from scratch. A good first draft, which you edit rather than write, turns a five-minute reply into a thirty-second one. Zeroness writes those drafts for threads where someone is waiting on you.</p>

  <div class="note-box">Zeroness does steps 3, 4 and 6 for you: it sorts mail into splits, clears finished threads with undo, and drafts the replies people are waiting on. Every action in step 2 is a single key.</div>
""", [crumbs("Inbox zero guide", "/inbox-zero/"), guide], ogtype="article")

# ---------- Pricing ----------
pr_faq = [
    ("What is the Founding 100?", "The first 100 people to connect an account get Zeroness free until January 31, 2027, then $5 a month for as long as they stay subscribed, half the Personal price. Google limits apps that have not finished its security review to 100 users, so these are the only spots before that review."),
    ("How much does Zeroness cost?", "Zeroness is free for work email on company domains during launch. Personal is $9.99 a month, or $30 for the first year at launch. Students pay $1 a month with a .edu address."),
    ("Is AI included?", "Yes. Every plan includes every feature, including drafts, summaries, Ask and sorting."),
    ("Will my price go up after launch?", "No. Launch prices stay the same for as long as you stay subscribed."),
    ("Can I cancel any time?", "Yes. Cancel any time and keep access until the end of the billing period."),
]
page("/pricing/", "Pricing · Zeroness", "Zeroness pricing: free for work email during launch, $9.99 a month for personal accounts, $1 a month for students. Every feature and all AI included.", """
  <span class="kicker">Pricing</span>
  <h1 class="serif">Simple pricing. Everything included.</h1>
  <p class="intro">Every plan has every feature, AI included. Launch prices stay the same for as long as you subscribe.</p>
  <div class="note-box"><strong>Founding 100.</strong> The first 100 people to connect an account get Zeroness free until January 31, 2027, then $5 a month for life. Google lets an app that has not finished its security review onboard 100 users, so these are the only spots until it does. <a href="/connect/">How connecting works</a>.</div>
  <div class="tbl"><table>
    <tr><th>Plan</th><th>Price</th><th>For</th></tr>
    <tr><td>Work email</td><td>Free during launch</td><td>Any company domain on Google Workspace</td></tr>
    <tr><td>Personal</td><td>$9.99 a month, or $30 for the first year at launch</td><td>Gmail and personal accounts</td></tr>
    <tr><td>Students</td><td>$1 a month</td><td>Anyone with a .edu address</td></tr>
  </table></div>
  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in pr_faq), [crumbs("Pricing", "/pricing/"), faq(pr_faq)])

# ---------- Connect (Google warning walkthrough) ----------
cn_faq = [
    ("Why does Google say Zeroness is not verified?", "Apps that read Gmail must pass a paid third-party security assessment before Google removes the warning. Zeroness has verified its brand with Google and will complete the assessment after launch. Until then Google shows the warning and limits the app to 100 users."),
    ("Is my email used to train AI?", "No. Zeroness does not use your mail to train any model, and its AI provider is bound by API terms that prohibit training on your data. The privacy policy has the details."),
    ("Can I disconnect later?", "Yes. Remove the account in Zeroness, or revoke access at any time at myaccount.google.com/permissions. Your Gmail stays exactly as it was."),
]
page("/connect/", "Connecting your Google account · Zeroness", "What to click on Google's 'app not verified' screen when you connect Zeroness, why it appears, and what Zeroness can and cannot do with your mail.", """
  <span class="kicker">Connect</span>
  <h1 class="serif">Connecting your Google account.</h1>
  <p class="intro">It takes about a minute. Google will show one warning screen along the way. Here is what to click, and why it is there.</p>

  <h2>The five steps</h2>
  <ol>
    <li>Click <strong>Sign in with Google</strong> and pick your account.</li>
    <li>Google shows <strong>“Google hasn't verified this app.”</strong></li>
    <li>Click <strong>Advanced</strong>, at the bottom left of that screen.</li>
    <li>Click <strong>Go to Zeroness (unsafe)</strong>. “Unsafe” is the label Google puts on every app that has not finished its paid security assessment.</li>
    <li>Tick the permission boxes and click <strong>Continue</strong>. Your inbox opens and starts sorting.</li>
  </ol>

  <h2>Why the warning is there</h2>
  <p>Any app that reads Gmail has to pass a third-party security assessment before Google removes this screen. We have verified our brand with Google and will complete the assessment once our first users tell us Zeroness is worth it. Until then, Google lets us onboard 100 people. Those 100 are the Founding 100: free until January 31, 2027, then $5 a month for life.</p>

  <h2>What Zeroness can do with your account</h2>
  <ul>
    <li>Read, sort, label and archive your mail, and send the replies you approve. Nothing sends without you.</li>
    <li>Read and add calendar events, so drafts know about meetings already booked.</li>
    <li>Your mail is never sold, never used for ads and never used to train AI models. The <a href="/privacy/">privacy policy</a> lists exactly what is stored and where.</li>
  </ul>

  <div class="note-box">Stuck on any step? Email <a href="mailto:sai@appliedcrew.com">sai@appliedcrew.com</a>, or <a href="https://cal.com/saiveda/15min">book 15 minutes with Sai</a> and he will set it up with you.</div>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in cn_faq), [crumbs("Connect", "/connect/"), faq(cn_faq)])

# ---------- Notion Mail alternative ----------
nm_faq = [
    ("Is Zeroness a Notion Mail alternative?", "Yes. Notion Mail shut down on September 22, 2026. Zeroness is an email app for Gmail and Google Workspace with an AI-sorted inbox, keyboard commands and drafted replies, on web and iPhone."),
    ("Do I need to migrate anything from Notion Mail?", "No. Notion Mail synced with Gmail, so your mail is already in Gmail. Zeroness connects to the same account and sorts it on its own, with no rules to rebuild."),
    ("How much does Zeroness cost?", "The first 100 users get it free until January 31, 2027, then $5 a month for life. After that, Personal is $9.99 a month and work email is free during launch."),
]
page("/notion-mail-alternative/", "Notion Mail alternative: Zeroness for Gmail", "Notion Mail shut down on September 22, 2026. Zeroness is a Gmail app with an inbox that sorts itself, plain-English commands and drafted replies, on web and iPhone.", """
  <span class="kicker">Notion Mail alternative</span>
  <h1 class="serif">Notion Mail is gone. Your inbox doesn't have to go back to Gmail.</h1>
  <p class="intro">Notion Mail shut down on September 22, 2026. If you liked an inbox that organized itself and a command bar for everything, Zeroness does both for Gmail and Google Workspace, on web and iPhone.</p>
  <p class="meta-line">Last checked November 5, 2026.</p>

  <div class="tbl"><table>
    <tr><th>What you used in Notion Mail</th><th>In Zeroness</th></tr>
    <tr><td>Auto labels and views</td><td>Five AI-sorted splits (Important, Team, Calendar, News, Other) plus auto labels like pitch, receipts and invoices. No rules to rebuild.</td></tr>
    <tr><td>Commands and keyboard</td><td>⌘K in plain English, with a preview before anything changes. E, H, R, J/K for everything else.</td></tr>
    <tr><td>AI drafts</td><td>Drafts in your voice that search your other mail for decisions already made.</td></tr>
    <tr><td>Snippets and scheduled send</td><td>Undo send and Remind me in plain words (“monday 9am”). Snippets are not in Zeroness yet.</td></tr>
    <tr><td>Notion database sync</td><td>Not supported. Zeroness is an email app, not a Notion integration.</td></tr>
    <tr><td>Price</td><td>Free for the first 100 users until January 31, 2027, then $5 a month for life. No AI credits to buy.</td></tr>
  </table></div>

  <h2>Switching takes a minute</h2>
  <p>Notion Mail always synced with Gmail, so every message is already there. Connect the same Google account to Zeroness and it sorts your inbox on the first open. <a href="/connect/">Here is what to click</a>.</p>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in nm_faq), [crumbs("Notion Mail alternative", "/notion-mail-alternative/"), faq(nm_faq)])

# ---------- Gmail keyboard shortcuts ----------
ks_faq = [
    ("How do I turn on Gmail keyboard shortcuts?", "In Gmail on the web, open Settings (the gear), choose See all settings, find Keyboard shortcuts on the General tab, select Keyboard shortcuts on, and click Save Changes at the bottom."),
    ("What is the Gmail shortcut to archive an email?", "Press E to archive the open or selected conversation. Press Z right after to undo."),
    ("Why are my Gmail shortcuts not working?", "Single-key shortcuts only work after you turn them on in Settings, and they are ignored while the cursor is in a text box such as the search bar or a reply. Press Esc to leave the text box first."),
    ("Are there shortcuts for snoozing in Gmail?", "Yes. Press B to snooze the selected conversation."),
]
ks_guide = {"@context": "https://schema.org", "@type": "Article", "headline": "Gmail keyboard shortcuts: the complete cheat sheet", "datePublished": "2026-11-05", "dateModified": "2026-11-05", "author": {"@type": "Person", "name": "Sai Veda"}, "publisher": {"@id": "https://zeroness.io/#org"}, "mainEntityOfPage": "https://zeroness.io/gmail-keyboard-shortcuts/"}
page("/gmail-keyboard-shortcuts/", "Gmail keyboard shortcuts: the complete cheat sheet (2026) · Zeroness", "Every Gmail keyboard shortcut worth learning, how to turn them on, and the twelve that save the most time. Printable cheat sheet.", """
  <span class="kicker">Guide</span>
  <h1 class="serif">Gmail keyboard shortcuts: the cheat sheet.</h1>
  <p class="intro">Learn twelve keys and you will never reach for the mouse to clear your inbox again. Here is how to turn shortcuts on, the twelve that matter most, and the full list.</p>
  <p class="meta-line">By Sai Veda · Updated November 5, 2026</p>

  <h2>Turn them on first</h2>
  <ol>
    <li>In Gmail on the web, click the gear and choose <strong>See all settings</strong>.</li>
    <li>On the <strong>General</strong> tab, find <strong>Keyboard shortcuts</strong> and select <strong>Keyboard shortcuts on</strong>.</li>
    <li>Scroll down and click <strong>Save Changes</strong>.</li>
  </ol>
  <p>Press <strong>?</strong> in Gmail at any time to see the list. Shortcuts are ignored while you are typing in a box; press <strong>Esc</strong> first.</p>

  <h2>The twelve that save the most time</h2>
  <div class="tbl"><table>
    <tr><th>Key</th><th>What it does</th></tr>
    <tr><td>E</td><td>Archive the conversation</td></tr>
    <tr><td>J / K</td><td>Next / previous conversation</td></tr>
    <tr><td>O or Enter</td><td>Open the conversation</td></tr>
    <tr><td>U</td><td>Back to the list</td></tr>
    <tr><td>R</td><td>Reply</td></tr>
    <tr><td>A</td><td>Reply all</td></tr>
    <tr><td>F</td><td>Forward</td></tr>
    <tr><td>C</td><td>Compose</td></tr>
    <tr><td>⌘ Enter / Ctrl Enter</td><td>Send</td></tr>
    <tr><td>/</td><td>Search</td></tr>
    <tr><td>B</td><td>Snooze</td></tr>
    <tr><td>Z</td><td>Undo the last action</td></tr>
  </table></div>

  <h2>Selecting and organizing</h2>
  <div class="tbl"><table>
    <tr><th>Key</th><th>What it does</th></tr>
    <tr><td>X</td><td>Select the conversation</td></tr>
    <tr><td>S</td><td>Star or unstar</td></tr>
    <tr><td>#</td><td>Move to trash</td></tr>
    <tr><td>!</td><td>Report spam</td></tr>
    <tr><td>L</td><td>Label</td></tr>
    <tr><td>V</td><td>Move to a label</td></tr>
    <tr><td>Shift + I</td><td>Mark as read</td></tr>
    <tr><td>Shift + U</td><td>Mark as unread</td></tr>
    <tr><td>M</td><td>Mute the conversation</td></tr>
  </table></div>

  <h2>Jumping around</h2>
  <div class="tbl"><table>
    <tr><th>Keys</th><th>Goes to</th></tr>
    <tr><td>G then I</td><td>Inbox</td></tr>
    <tr><td>G then S</td><td>Starred</td></tr>
    <tr><td>G then T</td><td>Sent</td></tr>
    <tr><td>G then D</td><td>Drafts</td></tr>
    <tr><td>G then A</td><td>All mail</td></tr>
  </table></div>

  <h2>A faster workflow with the same keys</h2>
  <p>Shortcuts make each action faster, but you still decide every email one by one. The method that gets people to inbox zero is four decisions: done, reply, remind me later, or waiting on someone. Our <a href="/inbox-zero/">inbox zero guide</a> walks through it.</p>
  <div class="note-box">Zeroness uses the same muscle memory (E, J, K, R, /, Z) and adds what Gmail leaves to you: the inbox is already sorted into Important, Team, Calendar, News and Other, replies are drafted before you open the thread, and ⌘K takes plain English. <a href="/features/">See every Zeroness shortcut</a>.</div>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in ks_faq), [crumbs("Gmail keyboard shortcuts", "/gmail-keyboard-shortcuts/"), ks_guide, faq(ks_faq)], ogtype="article")

# ---------- Superhuman cost calculator ----------
SH_PRICES = {"starter_annual": 25, "starter_monthly": 30, "business_annual": 33, "business_monthly": 40}
calc_faq = [
    ("How much does Superhuman cost for a team?", f"Superhuman Mail lists Starter at ${SH_PRICES['starter_annual']} and Business at ${SH_PRICES['business_annual']} per member a month billed annually (about ${SH_PRICES['starter_monthly']} and ${SH_PRICES['business_monthly']} billed monthly) as of November 2026. A five-person team on Starter billed annually pays ${SH_PRICES['starter_annual']*5*12:,} a year."),
    ("How much does Zeroness cost for a team?", "Zeroness is free for company domains on Google Workspace during launch. Personal accounts are $9.99 a month. The first 100 users get it free until January 31, 2027, then $5 a month for life."),
]
page("/superhuman-cost-calculator/", "Superhuman cost calculator: what your team would pay · Zeroness", "Work out what Superhuman costs your team per month and per year on Starter or Business, billed monthly or annually, and compare it with Zeroness.", """
  <span class="kicker">Calculator</span>
  <h1 class="serif">What would Superhuman cost your team?</h1>
  <p class="intro">Pick a team size and plan. Prices are Superhuman's published per-member prices, checked November 5, 2026.</p>
  <div class="note-box" id="calc">
    <p><label>Team size <input id="n" type="number" min="1" max="500" value="3" style="width:80px;margin-left:8px;font:inherit;padding:4px 8px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)"></label></p>
    <p><label>Plan <select id="plan" style="margin-left:8px;font:inherit;padding:4px 8px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)">
      <option value="starter_annual">Starter, billed annually</option>
      <option value="starter_monthly">Starter, billed monthly</option>
      <option value="business_annual">Business, billed annually</option>
      <option value="business_monthly">Business, billed monthly</option>
    </select></label></p>
    <p style="font-size:20px;color:var(--ink);margin-top:18px"><strong id="out"></strong></p>
    <p id="out2"></p>
  </div>
  <script>
  (function(){var P=""" + json.dumps(SH_PRICES) + """;var n=document.getElementById('n'),pl=document.getElementById('plan'),o=document.getElementById('out'),o2=document.getElementById('out2');
  function f(x){return '$'+Math.round(x).toLocaleString('en-US')}
  function run(){var k=Math.max(1,Math.min(500,parseInt(n.value||'1',10)));var m=P[pl.value]*k;o.textContent='Superhuman: '+f(m)+' a month, '+f(m*12)+' a year.';
  o2.textContent='Zeroness for the same '+k+(k===1?' person':' people')+': free on a company domain during launch, or '+f(9.99*k)+' a month on personal accounts ('+f(5*k)+' for founding users).';}
  n.addEventListener('input',run);pl.addEventListener('change',run);run();})();
  </script>

  <h2>How the numbers work</h2>
  <p>Superhuman charges per member. Billing annually is cheaper per month but is paid up front for the year. Every Zeroness plan includes every feature and all AI, with no per-tier limits.</p>
  <p>Want the full feature comparison? See <a href="/superhuman-alternative/">Zeroness vs Superhuman</a>.</p>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in calc_faq), [crumbs("Superhuman cost calculator", "/superhuman-cost-calculator/"), faq(calc_faq)])

# ---------- Best Superhuman alternatives (2026) ----------
alt_rows = [
  # name, price (cheapest paid; tier with AI drafts), providers, platforms, best for
  ("Zeroness", "$9.99 a month, AI drafts included. Free for work email during launch; first 100 users free until Jan 31, 2027.", "Gmail, Google Workspace", "Web, iPhone", "Gmail users who want Superhuman's speed and AI drafts at a third of the price."),
  ("Shortwave", "Pro $18 a month (billed monthly). Business $30, Premier $45, Max $120 per seat. Limited free plan.", "Gmail, Google Workspace", "Web, Mac, Windows, iPhone, Android", "Gmail power users who want AI search and AI filters, and can pay for higher tiers."),
  ("Spark", "Free plan. Plus $10 a month ($8.25 annual). Auto-drafts need Pro, $20 a month ($16.58 annual).", "Gmail, Outlook, iCloud, Yahoo, IMAP", "Mac, Windows, iPhone, Android", "People with many non-Gmail accounts who want a polished free client."),
  ("Inbox Zero", "App free; AI from $20 a month ($18 annual).", "Gmail, Outlook", "Web, desktop, iPhone", "People who want open source and self-hosting."),
  ("Fyxer AI", "Free plan with 400 credits. Pro $49 a month ($37 annual).", "Gmail, Outlook", "Works inside Gmail and Outlook", "People who want to keep Gmail or Outlook and add an assistant on top."),
  ("Missive", "From $18 a month ($14 annual). 30-day trial.", "Gmail, Outlook, IMAP", "Web, Mac, Windows, iPhone, Android", "Teams that share inboxes and need comments and assignment."),
  ("Gmail with Gemini", "Summaries and prompt-based drafting free; AI inbox triage needs a paid Google AI plan (AI Plus $9.99 a month).", "Gmail", "Web, iPhone, Android", "People who don't want another app."),
  ("Superhuman Mail (for reference)", "Starter $30 a month ($25 annual). Auto Drafts and Ask AI need Business, $40 a month ($33 annual).", "Gmail, Outlook", "Web, Mac, Windows, iPhone, Android", "Teams that need Outlook, Android or desktop apps and can pay $300-480 a year per person."),
]
alt_faq = [
    ("What is the cheapest Superhuman alternative?", "For a full email app with AI drafts, Zeroness is $9.99 a month with AI on every plan (free for work email during launch). Spark has a free plan but puts auto-drafts on Pro at $20 a month. Gmail itself has free summaries and prompt-based drafting through Gemini."),
    ("Which Superhuman alternative works only with Gmail?", "Zeroness and Shortwave both focus on Gmail and Google Workspace. Spark, Missive, Fyxer and Inbox Zero also support Outlook."),
    ("Does Superhuman's cheapest plan include AI drafts?", "No. As of November 2026 Superhuman's Starter plan ($25 a month billed annually, $30 monthly) does not include Auto Drafts or Ask AI; both are on Business ($33 annual, $40 monthly)."),
    ("What replaced Notion Mail?", "Notion Mail shut down on September 22, 2026 and Notion did not launch a replacement inbox. Former users moved to Gmail apps such as Zeroness, Shortwave and Spark."),
]
page("/best-superhuman-alternatives/", "The best Superhuman alternatives in 2026 (compared, with prices) · Zeroness", "Seven Superhuman alternatives compared on price, AI drafts, email providers and platforms, with each vendor's November 2026 prices and who each one is best for.", """
  <span class="kicker">Compare</span>
  <h1 class="serif">The best Superhuman alternatives in 2026.</h1>
  <p class="intro">The short answer: for Gmail users, Zeroness gives you Superhuman's keyboard-first speed and AI drafts for $9.99 a month. If you need Outlook or Android, look at Spark or Missive. If you want to stay in Gmail itself, Gemini covers the basics for free.</p>
  <p class="meta-line">Last checked November 5, 2026, from each vendor's own pricing page. We make Zeroness, so we have listed what each product does better than ours too.</p>

  <div class="tbl"><table>
    <tr><th>App</th><th>Price</th><th>Works with</th><th>Platforms</th><th>Best for</th></tr>
""" + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in alt_rows) + """
  </table></div>

  <h2>Why people leave Superhuman</h2>
  <p>Price, mostly. Superhuman Mail is $25 a month per person billed annually, and the AI that writes replies for you (Auto Drafts) and answers questions about your mail (Ask AI) is only on Business, $33 a month annually or $40 monthly. Since the Grammarly acquisition, the Superhuman suite only includes Mail from Business up. For a three-person startup that is $1,188 to $1,440 a year for email.</p>

  <h2>Zeroness</h2>
  <p>An email app for Gmail and Google Workspace on web and iPhone. AI sorts every thread into Important, Team, Calendar, News and Other, drafts replies in your voice after checking your other mail for decisions already made, and every action has one key. Every feature is on every plan. <strong>Not yet:</strong> Outlook, Android, Mac and Windows apps, shared team inboxes. <a href="/superhuman-alternative/">Zeroness vs Superhuman in detail</a>.</p>

  <h2>Shortwave</h2>
  <p>The closest Gmail-only alternative, built around an AI agent you prompt to search, organize and write. Strong AI search across years of mail. Paid plans are billed monthly and the higher tiers are priced per seat. Fully automatic drafting runs through its sister product, Tasklet.</p>

  <h2>Spark</h2>
  <p>A long-standing cross-platform client with a capable free plan and support for almost any provider, including IMAP. AI auto-drafts and Autopilot are on Pro. We did not find a browser version.</p>

  <h2>Inbox Zero</h2>
  <p>Open source and self-hostable, with a free email app on web, desktop and iPhone and paid AI plans for categorizing, drafting and a cold-email blocker.</p>

  <h2>Fyxer AI</h2>
  <p>An assistant that works inside Gmail and Outlook rather than replacing them: drafts in your tone, labels and meeting notes, metered in credits. Sorting starts on Pro.</p>

  <h2>Missive</h2>
  <p>Built for teams: shared inboxes, comments and assignment across Gmail, Outlook and IMAP, with AI on every plan through credits or your own API key.</p>

  <h2>Gmail with Gemini</h2>
  <p>Gmail now summarizes threads and drafts from a prompt for free. AI inbox triage needs a paid Google AI plan and is a US, English-only beta. No tier writes drafts before you ask.</p>

  <h2>How we compared</h2>
  <p>Prices are per user per month in US dollars from each vendor's pricing page on November 5, 2026, with annual-billing prices in brackets. "AI drafts" means replies written before you ask, not writing help you prompt. We will update this page when prices change; email <a href="mailto:sai@appliedcrew.com">sai@appliedcrew.com</a> if something is out of date.</p>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in alt_faq), [crumbs("Best Superhuman alternatives", "/best-superhuman-alternatives/"), faq(alt_faq),
  {"@context": "https://schema.org", "@type": "ItemList", "name": "Superhuman alternatives in 2026", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": r[0].replace(" (for reference)", "")} for i, r in enumerate(alt_rows[:-1])]}])

# ---------- Superhuman pricing ----------
shp_faq = [
    ("How much does Superhuman cost per month?", "Superhuman Mail Starter is $30 a month billed monthly or $25 a month billed annually. Business is $40 monthly or $33 annually. Enterprise pricing is by quote. Prices are per member and checked November 5, 2026."),
    ("Is there a free version of Superhuman?", "There is no free Superhuman Mail plan. The free Superhuman suite plan covers Grammarly, Docs and Go, not the Mail app."),
    ("Which Superhuman plan includes AI drafts?", "Auto Drafts, Ask AI, and voice and tone matching are on Business and Enterprise, not Starter."),
    ("What changed after Grammarly bought Superhuman?", "Grammarly acquired Superhuman Mail and Coda in 2025 and renamed the company Superhuman. The new suite bundles Mail with Grammarly, Docs and Go, and only includes Mail from the Business plan ($33 annual, $40 monthly). The standalone Mail Starter plan is still listed on the Mail plans page."),
]
page("/superhuman-pricing/", "Superhuman pricing in 2026: every plan, what's included · Zeroness", "Superhuman Mail costs $25 to $40 per member a month in 2026. Every plan, monthly vs annual prices, which plan includes AI drafts, and what changed with the Grammarly bundle.", """
  <span class="kicker">Pricing explained</span>
  <h1 class="serif">Superhuman pricing in 2026.</h1>
  <p class="intro">Superhuman Mail costs <strong>$30 a month</strong> per person on Starter billed monthly, or <strong>$25</strong> billed annually. The plan with AI-written drafts, Business, is <strong>$40 monthly or $33 annually</strong>. There is no free Mail plan.</p>
  <p class="meta-line">Checked November 5, 2026 on superhuman.com/plans/mail and superhuman.com/plans. We make Zeroness, a cheaper alternative, and have kept this page to Superhuman's own published facts.</p>

  <div class="tbl"><table>
    <tr><th>Plan</th><th>Billed monthly</th><th>Billed annually</th><th>AI included</th><th>Seats</th></tr>
    <tr><td>Starter</td><td>$30 per member</td><td>$25 per member</td><td>Write with AI, Instant Reply, Auto Labels, Auto Summarize, Auto Archive, Split Inbox</td><td>Up to 25</td></tr>
    <tr><td>Business</td><td>$40 per member</td><td>$33 per member</td><td>Everything in Starter plus Auto Drafts, Ask AI, Voice and Tone Match, Knowledge Base, Mail MCP</td><td>Up to 25</td></tr>
    <tr><td>Enterprise</td><td colspan="2">By quote</td><td>Everything in Business plus SSO, admin and security controls</td><td>Unlimited</td></tr>
  </table></div>

  <h2>What a team actually pays</h2>
  <div class="tbl"><table>
    <tr><th>Team</th><th>Starter, annual</th><th>Business, annual</th><th>Business, monthly</th></tr>
    <tr><td>1 person</td><td>$300 a year</td><td>$396 a year</td><td>$480 a year</td></tr>
    <tr><td>3 people</td><td>$900 a year</td><td>$1,188 a year</td><td>$1,440 a year</td></tr>
    <tr><td>10 people</td><td>$3,000 a year</td><td>$3,960 a year</td><td>$4,800 a year</td></tr>
  </table></div>
  <p>Work out your own number with the <a href="/best-superhuman-alternatives/">Superhuman alternatives</a><a href="/superhuman-pricing/">Superhuman pricing</a><a href="/superhuman-cost-calculator/">Superhuman cost calculator</a>.</p>

  <h2>The two price sheets</h2>
  <p>Since Grammarly bought Superhuman and took its name, there are two pages. The Mail plans page lists Starter and Business as above. The Superhuman suite page bundles Mail with Grammarly, Docs and Go and only includes Mail from Business up; its $12 to $15 Pro plan includes an Email Assistant that works inside Gmail or Outlook, not the Superhuman Mail app.</p>

  <h2>Cheaper ways to get the same workflow</h2>
  <p>Zeroness covers the core Superhuman workflow for Gmail and Google Workspace (split inbox, keyboard shortcuts, reminders and AI drafts) for $9.99 a month with AI on every plan, and is free for work email during launch. See <a href="/best-superhuman-alternatives/">all Superhuman alternatives compared</a>.</p>

  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in shp_faq), [crumbs("Superhuman pricing", "/superhuman-pricing/"), faq(shp_faq)])

print("built")
