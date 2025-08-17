# freeplane-to-md

Convert Freeplane/Freemind mind maps to Markdown.

Will read the file provided and print out Markdown to `STDOUT`.

The mind map will be treated as a hierarchy and the output will just be a deeply
nested unordered list.

The first `--heading_levels` will get a heading format inside the lists. \
After that, it will be just plain text and hyperlinks.

# Installation on macOS

I highly recommend using a virtual environment so you only install the
dependencies in a local environment, not the global system.

I'm using `uv` to create a virtual environment and install the dependencies:

    uv venv create
    uv pip install -r requirements.txt

# Usage

    ./freeplane_to_md.py file.mm

See `--help` for options.

For larger mind maps, I first export individual branches into separate MM
files, and then convert those.