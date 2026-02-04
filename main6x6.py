#!/usr/bin/env python3
"""
PlayFair Cipher 6x6 - Main Entry Point
Extended cipher with alphanumeric support
"""

import sys
import argparse


def main():
    """Main entry point for the 6x6 application."""
    parser = argparse.ArgumentParser(
        description='PlayFair Cipher 6x6 - Extended alphanumeric cryptography tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s gui              Launch graphical interface (6x6)
  %(prog)s cli              Launch command-line interface (6x6)
  %(prog)s test             Run test suite (6x6)
        """
    )
    
    parser.add_argument(
        'mode',
        choices=['gui', 'cli', 'test'],
        help='Operating mode: gui (graphical), cli (command-line), or test'
    )
    
    args = parser.parse_args()
    
    if args.mode == 'gui':
        from src.gui.app6x6 import launch
        launch()
    
    elif args.mode == 'cli':
        from src.cli.demo6x6 import run_demo
        run_demo()
    
    elif args.mode == 'test':
        from tests.test_cipher6x6 import run_all_tests
        success = run_all_tests()
        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
