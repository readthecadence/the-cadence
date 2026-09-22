# The Cadence

*Scripture, Saints, and Rites of the Measured Life.*

An invented religion of software-engineering management, played dead straight as
scripture. Kings and prophets, a godhead, nine pillars, saints and sins, grace and
redemption, heretics, rites, nineteen parables, a bestiary of demons, and a
present-day holy war. Nearly every figure is real. Roughly half the jokes require
you to have suffered through the meeting. The followers of the faith are called
the Aligned.

**The whole thing in one line.** Measure honestly, serve the aim you cannot
measure, and never mistake the number for the thing.

Why it was written, and what it is made of, is in the [Preface](PREFACE.md).

## The canon

The book lives in `chapters/`, one file per chapter, in reading order.
`the-cadence.md` is the assembled whole; it is generated, and is never edited
directly.

```
make        # assemble the book
make test   # the regression test of the canon
```

The test refuses to pass if the chapter numerals have drifted or the Contents no
longer matches the chapters beneath it. The faith calls return *the regression
test of the soul*; this is the humbler kind.

**The canon is versioned.** Doctrine is amended by commit, and every amendment is
dated, attributed and reversible — which is more than most faiths can say.

## What you may do here

- **Name a demon** the Bestiary has not yet caught.
- **Propose a parable**, if it is true and if it carries a doctrine.
- **Confess a sin** the ledger has not yet recorded.
- **Report a corruption of the text**, which is the humble and holy work.
- **Put a question to the faith**, and it will be answered from the canon or not
  at all.

See [CONTRIBUTING.md](CONTRIBUTING.md) — *On the Submission of Heresies*.

## What you may not do here

Pull requests are closed. The congregation petitions; the scribe redacts. This is
not gatekeeping but liturgy: a scripture written by committee is a style guide.

## Licence

The text is under [CC BY-NC-ND 4.0](LICENSE); the tooling is MIT. Quote it,
screenshot it, read it aloud at standup. Do not sell it and do not rewrite it.
