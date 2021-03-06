# Copyright 2020 The TEMPO Collaboration
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Tests for the time_evolving_mpo.backends.base_backends module.
"""
import pytest

import numpy as np
import tensornetwork as tn

import time_evolving_mpo as tempo
from time_evolving_mpo.backends.backend_factory import \
    get_tempo_backend, get_pt_tempo_backend, get_process_tensor_backend
pass

def test_backend_factory_default():
    tempo_back = get_tempo_backend()
    pt_tempo_back = get_pt_tempo_backend()
    process_tensor_back = get_process_tensor_backend()
