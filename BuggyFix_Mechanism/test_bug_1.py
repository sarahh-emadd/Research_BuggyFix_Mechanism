from bug_1.bug_1_copilot import bitcount as copilot_version
from bug_1.bug_1_cursor import bitcount as cursor_version
from bug_1.bug_1_gpt import bitcount as gpt_version


def test_bitcount_versions():
    inputs = [127, 128, 0, 255]
    expected_outputs = [7, 1, 0, 8]

    for i, val in enumerate(inputs):
        assert copilot_version(val) == expected_outputs[i], f"Copilot failed for input {val}"
        assert cursor_version(val) == expected_outputs[i], f"Cursor failed for input {val}"
        assert gpt_version(val) == expected_outputs[i], f"Cursor failed for input {val}"
        