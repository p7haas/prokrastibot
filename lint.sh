pylint -d 'import-error' --const-rgx='[a-z_][a-z0-9_]{2,30}$' brain.py config.py groupme.py procrastibot.py > pylint.out