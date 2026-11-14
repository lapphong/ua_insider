commit:
	sh scripts/commit.sh "$(msg)"

amend:
	sh scripts/amend.sh

push:
	git push -f	
