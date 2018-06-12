# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from .nnabla import NnpExporter
from .utils import read_nnp


def generate_nnb_template(args, nnp, output):
    NnbExporter(nnp, args.batch_size).export(
        None, output, None, args.default_variable_type)
    return True


def nnb_template(args, ifiles, output):
    nnp = read_nnp(args, ifiles)
    if nnp is not None:
        return generate_nnb_template(args, nnp, output)
    else:
        print('Read from [{}] failed.'.format(ifiles))
        return False
