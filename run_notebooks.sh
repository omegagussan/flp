#!/usr/bin/env bash

docker run -it -v "$PWD"/src:/home/app/src:ro -v "$PWD"/data:/home/app/data -v "$PWD"/notebooks:/home/app/notebooks -v /tmp:/tmp -p 8888:8888 --rm --name run-fpl-notebook flp bash -c "jupyter notebook --ip 0.0.0.0 --notebook-dir /home/app/notebooks --allow-root"