#!/usr/bin/env python3
"""Script to take screenshots of course detail pages using Chromium headless."""
import subprocess
import os

OUTPUT_DIR = '/home/runner/work/course-explainer-app/course-explainer-app/test-output'

def take_screenshot(url, filename):
    """Take a screenshot using Chromium headless with xvfb."""
    output_path = os.path.join(OUTPUT_DIR, filename)
    screenshot_arg = '--screenshot=' + output_path

    cmd = [
        'xvfb-run', '-a',
        'chromium-browser',
        '--headless',
        '--no-sandbox',
        '--disable-gpu',
        screenshot_arg,
        '--window-size=1280,900',
        url
    ]

    print(f"Taking screenshot of: {url}")
    print(f"Saving to: {output_path}")

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

    print(f"Return code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT: {result.stdout[:300]}")
    if result.stderr:
        print(f"STDERR: {result.stderr[:300]}")

    if os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"Screenshot saved successfully! File size: {size} bytes")
        return True
    else:
        print(f"Screenshot file not found at: {output_path}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    screenshots = [
        ('http://127.0.0.1:5000/course/1', 'course-detail-1-introduction-to-python-2026-02-21.png'),
        ('http://127.0.0.1:5000/course/4', 'course-detail-4-go-programming-essentials-2026-02-21.png'),
        ('http://127.0.0.1:5000/', 'course-list-homepage-2026-02-21.png'),
    ]

    results = []
    for url, filename in screenshots:
        success = take_screenshot(url, filename)
        results.append((url, filename, success))
        print()

    print("=== Summary ===")
    for url, filename, success in results:
        status = "SUCCESS" if success else "FAILED"
        print(f"{status}: {filename} <- {url}")


if __name__ == '__main__':
    main()
