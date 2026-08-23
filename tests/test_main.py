import unittest
from unittest.mock import patch, call
from argparse import Namespace

import main

class TestMain(unittest.TestCase):
    @patch("main.save_results")
    @patch("main.scan_host")
    @patch("main.expand_targets")
    @patch("main.parse_arguments")
    def test_scans_all_expanded_targets(
            self,
            mock_parse_arguments,
            mock_expand_targets,
            mock_scan_host,
            mock_save_results
    ) -> None:
        mock_parse_arguments.return_value = Namespace(
            target = "192.168.1.0/30",
            timeout = 0.5,
            ports = [80,443],
            output = "test.csv",
            file_mode = "w"
        )

        mock_expand_targets.return_value =[
            "192.168.1.1",
            "192.168.1.2",
        ]

        mock_scan_host.side_effect = [
            [
                {
                    "target": "192.168.1.1",
                    "port": 80,
                    "service": "HTTP",
                    "status": "OPEN"
                 }
            ],
            [
                {
                    "target": "192.168.1.2",
                    "port": 443,
                    "service": "HTTPS",
                    "status": "OPEN"
                }
            ],
    ]

        main.main()

        self.assertEqual(
            mock_scan_host.call_args_list,
     [
         call (
               "192.168.1.1",
             {
                 80: "HTTP",
                 443: "HTTPS",
             },
             timeout = 0.5,
         ),
         call (
             "192.168.1.2",
             {
                 80: "HTTP",
                 443: "HTTPS",
             },
             timeout = 0.5,
         ),
    ],
        )

    @patch("main.save_results")
    @patch("main.scan_host")
    @patch("main.expand_targets")
    @patch("main.parse_arguments")
    def test_combines_results_before_saving(
            self,
            mock_parse_arguments,
            mock_expand_targets,
            mock_scan_host,
            mock_save_results,
    ) -> None:
        mock_parse_arguments.return_value = Namespace(
            target="192.168.1.0/30",
            timeout=0.5,
            ports=[80, 443],
            output="test.csv",
            file_mode="w",
        )

        mock_expand_targets.return_value = [
            "192.168.1.1",
            "192.168.1.2",
        ]

        mock_scan_host.side_effect = [
            [
                {
                    "target": "192.168.1.1",
                    "port": 80,
                    "service": "HTTP",
                    "status": "OPEN",
                }
            ],
            [
                {
                    "target": "192.168.1.2",
                    "port": 443,
                    "service": "HTTPS",
                    "status": "OPEN",
                }
            ],
        ]

        main.main()

        mock_save_results.assert_called_once_with(
            [
                {
                    "target": "192.168.1.1",
                    "port": 80,
                    "service": "HTTP",
                    "status": "OPEN",
                },
                {
                    "target": "192.168.1.2",
                    "port": 443,
                    "service": "HTTPS",
                    "status": "OPEN",
                },
            ],
            filename = "test.csv",
            mode = "w",
        )