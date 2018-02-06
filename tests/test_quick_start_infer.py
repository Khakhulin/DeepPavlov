import pytest
import subprocess as sp
import shutil
import os
import sys

# This should be executed from 'tests' directory!

# Model name to config mapping
N2C = {"go_bot_rnn": "../deeppavlov/skills/go_bot/config.json",
       "intents": "../deeppavlov/models/classifiers/intents/config_dstc2.json",
       "ner": "../deeppavlov/models/ner/config.json",
       "error_model": "../deeppavlov/models/spellers/error_model/config_en.json"}


def download(all=None):
    cmd = ["python", "-m", "deeppavlov.download"]
    if all:
        cmd.append("-all")
    # sp.run(cmd)

@pytest.mark.parametrize("model", [k for k, v in N2C.items()])
def test_download(model):
    assert os.path.exists("../download" + model)


# def teardown_module(module):
#     # shutil.rmtree("../download/", ignore_errors=True)
#     print(f"{module} teardown finished.")


@pytest.mark.parametrize("config_path", [v for k, v in N2C.items()])
def test_exitcode0(self, config_path):
    with sp.Popen(["python", "-m", "deeppavlov.deep", mode, config], stdin=sp.PIPE) as p:
        p.stdin.write(b"quit")

    assert p.returncode == 0
