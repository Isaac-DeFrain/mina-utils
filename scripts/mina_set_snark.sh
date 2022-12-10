#!/bin/bash

if [ "$MINA_PUBLIC_KEY" = "" ]; then
    echo "Please set MINA_PUBLIC_KEY and try again"
else
    mina client set-snark-work-fee 0.1
    mina client set-snark-worker --address $MINA_PUBLIC_KEY
fi
