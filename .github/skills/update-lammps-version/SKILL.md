---
name: update-lammps-version
description: Update the LAMMPS version used by njzjz/lammps-wheel. Use when the user asks to bump the packaged upstream LAMMPS release, references an upstream LAMMPS commit/tag, or says the wheel repo can be updated to a newer stable version.
license: MIT
metadata:
  author: njzjz-bot
  version: '1.0'
---

# Update LAMMPS Version

This skill is for version bumps in `njzjz/lammps-wheel`.

## What to change

The version pin lives in `pyproject.toml` under `tool.scikit-build.cmake.args`:

```toml
"-D LAMMPS_VERSION=stable_22Jul2025_update4"
```

For normal bumps, this is usually the only file that changes.

## When this skill applies

Use it when the user:

- says `lammps-wheel` can be updated
- shares an upstream LAMMPS commit, PR, or tag that bumps the release
- asks to sync the wheel package to a newer upstream stable release

## Workflow

1. Read `pyproject.toml` and record the current `LAMMPS_VERSION`.
2. Determine the target version:
   - If the user provided an upstream commit/PR/tag, inspect that first and prefer the exact version referenced there.
   - Otherwise, check the latest upstream `stable_*` tag from `lammps/lammps`.
3. If the target version is newer than the current one, update only the `LAMMPS_VERSION` entry in `pyproject.toml`.
4. Review the diff to confirm the bump is minimal.
5. Commit on a fresh branch and open a PR from the bot fork.

## Useful checks

### Find the current pinned version

```bash
grep -n 'LAMMPS_VERSION=' pyproject.toml
```

### Inspect a user-provided upstream commit

```bash
git show <commit> -- pyproject.toml
```

If the upstream change already contains the desired new tag, copy that exact tag.

### List upstream stable tags

```bash
git ls-remote --tags https://github.com/lammps/lammps.git 'refs/tags/stable_*'
```

Prefer the newest stable tag, but sanity-check the naming instead of blindly trusting lexical order.

## Editing rule

Do not rewrite unrelated build settings. For a routine release bump, keep the change scoped to the single `LAMMPS_VERSION` line unless the user explicitly asks for more.

## Validation

Before opening the PR:

- run `git diff -- pyproject.toml`
- make sure the diff is only the expected version bump
- mention the old and new versions in the PR body

## Suggested branch / PR shape

- Branch: `openclaw/update-lammps-<target-version>`
- Commit: `build(lammps): bump upstream stable tag to <target-version>`

PR body should briefly cover:

- current pinned version
- new pinned version
- where the target came from (upstream commit/tag)

## Notes

- `lammps-wheel` tracks upstream LAMMPS stable tags, not PyPI versions.
- If the current branch already contains unrelated commits, rebuild the branch from the upstream default branch before opening the PR.
