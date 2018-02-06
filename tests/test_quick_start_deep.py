import pytest
import subprocess as sp


@pytest.mark.parametrize("config", ["../deeppavlov/skills/go_bot/config.json",
                                    "../deeppavlov/models/classifiers/intents/config_dstc2.json",
                                    "../deeppavlov/models/ner/config.json",
                                    "../deeppavlov/models/spellers/error_model/config_en.json"])
@pytest.mark.parametrize("mode", ["train", "interact"])
class TestQuickStart(object):
    """Test whether instructions from Quick Start section of ReadMe is executable"""

    def test_exitcode0(self, mode, config):
        """Simple"""

        with sp.Popen(["python", "-m", "deeppavlov.deep", mode, config], stdin=sp.PIPE) as p:
            p.stdin.write(b"quit")

        assert p.returncode == 0
