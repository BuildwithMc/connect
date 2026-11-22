"""Builds the policy pages of connect.buildhq.xyz from the content below, with the site's header and footer.
Run: python scripts/build_legal.py   (writes privacy/, terms/, wallet-and-refunds/, delete-account/, support/)
Pages are plain HTML so any static host serves them at /privacy/ etc.
"""
import os

ROOT = os.path.join(os.path.dirname(__file__), '..')
UPDATED = '23 November 2026'
COMPANY = 'BuildHQ, trading as Connect Power'
ADDRESS = 'No 3 Kenechukwu Chime Close, Trans-Ekulu, Enugu, Nigeria'
EMAIL = 'info@buildhq.xyz'
PHONE = '+234 802 601 6804'

HEAD = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title} | Connect Power</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#1C130D">
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="/assets/styles.css">
  <link rel="stylesheet" href="/assets/legal.css">
</head>
<body>
  <header class="nav">
    <div class="wrap nav__inner">
      <a class="nav__logo" href="/" aria-label="Connect Power home"><img src="/assets/brand/connect-power-horizontal-reversed.svg" alt="Connect Power" width="190" height="30"></a>
      <nav class="nav__links" aria-label="Policies">
        <a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/wallet-and-refunds/">Wallet and refunds</a><a href="/support/">Support</a>
      </nav>
      <a class="btn btn--sun btn--sm" href="/">Home</a>
    </div>
  </header>
  <main id="main" class="legal wrap">
    <p class="kicker">{kicker}</p>
    <h1>{title}</h1>
    <p class="legal__updated">Last updated {updated}</p>
'''

FOOT = '''  </main>
  <footer class="footer">
    <div class="wrap footer__grid">
      <div><img src="/assets/brand/connect-power-horizontal-reversed.svg" alt="Connect Power" width="190" height="30"><p>Prepaid, metered power for homes and businesses. A BuildHQ company.</p></div>
      <div><p class="footer__h">Policies</p><p><a href="/privacy/">Privacy policy</a><br><a href="/terms/">Terms of service</a><br><a href="/wallet-and-refunds/">Wallet and refunds</a><br><a href="/delete-account/">Delete your account</a></p></div>
      <div><p class="footer__h">Talk to us</p><p>{phone}<br>{email}</p></div>
      <div><p class="footer__h">Visit</p><p>{address}</p></div>
    </div>
    <div class="wrap footer__base">© 2026 Connect Power by BuildHQ · <a href="/admin/">Staff sign-in</a></div>
  </footer>
</body>
</html>
'''

PAGES = {
  'privacy': dict(title='Privacy policy', kicker='Your data', desc='What Connect Power collects, why, who we share it with and your rights under the Nigeria Data Protection Act 2023.', body=f'''
<p>This policy explains what personal data {COMPANY} ("Connect Power", "we") collects when you use the Connect Power app, the USSD service, this website and our meters, why we use it, who we share it with, and your rights. We follow the Nigeria Data Protection Act 2023 (NDPA) and the rules of the Nigeria Data Protection Commission (NDPC).</p>

<h2>Who is responsible</h2>
<p>{COMPANY}, {ADDRESS}, is the data controller. Contact us about your data at <b>{EMAIL}</b> or {PHONE}.</p>

<h2>What we collect</h2>
<ul>
  <li><b>Account details:</b> your email address, name, business name if you give one, and phone number.</li>
  <li><b>Identity details for your account number:</b> your BVN, bank account number and bank, which go straight to our payment partner Paystack to confirm your identity and give you a dedicated account number. <b>We do not store your BVN.</b> We keep the result of the check and the account number Paystack gives you.</li>
  <li><b>Meter data:</b> readings from meters linked to your account (energy used, power, voltage, current, power factor, frequency, the meter's on/off state, times) and the nickname you give each meter.</li>
  <li><b>Money:</b> wallet top-ups, plans you create, energy charges, refunds and adjustments, with dates and amounts. We do not see or store your bank card or online banking details.</li>
  <li><b>Support and messages:</b> what you write to us, and the notifications we send you.</li>
  <li><b>Device data:</b> a push-notification token for your phone, and basic technical logs (IP address, time, the request made) to keep the service secure.</li>
  <li><b>Questions to the energy adviser:</b> questions you type into the AI energy insights feature.</li>
</ul>

<h2>Why we use it, and on what legal basis</h2>
<ul>
  <li><b>To provide the service (contract):</b> sign-in, linking your meters, your wallet and plans, charging only for the energy used and never past your plan, receipts, and support.</li>
  <li><b>To meet legal duties (legal obligation):</b> identity checks required for payment accounts in Nigeria, financial record keeping, tax, and answering lawful requests from authorities.</li>
  <li><b>To keep the service safe and working (legitimate interests):</b> fraud prevention, security logs, fixing faults, and understanding how the network is used, in a way that does not override your rights.</li>
  <li><b>With your consent:</b> push notifications (you can turn them off on your phone) and optional marketing messages (you can opt out at any time).</li>
</ul>

<h2>AI energy insights</h2>
<p>When you ask for insights or ask a question about your energy, we send your meter's figures (usage, cost at our price, times, supply quality, plan status) and the meter's nickname to our AI provider, Groq, to write the answer. <b>We do not send your name, email, phone, BVN, bank details or wallet balance.</b> Answers are written by AI and may be imperfect; the figures shown in the app come from your meter.</p>

<h2>Who we share data with</h2>
<p>We share only what each partner needs, under contracts that require them to protect it:</p>
<ul>
  <li><b>Paystack</b> (payments, identity checks and your dedicated account number).</li>
  <li><b>Switch Electric</b> (the metering network that reads your meter and sends us its data).</li>
  <li><b>Supabase</b> (database, sign-in and hosting).</li>
  <li><b>eBulkSMS</b> (sending phone verification codes) and <b>Zoho Mail</b> (sending emails).</li>
  <li><b>Groq</b> (AI energy insights, meter figures only) and <b>Expo</b> (delivering push notifications).</li>
  <li>Authorities, where the law requires it.</li>
</ul>
<p>We do not sell your personal data.</p>

<h2>International transfers</h2>
<p>Some of these partners store or process data outside Nigeria. Where they do, we rely on the safeguards the NDPA allows, such as contractual commitments to protect the data to a standard comparable to Nigerian law.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Detailed meter readings: 90 days. Hourly energy history: while your account is open, then up to 6 years as part of billing records.</li>
  <li>Wallet, plans and payments: at least 6 years after the transaction, as financial records the law requires.</li>
  <li>Support messages: 2 years after the request is closed.</li>
  <li>Security logs: up to 12 months.</li>
</ul>

<h2>Your rights</h2>
<p>You can ask to access your data, correct it, delete it (see <a href="/delete-account/">Delete your account</a>), restrict or object to how we use it, receive a copy in a portable format, and withdraw consent at any time. Email <b>{EMAIL}</b>; we answer within 30 days. If you are not satisfied, you can complain to the Nigeria Data Protection Commission (ndpc.gov.ng).</p>

<h2>Security</h2>
<p>Data is encrypted in transit, access is limited to staff who need it, every staff change is recorded in an audit log that cannot be edited, and payment details stay with Paystack. No system is perfectly secure: tell us at once at {EMAIL} if you think your account has been misused.</p>

<h2>Children</h2>
<p>Connect Power is for people aged 18 and over. We do not knowingly collect data from children.</p>

<h2>Cookies</h2>
<p>This website uses no advertising or tracking cookies. The staff dashboard stores a sign-in session in your browser so you stay signed in. Fonts are loaded from Google Fonts, which receives your IP address to deliver them.</p>

<h2>Changes</h2>
<p>We will post changes here and tell you in the app before important changes take effect.</p>
'''),

  'terms': dict(title='Terms of service', kicker='Using Connect Power', desc='The terms for using the Connect Power app, USSD service, wallet, plans and meters.', body=f'''
<p>These terms are an agreement between you and {COMPANY}. By creating an account or using the Connect Power app, USSD service or a Connect Power meter, you agree to them. If you do not agree, do not use the service.</p>

<h2>1. The service</h2>
<p>Connect Power provides prepaid, metered electricity through smart meters, a wallet you fund by bank transfer, plans you create to control how much each meter may spend, usage analytics and AI energy insights. Meter readings come from the Switch Electric metering network.</p>

<h2>2. Your account</h2>
<ul>
  <li>You must be 18 or over and give true details. You sign in with a code sent to your email; keep access to that email and your phone safe and never share codes.</li>
  <li>To get a dedicated account number you must verify your phone and identity (BVN and bank account) through Paystack.</li>
  <li>You are responsible for activity on your account. Tell us at once if you think someone else has used it.</li>
</ul>

<h2>3. Meters</h2>
<ul>
  <li>A meter is linked to your account by Connect Power. You must have the right to use the supply at that place.</li>
  <li>Do not tamper with, bypass, move or open a meter or its seals. Tampering is a serious offence; we may end the service and recover costs.</li>
  <li>Meter readings are the basis of charging. If you think a reading is wrong, open a support request; we will check it against the network's records.</li>
</ul>

<h2>4. Wallet, price and plans</h2>
<ul>
  <li><b>Price:</b> energy is charged per kWh at the price shown in the app for your meter's site. We may change the price; a new price applies only to energy used after it takes effect, and we show it in the app beforehand.</li>
  <li><b>Plans:</b> you decide how much a meter may spend: a set amount from your wallet or your whole balance. You are charged only for the energy the meter uses, and <b>never more than the plan you set</b>. When the plan is used up, power to that meter is switched off until you start a new plan. You can stop a plan at any time.</li>
  <li><b>Auto-renew:</b> if you turn it on, a new plan of the same amount starts when the last one is used up, if your wallet can cover it.</li>
  <li><b>The wallet</b> holds money only for using Connect Power. It does not earn interest. See <a href="/wallet-and-refunds/">Wallet and refunds</a>.</li>
</ul>

<h2>5. Supply and availability</h2>
<p>We work to keep power and the service available but cannot promise uninterrupted supply. Supply may stop for maintenance, faults, weather, network problems, or events beyond our control. You are not charged for energy you do not receive. We are not liable for loss of stock, business or profit caused by interruptions, except where the law does not allow us to limit liability.</p>

<h2>6. Acceptable use</h2>
<p>Do not misuse the service: no fraud, no use of someone else's account or identity, no attempts to break into our systems, and no abusive messages to staff.</p>

<h2>7. AI energy insights</h2>
<p>Insights and answers are written by AI from your meter's data to help you make decisions. They may be imperfect and are not professional, electrical or financial advice.</p>

<h2>8. Ending the service</h2>
<p>You can close your account at any time (see <a href="/delete-account/">Delete your account</a>). We may suspend or close accounts that break these terms, after telling you why where the law allows. Money left in your wallet is refunded as set out in the wallet policy.</p>

<h2>9. Liability</h2>
<p>Nothing in these terms limits rights you have under Nigerian consumer protection law, including the Federal Competition and Consumer Protection Act 2018. To the extent the law allows, our total liability to you is limited to the amount you paid us in the 3 months before the claim.</p>

<h2>10. Complaints and disputes</h2>
<p>Contact us first at {EMAIL} or {PHONE}; we aim to resolve complaints within 14 days. These terms are governed by the laws of the Federal Republic of Nigeria, and the courts of Enugu State have jurisdiction.</p>

<h2>11. Changes</h2>
<p>We may update these terms. We will tell you in the app before important changes take effect. Continuing to use the service after that means you accept them.</p>
'''),

  'wallet-and-refunds': dict(title='Wallet and refunds', kicker='Your money', desc='How the Connect Power wallet works, how to top up, and how refunds work.', body=f'''
<h2>Topping up</h2>
<p>After you verify your identity, you get a dedicated account number from Paystack. Send money to it from any Nigerian bank app; it reaches your wallet in about a minute and you get a receipt. Transfers are processed by Paystack. Your wallet receives the full amount you send.</p>

<h2>How money leaves your wallet</h2>
<ul>
  <li>Only for energy your meters actually use, at the price per kWh shown in the app, and never past the plan you set for each meter.</li>
  <li>For bills you choose to pay in the app (such as airtime or data), when that feature is available.</li>
  <li>Every charge appears in your wallet history with a receipt.</li>
</ul>

<h2>Refunds</h2>
<ul>
  <li><b>Wrong charges:</b> if a meter reading or charge is wrong, open a support request. If we confirm the error, we credit your wallet. Corrections need approval by two members of our finance team.</li>
  <li><b>Closing your account:</b> we refund your remaining wallet balance to a Nigerian bank account in your own name, usually within 10 working days of confirming your request.</li>
  <li><b>Failed transfers in:</b> if you sent money and it has not arrived after 24 hours, contact us with the time, amount and your bank's reference.</li>
</ul>

<h2>What the wallet is not</h2>
<p>The wallet is a prepaid balance for Connect Power services. It is not a bank account, it does not earn interest, and money cannot be sent from it to other people.</p>

<h2>Questions</h2>
<p>{EMAIL} · {PHONE}</p>
'''),

  'delete-account': dict(title='Delete your account', kicker='Your choice', desc='How to delete your Connect Power account and what happens to your data.', body=f'''
<p>You can ask us to delete your Connect Power account and personal data at any time.</p>

<h2>How to ask</h2>
<ol>
  <li><b>In the app:</b> go to <i>More → Account → Delete my account</i>.</li>
  <li><b>By email:</b> write to <b>{EMAIL}</b> from the email address on your account, with the subject "Delete my account".</li>
</ol>

<h2>What happens next</h2>
<ul>
  <li>Your running plans stop at once, so nothing more is charged.</li>
  <li>We refund your remaining wallet balance to a Nigerian bank account in your own name.</li>
  <li>Within 30 days we delete your profile, phone number, meter nicknames, notifications, support messages and device tokens, and we unlink your meters.</li>
  <li><b>What we must keep:</b> records of payments, charges and refunds for at least 6 years, as Nigerian law requires for financial records. These are kept securely and used for nothing else.</li>
</ul>

<h2>Questions</h2>
<p>{EMAIL} · {PHONE}</p>
'''),

  'support': dict(title='Support', kicker='We are here to help', desc='How to get help with Connect Power: meters, wallet, plans and your account.', body=f'''
<h2>In the app</h2>
<p>Go to <i>More → Help</i> to open a request about a meter, your wallet, a plan, identity checks or your account. We reply in the app and you get a notification.</p>

<h2>Call, WhatsApp or email</h2>
<p><b>{PHONE}</b> (call or WhatsApp) · <b>{EMAIL}</b></p>
<p>Office: {ADDRESS}. Monday to Saturday, 8 am to 6 pm.</p>

<h2>Common questions</h2>
<h3>My power is off</h3>
<p>Check that the meter has a plan running and your wallet has money. If both are fine, open a request and tell us the meter's name.</p>
<h3>I sent money but my wallet did not change</h3>
<p>Transfers usually arrive in about a minute. If it has been more than 24 hours, send us the time, amount and your bank's reference.</p>
<h3>Can a meter spend more than my plan?</h3>
<p>No. You are charged only for energy used and never more than the plan you set.</p>
<h3>How do I close my account?</h3>
<p>See <a href="/delete-account/">Delete your account</a>.</p>
'''),
}

for slug, p in PAGES.items():
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    html = HEAD.format(title=p['title'], desc=p['desc'], kicker=p['kicker'], updated=UPDATED) + p['body'] + FOOT.format(phone=PHONE, email=EMAIL, address=ADDRESS)
    with open(os.path.join(ROOT, slug, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    print('wrote', slug)
