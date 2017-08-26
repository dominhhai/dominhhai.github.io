# for dev
dev:
	@hugo server -D

# for publish
deploy:
	@hugo \
		&& cd public \
		&& git add --all \
		&& git commit -m "Build on $$(date)" \
		&& cd .. \
		&& git push origin master

# add publish page
set-publish:
	@rm -rf public && mkdir public \
		&& git worktree prune \
		&& rm -rf .git/worktrees/public/ \
		&& git worktree add -B master public origin/master \
		&& rm -rf public/*
