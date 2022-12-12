#!/bin/bash

mina-archive run \
  --postgres-uri postgres://localhost:5432/archive \
  --server-port 3086
