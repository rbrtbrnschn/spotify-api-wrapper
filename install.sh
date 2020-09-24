#!/bin/bash
BASHRC=$(cat $HOME/.bashrc)
BOO=$( echo $BASHRC | grep dotenv)
sudo apt-get install -y curl

if [ "${#BOO}" -eq 0 ]; then
	echo "
# Setup .env
function dotenv {
	if [ -f \"\$PWD/.env\" ]; then
		for VAR in \$(cat \"\$PWD/.env\" | xargs); do
			export \$VAR
		done
	fi
}
export -f dotenv
	" >> $HOME/.bashrc
	echo "Added dotenv() to $HOME/.bashrc"
fi

echo "Please 'source $HOME/.bashrc'"
