#!/usr/bin/env python3
"""Simple version bump script for clickmd"""

import sys
import re
from pathlib import Path

def bump_version(version_type):
    """Bump version in pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    
    if not pyproject_path.exists():
        print("ERROR: pyproject.toml not found")
        return 1
    
    content = pyproject_path.read_text()
    
    # Find current version
    version_match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if not version_match:
        print("ERROR: Could not find version in pyproject.toml")
        return 1
    
    current_version = version_match.group(1)
    parts = current_version.split('.')
    
    if len(parts) != 3:
        print(f"ERROR: Invalid version format: {current_version}")
        return 1
    
    try:
        major, minor, patch = map(int, parts)
    except ValueError:
        print(f"ERROR: Version parts must be integers: {current_version}")
        return 1
    
    # Bump the appropriate part
    if version_type == "patch":
        patch += 1
    elif version_type == "minor":
        minor += 1
        patch = 0
    elif version_type == "major":
        major += 1
        minor = 0
        patch = 0
    else:
        print(f"ERROR: Invalid version type: {version_type}")
        return 1
    
    new_version = f"{major}.{minor}.{patch}"
    
    # Update the file
    new_content = re.sub(
        r'^version\s*=\s*"[^"]+"',
        f'version = "{new_version}"',
        content,
        flags=re.MULTILINE
    )
    
    pyproject_path.write_text(new_content)
    
    # Also update VERSION file if it exists
    version_file = Path("VERSION")
    if version_file.exists():
        version_file.write_text(f"{new_version}\n")
    
    print(f"✓ Bumped version from {current_version} to {new_version}")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py [patch|minor|major]")
        sys.exit(1)
    
    version_type = sys.argv[1]
    sys.exit(bump_version(version_type))
