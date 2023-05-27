# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# https://argo-cd.readthedocs.io/en/stable/operator-manual/metrics/
METRICS = {
    # General metrics
    'go_gc_duration_seconds': 'go.gc.duration.seconds',
    'go_goroutines': 'go.goroutines',
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck_hash.sys_bytes',
    'go_memstats_frees': 'go.memstats.frees',
    'go_memstats_gc_cpu_fraction': 'go.memstats.gc.cpu_fraction',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc.sys_bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap.alloc_bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap.idle_bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap.inuse_bytes',
    'go_memstats_heap_objects': 'go.memstats.heap.objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap.released_bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap.sys_bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last_gc_time.seconds',
    'go_memstats_lookups': 'go.memstats.lookups',
    'go_memstats_mallocs': 'go.memstats.mallocs',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache.inuse_bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache.sys_bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan.inuse_use',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan.sys_bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next.gc_bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other.sys_bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack.inuse_bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack.sys_bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys_bytes',
    'go_threads': 'go.threads',
    'process_cpu_seconds': 'process.cpu.seconds',
    'process_max_fds': 'process.max_fds',
    'process_open_fds': 'process.open_fds',
    'process_resident_memory_bytes': 'process.resident_memory.bytes',
    'process_start_time_seconds': 'process.start_time.seconds',
    'process_virtual_memory_bytes': 'process.virtual_memory.bytes',
    'process_virtual_memory_max_bytes': 'process.virtual_memory.max_bytes',
    'promhttp_metric_handler_requests': 'promhttp.metric_handler.requests',
    'promhttp_metric_handler_requests_in_flight': 'promhttp.metric_handler.requests_in_flight',
    # Weaviate specific metrics
    'batch_durations_ms': 'batch.durations_ms',
    'batch_delete_durations_ms': 'batch.delete.durations_ms',
    'objects_durations_ms': 'objects.durations_ms',
    'object_count': 'object_count',
    'async_operations_running': 'async.operations.running',
    'lsm_active_segments': 'lsm.active.segments',
    'lsm_bloom_filter_duration_ms': 'lsm.bloom_filter.duration_ms',
    'lsm_segment_objects': 'lsm.segment.objects',
    'lsm_segment_size': 'lsm.segment.size',
    'lsm_segment_count': 'lsm.segment.count',
    'vector_index_tombstones': 'vector.index.tombstones',
    'vector_index_tombstone_cleanup_threads': 'vector.index.tombstone.cleanup.threads',
    'vector_index_tombstone_cleaned': 'vector.index.tombstone.cleaned',
    'vector_index_operations': 'vector.index.operations',
    'vector_index_size': 'vector.index.size',
    'vector_index_maintenance_durations_ms': 'vector.index.maintenance.durations_ms',
    'vector_index_durations_ms': 'vector.index.durations_ms',
    'startup_durations_ms': 'startup.durations_ms',
    'startup_diskio_throughput': 'startup.diskio.throughput',
    'startup_progress': 'startup.progress',
    'queries_filtered_vector_durations_ms': 'queries.filtered_vector.durations_ms',
}
