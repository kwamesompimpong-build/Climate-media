/* ============================================================
   The Tide Playbook — Blue Crab Strategies
   Vanilla ES2020+, no dependencies. Defensive throughout:
   nothing here throws if an element is missing.
   ============================================================ */

// CSS guards reveal animations behind html.js — set this first.
document.documentElement.classList.add('js');

(() => {
  'use strict';

  const prefersReducedMotion =
    window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------
     1 + 2. Scroll reveal & stat count-up (shared observer)
     ------------------------------------------------------------ */

  const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);

  function formatStat(value, isDecimal, suffix) {
    return (isDecimal ? value.toFixed(1) : String(Math.round(value))) + suffix;
  }

  function runCountUp(el) {
    const target = parseFloat(el.dataset.count);
    if (Number.isNaN(target)) return;
    const suffix = el.dataset.suffix || '';
    const isDecimal = String(el.dataset.count).includes('.');

    if (prefersReducedMotion) {
      el.textContent = formatStat(target, isDecimal, suffix);
      return;
    }

    const duration = 1400;
    const start = performance.now();

    const tick = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const value = target * easeOutCubic(progress);
      el.textContent = formatStat(value, isDecimal, suffix);
      if (progress < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  function revealElement(el) {
    el.classList.add('is-visible');
    // Animate any stat numbers inside the revealed element.
    el.querySelectorAll('span.stat-num[data-count]').forEach(runCountUp);
    if (el.matches && el.matches('span.stat-num[data-count]')) runCountUp(el);
  }

  function initReveal() {
    const targets = new Set([
      ...document.querySelectorAll('.reveal'),
      // Catch stat-nums that might live outside a .reveal wrapper.
      ...document.querySelectorAll('span.stat-num[data-count]'),
    ]);
    if (!targets.size) return;

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      targets.forEach(revealElement);
      return;
    }

    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          revealElement(entry.target);
          obs.unobserve(entry.target);
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    targets.forEach((el) => observer.observe(el));
  }

  /* ------------------------------------------------------------
     3. Case-study filters
     ------------------------------------------------------------ */

  function initFilters() {
    const chips = document.querySelectorAll('.chip[data-filter]');
    const cases = document.querySelectorAll('details.case');
    if (!chips.length || !cases.length) return;

    chips.forEach((chip) => {
      chip.addEventListener('click', () => {
        chips.forEach((c) => c.classList.toggle('is-active', c === chip));
        const filter = chip.dataset.filter;

        cases.forEach((card) => {
          const cats = (card.dataset.cat || '').split(/\s+/);
          const show = filter === 'all' || cats.includes(filter);
          card.classList.toggle('is-hidden', !show);
          if (!show) card.removeAttribute('open');
        });
      });
    });
  }

  /* ------------------------------------------------------------
     4. Single-open accordion for case cards
     ------------------------------------------------------------ */

  function initAccordion() {
    const cases = document.querySelectorAll('details.case');
    cases.forEach((card) => {
      card.addEventListener('toggle', () => {
        if (!card.open) return;
        cases.forEach((other) => {
          if (other !== card) other.removeAttribute('open');
        });
      });
    });
  }

  /* ------------------------------------------------------------
     5. Play builder
     ------------------------------------------------------------ */

  const PLATFORMS = {
    scripted: {
      label: 'Scripted TV & Film',
      title: "The Writers' Room Pipeline",
      summary:
        "Place vetted climate-domain experts (health, insurance, food, migration) inside the writers' rooms of returning shows your audiences already trust, so climate shows up as plot pressure, not message.",
      moves: [
        'Identify 3 returning shows your priority audience over-indexes on; map current climate presence (usually near zero — only 2.8% of scripts mention climate at all).',
        'Fund a broker org (Green Screen / Good Energy model) to match each show with one domain expert on retainer, not a one-off consult.',
        'Pre-negotiate a discourse plan: clips, creator reactions and explainers ready for the night the episode airs.',
      ],
      metric:
        'Climate-keyword presence in next-season scripts of target shows, plus pre/post audience salience polling.',
      precedent:
        "Grey's Anatomy's heat-dome arc, built with Green Screen / CAA Foundation science advisers.",
    },
    serial: {
      label: 'Soaps & Serial Drama',
      title: 'The Synchronized Storyline',
      summary:
        'Convene rival soaps and serials around one shared climate week of storylines — coordinated backstage, aired simultaneously, anchored to a real policy moment.',
      moves: [
        'Hire the convener: one trusted producer-diplomat to run months of quiet coordination across rival editorial teams (the Jane Hudson role).',
        'Anchor the week to a calendar moment — a COP, a climate week, the start of heat season.',
        "Write transitional characters, not heroes: a sceptic moving one believable step (the Sabido method's 50-year evidence base).",
      ],
      metric:
        'Combined reach of the synchronized week, story spillover into news/social, and audience attitude shift in serial-viewer panels.',
      precedent:
        'The 2021 COP26 week, when EastEnders, Coronation Street, Emmerdale, Hollyoaks, Casualty, Doctors and Holby City crossed characters for the first time ever.',
    },
    music: {
      label: 'Music & Live Events',
      title: 'The Civic Tour Stop',
      summary:
        'Ride existing tours — fund the civic wrapper (local activists on the bill, plant-based catering, action booths, verified green ops) that converts arena nights into climate moments city by city.',
      moves: [
        'Map the next 12 months of major tours through your priority cities and rank by audience fit.',
        'Offer artists a turnkey civic package: local partners, venue greening, fan action layer — zero extra lift for the tour.',
        "Fund independent verification of the tour's footprint; the verified number IS the story.",
      ],
      metric:
        "Fan actions taken per stop, earned media on the verified footprint, and partner orgs' local sign-ups.",
      precedent:
        "Billie Eilish's Overheated at The O2 in London; Coldplay's Music of the Spheres tour, 59% emissions cut verified by MIT with no offsets counted.",
    },
    gaming: {
      label: 'Gaming & Interactive',
      title: 'The Mechanics Play',
      summary:
        'Put climate stakes inside gameplay — restoration mechanics, in-game events, jam prizes — where 3B+ players protect what they build, instead of watching cutscene messages.',
      moves: [
        'Sponsor a Green Game Jam track or prize aimed at studios whose players match your audience.',
        'Fund a climate design toolkit so mid-size studios can ship restoration/resilience mechanics without research overhead.',
        'Build the bridge: every in-game act pairs with one real-world act (tree planted, pledge, local event).',
      ],
      metric:
        'Player activations, in-game-to-real-world conversion rate, and number of studios shipping climate mechanics.',
      precedent:
        "UNEP's Playing for the Planet Alliance and its Green Game Jams, reaching hundreds of millions of players with in-game activations.",
    },
    sport: {
      label: 'Sport & Fandom',
      title: 'The First Mover Club',
      summary:
        'Make one club, team or athlete in each league the total-identity sustainability flagship — and let tribal rivalry do the distribution.',
      moves: [
        'Pick the league/country and find the willing first mover (often a smaller, hungrier club).',
        'Fund the full identity shift — energy, food, kit, pitch — not a sponsorship patch.',
        'Arm the fandom: chants, banter, derby-day content that makes sustainability a point of pride.',
      ],
      metric:
        'Share of league media conversation, copycat commitments by rival clubs, and fan-community growth beyond the home region.',
      precedent:
        'Forest Green Rovers, the world’s first UN-certified carbon-neutral football club — global fanbase, outsized media footprint.',
    },
    creator: {
      label: 'Creators & Social',
      title: 'The Portable Phrase',
      summary:
        "Seed one sticky, argument-starting phrase (the 'Just Look Up' play) through creators your audience actually follows — then fund the discourse layer that keeps it alive.",
      moves: [
        'Workshop 3 candidate phrases with creators and fandom insiders — test for remixability, not approval ratings.',
        'Brief 20 mid-size creators across niches (gaming, beauty, sport, finance) to carry it natively — no scripts.',
        "Stand up a rapid-response desk to feed the conversation while it's alive: stitches, duets, explainers, counter-memes.",
      ],
      metric:
        'Organic (unpaid) usage of the phrase by strangers, share of voice in climate conversation, and fandom-led actions triggered.',
      precedent:
        "Don't Look Up's 'Just Look Up' becoming protest-sign shorthand; Kpop4Planet converting fandom into corporate-policy wins.",
    },
  };

  const GOALS = {
    normalize: {
      label: 'Normalize climate in everyday story',
      summaryAppend:
        ' Aim for presence, not prominence: climate as believable background pressure in stories about love, work and family.',
      replaceMove3:
        "Set a 'background presence' quota with partners: heat pumps, floods, induction hobs, green jobs appearing without comment — normal life, on screen.",
      metricPrefix:
        'Narrative-presence audit year over year (the 2.8% baseline is your scoreboard) — plus: ',
    },
    mobilize: {
      label: 'Mobilize a specific audience',
      summaryAppend:
        ' Every story moment lands with a single, low-friction next action for one named audience.',
      extraMove:
        "Define ONE audience and ONE action before any creative is funded; reject plays that can't name both.",
      metricPrefix:
        'Actions completed by the named audience (sign-ups, pledges, turnout) — plus: ',
    },
    window: {
      label: 'Shift a policy window',
      summaryAppend:
        ' Time everything to a live policy moment so culture and politics peak together.',
      extraMove:
        'Reverse-engineer the calendar: schedule the cultural peak 2–3 weeks before the policy decision, when coverage is hungriest (the COP26 soap-week timing).',
      metricPrefix:
        'Policymaker citations, press linking the story to the policy moment, polling movement in the decision window — plus: ',
    },
    localize: {
      label: 'Localize a global narrative',
      summaryAppend:
        ' Translate the play into local formats, languages and trusted faces — adaptation, not dubbing.',
      extraMove:
        "Pair every global property with a local creative owner who can veto anything that doesn't ring true (the Population Media Center adaptation model).",
      metricPrefix:
        'Local-language reach and locally-produced derivative works — plus: ',
    },
  };

  // Compose a play object from a platform + goal pair.
  function composePlay(platform, goal) {
    const summary = platform.summary + (goal.summaryAppend || '');

    const moves = platform.moves.slice();
    if (goal.replaceMove3) {
      moves[2] = goal.replaceMove3;
    } else if (goal.extraMove) {
      moves.push(goal.extraMove);
    }

    // Lowercase first letter of platform metric when prefixed.
    const metricBody =
      platform.metric.charAt(0).toLowerCase() + platform.metric.slice(1);
    const metric = (goal.metricPrefix || '') + metricBody;

    return {
      meta: `OPENING PLAY · ${platform.label} × ${goal.label}`,
      title: platform.title,
      summary,
      moves,
      metric,
      precedent: platform.precedent,
    };
  }

  // Minimal escaper — data is our own constants, but belt and braces.
  function escapeHTML(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderPlay(card, play) {
    card.innerHTML = `
      <p class="play-meta">${escapeHTML(play.meta)}</p>
      <h3 class="play-title">${escapeHTML(play.title)}</h3>
      <div class="play-section"><h5>The play</h5><p>${escapeHTML(play.summary)}</p></div>
      <div class="play-section"><h5>First three moves</h5><ol>${play.moves
        .map((m) => `<li>${escapeHTML(m)}</li>`)
        .join('')}</ol></div>
      <div class="play-section"><h5>What you measure</h5><p>${escapeHTML(play.metric)}</p></div>
      <p class="play-ref">Precedent: ${escapeHTML(play.precedent)}</p>
    `;

    // Re-trigger the entrance animation (force reflow between).
    card.classList.remove('is-dealt');
    void card.offsetWidth;
    card.classList.add('is-dealt');
  }

  function playToPlainText(play) {
    const moves = play.moves.map((m, i) => `${i + 1}. ${m}`).join('\n');
    return [
      play.meta,
      play.title,
      '',
      'THE PLAY',
      play.summary,
      '',
      'FIRST MOVES',
      moves,
      '',
      'WHAT YOU MEASURE',
      play.metric,
      '',
      `Precedent: ${play.precedent}`,
    ].join('\n');
  }

  function initBuilder() {
    const selPlatform = document.getElementById('sel-platform');
    const selGoal = document.getElementById('sel-goal');
    const btnGenerate = document.getElementById('btn-generate');
    const card = document.getElementById('play-card');
    const btnCopy = document.getElementById('btn-copy');
    if (!selPlatform || !selGoal || !btnGenerate || !card) return;

    let currentPlay = null;

    btnGenerate.addEventListener('click', () => {
      const platform = PLATFORMS[selPlatform.value];
      const goal = GOALS[selGoal.value];
      if (!platform || !goal) return;

      currentPlay = composePlay(platform, goal);
      renderPlay(card, currentPlay);
      if (btnCopy) btnCopy.hidden = false;
    });

    if (btnCopy) {
      const defaultLabel = btnCopy.textContent;
      let resetTimer = null;

      btnCopy.addEventListener('click', async () => {
        if (!currentPlay) return;
        const text = playToPlainText(currentPlay);
        try {
          await navigator.clipboard.writeText(text);
          btnCopy.textContent = 'Copied ✓';
        } catch {
          btnCopy.textContent = 'Copy failed — select manually';
        }
        clearTimeout(resetTimer);
        resetTimer = setTimeout(() => {
          btnCopy.textContent = defaultLabel;
        }, 2000);
      });
    }
  }

  /* ------------------------------------------------------------
     Boot — each feature isolated so one failure can't sink the rest.
     ------------------------------------------------------------ */

  const safely = (fn) => {
    try {
      fn();
    } catch (err) {
      console.warn('[Tide Playbook]', err);
    }
  };

  const boot = () => {
    safely(initReveal);
    safely(initFilters);
    safely(initAccordion);
    safely(initBuilder);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
