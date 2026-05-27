# BUILD_LOG.md

## AI Workflow

The agentic workflow let me ship a working flashcard app in
a fraction of the time it would have taken alone. Things like
setting up Flask routes, creating HTML templates, and wiring
up the study view would have taken me hours to figure out
from scratch. With Claude Code handling the implementation,
I could focus on whether the feature actually worked the way
I wanted.

I had to override Claude several times. The biggest moment
was when it tried to add a database for storing flashcards
when I specifically said to use a simple list of dicts. I
caught it in plan mode and redirected it before it wrote
any code. That's something only I could catch because I
knew the constraint mattered for keeping the project simple.

This project revealed that my biggest knowledge gap is
understanding how web apps actually work under the hood.
I could verify that things worked in the browser, but
sometimes I didn't fully understand why the code worked.
That's something I need to keep building — being able to
read and understand the code Claude writes, not just verify
it runs. I also learned that writing good briefs upfront
saves a lot of back and forth later.

On day one of my internship I'll start by understanding
the team's existing CLAUDE.md or coding conventions before
I touch anything. Then I'll decompose whatever task I'm
given into small verifiable steps before opening Claude
Code. The habit of plan first, verify after is the thing
I'll bring with me.
