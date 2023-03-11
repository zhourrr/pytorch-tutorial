import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from gradescope_utils.autograder_utils.files import check_submitted_files

# Keep this as separate file since others look nicer with import at top.
# note, this file checks against autograder paths (/autograder/submission),
# and will fail on local execution.
class TestFiles(unittest.TestCase):
    @weight(0)
    @visibility("visible")  # set to visible, so students know if they're missing files
    def test_submitted_files(self):
        """Check for submitted files"""
        missing_files = check_submitted_files(["submitted.py"])
        if len(missing_files) > 0:
            # both students and graders see this output
            print("missing files %s" % str(missing_files))
        self.assertEqual(len(missing_files), 0, "Missing some required files!")
        print("All required files submitted!")
