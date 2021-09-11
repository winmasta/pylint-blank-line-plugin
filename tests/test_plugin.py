import pylint.testutils
from astroid.nodes.scoped_nodes import Module
from pylint.interfaces import Confidence

from pylint_blank_line_plugin import checker


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = checker.BlankLineChecker

    def test_wrong_blank_line_first_stmt_after_indent(self):
        with open('tests/fixtures/fixture1.txt', encoding='utf-8') as f:
            with self.assertAddsMessages(
                    pylint.testutils.Message(
                        msg_id='wrong-blank-line',
                        line=2,
                        confidence=Confidence(
                            name='UNDEFINED',
                            description='Warning without any associated confidence level.',
                        ),
                    )
            ):
                self.checker.process_module(Module(name='temp', doc='', file=f.name))

    def test_need_blank_line_before(self):
        with open('tests/fixtures/fixture2.txt', encoding='utf-8') as f:
            with self.assertAddsMessages(
                    pylint.testutils.Message(
                        msg_id='need-blank-line',
                        line=3,
                        confidence=Confidence(
                            name='UNDEFINED',
                            description='Warning without any associated confidence level.',
                        ),
                    )
            ):
                self.checker.process_module(Module(name='temp', doc='', file=f.name))

    def test_need_blank_line_after(self):
        with open('tests/fixtures/fixture3.txt', encoding='utf-8') as f:
            with self.assertAddsMessages(
                    pylint.testutils.Message(
                        msg_id='need-blank-line',
                        line=5,
                        confidence=Confidence(
                            name='UNDEFINED',
                            description='Warning without any associated confidence level.',
                        ),
                    )
            ):
                self.checker.process_module(Module(name='temp', doc='', file=f.name))

    def test_no_messages(self):
        with open('tests/fixtures/fixture4.txt', encoding='utf-8') as f:
            with self.assertNoMessages():
                self.checker.process_module(Module(name='temp', doc='', file=f.name))

    def test_no_messages_2(self):
        with open('tests/fixtures/fixture5.txt', encoding='utf-8') as f:
            with self.assertNoMessages():
                self.checker.process_module(Module(name='temp', doc='', file=f.name))

    def test_no_messages_3(self):
        with open('tests/fixtures/fixture6.txt', encoding='utf-8') as f:
            with self.assertNoMessages():
                self.checker.process_module(Module(name='temp', doc='', file=f.name))
