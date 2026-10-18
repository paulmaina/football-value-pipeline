# Closing odds provider alerts

The collector retains `football_output_v2/closing_odds/provider_status.json`
independently of per-poll `collector_status.json`. Idle checks do not clear a
failure. A successful live response records recovery and retains the last
failure for diagnosis. Provider availability does not imply usable market quotes.

`CREDITS_EXHAUSTED` requires an explicit `OUT_OF_USAGE_CREDITS` code for every
configured credential tried. A lone HTTP 429 or a mixed exhausted/throttled
credential set is `RATE_LIMITED`, not confirmed monthly depletion. Other HTTP
failures are `HTTP_ERROR`. Only credential environment names, HTTP status,
known provider codes and numeric usage headers are persisted; response text,
request URLs and secret values are excluded. Daily attempt counters are not
provider credit balances.

A terminal provider error ends the current collection session with a nonzero
exit. Existing finalization publishes evidence and settles the reservation;
the recovery artifact also retains the provider checkpoint. The workflow emits
an error annotation and a summary even when final publication fails. API fallback
keys are still attempted before a terminal failure. No extra provider probes or
API requests are introduced for monitoring.

GitHub failed-workflow email/mobile delivery requires the user's GitHub Actions
notification settings and applicable workflow subscriptions. A failed job or
annotation alone does not prove delivery. The existing hourly Football pipeline
health watch also reads this checkpoint and recovery artifacts, deduplicates
unchanged incidents and reports new actionable failures through its existing
notification channel. It is polling, so an alert is not guaranteed immediately.

Deployment requires merging the alert fix. Already-running jobs retain their
old code; old generic RuntimeError records cannot establish historical monthly
depletion and are not retroactively relabelled.
