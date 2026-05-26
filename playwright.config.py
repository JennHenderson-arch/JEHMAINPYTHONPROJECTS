# Configuration for Playwright tests
# https://playwright.dev/python/docs/test-runners

config = {
    "testDir": "tests",
    "testMatch": ["test_*.py", "*_test.py"],
    "timeout": 30000,
    "expect": {"timeout": 5000},
    "reporters": "html",
    "use": {
        "browserName": "chromium",
        "headless": False,
        "viewport": {"width": 1280, "height": 720},
    },
    "projects": [
        {"name": "chromium", "use": {"browserName": "chromium"}},
        {"name": "firefox", "use": {"browserName": "firefox"}},
        {"name": "webkit", "use": {"browserName": "webkit"}},
    ],
}
