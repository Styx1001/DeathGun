#!/bin/bash

if [ "$(whoami)" = "root" ] || [[ "$(whoami)" = *"u0"* ]]; then
    echo "Installing Tyfe..."
    apt-get install python3 -y &> /dev/null
    apt-get install python -y &> /dev/null
    apt-get install python3-pip -y &> /dev/null
    apt-get install python-pip -y &> /dev/null
    apt-get install nano -y &> /dev/null
    rm -rf /etc/tyfe/
    mkdir /etc/tyfe/
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    cp -r $SCRIPT_DIR/Tyfe/* /etc/tyfe/
    cp $SCRIPT_DIR/Tyfe/tyfe /usr/bin/
    cd /etc/tyfe/
    pip3 install -r requirements.txt &> /dev/null
    printf "Done!\n\n"
else
    echo "Failed to execute: root permission needed"
fi
