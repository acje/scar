# Jujutsu candidate stacks, not automatic acceptance

The [normative environment](ALGORITHM.html#environment), [stack scope](ALGORITHM.html#candidate-stack)
and [authority boundary](ALGORITHM.html#authority) govern. This is a documentation/config-example
workflow, not installed enforcement or a repository migration. On 2026-10-04 `command -v jj`
exited 1 on the inspected PATH; no installed version, live jj configuration or executable jj
guard, interoperability, concurrency or recovery test is established. No install/init is prescribed here.

## Exact accepted state and candidate scope

For Git-only tasks the accepted locator is `refs/heads/main`. For a Git-backed jj task,
resolve local `main` to exactly one full commit ID and require agreement with Git
`refs/heads/main`, recording the observation context. A detached Git `HEAD`, workspace
`@`, `trunk()`, change ID, bookmark spelling or remote last-seen position is not the accepted
identity. Missing/conflicted/multiple/stale observations are Unknown/Unresolved, not fallback authority.

Use a linear candidate stack A → C1 → C2 rooted at exact accepted A. Record full IDs,
sole parent IDs, trees, scoped additions/deletions and all introduced prefix changes,
including an intermediate change later canceled at the top. To accept C2 authorize both
C1 and C2; C1 approval alone permits only that exact prefix. Rewriting C1 changes its
commit ID and may rewrite descendants: refresh affected checks and authority. After
accepting C1, reconcile remaining descendants against the new accepted base. Merge or
unrelated ancestry requires separate scope/authority outside this workflow.

Snapshotting, `jj new` or `jj commit` can create/rewrite candidates without accepting
anything. jj working-copy changes are normally committed by commands, and bookmarks
can move on rewrites. Neither storage mechanics nor operation history proves review,
finite credits, protected obligations or designated authority.

Before authorized main advancement establish external writer exclusion for Git, jj,
IDE and fetch writers, re-resolve actual accepted main and recheck exact prefix/context.
Then confirm the resulting unique full main ID, Git-main agreement and exact introduced
content. Without writer exclusion no race-free acceptance claim is available; operation
reconciliation is not compare-and-swap. Failure, conflict, stale evidence or interruption
is Unresolved; preserve candidates/unrelated work and reconcile, never overwrite.
Keep the six lifecycle positions, one active task, shared precharged finite work and
protected return reserve; candidate commits add no stage or actor.

## Explicit configuration example

[jj-scar.example.toml](jj-scar.example.toml) extends the documented built-in immutable
heads with a uniquely resolved local `main`. A tracked TOML file is **not auto-loaded**.
For a separately provisioned, version-checked jj workspace, from the repository root,
the explicit invocation pattern is:

```sh
jj --config-file jj-scar.example.toml config list
jj --config-file jj-scar.example.toml log -r 'exactly(main, 1)'
```

These commands are specified, **not executed here**. Verify the selected release's
`jj help`, effective configuration and exact main resolution before adopting the example;
repeat `--config-file` on each intended invocation, not just the probe. The log output
is for inspection, not a full-ID acceptance record or authorization command. Commands
may snapshot the working copy; they are not guaranteed read-only filesystem probes.
Repository/workspace config lives outside tracked content; later config/CLI overrides
can change effective policy. `JJ_CONFIG` only replaces system/user config locations.

`immutable_heads()` protects ancestors from ordinary rewrites, not bookmark movement,
SCAR authorization, secret retention or concurrent acceptance. `--ignore-immutable`
bypasses non-root rewrite protection; redefining `immutable()` is not equivalent.
Missing/conflicted `main` is not repaired by this example. No immutable guard-bite proof
is claimed because jj is unavailable. Do not infer a hard enforcement boundary from TOML.
Git hooks and staging do not supply jj acceptance enforcement; colocated Git HEAD is
usually detached and conflicted bookmarks can disagree with Git branches.

## Scratch ownership and recovery

Before using ignored workspace-local `.scratchpad/`, record task owner, recovery/evidence
pointers and retention deadline in Beads. Keep temporary files scoped to that owner;
promote needed durable evidence into Beads descriptions before owned cleanup at close
or deadline. Interruption retains the Beads recovery record; missing files make dependent
evidence Unknown. Do not store secrets; redact durable evidence. Ignore is not untracking,
secrecy, secure erasure, backup exclusion or automatic retention enforcement. Existing
`.ooda/` remains live and unchanged; no migration/deletion is authorized by this workflow.

## Primary sources and evidence boundary

Primary latest documentation inspected in Beads `gacr-u95` on 2026-10-04; mutable latest
pages are not evidence of behavior for an installed release. Local protocol additions
(linear stack scope, accepted-main agreement, writer exclusion and scratch ownership)
are SCAR requirements, not features attributed to jj.

- [Working copy](https://docs.jj-vcs.dev/latest/working-copy/): snapshots/rewrite, ignore and already-tracked files, stale-workspace recovery.
- [Glossary](https://docs.jj-vcs.dev/latest/glossary/): commit versus change IDs, parents and rewrite.
- [Revsets](https://docs.jj-vcs.dev/latest/revsets/): full commit identity, `exactly`, `@`, `trunk()` and immutable aliases.
- [Bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/): rewrite movement, conflicts and remote last-seen targets.
- [Configuration](https://docs.jj-vcs.dev/latest/config/): explicit config loading/precedence, immutable heads and bypass.
- [CLI reference](https://docs.jj-vcs.dev/latest/cli-reference/): `--config-file`, `--ignore-immutable`, commit/new mechanics; installed `jj help` is more authoritative.
- [Operation log](https://docs.jj-vcs.dev/latest/operation-log/) and [concurrency](https://docs.jj-vcs.dev/latest/technical/concurrency/): consistent initial views and divergent-operation merging, not serialized SCAR acceptance.
- [Git compatibility](https://docs.jj-vcs.dev/latest/git-compatibility/): colocated HEAD, imports/exports, staging and hook limitations.

Packaging/unit checks validate catalogue structure and links, not these substantive
claims, command activation, runtime policy or browser/accessibility behavior.
