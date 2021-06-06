#!/bin/sh

# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$FILES_PASSPHRASE" \
    -vo tests/files.tar tests/files.enc

# ls -R

tar -xvf tests/files.tar -C tests/
