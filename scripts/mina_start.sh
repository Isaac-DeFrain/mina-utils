#!/bin/bash

systemctl --user daemon-reload
systemctl --user start mina
systemctl --user enable mina
sudo loginctl enable-linger
mina daemon --peer-list-url https://storage.googleapis.com/mina-seed-lists/mainnet_seeds.txt
