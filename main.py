import os

# The excuse: speculative decoding's draft finished on time;
# the verifier (me) rejected it, so the deadline slipped.
LINE = "A draft model finished on time. I rejected its work."


def main():
    assert "\n" not in LINE and 1 <= len(LINE) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
