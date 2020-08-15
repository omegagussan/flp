#!/usr/bin/env bash

docker run -it -v "$PWD"/src:/home/app/src:ro -v "$PWD"/data:/home/app/data --rm --name run-fpl-shell flp bash