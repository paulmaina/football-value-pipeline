# Card research collection order

The scheduled API-Football workflow calls the research workflow before its
supplementary collector. Both jobs and manual research use the same collection
concurrency group; the outer scheduled cycle uses a distinct group to avoid a
parent/child concurrency deadlock. Ordering therefore survives Actions queue delays.
The existing provider allowance and research batch cap still apply; provider
availability and credits are never assumed or increased.

Research code remains on `research/card-bookings`, outside production. The shared
Actions cache retains event responses, progress and the completion marker. A
completed study makes no more requests; the reusable workflow stays enabled so
future supplementary cycles can call it. Cache loss or eviction can require
recollection; this change does not recover data held only on a local machine.

An incomplete batch with zero fetched responses now fails visibly with its stop
reason in the summary. Partial progress warns and retains its cache. Recovery
artifacts include hidden study paths. The supplementary collector still runs after
a research failure, preserving its publication and diagnostics.

No live provider probe is needed to validate this change. Confirm progress and
provider responses on the first scheduled cycle after deployment; merging alone
is not evidence that the exhausted provider allowance has reset.
