"""The Absurd Clause Contest entry.

Writes one original English sentence, phrased as a clause buried deep
inside a terms-of-service agreement, to /output/entry.txt.
Deterministic, standard library only, no network access.

The clause: a dispute-resolution clause that sounds like real
legal boilerplate until the absurdity hits -- disputes are settled
by arm wrestling, and the loser pays the winner's legal fees in
sandwiches. A concrete absurd image, one clean sentence, no
explaining of its own joke.

Draft (v1, 200 chars):
  "Any dispute arising under these Terms shall be settled by
  single-elimination arm wrestling in our office car park on the
  first Tuesday of March, the loser paying the winner's legal fees
  in sandwiches."

Revision (v2, 193 chars -- genuine improvement, not a no-op):
  - "arising under these Terms" -> "under these Terms, including
    this clause": the clause now covers disputes about itself, a
    self-referential legal joke that deepens both the boilerplate
    voice and the absurdity.
  - "office car park" -> "parking lot": consistent US terms-of-
    service register instead of mixed British/American wording.
  - "single-elimination" dropped: the tournament detail cost 19
    characters and the arm-wrestling image lands without it; the
    freed room pays for the self-reference above.
  Final (193 chars), verified byte-identical across two runs.
"""

import os

CLAUSE = (
    "Any dispute under these Terms, including this clause, shall be "
    "settled by arm wrestling in our parking lot on the first Tuesday "
    "in March, the loser paying the winner's legal fees in sandwiches."
)


def main() -> None:
    if not 1 <= len(CLAUSE) <= 200:
        raise ValueError("clause must be 1-200 characters")
    if CLAUSE.count(".") != 1:
        raise ValueError("clause must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
