# Rebuilding *The Tide Playbook* in Gemini Canvas

Everything you need to recreate this site — **The Tide Playbook** by Blue Crab Strategies —
inside **Gemini Canvas**. The original is a hand-built single page (static HTML + CSS +
vanilla JS). Canvas works best when you give it **one self-contained brief** and then refine
in small follow-up turns. This document gives you (1) a paste-ready master prompt, (2) the
complete content so nothing gets paraphrased away, (3) the exact design system, and (4) a
sequence of refinement prompts to dial it in.

---

## 0. How to drive Gemini Canvas for this

1. Open **gemini.google.com**, start a chat, and turn on **Canvas** (the Canvas button in the
   prompt bar). Canvas renders a live preview of code/HTML beside the chat.
2. Paste **Section 1 (the master prompt)** as your first message. Ask it to produce **one
   self-contained `index.html`** with CSS and JS inline — Canvas previews single files most
   reliably.
3. Iterate with the **Section 5** follow-ups, one change per turn. Canvas edits in place, so
   small, specific asks ("make the stat numbers count up on scroll") beat one giant re-prompt.
4. When it looks right, use Canvas's **Download / Copy code** to export the HTML, or **Share →
   Publish** to get a hosted link.

> **Tip:** Canvas can drift on long copy. Paste the verbatim text blocks from Section 2 when a
> section's wording matters — tell it *"use this exact copy, don't rewrite it."*

---

## 1. Master prompt (paste this first)

> Build a single self-contained `index.html` file (all CSS and JavaScript inline, no external
> build step, no frameworks) for a one-page marketing/playbook site called **"The Tide
> Playbook"** by **Blue Crab Strategies**. It is a working playbook for climate funders and
> foundations, made for **London Climate Week 2026**, about shaping climate narratives through
> the entertainment and culture people already love.
>
> **Fonts:** Load from Google Fonts — **Rajdhani** (weights 500/600/700) for all headings, UI
> labels, buttons, and numbers; **Inter** (400–700) for body text.
>
> **Brand palette:**
> - Navy `#27396B` (primary), deep navy `#1E2D55`
> - Slate teal `#74A0AB`, deep slate `#3F6E7A`
> - Paper white `#FFFFFF`, mist `#F4F6F8`
> - Body text `#46536A`, hairlines `#E1E6ED`
>
> **Look & feel:** Light, minimal, confident. Full-bleed color-blocked sections alternating
> white → deep navy → mist → navy → white. Rounded pill buttons, hairline-bordered cards,
> generous whitespace, uppercase letter-spaced kicker labels. No serif fonts, no italics in
> headings (use color for emphasis instead). A hand-drawn line-art **crab** is the brand mark.
>
> **Page sections, in order:**
> 1. **Sticky top nav** — crab mark + "Blue Crab Strategies" wordmark on the left; anchor links
>    (Why story · The framework · Case studies · Play builder · In the room); a pill badge
>    "London Climate Week '26" on the right.
> 2. **Hero** (white, centered) — large crab line-mark, kicker "A working playbook · London
>    Climate Week 2026", giant headline "Culture moves faster than carbon." ("faster than
>    carbon" in slate color), a sub-paragraph, two buttons (filled navy "Read the plays",
>    ghost "Build your own ↓"), and a **navy marquee strip** at the bottom scrolling culture
>    references. Add 3 soft blurred drifting background "wave" blobs.
> 3. **"01 — The case for story"** (navy block) — headline, lede about climate's absence from
>    entertainment being *whitespace* / opportunity, a **4-up stat grid** with numbers that
>    **count up when scrolled into view**, and a pull-quote.
> 4. **"02 — The framework"** (white) — the **TIDE** framework as 4 accent-topped cards (Tune
>    in / Immerse / Distribute / Evaluate), each with a big letter, description, and 3 bullets.
> 5. **"03 — The case files"** (mist) — filter chips (All / TV & Film / Soaps & Serials /
>    Music & Live / Gaming / Sport / Fandom) and **9 expandable accordion cards** (`<details>`),
>    each with a tag, title, one-line hook, and on expand: "The story / The move / The receipts"
>    plus a highlighted "Steal this" takeaway box. Only one card open at a time; chips filter.
> 6. **"04 — Make it yours" → the Play Builder** (navy block) — two dropdowns (Medium, Goal)
>    and a "Deal the play" button that generates a tailored play card from JS data, plus a
>    "Copy play to clipboard" button.
> 7. **"05 — In the room"** (white) — a numbered 90-minute session agenda (timeline style) and
>    a slate-teal "Provocations for the pub" box.
> 8. **Footer** (navy) — crab mark, ethos line, and a "Receipts & further reading" link list.
>
> **Interactions:** scroll-reveal fade-up on sections; stat count-up; chip filtering; single-open
> accordion; the play builder (compose text from medium × goal); copy-to-clipboard. Make it fully
> responsive (4-col → 2-col → 1-col stat grid; nav links hide on mobile) and include a print
> stylesheet that flattens dark sections to white for a handout. Respect `prefers-reduced-motion`.
>
> I will paste the exact copy for each section next — use it verbatim.

Then paste Section 2 content block-by-block as Canvas builds each section.

---

## 2. Exact content (verbatim copy)

### Meta / SEO
- **Title:** `The Tide Playbook — Climate Narratives Through Media & Culture | Blue Crab Strategies`
- **Meta description:** `A working playbook for foundations and philanthropies shaping climate narratives through the media people already love. Built by Blue Crab Strategies for London Climate Week.`
- **Favicon:** the crab SVG (see Section 4).

### Nav
- Wordmark: **Blue Crab** *Strategies* ("Strategies" lighter weight, slate color)
- Links: `Why story` `The framework` `Case studies` `Play builder` `In the room`
- Badge: `London Climate Week '26`

### Hero
- Kicker: `A working playbook · London Climate Week 2026`
- Headline: **Culture moves / faster than carbon.** (line break before "faster than carbon"; that phrase in slate)
- Sub: *Policy follows public imagination — and public imagination lives in the shows we binge, the songs we scream, and the games we play. This is a field guide for funders ready to meet the planet's messiest problem inside the stories people already love.*
- Buttons: `Read the plays` (→ #cases), `Build your own ↓` (→ #builder)
- Marquee items (loop them): Grey's Anatomy ◆ EastEnders × COP26 ◆ K-drama ◆ Telenovelas ◆ Stadium tours ◆ The O2 ◆ Fortnite ◆ Forest Green Rovers ◆ Fandom ◆

### 01 — The case for story (navy)
- Kicker: `01 — The case for story`
- Headline: **The biggest stage on Earth is almost silent on climate.**
- Lede: *Entertainment reaches billions of people a day in the exact emotional register where worldviews are formed. Yet the climate crisis barely appears. That silence isn't a failure — it's **whitespace**. For philanthropy, it may be the most undervalued narrative real estate in the world.*
- **Stats (animate from 0):**

| Number | Label | Source |
|---|---|---|
| **2.8%** | of 37,000+ film & TV scripts (2016–20) mention *any* climate keyword | Good Energy × USC Norman Lear Center |
| **0.6%** | say the words "climate change" out loud | same study |
| **90%** | of South Koreans call climate a pressing crisis — while it fills 0.36% of top K-drama screen time | IJoC, 60 dramas 2019–24 |
| **3B+** | people play video games — a bigger audience than film and music combined | UNEP Playing for the Planet |

- Pull-quote: *"People don't change their minds because of data. They change their minds when someone they love — even a fictional someone — changes theirs."*

### 02 — The framework: TIDE (white)
- Kicker: `02 — The framework`
- Headline: **Work like the tide.** sub: *Four moves, in any medium.*
- Lede: *Blue crabs grow by molting — shedding a shell that no longer fits. So do narratives. The **TIDE** framework is how we help funders shed the PSA-era playbook and move with culture instead of against it.*

Four cards (accent colors: T `#27396B`, I `#3F6E7A`, D `#74A0AB`, E `#5577A8`):

**T — Tune in** · *Map the narrative ocean before you make waves. Who already holds the audience's heart — which shows, artists, leagues, fandoms? Where is climate already present, absent, or distorted?*
- Commission a narrative audit (the 2.8% stat exists because someone funded the counting)
- Listen to fandoms, not just focus groups
- Find the whitespace — silence is your map

**I — Immerse** · *Don't make climate content. Make the content people already love climate-fluent. Embed scientists in writers' rooms, retrofit the tour, write the storyline — never the lecture.*
- Fund expertise pipelines into creative rooms (the Green Screen model)
- Back transitional characters, not perfect heroes
- Let the plot carry the planet — stakes, not statistics

**D — Distribute** · *One story is a ripple; synchronized stories are a tide. Coordinate across rival properties, platforms, and borders — and design every moment for the second screen.*
- Anchor to calendar moments (COP, climate weeks, heat seasons)
- Give the internet a phrase to carry ("Just Look Up")
- Treat fandoms as distribution infrastructure

**E — Evaluate** · *Measure narrative change, not impressions. Did salience move? Did conversation move? Did the policy window move? Publish what you learn so the whole field compounds.*
- Pre/post audience studies, not vanity reach
- Track "story spillover" into news & social discourse
- Independent verification beats self-reporting (see: Coldplay × MIT)

### 03 — The case files (mist)
- Kicker: `03 — The case files`
- Headline: **Nine plays that already worked.**
- Lede: *Filter by medium. Open a card for the story, the strategic move, the receipts, and the **steal-this** takeaway you can run in your own portfolio.*
- Filter chips: `All plays` `TV & Film` `Soaps & Serials` `Music & Live` `Gaming` `Sport` `Fandom`

The 9 accordion cards (each has tag · title · hook · The story · The move · The receipts · **Steal this**). Filter categories in brackets:

1. **[tv]** Tag `TV & Film · US` — **Grey's Anatomy: the heat dome comes to Grey Sloan** — hook: *19 seasons of trust, one deadly heat wave — and not a lecture in sight.*
   - Story: Season 21 midseason finale hit Seattle with a deadly heat dome modeled on the real 2021 Pacific Northwest event — climate as triage, not an "issue episode."
   - Move: **Embed expertise, not messaging.** Green Screen (co-founded by the CAA Foundation) connected the writers' room with climate-health experts so the science was load-bearing.
   - Receipts: Major press, strong audience response, a recurring climate thread institutionalized inside one of the most-watched dramas on Earth.
   - Steal this: Fund the connective tissue — expert-to-writers'-room pipelines — rather than commissioning "climate shows." Trust travels through characters audiences already love.

2. **[serial]** Tag `Soaps & Serials · UK` — **The great British soap crossover, COP26 week** — hook: *Seven rival soaps. One synchronized climate week. A first in TV history.*
   - Story: The week COP26 opened (Nov 2021), EastEnders, Coronation Street, Emmerdale, Hollyoaks, Casualty, Doctors and Holby City all wove in climate — and crossed characters between rival shows for the first time ever.
   - Move: **Synchronize the tide.** Months of quiet coordination between competing teams (sparked by Emmerdale's Jane Hudson) turned seven ripples into one national moment.
   - Receipts: Climate reached tens of millions of British living rooms in a single week, timed to the global policy spotlight.
   - Steal this: Philanthropy is the natural neutral convener of rivals. Fund the backstage coordination no single broadcaster can lead — anchor it to a climate week.

3. **[serial]** Tag `Soaps & Serials · Global South` — **Telenovelas & the Sabido method** — hook: *The 50-year-old proof that serial drama changes behavior at national scale.*
   - Story: 1970s Mexico, producer Miguel Sabido engineered telenovelas around "transitional characters" — flawed people who wrestle toward change. Adapted by Population Media Center across dozens of countries.
   - Move: **Long-arc transformation beats the PSA.** Audiences lean in when a character they recognize slowly changes.
   - Receipts: Five decades of evaluated, replicated behavior change across continents.
   - Steal this: Fund the *transitional character* — the skeptic-becoming-advocate. And budget for evaluation from day one.

4. **[tv fandom]** Tag `TV & Film · Global` — **Don't Look Up and the second screen** — hook: *A comet allegory that handed the internet a four-word climate vocabulary.*
   - Story: Adam McKay's satire never says "decarbonize" — it made denial the villain and became one of Netflix's most-watched films ever.
   - Move: **Design for the conversation, not just the screen.** "Just Look Up" became instant activist shorthand.
   - Receipts: A record-scale global discourse moment — op-eds, scientist explainers, weeks of social conversation.
   - Steal this: Every funded story needs a *portable phrase*. Budget for the discourse layer before launch.

5. **[tv fandom]** Tag `TV & Film · Korea` — **K-drama's climate whitespace — and the fans filling it** — hook: *90% of Koreans call climate a crisis. Their dramas give it 0.36% of screen time.*
   - Story: 60 K-dramas (2019–24) showed climate in just 4 of 1,135 viewing hours. Meanwhile Kpop4Planet mobilized fans worldwide and idols carried climate messages to COP26.
   - Move: **Measure the silence, then fund both sides of it.** The gap between ~90% concern and 0.36% screen time is a quantified opportunity.
   - Receipts: Kpop4Planet campaigns have won concrete commitments from major platforms — fan power converted to corporate policy.
   - Steal this: Fund the audit that makes the whitespace undeniable, then back fandom-led campaigns as a parallel channel.

6. **[music]** Tag `Music & Live · Global` — **Coldplay: the tour that made the solution the spectacle** — hook: *A 59% emissions cut, verified by MIT — powered partly by dancing fans.*
   - Story: Coldplay pledged a 50% cut vs their last tour, hit 59%, verified by MIT's Environmental Solutions Initiative with no offsets. Kinetic dance floors and power bikes let the crowd generate the encore; 7M+ trees planted.
   - Move: **Turn infrastructure into narrative.** The audience *is* the clean energy — embodied, communal, independently verified.
   - Receipts: Published, third-party-checked emissions reporting reset expectations for the live-events industry.
   - Steal this: Fund the verification layer — exactly the kind of unglamorous cost philanthropy is built to cover.

7. **[music]** Tag `Music & Live · London` — **Billie Eilish's Overheated at The O2** — hook: *Six arena nights in London, converted into a climate summit for fans.*
   - Story: June 2022, during her six-night O2 residency, Eilish — with REVERB, Support+Feed and the venue — staged *Overheated*: a multi-day public climate event with plant-based catering. Since traveled to Atlanta and Berlin.
   - Move: **Convert tour stops into civic moments.** The artist as convener; fans arrive for music, leave inside a climate community.
   - Receipts: A replicable city-by-city format; her touring practice earned TIME100 Climate recognition.
   - Steal this: Map the next 12 months of major tours through your priority cities and fund the civic wrapper. The audience is already coming.

8. **[gaming]** Tag `Gaming · Global` — **Playing for the Planet: climate inside 3 billion screens** — hook: *The biggest entertainment medium on Earth, organized through play itself.*
   - Story: The UN-facilitated Playing for the Planet Alliance enlists studios; annual Green Game Jams reach hundreds of millions with in-game forests, restoration mechanics, tree-planting tie-ins.
   - Move: **Stakes in the mechanics, not the cutscene.** Games persuade through agency — players protect what they build.
   - Receipts: Hundreds of millions of activations per jam, studio decarbonization commitments, a standing alliance.
   - Steal this: Gaming is the most underfunded channel relative to reach. Fund jam prizes, design toolkits, and in-game→real-world action bridges.

9. **[sport]** Tag `Sport · UK` — **Forest Green Rovers: the greenest club in the world** — hook: *A tiny football club that made sustainability its entire identity — and went global.*
   - Story: A small Gloucestershire club became the world's first UN-certified carbon-neutral football club — vegan matchday food, organic pitch, renewable energy, recycled/plant-based kits.
   - Move: **Total identity, not sponsorship.** Sport's tribal loyalty becomes the carrier wave.
   - Receipts: A global press footprint wildly disproportionate to club size; a template the sports industry now studies.
   - Steal this: In sport, fund the *first mover* in each league or country — one fully-committed club reshapes what fans expect.

### 04 — Play Builder (navy)
- Kicker: `04 — Make it yours`
- Headline: **Build your opening play.**
- Lede: *Pick a medium and a goal. The builder drafts a starter play — grounded in the case files above — that you can copy into your notes and pressure-test in the working session.*
- Empty state: *Your play will wash up here.*
- Buttons: `Deal the play`, `Copy play to clipboard`
- **Logic & data:** see Section 3.

### 05 — In the room (white)
- Kicker: `05 — In the room`
- Headline: **Bring this to London.**
- Lede: *A suggested 90-minute working-session arc for funders and partners during Climate Week — designed to leave the room with named plays, not nodding agreement.*
- Agenda (time · title · description):
  - **0:00 — Tune in — the whitespace map** · Walk the stats above. Where is climate absent in the media your grantees' audiences love most? Name three silences.
  - **0:20 — Case sprint — steal in pairs** · Each pair takes one case file and answers: what would this look like in *our* portfolio, region, or language? Two minutes to pitch back.
  - **0:50 — Deal the plays** · Run the play builder live for each funder's priority audience. Argue with the card. Improve it. The argument is the strategy.
  - **1:15 — Commit — one tide, one date** · Choose one synchronized moment in the next 12 months and one play each funder will move toward it. Name owners before leaving the room.
- Provocations box (slate teal) — heading **Provocations for the pub afterwards**:
  - If 97% of stories ignore climate, is funding one more documentary the highest-leverage pound we can spend?
  - The UK soap crossover took a producer with an idea and months of backstage diplomacy. Who plays that role in your region — and who pays for it?
  - What is climate philanthropy's "Just Look Up" — the phrase we want strangers arguing about next year?

### Footer (navy)
- Brand: **Blue Crab Strategies** (with crab mark)
- Ethos: *Meeting the planet's messiest problems with the collective power of people.*
- **Receipts & further reading** (links open in new tab):
  - Good Energy × USC Norman Lear Center — climate silence in TV & film → `https://www.goodenergystories.com/playbook/research-findings-climate-silence-in-tv-and-film`
  - THR — anatomy of a Grey's Anatomy climate episode → `https://www.hollywoodreporter.com/tv/tv-features/green-screen-climate-crisis-greys-anatomy-heat-wave-1236196669/`
  - ITV — the COP26 soap crossover → `https://www.itv.com/news/2021-11-01/coronation-street-and-emmerdale-stars-on-new-stories-highlighting-climate-change`
  - IJoC — climate representation in 60 K-dramas → `https://ijoc.org/index.php/ijoc/article/view/24684`
  - Coldplay — Music of the Spheres sustainability reporting → `https://sustainability.coldplay.com/`
  - REVERB — Billie Eilish tour impact & Overheated → `https://reverb.org/impact_report/happier-than-ever-world-tour-impact-report/`
- Fine print: *A working draft for the London Climate Week session · Built with salt water and stubborn optimism.*

---

## 3. The Play Builder logic (give Canvas this verbatim)

The builder composes a play from a **Medium × Goal** pair. Provide Gemini these two data
objects and the compose rules.

**Medium dropdown options** (`value`: label):
`scripted`: Scripted TV & Film · `serial`: Soaps & Serial Drama · `music`: Music & Live Events ·
`gaming`: Gaming & Interactive · `sport`: Sport & Fandom · `creator`: Creators & Social

**Goal dropdown options:**
`normalize`: Normalize climate in everyday story · `mobilize`: Mobilize a specific audience ·
`window`: Shift a policy window · `localize`: Localize a global narrative

**Each Medium carries:** a `title`, a `summary`, three `moves`, a `metric`, and a `precedent`:

- **scripted → "The Writers' Room Pipeline"** — Summary: *Place vetted climate-domain experts (health, insurance, food, migration) inside the writers' rooms of returning shows your audiences already trust, so climate shows up as plot pressure, not message.* Moves: (1) Identify 3 returning shows your priority audience over-indexes on; map current climate presence (usually near zero — only 2.8% of scripts mention climate at all). (2) Fund a broker org (Green Screen / Good Energy model) to match each show with one domain expert on retainer, not a one-off consult. (3) Pre-negotiate a discourse plan: clips, creator reactions and explainers ready for the night the episode airs. Metric: *Climate-keyword presence in next-season scripts of target shows, plus pre/post audience salience polling.* Precedent: *Grey's Anatomy's heat-dome arc, built with Green Screen / CAA Foundation science advisers.*

- **serial → "The Synchronized Storyline"** — Summary: *Convene rival soaps and serials around one shared climate week of storylines — coordinated backstage, aired simultaneously, anchored to a real policy moment.* Moves: (1) Hire the convener: one trusted producer-diplomat to run months of quiet coordination across rival editorial teams (the Jane Hudson role). (2) Anchor the week to a calendar moment — a COP, a climate week, the start of heat season. (3) Write transitional characters, not heroes: a sceptic moving one believable step (the Sabido method's 50-year evidence base). Metric: *Combined reach of the synchronized week, story spillover into news/social, and audience attitude shift in serial-viewer panels.* Precedent: *The 2021 COP26 week, when EastEnders, Coronation Street, Emmerdale, Hollyoaks, Casualty, Doctors and Holby City crossed characters for the first time ever.*

- **music → "The Civic Tour Stop"** — Summary: *Ride existing tours — fund the civic wrapper (local activists on the bill, plant-based catering, action booths, verified green ops) that converts arena nights into climate moments city by city.* Moves: (1) Map the next 12 months of major tours through your priority cities and rank by audience fit. (2) Offer artists a turnkey civic package: local partners, venue greening, fan action layer — zero extra lift for the tour. (3) Fund independent verification of the tour's footprint; the verified number IS the story. Metric: *Fan actions taken per stop, earned media on the verified footprint, and partner orgs' local sign-ups.* Precedent: *Billie Eilish's Overheated at The O2 in London; Coldplay's Music of the Spheres tour, 59% emissions cut verified by MIT with no offsets counted.*

- **gaming → "The Mechanics Play"** — Summary: *Put climate stakes inside gameplay — restoration mechanics, in-game events, jam prizes — where 3B+ players protect what they build, instead of watching cutscene messages.* Moves: (1) Sponsor a Green Game Jam track or prize aimed at studios whose players match your audience. (2) Fund a climate design toolkit so mid-size studios can ship restoration/resilience mechanics without research overhead. (3) Build the bridge: every in-game act pairs with one real-world act (tree planted, pledge, local event). Metric: *Player activations, in-game-to-real-world conversion rate, and number of studios shipping climate mechanics.* Precedent: *UNEP's Playing for the Planet Alliance and its Green Game Jams, reaching hundreds of millions of players with in-game activations.*

- **sport → "The First Mover Club"** — Summary: *Make one club, team or athlete in each league the total-identity sustainability flagship — and let tribal rivalry do the distribution.* Moves: (1) Pick the league/country and find the willing first mover (often a smaller, hungrier club). (2) Fund the full identity shift — energy, food, kit, pitch — not a sponsorship patch. (3) Arm the fandom: chants, banter, derby-day content that makes sustainability a point of pride. Metric: *Share of league media conversation, copycat commitments by rival clubs, and fan-community growth beyond the home region.* Precedent: *Forest Green Rovers, the world's first UN-certified carbon-neutral football club — global fanbase, outsized media footprint.*

- **creator → "The Portable Phrase"** — Summary: *Seed one sticky, argument-starting phrase (the 'Just Look Up' play) through creators your audience actually follows — then fund the discourse layer that keeps it alive.* Moves: (1) Workshop 3 candidate phrases with creators and fandom insiders — test for remixability, not approval ratings. (2) Brief 20 mid-size creators across niches (gaming, beauty, sport, finance) to carry it natively — no scripts. (3) Stand up a rapid-response desk to feed the conversation while it's alive: stitches, duets, explainers, counter-memes. Metric: *Organic (unpaid) usage of the phrase by strangers, share of voice in climate conversation, and fandom-led actions triggered.* Precedent: *Don't Look Up's 'Just Look Up' becoming protest-sign shorthand; Kpop4Planet converting fandom into corporate-policy wins.*

**Each Goal modifies the play:**

- **normalize** — append to summary: *" Aim for presence, not prominence: climate as believable background pressure in stories about love, work and family."* · **Replace move #3** with: *"Set a 'background presence' quota with partners: heat pumps, floods, induction hobs, green jobs appearing without comment — normal life, on screen."* · Prefix metric with: *"Narrative-presence audit year over year (the 2.8% baseline is your scoreboard) — plus: "*
- **mobilize** — append to summary: *" Every story moment lands with a single, low-friction next action for one named audience."* · **Add a 4th move:** *"Define ONE audience and ONE action before any creative is funded; reject plays that can't name both."* · Prefix metric: *"Actions completed by the named audience (sign-ups, pledges, turnout) — plus: "*
- **window** — append to summary: *" Time everything to a live policy moment so culture and politics peak together."* · **Add a 4th move:** *"Reverse-engineer the calendar: schedule the cultural peak 2–3 weeks before the policy decision, when coverage is hungriest (the COP26 soap-week timing)."* · Prefix metric: *"Policymaker citations, press linking the story to the policy moment, polling movement in the decision window — plus: "*
- **localize** — append to summary: *" Translate the play into local formats, languages and trusted faces — adaptation, not dubbing."* · **Add a 4th move:** *"Pair every global property with a local creative owner who can veto anything that doesn't ring true (the Population Media Center adaptation model)."* · Prefix metric: *"Local-language reach and locally-produced derivative works — plus: "*

**Compose rules:**
1. `summary = medium.summary + goal.summaryAppend`
2. `moves = medium.moves`; if the goal has `replaceMove3`, replace index 2; else push the goal's `extraMove`.
3. `metric = goal.metricPrefix + (medium.metric with first letter lowercased)`
4. Card header reads: `OPENING PLAY · {Medium label} × {Goal label}` then the title.
5. Render sections: **The play** (summary), **First three moves** (numbered list), **What you measure** (metric), and a `Precedent:` footer line.
6. "Copy" produces a plain-text version (meta, title, blank, `THE PLAY` + summary, `FIRST MOVES` numbered, `WHAT YOU MEASURE` + metric, `Precedent: …`).

---

## 4. Design system reference

### Type
- **Display/headings/UI/numbers:** Rajdhani — H1 `clamp(3rem,7.5vw,6rem)`, H2 `clamp(2.1rem,4.5vw,3.6rem)`, weight 700, line-height ~1.1, letter-spacing `0.01em`.
- **Body:** Inter, 16px base, line-height 1.65, color `#46536A`.
- **Kickers:** Rajdhani, 14px, weight 600, `letter-spacing:0.22em`, uppercase, slate-deep color.
- **No italics in headings** — emphasis (`<em>`) is rendered upright in slate-deep `#3F6E7A`.

### Color blocks (full-bleed section backgrounds)
| Section | Background | Text |
|---|---|---|
| Hero, TIDE, Session | white `#FFFFFF` | navy headings, body grey |
| 01 Why, Play Builder, Footer | navy `#27396B` | white headings, `rgba(255,255,255,.78)` body |
| Case files | mist `#F4F6F8` | navy headings |
| Builder panel | deep navy `#1E2D55` | — |
| Provocations box | slate teal `#74A0AB` | white |

### Components
- **Buttons:** pill (`border-radius:999px`), uppercase, Rajdhani 700, `padding:14px 30px`. Primary = navy fill / white text; ghost = navy border. On navy sections they invert to white fill.
- **Cards:** white, `1px solid #E1E6ED`, `border-radius:12–14px`. TIDE cards get a `4px` top border in the card's accent color and lift on hover.
- **Stat grid:** 4 columns sharing a 1px hairline gutter (use a `rgba(255,255,255,.22)` grid background showing through `gap:1px`), `border-radius:14px`. Responsive: 4 → 2 (≤900px) → 1 (≤560px).
- **Accordion:** native `<details>/<summary>`; hide the default marker; a circular `+` toggle that rotates 45° when open (`details[open] .case-toggle{transform:rotate(45deg)}`). "Steal this" box = dashed slate border, faint slate-teal fill, with an inline navy "STEAL THIS" pill label.
- **Marquee:** navy strip, Rajdhani 13px uppercase, content duplicated in markup and translated `-50%` over 40s linear infinite. `◆` separators in slate, smaller.
- **Hero waves:** 3 absolutely-positioned blurred (`filter:blur(60px)`) slate-tinted blobs drifting via a slow `translateX/rotate` keyframe alternate.

### Crab line-mark (inline SVG — use for nav, hero, footer, favicon)
```svg
<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round">
  <path d="M28 9C17 13 11 24 14 35C22 31 27 21 28 9Z"/>
  <path d="M36 9C47 13 53 24 50 35C42 31 37 21 36 9Z"/>
  <path d="M14 35C15 47 23 53 32 53C41 53 49 47 50 35"/>
  <path d="M8 56C16 43 24 41 32 41C40 41 48 43 56 56"/>
</svg>
```
Favicon: same SVG as a data-URI with stroke `#27396B`.

### Motion & accessibility
- **Scroll reveal:** elements start `opacity:0; translateY(24px)`, gain `.is-visible` via IntersectionObserver (threshold 0.15). Guard behind a `js` class added to `<html>` so content stays visible without JS.
- **Stat count-up:** ease-out cubic over ~1.4s, triggered when the stat scrolls in; decimals keep one place, suffix appended (`%`, `B+`).
- **Single-open accordion:** opening one card closes the others (`toggle` listener).
- **`prefers-reduced-motion`:** disable waves, marquee, deal-in animation, reveal transitions; render stats at final value.
- **Print stylesheet:** flatten navy/slate blocks to white, hide nav/marquee/waves/builder controls, force open `<details>` bodies, `break-inside:avoid` on cards — turns the page into a session handout.

---

## 5. Refinement prompts (use one per turn after the first build)

1. *"Load Rajdhani (500/600/700) and Inter from Google Fonts. Use Rajdhani for all headings, buttons, kickers, numbers; Inter for body. Headings have no italics — render `<em>` upright in slate `#3F6E7A`."*
2. *"Make the four stat numbers count up from 0 with an ease-out over ~1.4s, triggered when each scrolls into view. Keep one decimal place and the suffixes (2.8%, 0.6%, 90%, 3B+)."*
3. *"Turn the case studies into native `<details>` accordion cards with a circular + toggle that rotates 45° when open. Only one open at a time. Add the filter chips that show/hide cards by `data-cat`."*
4. *"Add the play builder: two dropdowns and a 'Deal the play' button that composes a play from this data [paste Section 3]. Add a 'Copy play to clipboard' button that copies a plain-text version."*
5. *"Add the navy scrolling marquee under the hero (duplicate the content and translate -50% over 40s). Add three soft blurred drifting wave blobs behind the hero."*
6. *"Add scroll-reveal fade-up on every section, guarded behind a `js` class so it degrades gracefully. Respect `prefers-reduced-motion` everywhere."*
7. *"Add a print stylesheet: flatten the navy and slate sections to white, hide the nav, marquee, waves and builder controls, force-open the accordion bodies, and avoid breaking cards across pages."*
8. *"Make it responsive: nav links hide below 900px, the badge below 640px; stat grid goes 4→2→1 columns; TIDE cards and builder controls stack on narrow screens."*

---

## 6. Differences to expect vs. the original

- The original ships as **three files** (`index.html`, `css/styles.css`, `js/main.js`); Canvas
  will likely give you **one inline file**. Functionally identical — split it back out later if
  you want.
- Canvas may swap exact CSS techniques (e.g. grid-gap hairlines, blur values). Re-prompt with the
  Section 4 specifics if a detail matters.
- Fonts, colors, copy, the 9 case studies, and the builder logic are the load-bearing parts —
  keep those verbatim and the rebuild will read as the same site.
