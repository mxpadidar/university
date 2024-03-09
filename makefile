source_dir = src
virtualenv = .venv
app_module = main:app
main_branch = master

run-app:
	cd $(source_dir) && uvicorn $(app_module) --reload

update-branch:
	git checkout $(main_branch)
	git pull origin $(main_branch)
	git checkout -
	git merge $(main_branch) -m "Get latest changes from $(main_branch)"
	git push origin `git rev-parse --abbrev-ref HEAD`

new-branch:
	@read -p "Enter new branch name: " branch; \
	git checkout $(main_branch); \
	git pull origin $(main_branch); \
	git checkout -b $$branch

commit-and-push:
	@read -p "Enter commit message: " message; \
	git add .; \
	git commit -m "$$message"; \
	git push -u origin `git rev-parse --abbrev-ref HEAD`

pre-commit:
	git add .
	@pre-commit run -a

cleanup:
	@find . -type d \( -path "./$(virtualenv)" -o -path "./.data" \) -prune -o -type d -name '*cache*' \
	-exec echo Removing {} \; \
	-exec rm -rf {} +

tree:
	@$(MAKE) cleanup
	@tree -a -I "$(virtualenv)|.git|.data"

dcup:
	@docker compose up -d

dcdown:
	@docker compose down

.PHONY: run-app update-branch new-branch commit-and-push pre-commit cleanup tree dcup dcdown
