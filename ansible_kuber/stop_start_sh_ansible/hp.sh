#!/bin/bash

# Get today's date in YYYYMMDD format
DATE=$(date +%Y%m%d)
DIR="/tmp/demo_$DATE"

case "$1" in
    start)
        if [ ! -d "$DIR" ]; then
            mkdir -p "$DIR"
            echo "Directory $DIR created."
        else
            echo "Directory $DIR already exists."
        fi
        ;;
    stop)
        if [ -d "$DIR" ]; then
            rm -rf "$DIR"
            echo "Directory $DIR deleted."
        else
            echo "Directory $DIR does not exist."
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
esac
