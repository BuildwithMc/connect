// Connect Power landing page: USSD demo phone and the pilot waitlist form.
(function () {
  'use strict';

  // ---------------------------------------------------------------- USSD demo
  var CODE = '*384*04227#';
  var view = document.getElementById('ussd-view');
  var clock = document.getElementById('ussd-clock');
  if (!view) return;

  var naira = function (k) {
    var kobo = k % 100 !== 0;
    return 'N' + (k / 100).toLocaleString('en-NG', { minimumFractionDigits: kobo ? 2 : 0, maximumFractionDigits: 2 });
  };
  var PLANS = [
    { name: '4 hours', price: 40000, mins: 240 },
    { name: '8 hours', price: 75000, mins: 480 },
    { name: 'Full day', price: 120000, mins: null }
  ];

  var state = { mode: 'dial', typed: '', reply: '', screen: null, balance: 149750, powerOn: true, endsAt: new Date(Date.now() + 320 * 60000), plan: null };

  function at(h, m) { var d = new Date(); d.setHours(h, m, 0, 0); return d; }
  function hhmm(d) {
    var h = d.getHours(), m = d.getMinutes();
    return ((h % 12) || 12) + ':' + (m < 10 ? '0' : '') + m + (h < 12 ? 'am' : 'pm');
  }
  function tick() { clock.textContent = hhmm(new Date()).replace(/(am|pm)$/, ''); }
  tick(); setInterval(tick, 30000);

  // Each screen: text, and what each reply leads to.
  var screens = {
    menu: function () {
      return { text: 'Connect Power\nWelcome back, Ada\n\n1. Buy power\n2. Check balance\n3. My meter\n4. Fund wallet\n0. Help', on: { '1': 'buy', '2': 'balance', '3': 'meter', '4': 'fund', '0': 'help' } };
    },
    buy: function () {
      var t = 'Buy power for Stall 14B\n\n';
      PLANS.forEach(function (p, i) { t += (i + 1) + '. ' + p.name + ' - ' + naira(p.price) + '\n'; });
      return { text: t + '0. Back', on: { '1': pick(0), '2': pick(1), '3': pick(2), '0': 'menu' } };
    },
    confirm: function () {
      var p = state.plan;
      if (state.balance < p.price) {
        return { text: 'Not enough money.\n' + p.name + ' costs ' + naira(p.price) + '.\nBalance: ' + naira(state.balance) + '\n\n4. Fund wallet\n0. Back', on: { '4': 'fund', '0': 'buy' } };
      }
      return { text: p.name + ' for ' + naira(p.price) + '\nBalance: ' + naira(state.balance) + '\n\nEnter your 4-digit PIN to pay:', pin: true };
    },
    paid: function () {
      var p = state.plan;
      state.balance -= p.price;
      var from = state.powerOn && state.endsAt > new Date() ? state.endsAt : new Date();
      state.endsAt = p.mins ? new Date(from.getTime() + p.mins * 60000) : at(23, 59);
      state.powerOn = true;
      return { text: 'Payment received!\n\nStall 14B is ON\nuntil ' + hhmm(state.endsAt) + '.\nNew balance: ' + naira(state.balance) + '\n\nToken: ' + token(), end: true };
    },
    balance: function () {
      var hours = Math.floor(state.balance / 9400);
      return { text: 'Wallet: ' + naira(state.balance) + '\nAbout ' + hours + ' h of light\nPower: ' + (state.powerOn ? 'ON until ' + hhmm(state.endsAt) : 'OFF') + '\n\n0. Back', on: { '0': 'menu' } };
    },
    meter: function () {
      return state.powerOn
        ? { text: 'Stall 14B: ON\nUsing 1.8 kW now\nPlan ends ' + hhmm(state.endsAt) + '\n\n1. Turn off for now\n0. Back', on: { '1': 'off', '0': 'menu' } }
        : { text: 'Stall 14B: OFF\nYour paid time is kept.\n\n1. Turn on\n0. Back', on: { '1': 'on', '0': 'menu' } };
    },
    off: function () { state.powerOn = false; return { text: 'Stall 14B is now OFF.\nYour paid time is kept\nfor when you turn it back on.', end: true }; },
    on: function () { state.powerOn = true; return { text: 'Stall 14B is ON again\nuntil ' + hhmm(state.endsAt) + '.', end: true }; },
    fund: function () { return { text: 'Fund by bank transfer\nfrom any bank app:\n\nWema Bank\n9932417805\nConnect Power/Ada Obi\n\nIt lands in about a minute.', end: true }; },
    help: function () { return { text: 'Need help?\nCall or WhatsApp\n0802 601 6804\n\nVisit our desk at\nOld Artisan Market.', end: true }; },
    wrong: function () { return { text: 'Unknown option.\n\n0. Back to menu', on: { '0': 'menu' } }; }
  };

  function pick(i) { return function () { state.plan = PLANS[i]; return 'confirm'; }; }
  function token() { var s = ''; for (var i = 0; i < 8; i++) s += Math.floor(Math.random() * 10); return s.slice(0, 4) + '-' + s.slice(4); }

  function render() {
    var s = state;
    if (s.mode === 'dial') {
      view.innerHTML = '';
      var hint = el('div', 'hint', s.typed ? '' : 'Type ' + CODE + '\nthen press the green key');
      view.appendChild(hint);
      view.appendChild(el('div', 'dial', s.typed || ' '));
    } else if (s.mode === 'busy') {
      view.innerHTML = '';
      view.appendChild(el('div', 'busy', 'USSD code running...'));
    } else if (s.mode === 'session') {
      view.innerHTML = '';
      view.appendChild(document.createTextNode(s.screen.text));
      if (!s.screen.end) {
        var r = el('div', 'reply', '');
        r.appendChild(el('span', '', s.screen.pin ? 'PIN:' : 'Reply:'));
        var b = el('b', '', s.screen.pin ? s.reply.replace(/./g, '*') : s.reply);
        r.appendChild(b);
        r.appendChild(el('span', '', 'Send ✆'));
        view.appendChild(r);
      } else {
        view.appendChild(el('div', 'hint', '\n\nPress ✕ to close'));
      }
    } else if (s.mode === 'error') {
      view.innerHTML = '';
      view.appendChild(el('div', 'busy', 'Connection problem\nor invalid MMI code.\n\nTry ' + CODE));
    }
    view.scrollTop = 0;
  }

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text) e.textContent = text; return e; }

  function go(name) {
    var next = typeof name === 'function' ? name() : name;
    state.screen = screens[next]();
    state.screenName = next;
    state.reply = '';
    state.mode = 'session';
    render();
  }

  function press(k) {
    if (state.mode === 'dial') { if (state.typed.length < 20) state.typed += k; }
    else if (state.mode === 'session' && !state.screen.end) {
      var max = state.screen.pin ? 4 : 2;
      if (state.reply.length < max && /\d/.test(k)) state.reply += k;
    }
    render();
  }

  function send() {
    if (state.mode === 'dial') {
      if (!state.typed) return;
      var ok = state.typed === CODE;
      state.mode = 'busy'; render();
      setTimeout(function () {
        if (ok) go('menu'); else { state.mode = 'error'; render(); }
      }, 900);
      return;
    }
    if (state.mode !== 'session' || state.screen.end) return;
    var sc = state.screen;
    if (sc.pin) {
      if (state.reply.length !== 4) return;
      state.mode = 'busy'; render();
      setTimeout(function () { go('paid'); }, 1100);
      return;
    }
    var target = sc.on && sc.on[state.reply];
    go(target || 'wrong');
  }

  function end() { state.mode = 'dial'; state.typed = ''; state.reply = ''; render(); }
  function clear() {
    if (state.mode === 'dial') state.typed = state.typed.slice(0, -1);
    else if (state.mode === 'session') state.reply = state.reply.slice(0, -1);
    render();
  }

  document.querySelectorAll('#ussd .key').forEach(function (b) {
    b.addEventListener('click', function () {
      var k = b.getAttribute('data-key'), act = b.getAttribute('data-act');
      if (k) press(k); else if (act === 'send') send(); else if (act === 'end') end(); else if (act === 'clear') clear();
    });
  });
  document.getElementById('ussd-dial').addEventListener('click', function () {
    end(); state.typed = CODE; render(); setTimeout(send, 250);
  });

  // Physical keyboard, while the pointer or focus is on the phone.
  var phone = document.getElementById('ussd');
  var active = false;
  phone.addEventListener('mouseenter', function () { active = true; });
  phone.addEventListener('mouseleave', function () { active = false; });
  phone.addEventListener('focusin', function () { active = true; });
  phone.addEventListener('focusout', function () { active = phone.contains(document.activeElement); });
  document.addEventListener('keydown', function (e) {
    if (!active || e.ctrlKey || e.metaKey || e.altKey) return;
    if (/^[0-9*#]$/.test(e.key)) { press(e.key); flash(e.key); e.preventDefault(); }
    else if (e.key === 'Enter') { send(); e.preventDefault(); }
    else if (e.key === 'Backspace') { clear(); e.preventDefault(); }
    else if (e.key === 'Escape') { end(); e.preventDefault(); }
  });
  function flash(k) {
    var b = phone.querySelector('[data-key="' + (k === '#' ? '\\#' : k === '*' ? '\\*' : k) + '"]');
    if (!b) return;
    b.classList.add('is-pressed'); setTimeout(function () { b.classList.remove('is-pressed'); }, 120);
  }

  render();
})();

(function () {
  'use strict';
  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());

  // ---------------------------------------------------------------- pilot waitlist
  // Set WAITLIST_ENDPOINT to the API (POST JSON) when it is live. Until then the form opens an email.
  var WAITLIST_ENDPOINT = '';
  var form = document.getElementById('pilot-form');
  var msg = document.getElementById('pilot-msg');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var data = { name: form.name.value.trim(), phone: form.phone.value.trim(), market: form.market.value.trim(), use: form.use.value };
    var phoneOk = /^(\+?234|0)?[789][01]\d{8}$/.test(data.phone.replace(/[\s-]/g, ''));
    msg.className = 'form__msg';
    if (!data.name || !data.market) { msg.textContent = 'Add your name and your market, please.'; msg.classList.add('is-err'); return; }
    if (!phoneOk) { msg.textContent = 'Enter a Nigerian mobile number, like 0803 123 4567.'; msg.classList.add('is-err'); form.phone.focus(); return; }

    if (!WAITLIST_ENDPOINT) {
      var body = 'Name: ' + data.name + '\nPhone: ' + data.phone + '\nMarket: ' + data.market + '\nNeeds power for: ' + data.use;
      window.location.href = 'mailto:info@buildhq.xyz?subject=' + encodeURIComponent('Connect Power pilot: ' + data.market) + '&body=' + encodeURIComponent(body);
      msg.textContent = 'Your email app should open with your details. Send it and we will call you.';
      msg.classList.add('is-ok');
      return;
    }
    var btn = form.querySelector('button');
    btn.disabled = true;
    fetch(WAITLIST_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw new Error(); form.reset(); msg.textContent = 'You are on the list. We will call you when a hub reaches your market.'; msg.classList.add('is-ok'); })
      .catch(function () { msg.textContent = 'That did not go through. Call or WhatsApp +234 802 601 6804 instead.'; msg.classList.add('is-err'); })
      .then(function () { btn.disabled = false; });
  });
})();
