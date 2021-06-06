#!/bin/sh

gpg --pinentry-mode=loopback -dv --passphrase "$FILES_PASSPHRASE" \
    -vo tests/files.tar tests/files.enc

ls -R

tar -xvf tests/files.tar -C tests/
