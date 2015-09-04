#!/usr/bin/env python3
import unittest
import pirate.torrent
import os

from tests import util


class TestTorrent(unittest.TestCase):

    def test_no_hits(self):
        res = util.read_data('no_hits.html')
        actual = pirate.torrent.parse_page(res)
        expected = []
        self.assertEqual(actual, expected)

    def test_blocked_mirror(self):
        res = util.read_data('blocked.html')
        with self.assertRaises(IOError):
            pirate.torrent.parse_page(res)

    def test_search_results(self):
        res = util.read_data('dan_bull_search.html')
        actual = pirate.torrent.parse_page(res)
        expected = [{'uploaded': '04-04\xa02014', 'seeds': '16', 'leechers': '1', 'id': '9890864', 'magnet': 'magnet:?xt=urn:btih:30df4f8b42b8fd77f5e5aa34abbffe97f5e81fbf&dn=Dan+Croll+%26bull%3B+Sweet+Disarray+%5B2014%5D+320&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['89.33', 'MiB']}, {'uploaded': '03-02\xa02014', 'seeds': '4', 'leechers': '0', 'id': '9684858', 'magnet': 'magnet:?xt=urn:btih:7abd3eda600996b8e6fc9a61b83288e0c6ac0d83&dn=Dan+Bull+-+Massive+Collection&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['294', 'MiB']}, {'uploaded': '01-19\xa02013', 'seeds': '2', 'leechers': '0', 'id': '8037968', 'magnet': 'magnet:?xt=urn:btih:8f8d68fd0a51237c89692c428ed8a8f64a969c70&dn=Dan+Bull+-+Generation+Gaming+-+2013&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['54.86', 'MiB']}, {'uploaded': '01-21\xa02010', 'seeds': '1', 'leechers': '0', 'id': '5295449', 'magnet': 'magnet:?xt=urn:btih:3da6a0fdc1d67a768cb32597e926abdf3e1a2fdd&dn=Dan+Bull+Collection&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['236.78', 'MiB']}, {'uploaded': '09-02\xa02014', 'seeds': '1', 'leechers': '0', 'id': '10954408', 'magnet': 'magnet:?xt=urn:btih:5cd371a235317319db7da52c64422f9c2ac75d77&dn=Dan+Bull+-+The+Garden+%7B2014-Album%7D&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['36.27', 'MiB']}, {'uploaded': '09-27\xa02009', 'seeds': '0', 'leechers': '1', 'id': '5101630', 'magnet': 'magnet:?xt=urn:btih:4e14dbd077c920875be4c15971b23b609ad6716a&dn=Dan+Bull+-+Dear+Lily+%5Ban+open+letter+to+Lily+Allen%5D+-+2009%5BMP3+%40&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['5.51', 'MiB']}, {'uploaded': '11-29\xa02009', 'seeds': '0', 'leechers': '0', 'id': '5185893', 'magnet': 'magnet:?xt=urn:btih:5d9319cf852f7462422cb1bffc37b65174645047&dn=Dan+Bull+-+Dear+Mandy+%5Ban+open+letter+to+Lord+Mandelson%5D&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['5.07', 'MiB']}, {'uploaded': '11-10\xa02011', 'seeds': '0', 'leechers': '0', 'id': '6806996', 'magnet': 'magnet:?xt=urn:btih:1c54af57426f53fdef4bbf1a9dbddf32f7b4988a&dn=Dan+Bull+-+Dear+Lily+%28Lily+Allen%29+%28Song+about+filesharing%29&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['5.34', 'MiB']}, {'uploaded': '12-20\xa02011', 'seeds': '0', 'leechers': '0', 'id': '6901871', 'magnet': 'magnet:?xt=urn:btih:942c5bf3e1e9bc263939e13cea6ad7bd5f62aa36&dn=Dan+Bull+-+SOPA+Cabana.mp3&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['4.8', 'MiB']}, {'uploaded': '12-21\xa02011', 'seeds': '0', 'leechers': '1', 'id': '6902247', 'magnet': 'magnet:?xt=urn:btih:d376f68a31b0db652234e790ed7256ac5e32db57&dn=Dan+Bull+-+SOPA+Cabana&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['3.4', 'MiB']}, {'uploaded': '12-21\xa02011', 'seeds': '0', 'leechers': '1', 'id': '6903548', 'magnet': 'magnet:?xt=urn:btih:28163770a532eb24b9e0865878288a9bbdb7a5e6&dn=Dan+Bull+-+SOPA+Cabana+%5BWORKING%5D&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['4.8', 'MiB']}, {'uploaded': '03-09\xa02012', 'seeds': '0', 'leechers': '1', 'id': '7088979', 'magnet': 'magnet:?xt=urn:btih:779ab0f13a3fbb12ba68b27721491e4d143f26eb&dn=Dan+Bull+-+Bye+Bye+BPI+2012++%5BMP3%40192%5D%28oan%29&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['60.72', 'MiB']}, {'uploaded': '10-24\xa02012', 'seeds': '0', 'leechers': '0', 'id': '7756344', 'magnet': 'magnet:?xt=urn:btih:2667e4795bd5c868dedcabcb52943f4bb7212bab&dn=Dan+Bull+-+Dishonored+%5BExplicit+ver.%5D+%28Single+2012%29&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['6.29', 'MiB']}, {'uploaded': '11-10\xa02012', 'seeds': '0', 'leechers': '0', 'id': '7812951', 'magnet': 'magnet:?xt=urn:btih:16364f83c556ad0fd3bb57a4a7c890e7e8087414&dn=Halo+4+EPIC+Rap+By+Dan+Bull&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['6.41', 'MiB']}, {'uploaded': '01-19\xa02013', 'seeds': '0', 'leechers': '1', 'id': '8037899', 'magnet': 'magnet:?xt=urn:btih:843b466d9fd1f0bee3a476573b272dc2d6d0ebae&dn=Dan+Bull+-+Generation+Gaming+-+2013&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969', 'size': ['54.87', 'MiB']}]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
