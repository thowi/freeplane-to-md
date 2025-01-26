#!/usr/bin/env bash

PYENV_NAME="freeplane-to-md"

# Initialize and activate pyenv if available.
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  if ! pyenv virtualenvs --bare | grep -q "$PYENV_NAME"; then
    pyenv virtualenv "$PYENV_NAME" || exit 1
  fi
  pyenv activate "$PYENV_NAME" || exit 1
  pip install freeplane-io mdutils || exit 1
fi

./freeplane_to_md.py "$@"

# Deactivate pyenv if available.
if command -v pyenv 1>/dev/null 2>&1; then
  pyenv deactivate
fi
