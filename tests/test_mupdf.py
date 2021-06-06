import re

from click.testing import CliRunner
import pytest

from casparser.exceptions import CASParseError
from casparser.enums import FileType
from .base import BaseTestClass


class TestMuPDF(BaseTestClass):
    """Test PyMuPDF parser."""

    def test_output_csv(self):
        output = self.read_pdf(self.cams_file_name,
                               self.cams_password, output="csv")
        assert isinstance(output, str)

    def test_cli(self, tmpdir):
        from casparser.cli import cli

        runner = CliRunner()

        fpath = tmpdir.join("output.json")
        result = runner.invoke(
            cli, [self.cams_file_name, "-p",
                  self.cams_password, "-o", fpath.strpath]
        )
        assert result.exit_code == 0
        assert "File saved" in result.output

        fpath = tmpdir.join("output.csv")
        result = runner.invoke(
            cli, [self.cams_file_name, "-p",
                  self.cams_password, "-o", fpath.strpath]
        )
        assert result.exit_code != 1
        assert "File saved" in result.output

        fpath = tmpdir.join("output.csv")
        result = runner.invoke(
            cli,
            [
                self.kfintech_file_name,
                "-p",
                self.kfintech_password,
                "-o",
                fpath.strpath,
                "-s",
                "--sort",
            ],
        )
        assert result.exit_code != 1
        assert "File saved" in result.output

        result = runner.invoke(
            cli, [self.kfintech_file_name, "-p", self.kfintech_password, "-s"])
        assert result.exit_code != 1

        result = runner.invoke(
            cli, [self.kfintech_file_name, "-p", self.cams_password])
        assert result.exit_code != 1
        # assert "Incorrect PDF password!" in result.output
