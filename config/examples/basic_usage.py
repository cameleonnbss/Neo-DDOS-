#!/usr/bin/env python3
"""
Example: Basic usage of Neo-DDOS
Run this script to see how to use Neo-DDOS programmatically.
"""

import subprocess
import sys
import os

def example_1():
    """Example 1: Run Neo-DDOS interactively."""
    print("[Example 1] Interactive Mode")
    print("Run: python main.py")
    print("Then enter:")
    print("  Target: 127.0.0.1")
    print("  Port: 8080")
    print("  Duration: 5")
    print("  Threads: 50")
    print("  Choice: 1 (UDP Flood)\n")

def example_2():
    """Example 2: Run a specific attack via command line."""
    print("[Example 2] Programmatic Usage")
    print("You can integrate Neo-DDOS into your own scripts:")
    print("""
from modules.udp import flood as udp_flood
from modules.http import get_flood

stats = {
    "udp": 0, "http_get": 0, "errors": 0
}

udp_flood("127.0.0.1", 8080, 5, 50, stats)

get_flood("http://127.0.0.1:8080", 5, 50, stats)

print(f"UDP Packets: {stats['udp']}")
print(f"HTTP GET Requests: {stats['http_get']}")
print(f"Errors: {stats['errors']}")
    """)

def example_3():
    """Example 3: Run all attacks (Apocalypse Mode)."""
    print("[Example 3] Apocalypse Mode")
    print("Run: python main.py")
    print("Then enter:")
    print("  Target: 127.0.0.1")
    print("  Port: 8080")
    print("  Duration: 5")
    print("  Threads: 50")
    print("  Choice: 14 (ALL ATTACKS)\n")

if __name__ == "__main__":
    print("=" * 50)
    print("Neo-Strike Multi-Attack Suite - Usage Examples")
    print("=" * 50)
    example_1()
    example_2()
    example_3()
    input("Press Enter to exit...")
