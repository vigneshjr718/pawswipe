# AI Usage Reflection — PawSwipe

## What Claude wrote end-to-end
- The entire Flask backend (`app.py`) including all three API endpoints and the deduplication logic
- The seed data script (`seed.py`) with all 100 pet entries
- The swipe gesture engine (touch + mouse drag, threshold detection, fly-off animation)
- The results rendering and all four sort/filter modes

## Where I pushed back or fixed Claude's output
**Concrete example:** Claude initially suggested using `localStorage` as the primary data store with an optional sync to the server. I rejected this because the assignment explicitly required the server to be the source of truth. I re-prompted specifying `INSERT OR REPLACE` with a `UNIQUE(item_id, session_id)` constraint to handle deduplication server-side, not client-side. Claude then produced the correct SQLite schema and vote endpoint.

## One thing Claude did better than expected
The swipe gesture physics — the card tilt proportional to drag distance, the opacity ramp on the YES/NO stamps, and the fly-off animation timing — all felt natural on the first attempt with no tweaking needed.

## One thing Claude did worse than expected
Claude's first attempt at the results "Most Divisive" sort was wrong: it sorted by total vote count rather than by proximity to a 50/50 split. I had to explicitly explain the correct formula (`abs(yes_rate - 0.5)` ascending) before it produced the right implementation.

## Other AI tools used
None — Claude was used exclusively for this project.
