# freeplane-to-md

Convert Freeplane mind maps to Markdown.

Will read the file provided and print out Markdown to `STDOUT`.

The mind map will be treated as a hierarchy and the output will just be a deeply
nested unordered list.

The first `--heading_levels` will get a heading format inside the lists. \
After that, it will be just plain text and hyperlinks.

# Installation on macOS

I highly recommend using a virtual environment so you only install the dependencies in a local environment, not the global system. \
On Mac, install these binaries:

    brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper

You'll need to install these dependencies in your environment:

    pip install freeplane-io mdutils

See the included `freeplane_to_md.sh` for a template to use with `pyenv`.

# Usage

    ./freeplane_to_md.sh file.mm

See `--help` for options.
