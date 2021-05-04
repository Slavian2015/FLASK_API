#!/bin/bash


DATA_DIR=/usr/local/WB/data

if [ "$(ls -A $DATA_DIR)" ]; then
    echo "Take action $DATA_DIR is not Empty. Data already parsed. Skipping..."
else
    echo "Init hist files..."
    python /usr/local/WB/dashboard/database_setup.py
    echo "done"
fi
echo ready
tail -f /dev/null