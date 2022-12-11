#!/bin/bash

echo "Enter wallet name: "
read wallet
sec_path="$(pwd)/../secrets"
sudo chmod 700 $sec_path
MINA_PRIVKEY_PASS="$(cat $sec_path/$wallet.pwd)"
export MINA_PRIVKEY_PASS
echo "MINA_PRIVKEY_PASS set!"
sudo chmod 600 $sec_path
