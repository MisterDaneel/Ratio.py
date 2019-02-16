from code.torrent import torrent

to = torrent('test.torrent')
rep = to.tracker_start_request()
to.tracker_process()

