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
<footer><div class="wrap"><span>© 2026 Applied Crew, Inc.</span><span><a href="/features/">Features</a><a href="/superhuman-alternative/">Zeroness vs Superhuman</a><a href="/inbox-zero/">Inbox zero guide</a><a href="/pricing/">Pricing</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></span></div></footer>
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
  <p class="meta-line">Last checked November 4, 2026, from each product's public pages.</p>

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
    ("How much does Zeroness cost?", "Zeroness is free for work email on company domains during launch. Personal is $9.99 a month, or $30 for the first year at launch. Students pay $1 a month with a .edu address."),
    ("Is AI included?", "Yes. Every plan includes every feature, including drafts, summaries, Ask and sorting."),
    ("Will my price go up after launch?", "No. Launch prices stay the same for as long as you stay subscribed."),
    ("Can I cancel any time?", "Yes. Cancel any time and keep access until the end of the billing period."),
]
page("/pricing/", "Pricing · Zeroness", "Zeroness pricing: free for work email during launch, $9.99 a month for personal accounts, $1 a month for students. Every feature and all AI included.", """
  <span class="kicker">Pricing</span>
  <h1 class="serif">Simple pricing. Everything included.</h1>
  <p class="intro">Every plan has every feature, AI included. Launch prices stay the same for as long as you subscribe.</p>
  <div class="tbl"><table>
    <tr><th>Plan</th><th>Price</th><th>For</th></tr>
    <tr><td>Work email</td><td>Free during launch</td><td>Any company domain on Google Workspace</td></tr>
    <tr><td>Personal</td><td>$9.99 a month, or $30 for the first year at launch</td><td>Gmail and personal accounts</td></tr>
    <tr><td>Students</td><td>$1 a month</td><td>Anyone with a .edu address</td></tr>
  </table></div>
  <h2>Questions</h2>
""" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in pr_faq), [crumbs("Pricing", "/pricing/"), faq(pr_faq)])

print("built")
