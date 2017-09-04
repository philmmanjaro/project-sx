# The kernel flusher threads will periodically wake up and write `old' data
# out to disk.  This tunable expresses the interval between those wakeups, in
# 100'ths of a second. Setting this to zero disables periodic writeback altogether.

echo '1500' > /proc/sys/vm/dirty_writeback_centisecs
