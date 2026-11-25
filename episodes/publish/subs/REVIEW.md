# Ep. 002 subtitles — independent review

You review a translation someone else made. The goal is subtitles a native viewer finds flawless and that say exactly what the English says. Read RULES.md first (the translator's rules).

## Method, per language
1. **Blind back-translation first.** Open only `<code>.json` (not source.json yet). Translate every cue back into English, literally but readably, and write it to `review/<code>.back.json` as `[{"id":…, "back":"…"}]`. Do not look at the English while doing this.
2. **Compare.** Now open `source.json` and compare each back-translation with `en`. Look for: meaning changes, anything added or dropped, a hedge or attribution softened or strengthened ("Bitget says", "according to one analysis", "lean the same way", "may have been", "for now", "the reports don't say"), wrong subject/object (who did what to whom), wrong number/date/time value, tense errors, a name changed.
3. **Native read.** Read `<code>.json` top to bottom as a native subtitle editor: grammar, agreement, punctuation, natural word order, idiomatic phrasing for a calm documentary, consistent terminology and form of address, sentences split across two cues reading naturally. Rewrite anything awkward, calqued or unnatural, staying within RULES.md.
4. **Fix in place** in `<code>.json` (keep ids/order, one string per cue, no line breaks). Then run `python3 /home/claude/siphon-ep002/scripts/build_subs_ep002.py <code>`: 0 hard errors required; reduce soft warnings where a shorter natural wording exists. Check every "number note" value by hand.
5. **Report** in `review/<code>.md`: every change you made (id, before → after, why), grouped as meaning / grammar / style / terminology, plus anything you are still unsure about.

## Clarifications from the producer (apply to every language)
- **Natural grammar beats digit matching.** The checker no longer forces digits: write Arabic dual forms (ساعتين), "tháng 9" in Vietnamese, local number words, as a native writer would. Values must stay identical. Clock times stay 19:05 (they match the graphics on screen).
- **53** "Mandiant dates the attacker's privileged access only to 24 September" = Mandiant's report puts the attacker's privileged access no earlier than 24 September (it does not confirm the 31 August date the other report gives). The next cue says the two reports haven't been reconciled.
- **84** = the system simply believed the requester when it said the checks had passed.
- **109** "the wrong switch" = blocking customer withdrawals was the wrong lever to pull (it did not stop the attacker's requests).
- **116** = for 2 hours and 39 minutes after the first alert (the signing service kept running).
- **124** "Covering tracks, or going for more." = maybe to cover their tracks, maybe to steal more; next cue: the reports don't say.
- **138** "about 1,000 pieces of coin" = each transfer combined about 1,000 small separate coin pieces (inputs); make it understandable, e.g. "about 1,000 small pieces of coin".
- **172** TraderTraitor is the FBI's name for a North Korean hacking group.
- **173 / 180** keep the full meaning: no government has said anything / named anyone (for Bitget).
- **186** "Still less than before." = the protection fund is still smaller than it was before the hack.
- **197** "I'm Thomas Archer. This was Siphon Files." — the narrator's sign-off; a conventional local sign-off is fine.

Do not commit to git; do not touch other languages' files.
