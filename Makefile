# The Cadence — the canon.
# chapters/ and the-cadence.md are synced from the working repo; edit them there.

CHAPTERS := $(sort $(wildcard chapters/*.md))
BOOK     := the-cadence.md

.PHONY: all test clean
all:
	@cat $(CHAPTERS) > $(BOOK)
	@echo "Built $(BOOK) from $(words $(CHAPTERS)) sections"

test: all
	@python3 tools/check.py

clean:
	@rm -f $(BOOK)
