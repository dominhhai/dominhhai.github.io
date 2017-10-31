# for dev
dev:
	@hugo server -D

# for publish
deploy:
	@hugo \
		&& cd public \
		&& minify -v -r -o . . # minify output https://github.com/tdewolff/minify/tree/master/cmd/minify#directories
		&& git add --all \
		&& git commit -m "Build on $$(date)" \
		&& git push \
		&& cd ..

# publish & push
push:
	@git add --all \
		&& git commit -m "Build on $$(date)" \
		&& git push \
		&& make deploy

# pull
pull:
	@git pull \
		&& cd public \
		&& git pull \
		&& cd ..

# add publish page
set-publish:
	@rm -rf public && mkdir public \
		&& git worktree prune \
		&& rm -rf .git/worktrees/public/ \
		&& git worktree add -B master public origin/master \
		&& rm -rf public/*
