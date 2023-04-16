from pathlib import Path

import pylint.testutils
from astroid.nodes.scoped_nodes import Module
from pylint.interfaces import UNDEFINED

from pylint_blank_line_plugin import checker


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = checker.BlankLineChecker

    def test_wrong_blank_line_first_stmt_after_indent(
        self: "TestUniqueReturnChecker",
    ) -> None:
        with (
            Path("tests/fixtures/fixture1.txt").open(encoding="utf-8") as f,
            self.assertAddsMessages(
                pylint.testutils.MessageTest(
                    msg_id="wrong-blank-line",
                    line=2,
                    confidence=UNDEFINED,
                ),
            ),
        ):
            self.checker.process_module(Module(name="temp", doc="", file=f.name))

    def test_need_blank_line_before(self: "TestUniqueReturnChecker") -> None:
        with (
            Path("tests/fixtures/fixture2.txt").open(encoding="utf-8") as f,
            self.assertAddsMessages(
                pylint.testutils.MessageTest(
                    msg_id="need-blank-line",
                    line=3,
                    confidence=UNDEFINED,
                ),
            ),
        ):
            self.checker.process_module(Module(name="temp", doc="", file=f.name))

    def test_need_blank_line_after(self: "TestUniqueReturnChecker") -> None:
        with (
            Path("tests/fixtures/fixture3.txt").open(encoding="utf-8") as f,
            self.assertAddsMessages(
                pylint.testutils.MessageTest(
                    msg_id="need-blank-line",
                    line=5,
                    confidence=UNDEFINED,
                ),
            ),
        ):
            self.checker.process_module(Module(name="temp", doc="", file=f.name))

    def test_no_messages(self: "TestUniqueReturnChecker") -> None:
        with Path("tests/fixtures/fixture4.txt").open(
            encoding="utf-8",
        ) as f, self.assertNoMessages():
            self.checker.process_module(Module(name="temp", doc="", file=f.name))

    def test_no_messages_2(self: "TestUniqueReturnChecker") -> None:
        with Path("tests/fixtures/fixture5.txt").open(
            encoding="utf-8",
        ) as f, self.assertNoMessages():
            self.checker.process_module(Module(name="temp", doc="", file=f.name))

    def test_no_messages_3(self: "TestUniqueReturnChecker") -> None:
        with Path("tests/fixtures/fixture6.txt").open(
            encoding="utf-8",
        ) as f, self.assertNoMessages():
            self.checker.process_module(Module(name="temp", doc="", file=f.name))

    def test_no_messages_4(self: "TestUniqueReturnChecker") -> None:
        with Path("tests/fixtures/fixture7.txt").open(
            encoding="utf-8",
        ) as f, self.assertNoMessages():
            self.checker.process_module(Module(name="temp", doc="", file=f.name))
