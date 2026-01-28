#!/usr/bin/env python3
"""
PlayFair Cipher - Main Entry Point
"""

import sys
import argparse


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description='PlayFair Cipher - Classical cryptography tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s gui              Launch graphical interface
  %(prog)s cli              Launch command-line interface
  %(prog)s test             Run test suite
        """
    )
    
    parser.add_argument(
        'mode',
        choices=['gui', 'cli', 'test'],
        help='Operating mode: gui (graphical), cli (command-line), or test'
    )
    
    args = parser.parse_args()
    
    if args.mode == 'gui':
        from src.gui.app import launch
        launch()
    
    elif args.mode == 'cli':
        from src.cli.demo import run_demo
        run_demo()
    
    elif args.mode == 'test':
        from tests.test_cipher import run_tests
        success = run_tests()
        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
