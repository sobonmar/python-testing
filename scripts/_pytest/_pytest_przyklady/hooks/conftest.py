# EXAMPLE 1: USING EXISTING HOOK
# Hook pytest_runtest_setup - runs before each test

def pytest_runtest_setup(item):
    """Hook executed before each test"""
    print(f"\n🚀 Starting test: {item.name}")
    
    # We can add logic before test
    if "slow" in item.keywords:
        print("⚠️  This is a slow test!")


def pytest_runtest_teardown(item):
    """Hook executed after each test"""
    print(f"✅ Finished test: {item.name}")


def pytest_collection_modifyitems(config, items):
    """Hook modifying collected tests"""
    print(f"\n📋 Found {len(items)} tests")
    
    # Add marker to tests with "slow" in name
    for item in items:
        if "slow" in item.name:
            item.add_marker("slow")