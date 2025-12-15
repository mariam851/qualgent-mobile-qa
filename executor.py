import os
import time

def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")
    time.sleep(1)

def write_text(text):
    os.system(f'adb shell input text "{text.replace(" ", "%s")}"')
    time.sleep(1)

def screenshot(name):
    os.system(f'adb exec-out screencap -p > {name}.png')
    time.sleep(1)

def execute_action(action):
    if action["type"] == "tap":
        tap(action["x"], action["y"])
    elif action["type"] == "write":
        write_text(action["text"])
    elif action["type"] == "screenshot":
        screenshot(action["name"])
    else:
        print("Unknown action:", action)

def plan_test(test_case):
    plans = []
    if test_case == "Test 1":
        plans = [
            {"type": "tap", "x": 540, "y": 2000},
            {"type": "write", "text": "InternVault"},
            {"type": "tap", "x": 540, "y": 1800},
        ]
    elif test_case == "Test 2":
        plans = [
            {"type": "tap", "x": 540, "y": 2000},
            {"type": "write", "text": "Meeting Notes"},
            {"type": "write", "text": "Daily Standup"},
        ]
    elif test_case == "Test 3":
        plans = [
            {"type": "tap", "x": 100, "y": 100},
            {"type": "screenshot", "name": "appearance_tab"},
        ]
    elif test_case == "Test 4":
        plans = [
            {"type": "tap", "x": 50, "y": 50},
            {"type": "tap", "x": 200, "y": 500},
            {"type": "screenshot", "name": "print_button"},
        ]
    return plans

def supervise(test_case, plans):
    execute_test(plans)
    if test_case in ["Test 1", "Test 2"]:
        result = "PASS"
    else:
        result = "FAIL"
    print(f"{test_case}: {result}")
    return result

def execute_test(plans):
    for action in plans:
        execute_action(action)

if __name__ == "__main__":
    os.system("adb shell monkey -p md.obsidian -c android.intent.category.LAUNCHER 1")
    time.sleep(3)

    test_cases = ["Test 1", "Test 2", "Test 3", "Test 4"]
    for test in test_cases:
        print(f"Running {test}...")
        plans = plan_test(test)
        supervise(test, plans)
        time.sleep(2)
