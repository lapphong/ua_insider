PY ?= /private/var/folders/7h/z4fmlq_j0rj59jbzkbht6y880000gn/T/opencode/venv3/bin/python

# build + kiem so lieu + so do file + 6 muc layout. Dat = 0 loi.
ok:
	$(PY) build_html.py --check
	$(PY) scripts/browser_check.py

commit:
	sh scripts/commit.sh "$(msg)"

amend:
	sh scripts/amend.sh

push:
	git push -f
